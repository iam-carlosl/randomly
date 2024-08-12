import flet as ft
from calet_theme import ClTheme
from calet_button import ClWinButton, ClCristalButton, ClCancelButton, ClCheck, ClRadio, ClMenuButton, ClTextButton, ClOptionButton
from calet_bar import ClAppBar
from randomly_templates import RlyAppSection
from randomly_control import RlyChoicesController

class RlySelectionSection(RlyAppSection):

    def __init__(self, theme:ClTheme, position:str="center"):
        super().__init__(theme=theme, position=position)
        self.controller = RlyChoicesController()
        self.choices_page = None

    def build(self):

        super().build()
        # CHOICES LIST
        # - choices list filter
        self.choices_filter = ft.TextField(
            expand=2,
            value="A",
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
            input_filter=ft.TextOnlyInputFilter(),
            on_blur=self.tf_blurred
        )
        # - choices list filter check
        self.choices_filter_check = ClCheck(
            expand=1,
            theme=self.theme,
            value=False,
            inversed_colors=True
        )
        # - choices list label
        self.choices_label = ft.Container(
            expand=3,
            alignment=ft.alignment.center,
            content=ft.Text(
                value="Filtrar con",
                color=self.theme.font_one,
                size=12,
                text_align=ft.TextAlign.CENTER
            )
        )
        # - choices list panel
        self.choices_list_panel = ft.Container(
            expand=6,
            bgcolor=self.theme.transparent_1,
            alignment=ft.alignment.center,
            padding=5,
            border_radius=10,
            content=ft.Row(
                spacing=0,
                controls=[self.choices_filter_check, self.choices_label, self.choices_filter]
            )
        )
        # - choices list button
        self.b_choices = ClCristalButton(
            expand=4,
            theme=self.theme,
            text="Posibilidades",
            content_size=12,
            action=self.b_choices_clicked
        )
        # - generate button
        self.b_generate = ClCristalButton(
            expand=3,
            theme=self.theme,
            text="Generar",
            content_size=12,
            action=self.b_generate_clicked
        )

        self.actions.controls.extend([ft.Container(expand=1), self.b_choices, self.choices_list_panel, self.b_generate, ft.Container(expand=1)])

        return self.section
    
    # METODOS DE ACCION
    def b_generate_clicked(self, e:ft.TapEvent):

        if not self.choices_filter.value:
            self.choices_filter.value = "A"
        self.result.value = self.controller.generate_result(
            filter=self.choices_filter.value if self.choices_filter_check.value else None
        )
        self.result.size = self.controller.result_size()
        self.update()

    def tf_blurred(self, e:ft.ControlEvent):
        if not e.control.value:
            e.control.value = "A"
            self.update()
    
    def b_choices_clicked(self, e:ft.TapEvent):
        if self.choices_page is None:
            self.choices_page = RlyChoicesPage(theme=self.theme, choices_controller=self.controller)
        self.choices_page.open()
    
    # METODOS DE ACCION
    def close_choices_page(self):
        if self.choices_page is not None:
            self.choices_page.close()

class RlyChoicesPage:

    def __init__(self, theme:ClTheme, choices_controller:RlyChoicesController):

        super().__init__()
        self.theme = theme
        self.controller = choices_controller
    
    def choices_main(self, choices_page: ft.Page):

        choices_page.padding = 0
        choices_page.window_width = 400
        choices_page.window_height = 500
        choices_page.window_resizable = False
        choices_page.window_title_bar_hidden = True
        choices_page.window_frameless = True
        choices_page.window_bgcolor = "#00000000"
        choices_page.bgcolor = "#00000000"
        choices_page.theme_mode = ft.ThemeMode.DARK
        choices_page.window_center()

        choices_page.add(
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=RlyChoicesWindow(self.theme, choices_controller=self.controller)
            )
        )

        self.page = choices_page
        self.controller.choices_listed = True
    
    def open(self):
        if not self.controller.choices_listed:
            ft.app(target=self.choices_main)

    def close(self):
        if self.controller.choices_listed:
            self.controller.choices_listed = False
            self.page.window_destroy()
            self.page = None

