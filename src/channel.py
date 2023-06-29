import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id__ = channel_id
        dict_to_print = youtube.channels().list(id=self.__channel_id__, part='snippet,statistics').execute()
        self.title = dict_to_print['items'][0]['snippet']['title']
        self.description = dict_to_print['items'][0]['snippet']['description']
        self.subscriber_count = dict_to_print['items'][0]['statistics']['subscriberCount']
        self.video_count = dict_to_print['items'][0]['statistics']['videoCount']
        self.view_count = dict_to_print['items'][0]['statistics']['viewCount']
        self.url = f'https://youtu.be/{dict_to_print["etag"]}'

    def __str__(self):
        return f'{self.title} - {self.url}'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)


    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=api_key)

    @property
    def channel_id(self):
        return self.channel_id

    def to_json(self, filename):
        with open (filename, 'w') as file:
            file.write(json.dumps({
                "channel_id": self.__channel_id__,
                "title": self.title,
                "description": self.description,
                "subscriber_count": self.subscriber_count,
                "video_count": self.video_count,
                "view_count": self.view_count
            }, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    channel1 = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    channel2 = Channel('UCwHL6WHUarjGfUM_586me8w')