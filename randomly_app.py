import flet as ft
from calet_theme import ClTheme, ClLightTheme, ClDarkTheme
from calet_bar import ClAppBar, ClSelectionBar
from calet_button import ClWinButton, ClSlideButton
from randomly_numbers import RlyNumbersSection
from randomly_choices import RlySelectionSection

class RlyApp(ft.UserControl):

    def __init__(self):

        super().__init__()
        self.theme = ClTheme(
            on_light=ClLightTheme(),
            on_dark=ClDarkTheme(
                background_one="#6E32A0",
                background_two="#001E5F",
                primary=ft.colors.PURPLE_900,
                divider=ft.colors.with_opacity(0.3, "black")
            ),
            mode="dark"
        )
        self.expand = True
    
    def build(self):

        # APP BAR
        self.app_bar = ClAppBar(
            theme=self.theme,
            title="Randomly",
            left_icon=ft.icons.LOCAL_PLAY,
            left_title=True,
            transparent=True,
            can_maximize=False,
            high_title_color=True,
            win_actions=[
                ClWinButton(theme=self.theme, winaction="minimize"),
                ClWinButton(theme=self.theme, action=self.b_close_clicked)
            ]
        )

        # APP SECTION
        # - numbers section
        self.app_numbers_section = RlyNumbersSection(theme=self.theme)
        # - choices section
        self.app_choices_section = RlySelectionSection(theme=self.theme, position="right")
        # - sections slide
        self.app_sections_slide = ClSelectionBar(
            expand=True,
            theme=self.theme,
            options=[
                ClSlideButton(
                    theme=self.theme,
                    text="Número aleatorio",
                    content_size=12,
                    selected=True,
                    action=self.b_numbers_section_clicked
                ),
                ClSlideButton(
                    theme=self.theme,
                    text="Selección aleatoria",
                    content_size=12,
                    selected=False,
                    action=self.b_choices_section_clicked
                )
            ]
        )

        # APP
        # - app content
        self.app_content = ft.Container(
            expand=True,
            padding=ft.padding.only(left=10, right=10, bottom=10),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Divider(thickness=1, height=1, color=self.theme.divider),
                    ft.Row(
                        expand=3, 
                        controls=[
                            ft.Stack(
                                expand=True,
                                controls=[
                                    self.app_numbers_section,
                                    self.app_choices_section
                                ]
                            )
                        ]
                    ),
                    ft.Row(expand=1, controls=[self.app_sections_slide])
                ]
            )
        )
        # - app
        self.app = ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                colors=[self.theme.background_one, self.theme.background_two],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center
            ),
            border_radius=10,
            content=ft.Column(
                spacing=0,
                controls=[
                    self.app_bar,
                    self.app_content
                ]
            )
        )

        return self.app

    def b_numbers_section_clicked(self, e:ft.TapEvent):
        self.app_numbers_section.upd(position="center")
        self.app_choices_section.upd(position="right")
    
    def b_choices_section_clicked(self, e:ft.TapEvent):
        self.app_numbers_section.upd(position="left")
        self.app_choices_section.upd(position="center")

    def b_close_clicked(self, e:ft.TapEvent):
        self.app_choices_section.close_choices_page()
        self.page.window_destroy()
