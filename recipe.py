from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import time 
from detect import get_ingredients_from_image

def generate_recipe(ingredients):
    # model = Ollama(model="llama3.2:1b")
    ingredients = ','.join(ingredients)
    model = Ollama(model="mistral:latest")
    # Create a prompt template for analysis
    prompt_template = PromptTemplate(
        input_variables=["ingredients"],
        template="generate 3 recipes from the given list of ingredients and return a only  JSON object with a recipe .\n\nIngredients:\n{ingredients}\n\nOutput JSON format: {{\"recipe\": score}}"
    )
    
    # Create an LLM chain
    llm_chain = LLMChain(llm=model, prompt=prompt_template)
    
    # Run the analysis
    result = llm_chain.run(ingredients = ingredients)
    
    return result

print(generate_recipe(get_ingredients_from_image('./fruits.jpg')))

