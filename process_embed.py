import requests
from create_embedding import create_embedding
import numpy as np
import joblib
import os
from dotenv import load_dotenv
from cerebras.cloud.sdk import Cerebras
from sklearn.metrics.pairwise import cosine_similarity

# Load .env
load_dotenv()

# Get API key securely
api_key = os.getenv("CEREBRAS_API_KEY")

# Initialize client
client = Cerebras(api_key=api_key)

# Load embeddings
df = joblib.load("embedding.joblib")


def inference(prompt):
    r = client.chat.completions.create(
        model="llama3.1-8b",
        messages=[
            {
                "role": "system",
                "content": "You are a strict assistant that answers ONLY using the provided context. Rules - 1. Use only the information from the context. 2. Do not add outside knowledge. 3. Keep the answer short and factual. 4. Do not ask questions."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return r.choices[0].message.content


def rag_pipeline(incoming_query):
    questions_embed = create_embedding(incoming_query)[0]

    similarity = cosine_similarity(
        np.vstack(df['embedding']),
        [questions_embed]
    ).flatten()

    top_k_idx = similarity.argsort()[::-1][:15]

    context = "\n".join(df.iloc[i]["text"] for i in top_k_idx)

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


# Test run
if __name__ == "__main__":
    query = input("Ask: ")
    print(rag_pipeline(query))