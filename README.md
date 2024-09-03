# 🇱🇰 🔍 LankaDoc Talk

LankaDoc Talk is an AI-powered chatbot application designed to interact with the contents of PDF documents using **LLAMA 3.1** with **Groq**, **Retrieval-Augmented Generation (RAG)**, **Langchain**, and **Generative AI**. Users can upload PDF files and ask questions to get relevant answers, making it a powerful tool for extracting and understanding information from documents.


## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **PDF Document Interaction**: Upload and analyze PDF documents by asking natural language questions.
- **LLAMA 3.1 and Groq Integration**: Leverages cutting-edge AI models for natural language processing and understanding.
- **Retrieval-Augmented Generation (RAG)**: Enhances the accuracy and relevance of answers by retrieving related document segments.
- **Conversational Memory**: Maintains chat history to provide context-aware responses.
- **User-Friendly Interface**: Designed with a responsive and aesthetically pleasing UI/UX using Streamlit.

## Technologies Used

- **[LLAMA 3.1](https://github.com/facebookresearch/llama)**: A large language model for natural language processing.
- **[Groq](https://groq.com/)**: Hardware acceleration for AI/ML tasks.
- **[Langchain](https://www.langchain.com/)**: A framework for building applications powered by language models.
- **[RAG](https://www.pinecone.io/learn/retrieval-augmented-generation/)**: Retrieval-Augmented Generation for improving the contextual relevance of AI-generated answers.
- **[Streamlit](https://streamlit.io/)**: A framework for building data applications with minimal code.
- **[FAISS](https://github.com/facebookresearch/faiss)**: Facebook AI Similarity Search for efficient document retrieval.
- **[HuggingFace Transformers](https://huggingface.co/transformers/)**: A library for Natural Language Processing tasks.

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (e.g., `venv`, `conda`)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pahinithi/LankaDoc-Talk-and-LangChain-with-Streamlit-Generative-artificial-intelligence
   cd LankaDoc-Talk/src
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   Or with `conda`:
   ```bash
   conda create --name lankadoc_talk python=3.8
   conda activate lankadoc_ttalk
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r ../requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the `src` directory and add the necessary environment variables. Example:
   ```plaintext
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   ```

5. **Run the application:**
   ```bash
   streamlit run main.py
   ```

## Usage

1. **Upload a PDF File:**
   - Click the "Upload your PDF file" button and select a PDF document from your local system.

2. **Ask Questions:**
   - Use the input field to ask questions related to the content of the uploaded PDF. The chatbot will respond with relevant information extracted from the document.

3. **Review the Conversation:**
   - Scroll through the chat history to review the conversation, including both your questions and the AI's responses.

4. **Reset or Start Over:**
   - To start a new conversation or upload a different PDF, refresh the page or clear the chat history.

## Screenshots

<img width="1728" alt="LLM04" src="https://github.com/user-attachments/assets/f4907bb5-3773-4c9e-988d-b8a410e5d8e1">


## Project Structure

```
LankaDoc-Talk/
│
├── requirements.txt        # Required Python packages
├── screenshots/            # Folder for screenshots
│   ├── main_interface.png
│   ├── pdf_upload.png
│   └── chat_interaction.png
├── src/
│   ├── main.py             # Main Streamlit application
│   ├── .env.example        # Example environment file
│   ├── sample.pdf          # Sample PDF file for testing
│   └── 25.Thanuja Rajapakshe1 Sanath Divakara2.pdf # Example PDF
└── README.md               # This README file
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request. You can also report any issues or suggest new features by opening an issue.

## License

This project is licensed under the MIT License.

## Contact

For any questions or support, please contact:

- **Name**: Pahirathan Nithilan
- **Email**: [nithilan32@gmail.com](mailto:nithilan32@gmail.com)
- **GitHub**: [Pahinithi](https://github.com/Pahinithi)

