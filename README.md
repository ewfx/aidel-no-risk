# 🚀 Project Name

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
This project enables a user to query a large Language Model regarding financial details of any company. 
Large Language Model (LLM) leverages multiple data sources for references. \
e.g. \
    * SEC-DATA - this data can be fetched in batches as required and LLM will update its knowledge base\
    * Wikipedia - LLM can leverage knowledge from wikipedia in near realtime\
    * Social Media - currently LLM will refere to latest data from X (Twitter) in near real time.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
This project enables a user to query a large Language Model regarding financial details of any company. 
Large Language Model (LLM) leverages multiple data sources for references. \
e.g. \
    * SEC-DATA - this data can be fetched in batches as required and LLM will update its knowledge base\
    * Wikipedia - LLM can leverage knowledge from wikipedia in near realtime\
    * Social Media - currently LLM will refere to latest data from X (Twitter) in near real time.

## ⚙️ What It Does
Our application leverages power of LLM model to fetch relevant answers from data sources. 
We have automated fetching of records from social media in near real-time so that model's knowledge base can be up-to-date.


## 🛠️ How We Built It
we have leveraged huggingface APIs for building LLM pipelines.\
Our initial aim was to train an LLM on data from SEC-EDGAR and social media. However, it proved to be a bigger challenge due to infrastructure and time constraints.
We have used "gemma2:2b" and google's "flan t5" for Q&A retrival and "distilroberta" for calculating risk score.\
Knowledge base for LLM is using ChromaDB as vector database.\
For data ingestion, we are using edgartools along with tweepy.

Workflow : 
![Alt text](https://cdn-lfs-us-1.hf.co/repos/13/3d/133d8ca2460bf82ba2bdbe928d91a6c780364a6d0cf9005087db081cca492c02/ed22547b1538ea4fd18ea26777e14d9f7e51b3388b34d3cadf165cc37a7f63e0?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27RAG_workflow.png%3B+filename%3D%22RAG_workflow.png%22%3B&response-content-type=image%2Fpng&Expires=1742993952&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0Mjk5Mzk1Mn19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy11cy0xLmhmLmNvL3JlcG9zLzEzLzNkLzEzM2Q4Y2EyNDYwYmY4MmJhMmJkYmU5MjhkOTFhNmM3ODAzNjRhNmQwY2Y5MDA1MDg3ZGIwODFjY2E0OTJjMDIvZWQyMjU0N2IxNTM4ZWE0ZmQxOGVhMjY3NzdlMTRkOWY3ZTUxYjMzODhiMzRkM2NhZGYxNjVjYzM3YTdmNjNlMD9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSomcmVzcG9uc2UtY29udGVudC10eXBlPSoifV19&Signature=iWCs2ogL7nMxBP9zfKQgnRYZi9-KNd9lksrztM8c9s7yJBAEl6RKpdv9ButJKGmS932TJkPrNOZGqcRZPusHbqGprf2QCDaCIkFF0RW8MUgLfTNX%7EfBb3%7EpKSwmTvCQULsAaJy0UXojouqMSxSQUVOtEIReeotMU2KZ05NcajX8eDBg0LXgzLoh37qlwXBqMbQXv61-rnYtULSDHO5PfkksfWY2bFE1FNORLCWRmXTzEm6BiAn29Ao0cXla5mrX9Z9sCYMTP3SJV2%7EBBctluV8rBVKaSgOuC9%7EXv3QicOgB%7EoWUa7FZKHUGlEX49xYXVe7kO5NXALikv7fXNrTOgbA__&Key-Pair-Id=K24J24Z295AEI9 "RAG flow")

1. Initially, static data like SEC-EDGAR data is fetched, tokenized and stored in vector database.
2. Fetching data from SEC can be a batch process which can be scheduled to run periodically.
3. When a user queries LLM, application is fetching data from wikipedia and twitter in realtime. \
   This data fetched from social media is tokenized and stored in vector database.
4. Now, "gemma" LLM will leverage updated vector database to fetch relevant result snippets back to user.
5. These results are then used by "distilroberta" LLM model to calculate a cumulative mean of all the snippets fetched by "gemma" to calculate risk score.
6. Thus we are calculating risk score depending on SEC data as well as using the latest information available in social media space.


## 🚧 Challenges We Faced
There were three major challenges for solving this problem. 
- First and foremost was knowledge. This problem is an open ended problem and we had a tough time nailing down what we wanted our application to achieve.\
  We started with looking for appropriate dataset to train LLM and once we had it narrowed down we ran into next challenges.\
  LLMs is a different universe when it comes to fine-tuning and it was quite an experience to learn how to process dataset and train/fine tune a model.\
- Second was infrastracture issues where even pre-trained models were giving an "out of memory" exception.
  Then, there were package incompatibility issues or models would not load unless GPU was available.
- Third was to understand what model does what. Huggingface has a huge collection of models and datasets and it was difficult to choose an appropriate one.
   

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/aidel-no-risk.git
   ```
2. Install dependencies  
   ```sh
   pip install -r requirements.txt
   ```
3. Populate initial records i.e. download static data from SEC
   ```sh
   cd aidel-no-risk
   mkdir -p data/sec-edgar-data/sec-data
   cd code/src
   python import_and_store_sec_data.py
   python populate_data_in_vectordb.py
   ```
   
3. Run the project  
   ```sh
   cd aidel-no-risk
   streamlit run ./code/src/app.py
   ```

## 🏗️ Tech Stack
- 🔹 Frontend: streamlit
- 🔹 Backend: Huggingface APIs
- 🔹 Vector Database: ChromaDb
- 🔹 Other: edgartools

## 👥 Team
- **Your Name** - [GitHub](https://github.com/piyjoshi) | [LinkedIn](https://www.linkedin.com/in/piyushsjoshi/)
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)
