import requests
import uuid
from colorama import Fore, Style, init
from typing import Optional


init(autoreset=True)


def url(username: str, slug: Optional[str], question: str):
    device_id = str(uuid.uuid4())

    endpoint = "https://ngl.link/api/submit"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": f"https://ngl.link/{username}/{slug}",
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    payload = {
        "username": username,
        "question": question,
        "deviceId": device_id,
        "gameSlug": slug,
        "referrer": ""
    }

    response = requests.post(
        endpoint,
        data=payload,
        headers=headers,
        timeout=30
    )

    if response.status_code == 200:
        data = response.json()
        print("MESSAGE SENT")
    else:
        print("USERNAME IS NOT EXIST")

    try:
        data = response.json()
    except ValueError:
        data = {"error": "Non-JSON response", "text": response.text[:200]}

    return {
        "error": "Request failed",
        "status_code": response.status_code,
        "data": data,
    }


def send_message(username: str, slug: str | None, question: str, count: int):
    for i in range(count):
        url(username, slug, question)

