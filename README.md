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

## 🚧 Challenges We Faced
There were three major challenges for solving this problem. 
- First and foremost was knowledge. This problem is an open ended problem and we had a tough time nailing down what we wanted our application to achieve.\
  We started with looking for appropriate dataset to train LLM and once we had it narrowed down we ran into next challenges.\
  LLMs is a different universe when it comes to fine-tuning and it was quite an experience to learn how to process dataset and train/fine tune a model.\
- Second was infrastracture issues where even pre-trained models were giving an "out of memory" exception.\
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
- **Your Name** - [GitHub](#) | [LinkedIn](#)
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)
