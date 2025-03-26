# langchain community document loader to parse xml files

from langchain.document_loaders import UnstructuredXMLLoader
from langchain.document_loaders import DirectoryLoader


## Parse SEC data stored in htm format
edgar_data_path = '../../data/sec-edgar-data/sec-data'
loader = DirectoryLoader(edgar_data_path, glob="**/*.htm", loader_cls=UnstructuredXMLLoader)
xml_docs = loader.load()
print("SEC Data converted to langchain documents successfully")
