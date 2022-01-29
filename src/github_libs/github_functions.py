from urllib import response
import requests as req
from requests.exceptions import HTTPError
from requests.adapters import HTTPAdapter

from config import ACCESS_TOKEN, GITHUB_API_ROOT_URL

class GitHubFunctions:

    def __init__(self) -> None:
        self.headers = {
            "Authorization": "token {}".format(ACCESS_TOKEN)
        }
        self.url = GITHUB_API_ROOT_URL
        self.github_adapter = HTTPAdapter(max_retries=3)

    def getNotifications(self):
        self.url += f"/notifications"
        try:
            session = req.Session()
            session.headers.update(self.headers)
            session.mount(self.url, self.github_adapter)
            response = session.get(self.url)
            response.raise_for_status
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Error Occurred: {err}")