class RlyChoicesWindow(ft.UserControl):

    def __init__(self, theme:ClTheme, choices_controller:RlyChoicesController):
        super().__init__()
        self.theme = theme
        self.controller = choices_controller

    def build(self):
        
        # CHOICES WINDOW APP BAR
        self.window_app_bar = ClAppBar(
            theme=self.theme,
            title="Lista de posibilidades",
            left_icon=ft.icons.LOCAL_PLAY,
            left_title=True,
            transparent=True,
            can_maximize=False,
            high_title_color=True,
            win_actions=[ClWinButton(theme=self.theme, action=self.b_close_window_clicked)]
        )

        # CHOICES WINDOW VIEWS
        # - list view
        self.window_list_view = RlyChoicesListView(
            theme=self.theme,
            choices_controller=self.controller,
            go_view=self.go_view
        )
        # - lote view
        self.window_lote_view = RlyChoicesLoteView(
            theme=self.theme,
            choices_controller=self.controller,
            position="right",
            go_view=self.go_view
        )

        # WINDOW
        # - main overlay
        self.main_overlay = ft.Container(
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
                    self.window_app_bar,
                    ft.Container(
                        expand=True,
                        padding=ft.padding.only(left=10, right=10, bottom=10),
                        content=ft.Column(
                            spacing=5,
                            controls=[
                                ft.Divider(thickness=1, height=1, color=self.theme.divider),
                                ft.Row(
                                    expand=9,
                                    controls=[ft.Stack(expand=1, controls=[self.window_list_view, self.window_lote_view])]
                                ),
                            ]
                        )
                    )
                ]
            )
        )
        # - window
        self.window = ft.Stack(
            expand=True,
            controls=[
                self.main_overlay
            ]
        )

        return self.window

    # METODOS MANEJADDORES DE EVENTOS
    def b_close_window_clicked(self, e:ft.TapEvent):
        self.controller.choices_listed = False
        self.page.window_destroy()
 
    # METODOS DE ACCION
    def go_view(self, view:str, reload_list:bool=None):
        if view == "list":
            self.window_list_view.upd(position="center")
            self.window_lote_view.upd(position="right")
            if reload_list:
                self.window_list_view.reload_choices_list()
        else:
            self.window_list_view.upd(position="left")
            self.window_lote_view.upd(position="center")
        self.update()

    def open_dialog(self, dlg):
        self.window.controls.insert(-1, dlg)
        self.update()
    
    def close_dialog(self, dlg):
        self.window.controls.remove(dlg)
        self.update()

