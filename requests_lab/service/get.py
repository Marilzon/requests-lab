import requests

def get_url_data(url, params=None):
  if not params:
    params = {}
  response = requests.get(url, params = params)
  response.raise_for_status()
  data = response.json()

  return data