import requests


def get_url(url: str) -> requests.models.Response | str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
