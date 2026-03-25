import json
import requests

url = "https://dummyjson.com/comments"
response = requests.get(url)
comments = response.json()
nimi = "jaces"

for comment in comments['comments']:
   
    if nimi == comment['user']['username']:
         print(comment['body'])

komentaarid = len(comments['comments'])
print(f"Koguarv kommentaare: {komentaarid}")

rohkem_meeldinud_komentaarid = max(comments['comments'], key=lambda x: x['likes'])
print(f"Enim meeldimisi saanud kommentaar: {rohkem_meeldinud_komentaarid['body']} - Meeldimised: {rohkem_meeldinud_komentaarid['likes']}")


