import jason
import requests


url= "https://dummyjson.com/comments"


response = requests.get(url)

# if response.status_code == 200: