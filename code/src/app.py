# streamlit code to get query from user and return result

##%%writefile app.py
import streamlit as st
from utils import load_chroma_from_db, fetch_wikipedia_documents, fetch_tweets, tweets_to_documents, split_and_embed_documents, save_chroma_to_db
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from evaluate_results import evaluate


# Load your LLM pipeline (assuming you have it defined as 'pipe')
model_id = "gemma2:2b"  # Replace with gemma2:2b if available
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=1024
)
user_query = st.text_input("Enter your query:")

# fetch wikipedia documents
wiki_docs = fetch_wikipedia_documents(user_query)

# fetch tweet data
tweets = fetch_tweets(user_query)
tweet_docs = tweets_to_documents(tweets=tweets)

## split and convert documents
docs = wiki_docs + tweet_docs
chroma_db = split_and_embed_documents(docs)

# Save vector database
persist_dir = '/./../data/sec-edgar-data/sec-data/chromadb/'
save_chroma_to_db(chroma_db, persist_dir)

# declare an hugging face pipeline and load data from vector database
llm = HuggingFacePipeline(pipeline=pipe)
db = load_chroma_from_db(persist_dir) 
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())

st.title("Query SEC Data")

if user_query:
    result = qa.run(user_query)
    # fetch results and query evaluation model for scoring
    score = evaluate(result)
    st.write("**Result:**")
    st.write(result)
    st.write(score)