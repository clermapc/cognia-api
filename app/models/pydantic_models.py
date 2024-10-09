from pydantic import BaseModel, Field

class TextGenerationInput(BaseModel):
    topic: str = Field(..., description="The topic to generate text about")

class TextGenerationOutput(BaseModel):
    generated_text: str = Field(..., description="The generated text")

class SummarizationInput(BaseModel):
    text: str = Field(..., description="The text to summarize")

class SummarizationOutput(BaseModel):
    summary: str = Field(..., description="The summarized text")

class QuestionAnsweringInput(BaseModel):
    question: str = Field(..., description="The question to be answered")

class QuestionAnsweringOutput(BaseModel):
    answer: str = Field(..., description="The answer to the question")

class ImageGenerationInput(BaseModel):
    image_desc: str = Field(..., description="The description of the image to generate")

class ImageGenerationOutput(BaseModel):
    image_url: str = Field(..., description="The URL of the generated image")
    enhanced_prompt: str = Field(..., description="The enhanced prompt used for image generation")