import vertexai
from vertexai.preview.language_models import TextGenerationModel
from .constants import PROJECT

vertexai.init(project=PROJECT, location="us-central1")


def query_ai(interested_policy: str, politician_name: str, website_text: str):
    parameters = {
        "max_output_tokens": 1024,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }

    model = TextGenerationModel.from_pretrained("text-bison-32k")

    prompt = f'''
    Given the following text scraped from the politicians website,
    give a summary of the politicians view on the specified topic/policy. 
    
    Relevant Policy: {interested_policy}.
    Politicians Name: {politician_name}.
    Website Text:
    {website_text}
    '''

    response = model.predict(prompt, **parameters)

    return response.text