class RlyChoice(ft.UserControl):

    def __init__(self, theme:ClTheme, text:str, choice_row:ft.Row, choice_controller:RlyChoicesController, expand:bool|int=False):
        super().__init__()
        self.theme = theme
        self.text = text
        self.choice_row = choice_row
        self.controller = choice_controller
        self.expand = expand
    
    def build(self):

        # CHOICE CONTENT
        # - choice text
        self.choice_text = ft.Container(
            expand=8,
            height=40,
            bgcolor=self.theme.transparent,
            alignment=ft.alignment.center_left,
            padding=5,
            content=ft.Text(
                value=self.text,
                color=self.theme.font_one,
                size=14,
                text_align=ft.TextAlign.LEFT,
                overflow=ft.TextOverflow.CLIP
            )
        )
        # - edit choice button
        self.b_edit_choice = ClCristalButton(
            expand=1,
            height=40,
            theme=self.theme,
            icon=ft.icons.EDIT,
            action=self.b_edit_choice_clicked
        )
        # - delete choice button
        self.b_delete_choice = ClCristalButton(
            expand=1,
            height=40,
            theme=self.theme,
            icon=ft.icons.DELETE,
            action=self.b_delete_choice_clicked
        )
        # - choice edition text field
        self.tf_edit_choice = ft.TextField(
            expand=8,
            height=40,
            value=self.text,
            hint_text="Escribe una nueva palabra...",
            hint_style=ft.TextStyle(size=12, color=self.theme.font_one),
            text_size=12,
            content_padding=5,
            text_align=ft.TextAlign.LEFT,
            color=self.theme.font_two,
            focused_color=self.theme.font_three,
            bgcolor=self.theme.transparent_1,
            focused_bgcolor=self.theme.transparent_05,
            border_color=self.theme.transparent,
            focused_border_color=self.theme.transparent,
            cursor_color=self.theme.font_two,
            selection_color=self.theme.primary
        )
        # - confirm choice edition button
        self.b_confirm_choice_edition = ClCristalButton(
            height=40,
            expand=1,
            theme=self.theme,
            icon=ft.icons.CHECK,
            action=self.b_confirm_choice_edition_clicked
        )
        # - cancel choice edition button
        self.b_cancel_choice_edition = ClCristalButton(
            height=40,
            expand=1,
            theme=self.theme,
            icon=ft.icons.CANCEL,
            action=self.b_cancel_choice_edition_clicked
        )

        # CHOICE
        # - read only panel
        self.readonly_panel = ft.Container(
            scale=1,
            bgcolor=self.theme.transparent,
            alignment=ft.alignment.center,
            animate_scale=ft.Animation(200, ft.AnimationCurve.LINEAR_TO_EASE_OUT),
            content=ft.Row(
                spacing=5,
                controls=[self.choice_text, self.b_edit_choice, self.b_delete_choice]
            )
        )
        # - edition panel
        self.edition_panel = ft.Container(
            scale=0,
            bgcolor=self.theme.transparent,
            alignment=ft.alignment.center,
            animate_scale=ft.Animation(200, ft.AnimationCurve.LINEAR_TO_EASE_OUT),
            content=ft.Row(
                spacing=5,
                controls=[self.tf_edit_choice, self.b_confirm_choice_edition, self.b_cancel_choice_edition]
            )
        )
        # - choice
        self.choice = ft.Container(
            bgcolor=self.theme.transparent,
            alignment=ft.alignment.center,
            padding=5,
            border=ft.border.only(bottom=ft.BorderSide(width=1, color=self.theme.divider)),
            content=ft.Stack(controls=[self.readonly_panel, self.edition_panel])
        )

        return self.choice
    
    # METODOS MANEJADORES DE EVENTOS
    def b_edit_choice_clicked(self, e:ft.TapEvent):
        self.readonly_panel.scale = 0
        self.edition_panel.scale = 1
        self.update()

    def b_cancel_choice_edition_clicked(self, e:ft.TapEvent):
        self.readonly_panel.scale = 1
        self.edition_panel.scale = 0
        self.update()
    
    def b_confirm_choice_edition_clicked(self, e:ft.TapEvent):
        self.controller.edit_choice(old=self.text, new=self.tf_edit_choice.value)
        self.text = self.tf_edit_choice.value
        self.choice_text.content.value = self.text
        self.readonly_panel.scale = 1
        self.edition_panel.scale = 0
        self.update()
    
    def b_delete_choice_clicked(self, e:ft.TapEvent):
        self.controller.remove_choice(self.text)
        self.choice_row.scale = 0
        self.choice_row.update()

