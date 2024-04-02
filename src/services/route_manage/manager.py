import flet as ft

from urls import Urls
from pages.not_found_page import NotFoundPage
from pages.root import RootPage


class RouteManager:
    def __init__(self, page: ft.Page):
        self.page = page

        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go(self.page.route)

    async def route_change(self, route):
        root_page = RootPage(self.page, route="/")
        self.page.views.clear()
        self.page.views.append(root_page)

        if self.page.route == "/":
            self.page.update()
            await root_page.start_animate()

            return
        elif self.page.route in Urls.urls():
            for endpoint in Urls.endpoints():
                if self.page.route in endpoint:
                    site_page = endpoint[self.page.route](self.page, route=self.page.route)

                    self.page.views.append(site_page)
                    self.page.update()

                    await site_page.start_animate()

                    break
        else:
            not_found = NotFoundPage(self.page, route=self.page.route)
            self.page.views.append(not_found)
            self.page.update()

            await not_found.start_animate()

    async def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
