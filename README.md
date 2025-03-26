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
    SEC-DATA - this data can be fetched in batches as required and LLM will update its knowledge base\
    Wikipedia - LLM can leverage knowledge from wikipedia in near realtime\
    Social Media - currently LLM will refere to latest data from X (Twitter) in near real time\

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
What inspired you to create this project? Describe the problem you're solving.

## ⚙️ What It Does
Explain the key features and functionalities of your project.

## 🛠️ How We Built It
Briefly outline the technologies, frameworks, and tools used in development.

## 🚧 Challenges We Faced
Describe the major technical or non-technical challenges your team encountered.

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