class RlyChoicesListView(ft.UserControl):

    def __init__(self, theme:ClTheme, choices_controller:RlyChoicesController, go_view, position:str="center", expand:bool|int=False):
        super().__init__()
        self.theme = theme
        self.controller = choices_controller
        self.go_view = go_view
        self.offset = ft.Offset({"left": -1.1, "center": 0, "right": 1.1}[position], y=0)
        self.animate_offset = ft.Animation(200, ft.AnimationCurve.LINEAR_TO_EASE_OUT)
        self.expand = expand
    
    def build(self):

        # VIEW CONTENT
        # - add new choice button
        self.b_add_choice = ClCristalButton(
            expand=1,
            theme=self.theme,
            icon=ft.icons.ADD,
            action=self.b_add_choice_clicked
        )
        # - new choice text field
        self.tf_new_choice = ft.TextField(
            expand=9,
            hint_text="Agrega una palabra o frase a la lista...",
            hint_style=ft.TextStyle(size=12, color=self.theme.font_one),
            text_size=12,
            content_padding=5,
            text_align=ft.TextAlign.LEFT,
            color=self.theme.font_two,
            focused_color=self.theme.font_three,
            bgcolor=self.theme.transparent,
            focused_bgcolor=self.theme.transparent,
            border_color=self.theme.transparent,
            focused_border_color=self.theme.transparent,
            cursor_color=self.theme.font_two,
            selection_color=self.theme.primary,
            input_filter=ft.InputFilter(r"^\w{0,25}", replacement_string="")
        )
        # new choice panel
        self.new_choice_panel = ft.Container(
            expand=1,
            bgcolor=self.theme.transparent_1,
            alignment=ft.alignment.center,
            padding=5,
            border_radius=10,
            content=ft.Row(spacing=5, controls=[self.tf_new_choice, self.b_add_choice])
        )
        # - choices list
        self.choices_list = [ft.Row(
            scale=0,
            animate_scale=ft.Animation(200, ft.AnimationCurve.LINEAR_TO_EASE_OUT),
            on_animation_end=self.choice_animation_ended,
            controls=[]
        )]
        for choice in self.controller.choices[::-1]:
            row = ft.Row(
                animate_scale=ft.Animation(200, ft.AnimationCurve.LINEAR_TO_EASE_OUT),
                on_animation_end=self.choice_animation_ended,
                controls=[]
            )
            row.controls.append(RlyChoice(
                theme=self.theme, 
                text=choice, 
                choice_row=row,
                choice_controller=self.controller,
                expand=1
            ))
            self.choices_list.append(row)
        # - window choices list panel
        self.choices_list_panel = ft.Container(
            expand=True,
            alignment=ft.alignment.top_center,
            padding=5,
            content=ft.Column(
                spacing=5,
                scroll=ft.ScrollMode.ADAPTIVE,
                controls=self.choices_list
            )
        )

        # VIEW ACTIONS
        # - add choices by lote button
        self.b_add_bylote = ClCristalButton(
            expand=9,
            height=40,
            theme=self.theme,
            text="Agregar un lote",
            icon=ft.icons.NAVIGATE_NEXT,
            left_icon=False,
            content_size=12,
            action=lambda e: self.go_view("lote")
        )

        # VIEW
        self.view = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                spacing=5,
                controls=[
                    ft.Row(expand=1, controls=[self.new_choice_panel]),
                    ft.Row(expand=8, controls=[self.choices_list_panel]),
                    ft.Row(expand=1, controls=[self.b_add_bylote])
                ]
            )
        )

        return self.view
    
    # METODOS MANEJADORES DE EVENTOS
    def b_add_choice_clicked(self, e:ft.TapEvent):
        added = self.controller.add_choice(self.tf_new_choice.value)
        if added:
            self.choices_list[0].controls.append(RlyChoice(
                theme=self.theme,
                text=self.tf_new_choice.value,
                choice_row=self.choices_list[0],
                choice_controller=self.controller,
                expand=1
            ))
            self.choices_list[0].scale = 1
            self.choices_list.insert(0, ft.Row(
                scale=0,
                animate_scale=ft.Animation(200, ft.AnimationCurve.LINEAR_TO_EASE_OUT),
                on_animation_end=self.choice_animation_ended,
                controls=[]
            ))
            self.tf_new_choice.value = ""
            self.update()

    # METODOS DE ACCION
    def choice_animation_ended(self, e:ft.ControlEvent):
        if e.control.scale == 0:
            self.choices_list.remove(e.control)
            self.update()
    
    def reload_choices_list(self):
        del self.choices_list[1:]
        for choice in self.controller.choices[::-1]:
            row = ft.Row(
                animate_scale=ft.Animation(200, ft.AnimationCurve.LINEAR_TO_EASE_OUT),
                on_animation_end=self.choice_animation_ended,
                controls=[]
            )
            row.controls.append(RlyChoice(
                theme=self.theme, 
                text=choice, 
                choice_row=row,
                choice_controller=self.controller,
                expand=1
            ))
            self.choices_list.append(row)
        self.update()

    def upd(self, position:str=None):
        if position is not None:
            self.offset.x = {"left": -1.1, "center": 0, "right": 1.1}[position]
            self.update()

