import flet as ft
from randomly_app import RlyApp

def main(page: ft.Page):

    page.padding = 0
    page.window_width = 400
    page.window_height = 300
    page.window_resizable = False
    page.window_title_bar_hidden = True
    page.window_frameless = True
    page.window_bgcolor = "#00000000"
    page.bgcolor = "#00000000"
    page.dark_theme = ft.Theme(color_scheme_seed="purple")
    page.theme_mode = ft.ThemeMode.DARK
    page.window_center()

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=RlyApp()
        )
    )

if __name__ == "__main__":

    ft.app(target=main, assets_dir="assets")