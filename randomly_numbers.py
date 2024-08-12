import flet as ft
from calet_theme import ClTheme
from calet_button import ClCristalButton
from randomly_templates import RlyAppSection
from randomly_control import RlyNumbersController

class RlyNumbersSection(RlyAppSection):

    def __init__(self, theme:ClTheme, position:str="center"):
        super().__init__(theme=theme, position=position)
        self.controller = RlyNumbersController()

    def build(self):
        
        super().build()

        # LIMITS CONFIGURATION
        # - left limit input field
        self.left_limit = ft.TextField(
            expand=1,
            value="0",
            text_size=12,
            content_padding=5,
            text_align=ft.TextAlign.CENTER,
            color=self.theme.font_two,
            focused_color=self.theme.font_three,
            bgcolor=self.theme.transparent_1,
            focused_bgcolor=self.theme.transparent_05,
            border_color=self.theme.transparent,
            focused_border_color=self.theme.transparent,
            cursor_color=self.theme.font_two,
            selection_color=self.theme.primary,
            input_filter=ft.NumbersOnlyInputFilter(),
            on_blur=self.tf_blurred
        )
        # - right limit input field
        self.right_limit = ft.TextField(
            expand=1,
            value="100",
            text_size=12,
            content_padding=5,
            text_align=ft.TextAlign.CENTER,
            color=self.theme.font_two,
            focused_color=self.theme.font_three,
            bgcolor=self.theme.transparent_1,
            focused_bgcolor=self.theme.transparent_05,
            border_color=self.theme.transparent,
            focused_border_color=self.theme.transparent,
            cursor_color=self.theme.font_two,
            selection_color=self.theme.primary,
            input_filter=ft.NumbersOnlyInputFilter(),
            on_blur=self.tf_blurred
        )
        # - limits label
        self.limits_label = ft.Container(
            expand=1,
            alignment=ft.alignment.center,
            padding=5,
            content=ft.Text(
                value="entre",
                color=self.theme.font_one,
                size=12,
                text_align=ft.TextAlign.CENTER
            )
        )
        # - limits panel
        self.limits_panel = ft.Container(
            expand=3,
            bgcolor=self.theme.transparent_1,
            alignment=ft.alignment.center,
            padding=5,
            border_radius=10,
            content=ft.Row(
                spacing=0,
                controls=[self.left_limit, self.limits_label, self.right_limit]
            )
        )
        # - generate button
        self.b_generate = ClCristalButton(
            expand=2,
            theme=self.theme,
            text="Generar",
            content_size=12,
            action=self.b_generate_clicked
        )

        self.actions.controls.extend([ft.Container(expand=1), self.limits_panel, self.b_generate, ft.Container(expand=1)])

        return self.section
    
    # METODOS DE ACCION
    def b_generate_clicked(self, e:ft.TapEvent):

        if not self.left_limit.value:
            self.left_limit.value = 0
        if not self.right_limit.value:
            self.right_limit.value = 0
        self.result.value = self.controller.generate_result(
            limit_1=int(self.left_limit.value),
            limit_2=int(self.right_limit.value)
        )
        self.result.size = self.controller.result_size()
        self.update()
    
    def tf_blurred(self, e:ft.ControlEvent):
        if not e.control.value:
            e.control.value = 0
            self.update()