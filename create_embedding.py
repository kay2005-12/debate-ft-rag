import requests
import os

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed",json = {
     "model" : "nomic-embed-text",
     "input" : text_list   
    })
    
    data = r.json()
    
    if "embeddings" not in data :
        print(f"Api Response {data}")
        return []
    
    return data["embeddings"]

prompt = "hello how are you?"
data_list = create_embedding(prompt)
print(data_list)