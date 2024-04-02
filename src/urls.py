from services.urls_manager import UrlCollector, EndPoint
from views.add_bot import AddBotPage
from views.view_bots import ViewBotsPage


class Urls(UrlCollector):
    ADD_BOT_PAGE: EndPoint = EndPoint("/add_bot", AddBotPage)
    VIEW_BOTS_PAGE: EndPoint = EndPoint("/view_bots", ViewBotsPage)
