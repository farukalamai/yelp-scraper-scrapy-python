# C
## Deployment

#### 1. Clone Repository 

```bash
  git clone https://github.com/farukalampro/ai-chatbot-using-Langchain-Pinecone.git
```
```bash
  cd ai-chatbot-using-Langchain-Pinecone
```
#### 2. Create Virtual Environment
```bash
  python -m venv env
```
 - For Windows:
```bash
  .\env\Scripts\activate
```
 - For macOS/Linux:
```bash
  source env/bin/activate
```

#### 3. To install require packages 

```bash
  pip install -r requirements.txt
```
#### 4. Replace your own document in **data** folder

#### 5. Replace your own OpenAI, Pinecone API Key and Pinecone environment in indexing.py, main.py & utils.py
 - [OpenAI API Key](https://platform.openai.com)
 - [Pinecone](app.pinecone.io)
   - When you are creating the pinecone index make sure, **Dimensions of the index is 384**
 
#### 6. Run the web app
```bash
  streamlit run main.py
```
