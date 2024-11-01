# InsightIQ: Intelligent Document Question Answering Bot

## 🚀 Project Overview
**InsightIQ** is an advanced question-answering bot designed to retrieve and generate highly contextual answers based on document content. Built using powerful NLP and vector search techniques, InsightIQ efficiently scans, understands, and answers user questions by retrieving relevant text segments from large documents and leveraging sophisticated language models for natural, precise responses.

## ✨ Features
- **Contextual QA Capability**: Utilizes Sentence Transformers for generating text embeddings, ensuring that answers are directly relevant to the document context.
- **Fast, Scalable Vector Search**: Pinecone is integrated for quick and scalable document segment retrieval, ideal for high-performance applications.
- **State-of-the-Art Response Generation**: Powered by Groq’s LLaMA 3.1 API, the bot provides well-formed, accurate answers based on retrieved context.
- **Intuitive Front-End with Streamlit**: A user-friendly interface enables seamless interaction, making it easy to ask questions and explore document insights.
- **Portable and Scalable with Docker**: Containerized for quick deployment, enabling easy scalability and environment compatibility.

## 🛠️ Tech Stack
- **Backend**: Python, Sentence Transformers, Pinecone, Groq's LLaMA API
- **Frontend**: Streamlit
- **Deployment**: Docker

## ⚙️ Installation and Setup

### Prerequisites
- **Python 3.7+**
- **Docker**
- API keys for Pinecone and Groq (sign up for access if needed)

### Steps to Set Up

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/InsightIQ.git
    cd InsightIQ
    ```

2. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure API Keys**:
    Set up your API keys as environment variables:
    ```bash
    export PINECONE_API_KEY='your_pinecone_api_key'
    export GROQ_API_KEY='your_groq_api_key'
    ```

4. **Run in Docker**:
    Build and start the container:
    ```bash
    docker build -t insightiq .
    docker run -p 8501:8501 insightiq
    ```

5. **Access the Interface**:
    Open a browser and go to `http://localhost:8501` to begin interacting with InsightIQ.

## 📝 Usage Guide
- **Ask Your Question**: Input a question in the query box and submit.
- **View Results**: The bot retrieves relevant content from the document and generates an answer.

## 📂 Project Structure
- `app.py`: Contains the Streamlit front end, designed for intuitive query interaction.
- `backend.py`: Manages the backend processes, including chunking, embedding, and answer generation.
- `requirements.txt`: Lists all dependencies needed for the project.
- `Dockerfile`: Defines the environment for containerized deployment.

## 🚀 Future Plans
- Support larger datasets and multi-document querying
- Add caching for frequently asked questions to speed up response times
- Expand model choices for answer generation based on document type

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 👤 Author
Created by **S. Venkat Sai Reddy** - feel free to reach out with questions or collaboration ideas!
