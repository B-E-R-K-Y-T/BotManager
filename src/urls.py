from services.urls_manager import UrlCollector, EndPoint
from views.add_bot import AddBotPage


class Urls(UrlCollector):
    ADD_BOT_PAGE: EndPoint = EndPoint('/add_bot', AddBotPage)
