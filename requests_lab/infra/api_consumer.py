import requests, json


class APIConsumer:
    @classmethod
    def get(self, url: str, kind: str, page: int) -> json:
        params = {"page": page}
        response = requests.get(f"{url}/{kind}", params=params)

        return response.json()
