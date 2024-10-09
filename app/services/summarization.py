from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatAnthropic
from app.models import anthropic_model
from app.models.pydantic_models import SummarizationInput, SummarizationOutput

prompt = ChatPromptTemplate.from_template("Summarize the following text:\n\n{text}")
model = anthropic_model.get_model()

def summarize(input: SummarizationInput) -> SummarizationOutput:
    result = model(prompt.format(text=input.text))
    return SummarizationOutput(summary=result.content)

chain = summarize