import os 
from dotenv import load_dotenv

load_dotenv()

NASA_DEMO_KEY = os.getenv("NASA_DEMO_KEY")
NASA_BASE_URL = "https://api.nasa.gov/planetary/apod"
POKE_BASE_URL = "https://pokeapi.co/api/v2/pokemon"
JSONPL_BASE_URL = "https://jsonplaceholder.typicode.com"