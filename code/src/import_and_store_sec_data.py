## File is available at https://www.sec.gov/files/company_tickers.json
fpath = "../../data/sec-data/company_tickers.json"

import json
import pandas as pd
from edgar import *
import pandas as pd
import os
from pathlib import Path
from utils import save_chroma_to_db, split_and_embed_documents
from langchain.document_loaders import UnstructuredXMLLoader
from langchain.document_loaders import DirectoryLoader
from dotenv import load_dotenv
load_dotenv()

os.environ['EDGAR_IDENTITY'] = os.getenv('EDGAR_IDENTITY')


## Read company_tickers file and add records to list
content = ""
with open(fpath) as f:
    content = f.readline()
data = json.loads(content)

company_tickers = list()
for indx, val in data.items():
    company_tickers.append(val)

set_identity(os.environ['EDGAR_IDENTITY'])

def download_attachments(company, fpath: str):
    filings = company.get_filings(form='10-K', filing_date='2024-01-01:')
    for i, _ in enumerate(filings):
        filing = filings.get(i)
        if filing:
            attachments = filing.attachments
            for j, _ in enumerate(attachments):
                attachment = attachments.get_by_index(0)
                attachment.download(fpath)


edgar_data_path = '../../data/sec-edgar-data/sec-data'
def save_data(df, path:str):
    df.reset_index().to_json(path, orient='records')

def populate_data(company: str):
    c = Company(company)
    try:
        financials = c.financials
        company_fpath = os.path.join(edgar_data_path, company)
        if os.path.exists(company_fpath):
            print(f"Data is already fetched for {company}. Moving on to next record.")
            return
        os.makedirs(company_fpath, exist_ok=True)
        ## Fetch company filings and save 
        download_attachments(c, company_fpath)
    
        save_data(financials.get_balance_sheet().data, os.path.join(company_fpath, "balance_sheet.json")) 
        save_data(financials.get_income_statement().data, os.path.join(company_fpath, "income_statement.json")) 
        save_data(financials.get_cash_flow_statement().data, os.path.join(company_fpath, "cash_flow_statement.json")) 
        save_data(financials.get_statement_of_changes_in_equity().data, os.path.join(company_fpath, "statement_of_changes_in_equity.json")) 
        save_data(financials.get_statement_of_comprehensive_income().data, os.path.join(company_fpath, "comprehensive_income.json")) 
        print(f"saved data for company : {company}")
    except:
        print(f"Failed to fetch complete data for {company}")


if __name__ == '__main__' :
    limit = 100 # fetch only hundred random records

    for i, company in enumerate(company_tickers):
        if i > limit:
            break
        populate_data(company=company['ticker'])
    loader = DirectoryLoader('/content/drive/My Drive/sec-edgar-data/sec-data/', glob="**/*.htm", loader_cls=UnstructuredXMLLoader)
    xml_docs = loader.load()
    chroma_db = split_and_embed_documents(xml_docs)
    # Save vector database
    persist_dir = '/./../data/sec-edgar-data/sec-data/chromadb/'
    save_chroma_to_db(chroma_db, persist_dir)
