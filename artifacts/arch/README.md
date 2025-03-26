## Architecture and workflow

Workflow : 
![Alt text](https://cdn-lfs-us-1.hf.co/repos/13/3d/133d8ca2460bf82ba2bdbe928d91a6c780364a6d0cf9005087db081cca492c02/ed22547b1538ea4fd18ea26777e14d9f7e51b3388b34d3cadf165cc37a7f63e0?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27RAG_workflow.png%3B+filename%3D%22RAG_workflow.png%22%3B&response-content-type=image%2Fpng&Expires=1742993952&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0Mjk5Mzk1Mn19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy11cy0xLmhmLmNvL3JlcG9zLzEzLzNkLzEzM2Q4Y2EyNDYwYmY4MmJhMmJkYmU5MjhkOTFhNmM3ODAzNjRhNmQwY2Y5MDA1MDg3ZGIwODFjY2E0OTJjMDIvZWQyMjU0N2IxNTM4ZWE0ZmQxOGVhMjY3NzdlMTRkOWY3ZTUxYjMzODhiMzRkM2NhZGYxNjVjYzM3YTdmNjNlMD9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSomcmVzcG9uc2UtY29udGVudC10eXBlPSoifV19&Signature=iWCs2ogL7nMxBP9zfKQgnRYZi9-KNd9lksrztM8c9s7yJBAEl6RKpdv9ButJKGmS932TJkPrNOZGqcRZPusHbqGprf2QCDaCIkFF0RW8MUgLfTNX%7EfBb3%7EpKSwmTvCQULsAaJy0UXojouqMSxSQUVOtEIReeotMU2KZ05NcajX8eDBg0LXgzLoh37qlwXBqMbQXv61-rnYtULSDHO5PfkksfWY2bFE1FNORLCWRmXTzEm6BiAn29Ao0cXla5mrX9Z9sCYMTP3SJV2%7EBBctluV8rBVKaSgOuC9%7EXv3QicOgB%7EoWUa7FZKHUGlEX49xYXVe7kO5NXALikv7fXNrTOgbA__&Key-Pair-Id=K24J24Z295AEI9 "RAG flow")

## Idea: 
   1. Use latest data available on internet to fetch relevant results for user's query.
   2. Combine results with financial data and calculate risk score for the query.

## Workflow
1. We are using two LLMs in this application
   - "gemma" for text-generation. This model will be responsible for answering user's query using data from SEC, social media etc.\
     Please note that in this case LLM is leveraging latest data from social media.
   - "distilroberta" will use the results returned by "gemma" to calculate risk score (using sentiment analysis).\
      Since "gemma" is 
3. Initially, static data like SEC-EDGAR data is fetched, tokenized and stored in vector database.
4. Fetching data from SEC can be a batch process which can be scheduled to run periodically.
5. When a user queries LLM, application is fetching data from wikipedia and twitter in realtime. \
   This data fetched from social media is tokenized and stored in vector database.
6. Now, "gemma" LLM will leverage updated vector database to fetch relevant result snippets back to user.
7. These results are then used by "distilroberta" LLM model to calculate a cumulative mean of all the snippets fetched by "gemma" to calculate risk score.
8. Thus we are calculating risk score depending on SEC data (financial data) as well as using the latest information available in social media space.
