from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.tools import DallEAPIWrapper
from app.models import openai_model
from app.models.pydantic_models import ImageGenerationInput, ImageGenerationOutput

prompt = PromptTemplate(
    input_variables=["image_desc"],
    template="Generate a detailed prompt for DALL-E to create an image based on this description: {image_desc}"
)

llm = openai_model.get_model()
llm_chain = LLMChain(llm=llm, prompt=prompt)
dalle_tool = DallEAPIWrapper()

def generate_image(input: ImageGenerationInput) -> ImageGenerationOutput:
    enhanced_prompt = llm_chain.run(input.image_desc)
    image_url = dalle_tool.run(enhanced_prompt)
    return ImageGenerationOutput(image_url=image_url, enhanced_prompt=enhanced_prompt)

chain = generate_image