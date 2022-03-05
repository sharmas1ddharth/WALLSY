import requests
import config


class Wallpaper:
    def __init__(self, path, keyword="8k"):
        self.URL = f"https://api.pexels.com/v1/search?query={keyword}&orientation=landscape&size=large&per_page=1"
        self.HEADERS = {"Authorization": f"{config.api_key}"}
        self.JSON = self.get_json()
        self.path = path

    def get_json(self):
        response = requests.get(self.URL, headers=self.HEADERS)
        return response.json()

    def download(self):
        json_object = self.JSON
        response = requests.get(json_object['photos'][0]['src']['large2x'])
        filename = json_object['photos'][0]['alt']
        with open(f"{self.path}/{filename}.jpeg", "wb") as f:
            f.write(response.content)
