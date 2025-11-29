# Sentiment Analysis API (FastAPI + LangChain)

A simple sentiment analysis API built using **FastAPI**, **LangChain**, and **OpenAI's Chat Completions API**.  
It analyzes any input text and returns:

- **sentiment**: `positive`, `negative`, or `neutral`
- **explanation**: why the model chose that label

------------------------------------------------------------------------

## 🚀 Features

-   Lightweight FastAPI backend
-   Uses OpenAI GPT models
-   Clean structured JSON output
-   Docker support
-   Interactive API docs via Swagger UI (`/docs`)

------------------------------------------------------------------------

## 📁 Project Structure

    .
    ├── main.py
    ├── requirements.txt
    ├── Dockerfile
    ├── .env
    └── README.md

------------------------------------------------------------------------

## 🔧 Requirements

-   Python 3.10+
-   OpenAI API Key
-   (Optional) Docker

------------------------------------------------------------------------

## 🔑 Environment Variables

Create a `.env` file in the project root:

    OPENAI_API_KEY=your_openai_api_key_here

------------------------------------------------------------------------

## 🏃 Run Locally (Without Docker)

### 1. Create and activate virtual environment

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

``` bash
pip install -r requirements.txt
```

### 3. Start the API server

``` bash
uvicorn main:app --reload
```

### 4. Open in browser

-   API Root → http://127.0.0.1:8000\
-   Swagger Docs → http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 🐳 Run with Docker

### 1. Build the image

``` bash
docker build -t sentiment-api .
```

### 2. Run the container

``` bash
docker run -p 8000:8000 --env-file .env sentiment-api
```

### 3. Access the API

-   http://localhost:8000\
-   Swagger docs: http://localhost:8000/docs

------------------------------------------------------------------------

## 📡 Example Request

### POST `/analyze-sentiment`

#### Request Body:

``` json
{
  "text": "I absolutely love this new product!"
}
```

#### Example Response:

``` json
{
  "sentiment": "positive",
  "explanation": "The text expresses strong appreciation and enthusiasm."
}
```

------------------------------------------------------------------------
