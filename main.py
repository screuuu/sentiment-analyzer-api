import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# LangChain Imports
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


# Load environment variables (specifically OPENAI_API_KEY)
load_dotenv()


app = FastAPI(title="Sentiment Analysis API")

# --- Data Models ---
class SentimentRequest(BaseModel):
    text: str = Field(..., description="The text to analyze", example="I absolutely love this new product, it's fantastic!")

class SentimentResponse(BaseModel):
    sentiment: str = Field(..., description="positive, negative, or neutral")
    explanation: str = Field(..., description="Why the AI chose this sentiment")

# --- LangChain Setup ---

# 1. Initialize the LLM

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 2. Define the parser to ensure we get clean JSON back
response_schemas = [
    ResponseSchema(
        name="sentiment",
        description="The sentiment of the text: positive, negative, or neutral"
    ),
    ResponseSchema(
        name="explanation",
        description="Explanation for why this sentiment was chosen"
    )
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

# 3. Create the prompt template
# We inject format instructions so the LLM knows strictly how to structure the JSON.
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful sentiment analysis assistant. Use the required JSON format. {format_instructions}"),
    ("user", "{text}")
])

# 4. Create the Chain using LCEL (LangChain Expression Language)
chain = prompt_template | llm | parser

# --- Endpoints ---

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API. POST to /analyze-sentiment to use."}

@app.post("/analyze-sentiment", response_model=SentimentResponse)
async def analyze_sentiment(request: SentimentRequest):
    try:
        # Invoke the LangChain chain
        result = chain.invoke({
            "text": request.text,
            "format_instructions": parser.get_format_instructions()
        })
        return result
    except Exception as e:
        # In a real app, you would log the error properly
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Run the server locally
    uvicorn.run(app, host="0.0.0.0", port=8000)