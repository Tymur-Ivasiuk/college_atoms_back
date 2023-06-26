import requests
import os
from dotenv import load_dotenv

load_dotenv()


def create_zvit(title, date, executor):
    response = requests.post(
        os.environ.get("LINK_APPS_SCRIPT"),
        data={
            'password': os.environ.get('PASSWORD'),
            'title': title,
            'date': date,
            'executor': executor
        }
    )
    print(response.json())
    return response.json()['newDocUrl']


