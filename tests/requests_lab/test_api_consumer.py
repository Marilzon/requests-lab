from requests_lab.infra.api_consumer import APIConsumer
from requests_lab.infra.definitions import BASE_URL, STARSHIPS


class TestAPIConsumer:
    """
    Testing get method
    """

    api_consumer = APIConsumer

    def test_get_starships(self):
        response = self.api_consumer.get(url=BASE_URL, kind=STARSHIPS, page=1)
        assert isinstance(response, dict)
        assert "results" in response
