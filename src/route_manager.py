import flet as ft


from urls import URLS
from views.not_found_page import NotFound
from views.root import Root


class RouteManager:
    def __init__(self, page: ft.Page):
        self.page = page

        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go(self.page.route)

    async def route_change(self, route):
        self.page.views.clear()
        self.page.views.append(
            Root(self.page, route="/")
        )

        if self.page.route == "/":
            self.page.update()
            return

        elif self.page.route in URLS:
            self.page.views.append(URLS[self.page.route](self.page, route=self.page.route))
            self.page.update()
        else:
            not_found = NotFound(self.page, route=self.page.route)
            self.page.views.append(not_found)
            self.page.update()

            await not_found.start_animate()

    async def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
