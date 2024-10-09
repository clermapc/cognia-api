from langchain.prompts import ChatPromptTemplate
from langchain.llms import HuggingFacePipeline
from app.models import huggingface_model
from app.models.pydantic_models import QuestionAnsweringInput, QuestionAnsweringOutput

prompt = ChatPromptTemplate.from_template("Question: {question}\n\nAnswer:")
model = huggingface_model.get_model()

def answer_question(input: QuestionAnsweringInput) -> QuestionAnsweringOutput:
    result = model(prompt.format(question=input.question))
    return QuestionAnsweringOutput(answer=result)

chain = answer_question