class RlyChoicesLoteView(ft.UserControl):

    def __init__(self, theme:ClTheme, choices_controller:RlyChoicesController, go_view, position:str="center", expand:bool|int=False):
        super().__init__()
        self.theme = theme
        self.controller = choices_controller
        self.go_view = go_view
        self.offset = ft.Offset({"left": -1.1, "center": 0, "right": 1.1}[position], y=0)
        self.animate_offset = ft.Animation(200, ft.AnimationCurve.LINEAR_TO_EASE_OUT)
        self.expand = expand
    
    def build(self):

        # VIEW CONTENT
        # - new choices lote label
        self.new_lote_label = ft.Text(
            expand=1,
            value="Agrega múltiples posibilidades con un solo toque.",
            color=self.theme.font_one,
            size=12,
        )
        # - new choices lote input field
        self.tf_new_lote = ft.TextField(
            expand=1,
            hint_text="Escribe o pega el lote de posibilidades aquí...",
            hint_style=ft.TextStyle(size=12, color=self.theme.font_one),
            text_size=12,
            content_padding=5,
            text_align=ft.TextAlign.LEFT,
            color=self.theme.font_two,
            focused_color=self.theme.font_three,
            bgcolor=self.theme.transparent_1,
            focused_bgcolor=self.theme.transparent_05,
            border_color=self.theme.transparent,
            focused_border_color=self.theme.transparent,
            cursor_color=self.theme.font_two,
            selection_color=self.theme.primary,
            multiline=True,
            min_lines=12
        )
        # - new choices lote panel
        self.new_lote_panel = ft.Container(
            expand=1,
            alignment=ft.alignment.center_left,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Row(expand=1, controls=[self.new_lote_label]),
                    ft.Row(expand=4, controls=[self.tf_new_lote])
                ]
            )
        )
        # - new choices split separator options label
        self.split_label = ft.Text(
            value="Separar posibilidades del lote por...",
            color=self.theme.font_one,
            size=12,
            text_align=ft.TextAlign.LEFT
        )
        # - new choices split separator options
        self.b_byspaces_split = ClRadio(
            theme=self.theme,
            value=" ",
            label="Espacios",
            left_label=False,
            inversed_colors=True
        )
        self.b_bylines_split = ClRadio(
            theme=self.theme,
            value="\n",
            label="Líneas",
            left_label=False,
            inversed_colors=True
        )
        self.b_byother_split = ClRadio(
            theme=self.theme,
            value="other",
            label="Otro",
            left_label=False,
            inversed_colors=True
        )
        # - split options group
        self.rg_split_options = ft.RadioGroup(
            value=" ",
            on_change=self.rg_split_options_changed,
            content=ft.Column(
                spacing=0,
                controls=[self.b_byspaces_split, self.b_bylines_split, self.b_byother_split]
            )
        )
        # - split by other label
        self.split_byother_label = ft.Text(
            visible=False,
            value="Escribe la expresión que separa las posibilidades del lote:",
            color=self.theme.font_one,
            size=12,
            text_align=ft.TextAlign.LEFT,
        )
        # - split by other input field
        self.tf_byother_split = ft.TextField(
            visible=False,
            height=40,
            value="",
            text_size=12,
            content_padding=5,
            text_align=ft.TextAlign.LEFT,
            color=self.theme.font_two,
            focused_color=self.theme.font_three,
            bgcolor=self.theme.transparent_1,
            focused_bgcolor=self.theme.transparent_05,
            border_color=self.theme.transparent,
            focused_border_color=self.theme.transparent,
            cursor_color=self.theme.font_two,
            selection_color=self.theme.primary,
            input_filter=ft.InputFilter(r"^.{0,30}"),
        )
        # - split options panel
        self.split_options_panel = ft.Container(
            bgcolor=self.theme.transparent_05,
            alignment=ft.alignment.center_left,
            padding=5,
            border_radius=5,
            content=ft.Column(
                spacing=5,
                controls=[self.rg_split_options, self.split_byother_label, self.tf_byother_split]
            )
        )
        # - split panel
        self.split_panel = ft.Container(
            expand=1,
            alignment=ft.alignment.center,
            content=ft.Column(
                spacing=5,
                controls=[self.split_label, self.split_options_panel]
            )
        )

        # VIEW ACTIONS
        # - back to choices list view button
        self.b_back_to_list = ClCristalButton(
            expand=1,
            height=40,
            theme=self.theme,
            text="Lista",
            icon=ft.icons.NAVIGATE_BEFORE,
            content_size=12,
            action=lambda e: self.go_view("list")
        )
        # - add choices lote button
        self.b_add_lote = ClCristalButton(
            expand=2,
            height=40,
            theme=self.theme,
            text="Agregar lote",
            icon=ft.icons.ADD,
            content_size=12,
            action=self.b_add_lote_clicked
        )

        # VIEW
        self.view = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row(expand=4, controls=[self.new_lote_panel]),
                    ft.Row(expand=5, controls=[self.split_panel]),
                    ft.Row(expand=1, controls=[self.b_back_to_list, self.b_add_lote])
                ]
            )
        )

        return self.view

    # METODOS MANEJADORES DE EVENTOS
    def rg_split_options_changed(self, e:ft.ControlEvent):
        if self.rg_split_options.value == "other":
            self.split_byother_label.visible = True
            self.tf_byother_split.visible = True
        else:
            self.split_byother_label.visible = False
            self.tf_byother_split.visible = False
        self.update()

    def b_add_lote_clicked(self, e:ft.TapEvent):
        if self.tf_new_lote.value:
            if self.rg_split_options.value != "other":
                self.controller.add_choices(self.tf_new_lote.value.split(self.rg_split_options.value))
                self.go_view(view="list", reload_list=True)
            elif self.tf_byother_split.value:
                self.controller.add_choices(self.tf_new_lote.value.split(self.tf_byother_split.value))
                self.go_view(view="list", reload_list=True)
            self.update()

    # METODOS DE ACCION
    def upd(self, position:str=None):
        if position is not None:
            self.offset.x = {"left": -1.1, "center": 0, "right": 1.1}[position]
            self.update()

