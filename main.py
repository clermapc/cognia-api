from fastapi import FastAPI
from langserve import add_routes
from dotenv import load_dotenv
from app.services import text_generation, summarization, question_answering, image_generation
from app.models.pydantic_models import (
    TextGenerationInput, TextGenerationOutput,
    SummarizationInput, SummarizationOutput,
    QuestionAnsweringInput, QuestionAnsweringOutput,
    ImageGenerationInput, ImageGenerationOutput
)

load_dotenv()

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    text_generation.chain,
    path="/text-generation",
    input_type=TextGenerationInput,
    output_type=TextGenerationOutput,
)

add_routes(
    app,
    summarization.chain,
    path="/summarization",
    input_type=SummarizationInput,
    output_type=SummarizationOutput,
)

add_routes(
    app,
    question_answering.chain,
    path="/question-answering",
    input_type=QuestionAnsweringInput,
    output_type=QuestionAnsweringOutput,
)

add_routes(
    app,
    image_generation.chain,
    path="/image-generation",
    input_type=ImageGenerationInput,
    output_type=ImageGenerationOutput,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)