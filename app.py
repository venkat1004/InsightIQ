import streamlit as st
import pdfplumber
from backend import index_document, retrieve_and_generate_answer  # Import from backend.py

# Streamlit interface
def main():
    st.title("QA Bot with Document Upload")
    
    # File upload
    uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")
    
    if uploaded_file:
        # Load and index the PDF document
        with pdfplumber.open(uploaded_file) as pdf:
            document = ''.join([page.extract_text() for page in pdf.pages])
        chunks = index_document(document)
        st.success("Document uploaded and processed successfully.")
        
        # Ask a question
        query = st.text_input("Ask a question based on the document:")
        
        if query:
            # Generate and display the answer
            retrieved_text, answer = retrieve_and_generate_answer(query, chunks)
            st.subheader("Answer:")
            st.write(answer)
            
            # Display the retrieved document segments
            st.subheader("Retrieved Document Segments:")
            st.write(retrieved_text)

if __name__ == "__main__":
    main()
