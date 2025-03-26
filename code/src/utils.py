import time
import tweepy
import os
from langchain_community.document_loaders import WikipediaLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

from dotenv import load_dotenv
load_dotenv()

os.environ['X_BEARER_TOKEN'] = os.getenv('X_BEARER_TOKEN')

## split documents and embed into model
## Create ChromeDB as retriever using the documents and embeddings
def split_and_embed_documents(documents, chunk_size=512, chunk_overlap=50):
  """Splits documents into chunks and embeds them using model and ChromeDB.

  Args:
    documents: A list of LangChain Document objects.
    chunk_size: The maximum size of each chunk.
    chunk_overlap: The amount of overlap between chunks.

  Returns:
    A RetrievalQA chain with the embedded documents.
  """

  # Split documents into chunks
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)

  # Embed documents using model
  embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-large-en-v1.5')

  # Create ChromeDB retriever
  db = Chroma.from_documents(docs, embeddings)

  return db

def fetch_tweets(query: str):
    # Your bearer token from Twitter Developer Portal
    bearer_token = os.environ['X_BEARER_TOKEN']
    try:
        tweets = list()
        client = tweepy.Client(bearer_token=bearer_token)
        # Fetch tweets
        response = client.search_recent_tweets(query=query, max_results=10)
        # Print the tweets
        if response.data:
            for tweet in response.data:
                print(tweet.text)
                tweets.append(tweet)                    
                time.sleep(5)  # Add a delay to avoid rate limits
            return tweets
        else:
            print("No tweets found for the query.")
    except Exception as e:
        print(f'Failed with exception : {e}')
        return list()
 
def tweets_to_documents(tweets):
  """Converts a list of Tweepy tweet objects to LangChain Documents."""
  documents = []
  for tweet in tweets:
    documents.append(Document(
        page_content=tweet.text,
        metadata={
            "author_id": tweet.author_id,
            "created_at": tweet.created_at,
            "tweet_id": tweet.id,
            # Add other relevant metadata as needed
        }
    ))
  return documents

def fetch_wikipedia_documents(user_query:str):
    wiki_docs = WikipediaLoader(query=user_query, load_max_docs=5).load()
    return wiki_docs

def save_chroma_to_db(db, persist_directory="chroma_db"):
  """
  Saves a ChromaDB instance to a persistent directory.

  Args:
      db: The ChromaDB instance to save.
      persist_directory: The directory where the database will be saved.
  """
  db.persist(persist_directory)
  print(f"ChromaDB saved to {persist_directory}")

def load_chroma_from_db(persist_directory="chroma_db"):
  """
  Loads a ChromaDB instance from a persistent directory.

  Args:
      persist_directory: The directory where the database is saved.

  Returns:
      A ChromaDB instance.
  """
  embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-large-en')
  db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
  return db