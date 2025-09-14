import requests

def post_to_jsonplaceholder(url, data):
  if not data:
    data = {}
    
  post = requests.post(url, json=data)
  
  return post.json()