from openai import OpenAI
from dotenv import load_dotenv
from assignment_chat.prompts import return_instructions
import json
import requests
from utils.logger import get_logger
import os


_logs = get_logger(__name__)

load_dotenv(".env")
load_dotenv(".secrets")


client = OpenAI()

open_ai_model = os.getenv("OPENAI_MODEL", "gpt-4")

# Define a list of callable tools for the model
tools = [
    {
  "type": "function",
  "name": "get_weather",
  "description": "Retrieves current weather for the given location.",
  "parameters": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "City and country e.g. Bogotá, Colombia"
      },
      "units": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "Units the temperature will be returned in."
      }
    },
    "required": ["location", "units"],
    "additionalProperties": False
  },
  "strict": True
}
]

def get_weather(location:str, units:str) -> str:
    """
    An API call to a weather funtion is made.
    The function takes two parameters location and units.
    Accepted values for location are: cities and countries.
    Accepted values for units are: celsius and fahrenheit or their symbols.
    """
    
    response = get_weather_from_service(location, units)
    weather = get_weather_from_response(location, response)
    return weather

def get_weather_from_service(location:str, units:str):
    params = {
        "location": location.capitalize(),
        "units": units.upper()
        }
    response = requests.get(params=params)
    return response

def get_weather_from_response(location:str, response:requests.Response) -> str:
    resp_dict = json.loads(response.text)
    data = resp_dict.get("data")
    weather_data = data.get("weather_data", "No weather found.")
    units = data.get("units", "No units found.")
    weather = f"Weather for {location.capitalize()} in {units}: {weather_data}"
    return weather

def sanitize_history(history: list[dict]) -> list[dict]:
    clean_history = []
    for msg in history:
        clean_history.append({
            "role": msg.get("role"),
            "content": msg.get("content")
            })
        return clean_history
    

def tools_weather(message: str, history: list[dict] = []) -> str:
    _logs.info(f'User message: {message}')
    
    instructions = return_instructions()
    
    user_msg = {
        "role": "user",
        "content": message
    }
    
    conversation_input = sanitize_history(history) + [user_msg]
    
# Prompt the model with tools defined
    response = client.responses.create(
        model=open_ai_model,
        instructions=instructions,
        input=conversation_input,
        tools=tools,

)
    
# Save function call outputs for subsequent requests
    conversation_input += response.output

# Handle function calls if any
    for item in response.output:
        if item.type == "function_call":
            if item.name == "get_weather":
                args = json.loads(item.arguments)
                _logs.info(f'Function call args: {args}')
            
                # Call the horoscope function
                weather_result = get_weather(**args)
                
                # Add function call result to conversation
                func_call_output = {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps({
                        "weather": weather_result
                    })
                }
                
                _logs.debug(f"Function call output: {func_call_output}")
                
                conversation_input = conversation_input + [func_call_output]
                
                # Make second API call with function result
                response = client.responses.create(
                    model=open_ai_model,
                    instructions=instructions,
                    tools=tools,
                    input=conversation_input
                )
                break


    return response.output_text