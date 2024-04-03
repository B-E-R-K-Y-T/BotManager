from pages.bot_menu import BotMenuPage
from services.url_manage.manager import UrlCollector, EndPoint
from pages.add_bot import AddBotPage
from pages.view_bots import ViewBotsPage


class Urls(UrlCollector):
    ADD_BOT_PAGE: EndPoint = EndPoint("/add_bot", AddBotPage)
    VIEW_BOTS_PAGE: EndPoint = EndPoint("/view_bots", ViewBotsPage)
    BOT_MENU_PAGE: EndPoint = EndPoint("/bot_menu/:bot_id", BotMenuPage)
