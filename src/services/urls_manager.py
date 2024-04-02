from typing import Callable

from services.util import CollectorField


class EndPoint:
    def __init__(self, url: str, handler: Callable):
        self.__url = url
        self.__handler = handler
        self.seq = [self.__url, self.__handler]

    @property
    def url(self):
        return self.__url

    @property
    def handler(self):
        return self.__handler

    def __getitem__(self, item):
        return self.seq[item]


class UrlCollector(CollectorField):
    field_type = EndPoint

    @classmethod
    def urls(cls) -> list:
        field_seq: list = super().fields()

        res = []

        for field in field_seq:
            for url, handler in field.items():
                res.append(url)

        return res

    @classmethod
    def endpoints(cls) -> list[dict]:
        return super().fields()
