import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class APIClient:

    def __init__(self, base_url: str, timeout: int = 10):

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-key": os.getenv('X-API_KEY')
        })

    def get(self, endpoint: str, params: dict | None = None, **kwargs) -> requests.Response:
      
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, timeout=self.timeout, **kwargs)
        logger.info(f"GET {url} → {response.status_code}")
        return response

    def post(self, endpoint: str, data: dict | None = None, **kwargs) -> requests.Response:
        
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=data, timeout=self.timeout, **kwargs)
        logger.info(f"POST {url} → {response.status_code}")
        return response

    def put(self, endpoint: str, data: dict | None = None, **kwargs) -> requests.Response:
       
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, json=data, timeout=self.timeout, **kwargs)
        logger.info(f"PUT {url} → {response.status_code}")
        return response

    def patch(self, endpoint: str, data: dict | None = None, **kwargs) -> requests.Response:
       
        url = f"{self.base_url}{endpoint}"
        response = self.session.patch(url, json=data, timeout=self.timeout, **kwargs)
        logger.info(f"GET {url} → {response.status_code}")
        return response

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
       
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, timeout=self.timeout, **kwargs)
        logger.info(f"GET {url} → {response.status_code}")
        return response

    def close(self):
        self.session.close()