class RlyLoteChoicesDlg(ft.UserControl):

    def __init__(self, theme:ClTheme, choices_controller:RlyChoicesController, reload_choices_list, close_dialog):
        super().__init__()
        self.theme = theme
        self.controller = choices_controller
        self.reload_choices_list = reload_choices_list
        self.close_dialog = close_dialog
    
    def build(self):
        
        # DIALOG HEADER
        # - header title
        self.header_title = ft.Text(
            value="Agregar lote de posibilidades",
            color=self.theme.font_three,
            size=14
        )
        # - close dialog button
        self.b_close_dialog = ClCancelButton(
            theme=self.theme,
            icon=ft.icons.CLOSE,
            width=30,
            height=30,
            action=lambda e: self.close_dialog(self)
        )
        # - dialog header
        self.dlg_header = ft.Container(
            expand=1,
            padding=ft.padding.only(left=5),
            alignment=ft.alignment.center_left,
            content=ft.Row(
                expand=True,
                controls=[
                    self.header_title,
                    ft.Container(expand=True),
                    self.b_close_dialog
                ]
            )
        )

        # DIALOG CONTENT
        # - new choices lote input field
        self.tf_new_choices_lote = ft.TextField(
            hint_text="Escribe o pega todas las posibilidades aquí...",
            hint_style=ft.TextStyle(size=11, color=self.theme.font_one),
            text_size=12,
            content_padding=5,
            text_align=ft.TextAlign.LEFT,
            color=self.theme.font_two,
            focused_color=self.theme.font_three,
            bgcolor=self.theme.transparent,
            focused_bgcolor=self.theme.transparent,
            border_color=self.theme.transparent,
            focused_border_color=self.theme.transparent,
            cursor_color=self.theme.font_two,
            selection_color=self.theme.primary,
            multiline=True,
            min_lines=12
        )
        # - choices split input field
        self.tf_choices_split = ft.TextField(
            expand=1,
            height=40,
            value="",
            hint_text="Espacio",
            hint_style=ft.TextStyle(size=12, color=self.theme.font_one),
            text_size=12,
            content_padding=5,
            text_align=ft.TextAlign.LEFT,
            color=self.theme.font_two,
            focused_color=self.theme.font_three,
            bgcolor=self.theme.transparent_1,
            focused_bgcolor=self.theme.transparent_05,
            border_color=self.theme.transparent,
            focused_border_color=self.theme.transparent,
            cursor_color=self.theme.font_two,
            selection_color=self.theme.primary,
            input_filter=ft.InputFilter(r"^.{0,10}"),
        )
        # - choices split label
        self.choices_split_label = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Text(
                value="Separar posibilidades por",
                color=self.theme.font_one,
                size=12,
                text_align=ft.TextAlign.CENTER   
            )
        )
        # - dlg content
        self.dlg_content = ft.Container(
            expand=10,
            bgcolor=self.theme.transparent_05,
            padding=10,
            border_radius=10,
            alignment=ft.alignment.top_center,
            content=ft.Column(
                spacing=5,
                controls=[
                    ft.Row(expand=17, controls=[ft.Container(
                        expand=1,
                        alignment=ft.alignment.top_center,
                        content=self.tf_new_choices_lote
                    )]),
                    ft.Row(expand=3, controls=[self.choices_split_label, self.tf_choices_split])
                ]
            )
        )


        # ACCIONES DEL DIALOGO
        # - add choices button
        self.b_add_choices_lote = ClCristalButton(
            expand=2,
            theme=self.theme,
            icon=ft.icons.ADD,
            text="Agregar posibilidades",
            content_size=12,
            action=self.b_add_choices_lote_clicked
        )
        # - lista de acciones
        self.dlg_actions = ft.Row(
            expand=1,
            spacing=5,
            controls=[self.b_add_choices_lote]
        )

        # DIALOGO DEL LOTES
        # - dialogo
        self.dlg = ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                colors=[self.theme.background_one, self.theme.background_two],
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center
            ),
            border_radius=15,
            padding=10,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=5,
                color="black",
                blur_style=ft.ShadowBlurStyle.OUTER
            ),
            content=ft.Column(
                controls=[
                    self.dlg_header,
                    self.dlg_content,
                    self.dlg_actions
                ]
            )
        )
        # capa del dialogo
        self.dlg_overlay = ft.Container(
            expand=True,
            bgcolor=self.theme.transparent_05,
            alignment=ft.alignment.center,
            padding=20,
            border_radius=10,
            blur=5,
            content=ft.Row(
                expand=True,
                spacing=0,
                controls=[
                    ft.Column(expand=1),
                    ft.Column(
                        expand=8,
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row(expand=1),
                            ft.Row(
                                expand=8,
                                controls=[self.dlg]
                            ),
                            ft.Row(expand=1)
                        ]
                    ),
                    ft.Column(expand=1)
                ]
            )
        )

        return self.dlg_overlay
    
    def b_add_choices_lote_clicked(self, e:ft.TapEvent):
        if self.tf_new_choices_lote.value:
            lote = self.tf_new_choices_lote.value.split(
                self.tf_choices_split.value if self.tf_choices_split.value else " "
            )
            self.controller.add_choices(lote)
            self.reload_choices_list()
            self.close_dialog(self)