from langchain.tools import tool
import json
import requests

@tool
def search_recipes(recipe:str):
    """
    Returns thousands of recipes using advanced filtering and ranking. 
    This method combines searching by query, by ingredients, and by nutrients into one endpoint.
    """
    url = "https://api.spoonacular.com/recipes/complexSearch"
    response = requests.get(url, recipe)
    resp_dict = json.loads(response.text)
    recipe_list = resp_dict.get("data", [])
    recipe = "\n".join([f"{i+1}. {recipe}\n" for i, recipe in enumerate(recipe_list)])
    return recipe