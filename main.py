import requests as req
from config import ACCESS_TOKEN
import json

def getNotifications():
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "token {}".format(ACCESS_TOKEN)
        }
        url = "https://api.github.com/notifications"

        with req.Session() as session:
            session.headers.update(headers)
            resp = session.get(url)
            resp.raise_for_status()
            return resp.json()
    except Exception as E:
        print(f"Error occured: {E}")

if __name__ == "__main__":
    resp = getNotifications()
    print(resp, type(resp))

    with open('resp.json', 'w') as fileObject:
        json.dump(resp, fileObject)
