from sentence_transformers import SentenceTransformer
import os
from pinecone import Pinecone, ServerlessSpec
from groq import Groq

# Initialize Pinecone and embedding model
api_key = 'bdb54859-0658-427c-9142-2153417ddda1'  # Replace with your actual Pinecone API key
pc = Pinecone(api_key=api_key)
model = SentenceTransformer('all-mpnet-base-v2')  # Embedding model

# Check if index exists, else create one
index_name = 'qa-bot'
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=768,
        metric='euclidean',
        spec=ServerlessSpec(cloud='aws', region='us-east-1')
    )

index = pc.Index(index_name)

# Initialize Groq API
os.environ['groq_api_key'] = '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'
client = Groq(api_key=os.environ['groq_api_key'])

# Function to index document embeddings
def index_document(document):
    chunks = document.split('. ')  # Basic sentence chunking
    embeddings = model.encode(chunks)

    for i, embed in enumerate(embeddings):
        index.upsert(vectors=[(str(i), embed)])
    
    return chunks

# Function to retrieve and generate answers
def retrieve_and_generate_answer(query, chunks):
    query_embedding = model.encode([query])[0]
    
    # Query Pinecone
    result = index.query(vector=query_embedding.tolist(), top_k=3, include_metadata=True)
    retrieved_text = ' '.join([chunks[int(match['id'])] for match in result['matches'] if int(match['id']) < len(chunks)])

    # Generate answer with Groq's LLaMA model
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": f"Context: {retrieved_text}\nQuestion: {query}"}],
        model="llama3-70b-8192",
    )
    
    answer = chat_completion.choices[0].message.content
    return retrieved_text, answer
