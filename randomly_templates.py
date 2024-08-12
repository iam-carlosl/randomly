import flet as ft
from calet_theme import ClTheme

class RlyAppSection(ft.UserControl):

    def __init__(self, theme:ClTheme, position:str="center"):
        super().__init__()
        self.theme = theme
        self.offset = ft.Offset(x={"left": -1, "center": 0, "right": 1}[position], y=0)
        self.expand = True
        self.animate_offset = ft.Animation(300, ft.AnimationCurve.LINEAR_TO_EASE_OUT)

    def build(self):

        # GENERATED RESULT PANEL
        # - result text
        self.result = ft.Text(
            value="",
            color=self.theme.font_two,
            size=40,
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD
        )
        # - result panel
        self.result_panel = ft.Container(
            expand=True,
            padding=5,
            alignment=ft.alignment.center,
            content=self.result
        )

        # ACTIONS PANEL
        self.actions = ft.Row(
            expand=1,
            spacing=5,
            controls=[]
        )

        # SECTION
        self.section = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                spacing=5,
                controls=[
                    ft.Row(expand=4, controls=[self.result_panel]),
                    self.actions
                ]
            )
        )

        return self.section

    def upd(self, position:str=None):

        if position is not None:
            self.offset.x = {"left": -1, "center": 0, "right": 1}[position]
        self.update()