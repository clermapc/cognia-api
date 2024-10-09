from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from app.models import openai_model
from app.models.pydantic_models import TextGenerationInput, TextGenerationOutput

prompt = ChatPromptTemplate.from_template("Generate a short text about {topic}")
model = openai_model.get_model()

def generate_text(input: TextGenerationInput) -> TextGenerationOutput:
    result = model(prompt.format(topic=input.topic))
    return TextGenerationOutput(generated_text=result.content)

chain = generate_text