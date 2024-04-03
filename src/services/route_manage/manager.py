import flet as ft
from flet_core import TemplateRoute

from pages.bot_menu import BotMenuPage
from urls import Urls
from pages.not_found_page import NotFoundPage
from pages.root import RootPage


class RouteManager:
    def __init__(self, page: ft.Page):
        self.template_route = None
        self.page = page

        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go(self.page.route)

    async def init_site_page(self, site_page):
        self.page.views.append(site_page)

        await site_page.async_init()

        self.page.update()

        await site_page.start_animate()

    async def route_change(self, route):
        root_page = RootPage(self.page, route="/")
        self.page.views.clear()
        self.page.views.append(root_page)
        self.template_route = TemplateRoute(self.page.route)

        if self.page.route == "/":
            self.page.update()
            await root_page.start_animate()

            return
        elif self.template_route.match(Urls.BOT_MENU_PAGE.url):
            bot_id = self.template_route.bot_id
            site_page: BotMenuPage = Urls.BOT_MENU_PAGE.handler(
                self.page,
                route=Urls.BOT_MENU_PAGE.url,
                bot_id=bot_id
            )

            if not site_page.check_bot_exist():
                await self.init_page_not_found()
                return

            await self.init_site_page(site_page)
        elif self.page.route in Urls.urls():
            for endpoint in Urls.endpoints():
                if self.page.route in endpoint:
                    site_page = endpoint[self.page.route](self.page, route=self.page.route)

                    await self.init_site_page(site_page)

                    break
        else:
            await self.init_page_not_found()

    async def init_page_not_found(self):
        not_found = NotFoundPage(self.page, route=self.page.route)
        self.page.views.append(not_found)
        self.page.update()

        await not_found.start_animate()

    async def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
