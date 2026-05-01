import requests
from create_embedding import create_embedding
import numpy as np
import joblib
import os
import json
from cerebras.cloud.sdk import Cerebras
from sklearn.metrics.pairwise import cosine_similarity
client = Cerebras(
    api_key='csk-2c84xc8m8283k43e3vn3kt3mpr89wwm2hwdpnmvy46n8863t'
)
print(client.models.list())
df = joblib.load("embedding.joblib")
def inference(prompt):
    r = client.chat.completions.create(
        model="llama3.1-8b",
        messages=[
            {
                 "role": "system", 
                "content": "You are a strict assistant that answers ONLY using the provided context. Rules - 1. Use only the information from the context. 2. Do not add outside knowledge. 4. Keep the answer short and factual. 5. Do not ask questions."
            },
            {'role':'user',
             'content':prompt
             }
    ],
    )

    return r.choices[0].message.content

# df = joblib.load("embedding.joblib")
# incoming_query = input("Ask::")

def rag_pipeline(incoming_query):
    questions_embed = create_embedding(incoming_query)[0]
    simillarity = cosine_similarity(np.vstack(df['embedding']),[questions_embed]).flatten()
    # print(simillarity)
    max_index = simillarity.argsort()[::-1][:15]
    context = ""

    for i in max_index:
        context+=df.iloc[i]["text"]+"\n"
    prompt = f"""
    SYSTEM:
    You are a debate assistant that answers using the provided context.
    The context may have grammatical mistakes because it comes from a spoken debate.

    Fix grammar and present the answer clearly like a human discussing the topic.
    Do not add external knowledge.


    CONTEXT:
    {context}

    QUESTION:
    {incoming_query}
    """

    response = inference(prompt)
    return response