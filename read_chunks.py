import joblib
import os
import numpy as np
from create_embedding import create_embedding
import pandas as pd
import json
jsons = os.listdir("jsons")
chunk_id = 0
my_dict = []

for files in jsons:
    with open(f'jsons/{files}',"r") as f:
        content = json.load(f)
    # print(content)
    data = [c['text']for c in content['chunk']]
    embeddings = create_embedding(data)
    for i , chunk in enumerate(content['chunk']):
        if i>=len(embeddings):
            continue
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id+=1
        my_dict.append(chunk)
        
df = pd.DataFrame.from_records(my_dict)
joblib.dump(df,'embedding.joblib')