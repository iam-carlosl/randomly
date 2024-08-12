"""Calet: a visual components library based on Flet framework
   - Buttons module"""

import flet as ft
from calet_theme import ClTheme, ClLightTheme, ClDarkTheme
from calet_errors import ClError

# - text button (ok) (ok)
class ClTextButton(ft.UserControl):
    """Represents a text button to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, text:str=None, icon:str=None, hover_icon:str=None, content_size:int=16, 
                 content_padding:int=5, width:int=None, height:int=None, radius:int=5, left_icon:bool=True, expand:bool|int=False, 
                 rounded:bool=True, enabled:bool=True, data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button.
        - text: is the text to be displayed in the button.
        - icon: is the icon to be displayed in the button.
        - hover_icon: is the icon to be displayed in the button when it's on hover.
        - content_size: is the size of the text and icons of the button.
        - content_padding: is the padding from the button border to the text and icon inside.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - radius: is a custom radius for the button corners.
        - left_icon: is a flag saying if the button icon must be displayed at the left or the right side.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more information.
        - rounded: is a flag saying when the button shape is rectangular with rounded corners or circular.
        - enabled: is a flag saying when the button is enabled or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked.
        """
        # VALIDATION BLOCK
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if text is not None and not isinstance(text, str):
            raise ClError(
                error="Argument Error: <<text>> must be string"
            )
        if icon is not None and not isinstance(icon, str):
            raise ClError(
                error="Argument Error: <<icon>> must be string"
            )
        if hover_icon is not None and not isinstance(hover_icon, str):
            raise ClError(
                error="Argument Error: <<hover_icon>> must be string"
            )
        if not isinstance(content_size, int):
            raise ClError(
                error="Argument Error: <<content_size>> must be integer"
            )
        if not isinstance(content_padding, int):
            raise ClError(
                error="Argument Error: <<content_padding>> must be integer"
            )
        if width is not None and not isinstance(width, int):
            raise ClError(
                error="Argument Error: <<width>> must be integer"
            )
        if height is not None and not isinstance(height, int):
            raise ClError(
                error="Argument Error: <<height>> must be integer"
            )
        if not isinstance(radius, int):
            raise ClError(
                error="Argument Error: <<radius>> must be integer"
            )
        if not isinstance(left_icon, bool):
            raise ClError(
                error="Argument Error: <<left_icon>> must be boolean"
            )
        if not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean"
            )
        if not isinstance(rounded, bool):
            raise ClError(
                error="Argument Error: <<rounded>> must be boolean"
            )
        if not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )

        # INITIALIZATION BLOCK
        super().__init__()
        self.theme = theme
        self.text = text
        self.icon = icon
        self.hover_icon = hover_icon if hover_icon is not None else self.icon
        self.content_size = content_size
        self.content_padding = content_padding
        self.width = width
        self.height = height
        self.radius = radius
        self.left_icon = left_icon
        self.expand = expand
        self.rounded = rounded
        self.enabled = enabled
        self.data = data
        self.action = action
    
    def build(self):
        
        # BUTTON CONTENT
        # - button icon
        if self.icon is not None:
            self.button_icon = ft.Icon(
                name=self.icon,
                color=self.theme.font_one,
                size=self.content_size+4
            )
        # - button text
        if self.text is not None:
            self.button_text = ft.Text(
                value=self.text,
                color=self.theme.font_one,
                text_align=ft.TextAlign.CENTER,
                size=self.content_size
            )

        # BUTTON
        self.button = ft.TextButton(
            data=self,
            width=self.width,
            height=self.height,
            style=ft.ButtonStyle(
                bgcolor={
                    ft.MaterialState.DEFAULT: self.theme.transparent,
                    ft.MaterialState.HOVERED: self.theme.transparent_05,
                },
                overlay_color={
                    ft.MaterialState.DEFAULT: self.theme.transparent,
                    ft.MaterialState.HOVERED: self.theme.transparent_05,
                },
                shape=ft.RoundedRectangleBorder(radius=self.radius) if self.rounded else ft.StadiumBorder(),
                animation_duration=200,
                padding=self.content_padding
            ),
            disabled=not self.enabled,
            autofocus=False,
            content=ft.Row(
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[]
            ),
            on_click=self.action,
            on_hover=self.b_hovered
        )
        # - adding the button content
        if self.text is not None:
            self.button.content.controls.append(self.button_text)
        if self.icon is not None:
            if self.left_icon:
                self.button.content.controls.insert(0, self.button_icon)
            else:
                self.button.content.controls.append(self.button_icon)
        
        return self.button
    
    def b_hovered(self, e:ft.HoverEvent):
        if self.icon is not None:
            self.button_icon.name = self.hover_icon if e.data == "true" else self.icon
            self.button_icon.color = self.theme.font_two if e.data == "true" else self.theme.font_one
        if self.text is not None:
            self.button_text.color = self.theme.font_two if e.data == "true" else self.theme.font_one
        self.update()

    def upd(self, theme:ClTheme=None, enabled:bool=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        - enabled: a flag saying the new available status of the button.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if enabled is not None and not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if theme is not None:
            self.theme = theme
            if self.icon is not None:
                self.button_icon.color = self.theme.font_one
            if self.text is not None:
                self.button_text.color = self.theme.font_one
            self.button.style.bgcolor = {
                ft.MaterialState.DEFAULT: self.theme.transparent,
                ft.MaterialState.HOVERED: self.theme.transparent_05,
            }
            self.button.style.overlay_color = {
                ft.MaterialState.DEFAULT: self.theme.transparent,
                ft.MaterialState.HOVERED: self.theme.transparent_05,
            }
        if enabled is not None:
            self.enabled = enabled
            self.button.disabled = not enabled
        self.update()

# tonal button (ok) (ok)
class ClTonalButton(ClTextButton):
    """Represents a tonal button to be used in Flet apps.
    """
    def build(self):
        super().build()
        if self.icon is not None:
            self.button_icon.color = self.theme.primary_tonal
        if self.text is not None:
            self.button_text.color = self.theme.primary_tonal
        self.button.style.bgcolor = self.theme.primary_block
        self.button.style.overlay_color = {
            ft.MaterialState.HOVERED: self.theme.transparent_05
        }
        return self.button
    
    def b_hovered(self, e: ft.HoverEvent):
        if self.icon is not None:
            self.button_icon.name = self.hover_icon if e.data == "true" else self.icon
        self.update()

# - button (ok) (ok)
class ClButton(ClTextButton):
    """Represents a button with normal aspect to be used in Flet apps.
    """
    def build(self):
        super().build()
        if self.icon is not None:
            self.button_icon.color = self.theme.font_two
        if self.text is not None:
            self.button_text.color = self.theme.font_two
        self.button.style.bgcolor = {
            ft.MaterialState.DEFAULT: self.theme.action,
            ft.MaterialState.HOVERED: self.theme.action_hovered,
        }
        self.button.style.overlay_color = {
            ft.MaterialState.DEFAULT: self.theme.action,
            ft.MaterialState.HOVERED: self.theme.action_hovered,
        }
        return self.button
    
    def b_hovered(self, e: ft.HoverEvent):
        if self.icon is not None:
            self.button_icon.name = self.hover_icon if e.data == "true" else self.icon
            self.button_icon.color = self.theme.font_three if e.data == "true" else self.theme.font_two
        if self.text is not None:
            self.button_text.color = self.theme.font_three if e.data == "true" else self.theme.font_two
        self.update()

# cristal button
class ClCristalButton(ClTextButton):
    """Represents a button with semitransparent aspect to be used in Flet apps.
    """
    def build(self):
        super().build()
        self.button.style.bgcolor = {
            ft.MaterialState.DEFAULT: self.theme.transparent_1,
            ft.MaterialState.HOVERED: self.theme.transparent_1,
        }
        self.button.style.overlay_color = {
            ft.MaterialState.DEFAULT: self.theme.transparent_1,
            ft.MaterialState.HOVERED: self.theme.transparent_1,
        }
        return self.button

# - accept button (ok) (ok)
class ClAcceptButton(ClButton):
    """Represents a button with accept aspect to be used in Flet apps.
    """
    def build(self):
        super().build()
        self.button.style.bgcolor = {
            ft.MaterialState.DEFAULT: self.theme.accept,
            ft.MaterialState.HOVERED: self.theme.accept_hovered,
        }
        self.button.style.overlay_color = {
            ft.MaterialState.DEFAULT: self.theme.accept,
            ft.MaterialState.HOVERED: self.theme.accept_hovered,
        }
        return self.button

# cancel button (ok) (ok)
class ClCancelButton(ClButton):
    """Represents a button with cancel aspect to be used in Flet apps.
    """
    def build(self):
        super().build()
        self.button.style.bgcolor = {
            ft.MaterialState.DEFAULT: self.theme.cancel,
            ft.MaterialState.HOVERED: self.theme.cancel_hovered
        }
        self.button.style.overlay_color = {
            ft.MaterialState.DEFAULT: self.theme.cancel,
            ft.MaterialState.HOVERED: self.theme.cancel_hovered
        }
        return self.button

# select button (ok) (ok)
class ClSelectButton(ClTextButton):
    """Represents a button that alternate between selected and not selected status when is clicked 
    to be used in Flet apps. Can be combined with ```calet_bar.ClSelectionBar``` to set an special behavior.
    """
    def __init__(self, theme:ClTheme, text:str=None, icon:str=None, hover_icon:str=None, selected_icon:str=None, 
                 hover_selected_icon:str=None, content_size:int=16, content_padding:int=5, width:int=None, height:int=None,
                 radius:int=5, rounded:bool=True, expand:bool|int=False, enabled:bool=True, selected:bool=False,
                 data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button.
        - text: is the text to be displayed in the button.
        - icon: is the icon to be displayed in the button.
        - hover_icon: is the icon to be displayed in the button when it's hovered.
        - selected_icon: is the icon to be displayed in the button when it's selected.
        - hover_selected_icon: is the icon to be displayed in the button when it's hovered and selected.
        - content_size: is the size of the text and icons of the button.
        - content_padding: is the padding from the button border to the text and icon inside.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - radius: is a custom radius for the button corners.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more information.
        - rounded: is a flag saying when the button shape is rectangular with rounded corners or circular.
        - enabled: is a flag saying when the button is enabled or not.
        - selected: is a flag saying when the button is selected or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked.
        """
        # SUPER BLOCK
        super().__init__(
            theme=theme,
            text=text,
            icon=icon,
            hover_icon=hover_icon,
            content_size=content_size,
            content_padding=content_padding,
            width=width,
            height=height,
            radius=radius,
            expand=expand,
            rounded=rounded,
            enabled=enabled,
            data=data,
            action=action
        )
        # VALIDATION BLOCK
        if selected_icon is not None and not isinstance(selected_icon, str):
            raise ClError(
                error="Argument Error: <<selected_icon>> must be string"
            )
        if hover_selected_icon is not None and not isinstance(hover_selected_icon, str):
            raise ClError(
                error="Argument Error: <<hover_selected_icon>> must be string"
            )
        if not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        # INITIALIZATION BLOCK
        self.selected_icon = selected_icon if selected_icon is not None else self.hover_icon
        self.hover_selected_icon = hover_selected_icon if hover_selected_icon is not None else self.selected_icon
        self.selected = selected
        self.on_selection_bar = False
    
    def build(self):

        super().build()

        # BUTTON CONTENT
        # - button selected icon
        if self.icon is not None:
            if self.selected:
                self.button_icon.name = self.selected_icon
        else:
            if self.selected_icon is not None:
                self.button_icon = ft.Icon(
                    name=self.icon if not self.selected else self.selected_icon,
                    color=self.theme.font_one,
                    size=self.content_size+4
                )
                self.button.content.controls.insert(0,self.button_icon)

        # BUTTON
        if self.selected:
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.name = self.selected_icon
                self.button_icon.color = self.theme.font_two
            if self.text is not None:
                self.button_text.color = self.theme.font_two
            self.button.style.bgcolor = {
                ft.MaterialState.DEFAULT: self.theme.transparent_1,
                ft.MaterialState.HOVERED: self.theme.transparent_1,
            }
            self.button.style.overlay_color = {
                ft.MaterialState.DEFAULT: self.theme.transparent_1,
                ft.MaterialState.HOVERED: self.theme.transparent_1,
            }
        self.button.on_click = self.b_clicked
        return self.button
    
    # override
    def b_hovered(self, e: ft.HoverEvent):
        if self.selected:
            if self.selected_icon is not None:
                self.button_icon.name = self.hover_selected_icon if e.data == "true" else self.selected_icon
            self.update()
        else:
            super().b_hovered(e)
    
    def b_clicked(self, e:ft.TapEvent):
        self.selected = not self.selected
        if self.icon is not None or self.selected_icon is not None:
            self.button_icon.name = self.icon if not self.selected else self.selected_icon
            self.button_icon.color = self.theme.font_one if not self.selected else self.theme.font_three
        if self.text is not None:
            self.button_text.color = self.theme.font_one if not self.selected else self.theme.font_three
        self.button.style.bgcolor = {
            ft.MaterialState.DEFAULT: self.theme.transparent if not self.selected else self.theme.transparent_1,
            ft.MaterialState.HOVERED: self.theme.transparent_05 if not self.selected else self.theme.transparent_1,
        }
        self.button.style.overlay_color = {
            ft.MaterialState.DEFAULT: self.theme.transparent if not self.selected else self.theme.transparent_1,
            ft.MaterialState.HOVERED: self.theme.transparent_05 if not self.selected else self.theme.transparent_1,
        }
        self.update()
        if self.action is not None:
            self.action(e)

    def upd(self, theme:ClTheme=None, enabled:bool=None, selected:bool=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        - enabled: a flag saying the new available status of the button.
        - selected: a flag saying the new selection status of the button.
        """
        super().upd(theme, enabled)
        if selected is not None and not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if selected is not None:
            self.selected = selected
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.color = self.theme.font_one if not self.selected else self.theme.font_three
            if self.text is not None:
                self.button_text.color = self.theme.font_one if not self.selected else self.theme.font_three
            self.button.style.bgcolor = {
                ft.MaterialState.DEFAULT: self.theme.transparent if not self.selected else self.theme.transparent_1,
                ft.MaterialState.HOVERED: self.theme.transparent_05 if not self.selected else self.theme.transparent_1,
            }
            self.button.style.overlay_color = {
                ft.MaterialState.DEFAULT: self.theme.transparent if not self.selected else self.theme.transparent_1,
                ft.MaterialState.HOVERED: self.theme.transparent_05 if not self.selected else self.theme.transparent_1,
            }
        self.update()

# mode button (ok) (ok)
class ClModeButton(ClTextButton):
    """Represents a button that alternate between two modes when is clicked to be used in 
    Flet apps.
    """
    def __init__(self, theme:ClTheme, text:str=None, second_text:str=None, icon:str=None, hover_icon:str=None, 
                 second_icon:str=None, hover_second_icon:str=None, content_size:int=16, content_padding:int=5, 
                 width:int=None, height:int=None, radius:int=5, expand:bool|int=False, rounded:bool=True, 
                 enabled:bool=True, first_mode=True, data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button. 
        - text: is the text to be displayed in the button when it's in the first mode.
        - second_text: is the text to be displayed in the button when it's in the second mode.
        - icon: is the icon to be displayed in the button when it's in the first mode.
        - hover_icon: is the icon to be displayed in the button when it's hovered in the first mode.
        - second_icon: is the icon to be displayed in the button when it's in the second mode.
        - second_hover_icon: is the icon to be displayed in the button when it's hovered in the second mode.
        - content_size: is the size of the text and icons of the button.
        - content_padding: is the padding from the button border to the text and icon inside.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - radius: is a custom radius for the button corners.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more information.
        - rounded: is a flag saying when the button shape is rectangular with rounded corners or circular.
        - enabled: is a flag saying when the button is enabled or not.
        - fist_mode: is a flag saying when the button is in the first mode or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked.
        """
        # SUPER BLOCK
        super().__init__(
            theme=theme,
            text=text,
            icon=icon,
            hover_icon=hover_icon,
            content_size=content_size,
            content_padding=content_padding,
            width=width,
            height=height,
            radius=radius,
            expand=expand,
            rounded=rounded,
            enabled=enabled,
            data=data,
            action=action
        )
        # VALIDATION BLOCK
        if second_text is not None and not isinstance(second_text, str):
            raise ClError(
                error="Argument Error: <<second_text>> must be string"
            )
        if second_icon is not None and not isinstance(second_icon, str):
            raise ClError(
                error="Argument Error: <<second_icon>> must be string"
            )
        if hover_second_icon is not None and not isinstance(hover_second_icon, str):
            raise ClError(
                error="Argument Error: <<hover_second_icon>> must be string"
            )
        if not isinstance(first_mode, bool):
            raise ClError(
                error="Argument Error: <<first_mode>> must be boolean"
            )
        # INITIALIZATION BLOCK
        self.second_text = second_text if second_text is not None else self.text
        self.second_icon = second_icon if second_icon is not None else self.icon
        self.hover_second_icon = hover_second_icon if hover_second_icon is not None else self.second_icon
        self.first_mode = first_mode

    def build(self):

        super().build()

        # BUTTON CONTENT
        # - button second icon
        if self.icon is not None:
            if not self.first_mode:
                self.button_icon.name = self.second_icon
        else:
            if self.second_icon is not None:
                self.button_icon = ft.Icon(
                    name=self.icon if self.first_mode else self.second_icon,
                    color=self.theme.font_one,
                    size=self.content_size+4
                )
                self.button.content.controls.insert(0, self.button_icon)
        # - button second text
        if self.text is not None:
            if not self.first_mode:
                self.button_text.value = self.second_text
        else:
            if self.second_text is not None:
                self.button_text = ft.Text(
                    value=self.text if self.first_mode else self.second_text,
                    color=self.theme.font_one,
                    text_align=ft.TextAlign.CENTER,
                    size=self.content_size
                )
                self.button.content.controls.append(self.button_text)

        # BUTTON
        self.button.on_click = self.b_clicked
        return self.button
    
    # override
    def b_hovered(self, e: ft.HoverEvent):
        if self.first_mode:
            super().b_hovered(e)
        else:
            if self.second_icon is not None:
                self.button_icon.name = self.hover_second_icon if e.data == "true" else self.second_icon
            self.update()
    
    def b_clicked(self, e:ft.TapEvent):
        self.first_mode = not self.first_mode
        if self.icon is not None or self.second_icon is not None:
            self.button_icon.name = self.icon if self.first_mode else self.second_icon
        if self.text is not None or self.second_text is not None:
            self.button_text.value = self.text if self.first_mode else self.second_text
        self.update()
        if self.action is not None:
            self.action(e)

# filter button (ok) (ok)
class ClFilterButton(ClSelectButton):
    """Represents a filter button to be used in Flet apps.
    """
    def build(self):

        super().build()
        if self.selected:
            if self.selected_icon is not None:
                self.button_icon.name = self.selected_icon
                self.button_icon.color = self.theme.primary_tonal
            if self.text is not None:
                self.button_text.color = self.theme.primary_tonal
            self.button.style.bgcolor = {
                ft.MaterialState.DEFAULT: self.theme.primary_block,
                ft.MaterialState.HOVERED: self.theme.primary_block,
            }
            self.button.style.overlay_color = {
                ft.MaterialState.DEFAULT: self.theme.primary_block,
                ft.MaterialState.HOVERED: self.theme.primary_block,
            }
        else:
            self.button.style.bgcolor = {
                ft.MaterialState.DEFAULT: self.theme.transparent_05,
                ft.MaterialState.HOVERED: self.theme.transparent_1,
            }
            self.button.style.overlay_color = {
                ft.MaterialState.DEFAULT: self.theme.transparent_05,
                ft.MaterialState.HOVERED: self.theme.transparent_1,
            }
        return self.button

    # override
    def b_clicked(self, e:ft.TapEvent):
        self.selected = not self.selected
        if self.icon is not None or self.selected_icon is not None:
            self.button_icon.name = self.icon if not self.selected else self.selected_icon
            self.button_icon.color = self.theme.font_one if not self.selected else self.theme.primary_tonal
        if self.text is not None:
            self.button_text.color = self.theme.font_one if not self.selected else self.theme.primary_tonal
        self.button.style.bgcolor = {
            ft.MaterialState.DEFAULT: self.theme.transparent_05 if not self.selected else self.theme.primary_block,
            ft.MaterialState.HOVERED: self.theme.transparent_1 if not self.selected else self.theme.primary_block,
        }
        self.button.style.overlay_color = {
            ft.MaterialState.DEFAULT: self.theme.transparent_05 if not self.selected else self.theme.primary_block,
            ft.MaterialState.HOVERED: self.theme.transparent_1 if not self.selected else self.theme.primary_block,
        }
        self.update()
        if self.action is not None:
            self.action(e)

    def upd(self, theme: ClTheme = None, enabled: bool = None, selected: bool = None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        - enabled: a flag saying the new available status of the button.
        - selected: a flag saying the new selection status of the button.
        """
        super().upd(theme, enabled)
        if selected is not None and not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if selected is not None:
            self.selected = selected
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.name = self.icon if not self.selected else self.selected_icon
                self.button_icon.color = self.theme.font_one if not self.selected else self.theme.primary_tonal
            if self.text is not None:
                self.button_text.color = self.theme.font_one if not self.selected else self.theme.primary_tonal
            self.button.style.bgcolor = {
                ft.MaterialState.DEFAULT: self.theme.transparent_05 if not self.selected else self.theme.primary_block,
                ft.MaterialState.HOVERED: self.theme.transparent_1 if not self.selected else self.theme.primary_block,
            }
            self.button.style.overlay_color = {
                ft.MaterialState.DEFAULT: self.theme.transparent_05 if not self.selected else self.theme.primary_block,
                ft.MaterialState.HOVERED: self.theme.transparent_1 if not self.selected else self.theme.primary_block,
            }
        self.update()

# outlined filter button (ok) (ok)
class ClOutlineFilterButton(ClSelectButton):
    """Represents a filter button with outlined border to be used in Flet apps.
    """
    def build(self):
        
        super().build()
        self.button.style.bgcolor = {
            ft.MaterialState.DEFAULT: self.theme.transparent,
            ft.MaterialState.HOVERED: self.theme.transparent_05,
        }
        self.button.style.overlay_color = {
            ft.MaterialState.DEFAULT: self.theme.transparent,
            ft.MaterialState.HOVERED: self.theme.transparent_05,
        }
        self.button.style.side = ft.BorderSide(
            width=1,
            color=self.theme.font_one
        ) if self.selected else None
        return self.button
    
    # override
    def b_clicked(self, e: ft.TapEvent):
        super().b_clicked(e)
        self.button.style.side = ft.BorderSide(
            width=1,
            color=self.theme.font_one
        ) if self.selected else None
        self.button.style.bgcolor = {
            ft.MaterialState.DEFAULT: self.theme.transparent,
            ft.MaterialState.HOVERED: self.theme.transparent_05,
        }
        self.button.style.overlay_color = {
            ft.MaterialState.DEFAULT: self.theme.transparent,
            ft.MaterialState.HOVERED: self.theme.transparent_05,
        }
        self.update()

# slide button
class ClSlideButton(ClSelectButton):
    """Represents a button that alternate between selectedo and not selected status
    to be used in a ```calet_bar.ClSelectionBar```.
    """
    def build(self):
        
        super().build()
        if self.selected:
            self.opacity = 0
        self.button.style.bgcolor = {
            ft.MaterialState.DEFAULT: self.theme.transparent,
            ft.MaterialState.HOVERED: self.theme.transparent,
        }
        self.button.style.overlay_color = {
            ft.MaterialState.DEFAULT: self.theme.transparent,
            ft.MaterialState.HOVERED: self.theme.transparent,
        }
        return self.button

    # override
    def b_clicked(self, e:ft.TapEvent):
        self.selected = not self.selected
        self.opacity = 0 if self.selected else 1
        self.update()
        if self.action is not None:
            self.action(e)
    
    # override
    def upd(self, theme:ClTheme=None, enabled:bool=None, selected:bool=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        - enabled: a flag saying the new available status of the button.
        - selected: a flag saying the new selection status of the button.
        """
        super().upd(theme, enabled)
        if selected is not None and not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if selected is not None:
            self.selected = selected
            self.opacity = 0 if self.selected else 1
            if self.icon is not None and not self.selected:
                self.button_icon.color = self.theme.font_one
            if self.text is not None and not self.selected:
                self.button_text.color = self.theme.font_one
        self.update()

# experimental menu tab button with inversed round corners
class ClExperimentalMenuTab(ft.UserControl):
    """Represents a tab button to be used as an option tab in 'calet_bar.ClMenuBar'."""
    def __init__(self, theme:ClTheme, text:str=None, icon:str=None, hover_icon:str=None, 
                 selected_icon:str=None, hover_selected_icon:str=None, content_size:int=14, 
                 expand:bool|int=None, enabled:bool=True, selected:bool=False,
                 left_selected:bool=False, right_selected:bool=False,
                 data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of 'calet_theme.ClTheme' with the colors set to paint the button.
        - text: is the text to be displayed in the button.
        - icon: is the icon to be displayed in the button.
        - hover_icon: is the icon to be displayed in the button when it's hovered.
        - selected_icon: is the icon to be displayed in the button when it's selected.
        - hover_selected_icon: is the icon to be displayed in the button when it's hovered and selected.
        - content_size: is the size of the text and icons of the button.
        - expand: is the responsive expansion of the button in his container. See 'expand' Flet
            property for more information.
        - enabled: is a flag saying when the button is enabled or not.
        - selected: is a flag saying when the button is selected or not.
        - left_selected: is a flag saying when the button at the left of this one is selected or not.
        - right_selected: is a flag saying when the button at the right of this one is selected or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked.
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if text is not None and not isinstance(text, str):
            raise ClError(
                error="Argument Error: <<text>> must be string"
            )
        if icon is not None and not isinstance(icon, str):
            raise ClError(
                error="Argument Error: <<icon>> must be string"
            )
        if hover_icon is not None and not isinstance(hover_icon, str):
            raise ClError(
                error="Argument Error: <<hover_icon>> must be string"
            )
        if selected_icon is not None and not isinstance(selected_icon, str):
            raise ClError(
                error="Argument Error: <<selected_icon>> must be string"
            )
        if hover_selected_icon is not None and not isinstance(hover_selected_icon, str):
            raise ClError(
                error="Argument Error: <<hover_selected_icon>> must be string"
            )
        if content_size is not None and not isinstance(content_size, int):
            raise ClError(
                error="Argument Error: <<content_size>> must be integer"
            )
        if expand is not None and not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean"
            )
        if not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if not isinstance(left_selected, bool):
            raise ClError(
                error="Argument Error: <<left_selected>> must be boolean."
            )
        if not isinstance(right_selected, bool):
            raise ClError(
                error="Argument Error: <<right_selected>> must be boolean."
            )
        # INITIALIZATION
        super().__init__()
        self.theme = theme
        self.text = text
        self.icon = icon
        self.hover_icon = hover_icon if hover_icon is not None else self.icon
        self.selected_icon = selected_icon if selected_icon is not None else self.hover_icon
        self.hover_selected_icon = hover_selected_icon if hover_selected_icon is not None else self.selected_icon
        self.content_size = content_size
        self.expand = expand
        self.enabled = enabled
        self.selected = selected
        self.left_selected = left_selected if not selected and not right_selected else False
        self.right_selected = right_selected if not selected and not left_selected else False
        self.data = data
        self.action = action
        self.button = None
    
    def build(self):

        # BUTTON CONTENT
        # - button icon
        if self.icon is not None or self.selected_icon is not None:
            self.button_icon = ft.Icon(
                name=self.icon if not self.selected else self.selected_icon,
                color=self.theme.font_one if not self.selected else self.theme.font_two,
                size=self.content_size
            )
        # - button text
        if self.text is not None:
            self.button_text = ft.Text(
                value=self.text,
                color=self.theme.font_one if not self.selected else self.theme.font_two,
                text_align=ft.TextAlign.CENTER,
                size=self.content_size
            )
        
        # BUTTON
        # - creating the button
        self.button = ft.Container(
            data=self,
            alignment=ft.alignment.center,
            bgcolor=self.theme.background_one if not self.selected else self.theme.background_two,
            border=ft.border.only(
                left=ft.BorderSide(1, self.theme.background_one if not self.selected else self.theme.background_two),
                right=ft.BorderSide(1, self.theme.background_one if not self.selected else self.theme.background_two)
            ),
            padding=10,
            disabled=not self.enabled,
            animate=100,
            on_hover=self.b_hovered,
            on_click=self.b_clicked,
            content=ft.Row(
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[]
            )
        )
        # - adding the button content
        if self.icon is not None or self.selected_icon is not None:
            self.button.content.controls.append(self.button_icon)
        if self.text is not None:
            self.button.content.controls.append(self.button_text)
        # - setting the button initial status
        if self.selected:
            self.button.border_radius = ft.border_radius.only(top_left=10, top_right=10)
        elif self.left_selected:
            self.button.border_radius = ft.border_radius.only(bottom_left=5)
        elif self.right_selected:
            self.button.border_radius = ft.border_radius.only(bottom_right=5)
        else:
            self.button.border_radius = 0

        # TAB
        self.tab = ft.Container(
            alignment=ft.alignment.center,
            bgcolor=self.theme.background_one if not self.left_selected and not self.right_selected else self.theme.background_two,
            padding=0,
            animate=100,
            content=self.button
        )

        return self.tab

    def b_hovered(self, e:ft.HoverEvent):
        if not self.selected:
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.name = self.hover_icon if e.data == "true" else self.icon
                self.button_icon.color = self.theme.font_two if e.data == "true" else self.theme.font_one
            if self.text is not None:
                self.button_text.color = self.theme.font_two if e.data == "true" else self.theme.font_one
        else:
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.name = self.hover_selected_icon if e.data == "true" else self.selected_icon
        self.update()

    def b_clicked(self, e:ft.TapEvent):
        if not self.selected:
            self.selected = True
            self.left_selected = False
            self.right_selected = False
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.name = self.selected_icon
                self.button_icon.color = self.theme.font_two
            if self.text is not None:
                self.button_text.color = self.theme.font_two
            self.button.bgcolor = self.theme.background_two
            self.button.border_radius = ft.border_radius.only(top_left=10, top_right=10)
            self.button.border=ft.border.only(
                left=ft.BorderSide(1, self.theme.background_two),
                right=ft.BorderSide(1, self.theme.background_two)
            )
            self.tab.bgcolor = self.theme.background_one
            self.update()
            if self.action is not None:
                self.action(e)
    
    def upd(self, theme:ClTheme=None, enabled:bool=None, selected:bool=None, left_selected:bool=None, right_selected:bool=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ClTheme containing the new colors set for the button.
        - enabled: a flag saying the new available status of the button.
        - selected: a flag saying the new selection status of the button.
        - left_selected: a flag saying the new selection status of the button at the left of this button.
        - right_selected: a flag saying the new selection status of the button at the right of this button.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if enabled is not None and not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if selected is not None and not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if left_selected is not None and not isinstance(left_selected, bool):
            raise ClError(
                error="Argument Error: <<left_selected>> must be boolean"
            )
        if right_selected is not None and not isinstance(right_selected, bool):
            raise ClError(
                error="Argument Error: <<right_selected>> must be boolean"
            )
        if theme is not None:
            self.theme = theme
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.color = self.theme.font_one if not self.selected else self.theme.font_two
            if self.text is not None:
                self.button_text.color = self.theme.font_one if not self.selected else self.theme.font_two
            self.button.bgcolor = self.theme.background_one if not self.selected else self.theme.background_two
            self.tab.bgcolor = self.theme.background_one if not self.left_selected and not self.right_selected else self.theme.background_two
        if enabled is not None:
            self.enabled = enabled
            self.button.disabled = not enabled
        if selected is not None:
            self.selected = selected
            if selected:
                self.left_selected = False
                self.right_selected = False
        if left_selected is not None:
            self.left_selected = left_selected
            if left_selected:
                self.selected = False
                self.right_selected = False
        if right_selected is not None:
            self.right_selected = right_selected
            if right_selected:
                self.selected = False
                self.left_selected = False
        if selected is not None or left_selected is not None or right_selected is not None:
            if self.selected:
                if self.icon is not None or self.selected_icon is not None:
                    self.button_icon.name = self.selected_icon
                    self.button_icon.color = self.theme.font_two
                if self.text is not None:
                    self.button_text.color = self.theme.font_two
                self.button.bgcolor = self.theme.background_two
                self.button.border_radius = ft.border_radius.only(top_left=10, top_right=10)
                self.button.border=ft.border.only(
                    left=ft.BorderSide(1, self.theme.background_two),
                    right=ft.BorderSide(1, self.theme.background_two)
                )
                self.tab.bgcolor = self.theme.background_one
            else:
                if self.icon is not None or self.selected_icon is not None:
                    self.button_icon.name = self.icon
                    self.button_icon.color = self.theme.font_one
                if self.text is not None:
                    self.button_text.color = self.theme.font_one
                self.button.bgcolor = self.theme.background_one
                self.button.border=ft.border.only(
                    left=ft.BorderSide(1, self.theme.background_one),
                    right=ft.BorderSide(1, self.theme.background_one)
                )
                if self.left_selected:
                    self.button.border_radius = ft.border_radius.only(bottom_left=5)
                    self.tab.bgcolor = self.theme.background_two
                elif self.right_selected:
                    self.button.border_radius = ft.border_radius.only(bottom_right=5)
                    self.tab.bgcolor = self.theme.background_two
                else:
                    self.button.border_radius = 0
                    self.tab.bgcolor = self.theme.background_one
        self.update()

# nav tab button (ok) (ok)
class ClNavTab(ft.UserControl):
    """Represents a nav tab button to be used as an option tab in ```calet_bar.ClNavBar```."""
    def __init__(self, theme:ClTheme, text:str=None, icon:str=None, hover_icon:str=None, 
                 selected_icon:str=None, hover_selected_icon:str=None, content_size:int=16, width:int=None, height:int=None,
                 expand:bool|int=None, enabled:bool=True, selected:bool=False,
                 data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button.
        - text: is the text to be displayed in the button.
        - icon: is the icon to be displayed in the button.
        - hover_icon: is the icon to be displayed in the button when it's hovered.
        - selected_icon: is the icon to be displayed in the button when it's selected.
        - hover_selected_icon: is the icon to be displayed in the button when it's hovered and selected.
        - content_size: is the size of the text and icons of the button.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more information.
        - enabled: is a flag saying when the button is enabled or not.
        - selected: is a flag saying when the button is selected or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked.
        """
        # VALIDATION
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if text is not None and not isinstance(text, str):
            raise ClError(
                error="Argument Error: <<text>> must be string"
            )
        if icon is not None and not isinstance(icon, str):
            raise ClError(
                error="Argument Error: <<icon>> must be string"
            )
        if hover_icon is not None and not isinstance(hover_icon, str):
            raise ClError(
                error="Argument Error: <<hover_icon>> must be string"
            )
        if selected_icon is not None and not isinstance(selected_icon, str):
            raise ClError(
                error="Argument Error: <<selected_icon>> must be string"
            )
        if hover_selected_icon is not None and not isinstance(hover_selected_icon, str):
            raise ClError(
                error="Argument Error: <<hover_selected_icon>> must be string"
            )
        if not isinstance(content_size, int):
            raise ClError(
                error="Argument Error: <<content_size>> must be integer"
            )
        if width is not None and not isinstance(width, int):
            raise ClError(
                error="Argument Error: <<width>> must be integer"
            )
        if height is not None and not isinstance(height, int):
            raise ClError(
                error="Argument Error: <<height>> must be integer"
            )
        if expand is not None and not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean"
            )
        if not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        # INITIALIZATION
        super().__init__()
        self.theme = theme
        self.text = text
        self.icon = icon
        self.hover_icon = hover_icon if hover_icon is not None else self.icon
        self.selected_icon = selected_icon if selected_icon is not None else self.hover_icon
        self.hover_selected_icon = hover_selected_icon if hover_selected_icon is not None else self.selected_icon
        self.content_size = content_size
        self.width = width
        self.height = height
        self.expand = expand
        self.enabled = enabled
        self.selected = selected
        self.data = data
        self.action = action
    
    def build(self):

        # BUTTON CONTENT
        # - button icon
        if self.icon is not None or self.selected_icon is not None:
            self.button_icon = ft.Icon(
                name=self.icon if not self.selected else self.selected_icon,
                color=self.theme.font_one if not self.selected else self.theme.font_two,
                size=self.content_size
            )
        # - button text
        if self.text is not None:
            self.button_text = ft.Text(
                value=self.text,
                color=self.theme.font_one if not self.selected else self.theme.font_two,
                text_align=ft.TextAlign.CENTER,
                size=self.content_size
            )
        
        # TAB BUTTON
        # - creating the button
        self.button = ft.Container(
            data=self,
            width=self.width,
            height=self.height,
            alignment=ft.alignment.center,
            bgcolor=self.theme.background_one if not self.selected else self.theme.background_two,
            padding=ft.padding.only(left=10, top=5, right=10, bottom=5),
            border_radius=ft.border_radius.only(top_left=10, top_right=10),
            disabled=not self.enabled,
            animate=150,
            on_hover=self.b_hovered,
            on_click=self.b_clicked,
            content=ft.Row(
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[]
            )
        )
        # - adding the button content
        if self.icon is not None or self.selected_icon is not None:
            self.button.content.controls.append(self.button_icon)
        if self.text is not None:
            self.button.content.controls.append(self.button_text)

        return self.button

    def b_hovered(self, e:ft.HoverEvent):
        if not self.selected:
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.name = self.hover_icon if e.data == "true" else self.icon
                self.button_icon.color = self.theme.font_two if e.data == "true" else self.theme.font_one
            if self.text is not None:
                self.button_text.color = self.theme.font_two if e.data == "true" else self.theme.font_one
        else:
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.name = self.hover_selected_icon if e.data == "true" else self.selected_icon
        self.update()

    def b_clicked(self, e:ft.TapEvent):
        if not self.selected:
            self.selected = True
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.name = self.selected_icon
                self.button_icon.color = self.theme.font_two
            if self.text is not None:
                self.button_text.color = self.theme.font_two
            self.button.bgcolor = self.theme.background_two
            self.update()
            if self.action is not None:
                self.action(e)
    
    def upd(self, theme:ClTheme=None, enabled:bool=None, selected:bool=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        - enabled: a flag saying the new available status of the button.
        - selected: a flag saying the new selection status of the button.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if enabled is not None and not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if selected is not None and not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if theme is not None:
            self.theme = theme
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.color = self.theme.font_one if not self.selected else self.theme.font_two
            if self.text is not None:
                self.button_text.color = self.theme.font_one if not self.selected else self.theme.font_two
            self.button.bgcolor = self.theme.background_one if not self.selected else self.theme.background_two
        if enabled is not None:
            self.enabled = enabled
            self.button.disabled = not enabled
        if selected is not None:
            self.selected = selected
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.name = self.selected_icon if selected else self.icon
                self.button_icon.color = self.theme.font_two if selected else self.theme.font_one
            if self.text is not None:
                self.button_text.color = self.theme.font_two if selected else self.theme.font_one
            self.button.bgcolor = self.theme.background_two if selected else self.theme.background_one
        self.update()

# mark tab button (ok) (ok)
class ClMarkTab(ClNavTab):
    """Represents a nav tab button with a selection indicator to be used as an option tab in ```calet_bar.ClNavBar```
    or ```calet_bar.ClLateralNavBar```.
    """
    def __init__(self, theme:ClTheme, text:str=None, icon:str=None, hover_icon:str=None, 
                 selected_icon:str=None, hover_selected_icon:str=None, content_size:int=16, width:int=None, height:int=None,
                 mark_side:str="left", expand:bool|int=None, enabled:bool=True, selected:bool=False,
                 data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button.
        - text: is the text to be displayed in the button.
        - icon: is the icon to be displayed in the button.
        - hover_icon: is the icon to be displayed in the button when it's hovered.
        - selected_icon: is the icon to be displayed in the button when it's selected.
        - hover_selected_icon: is the icon to be displayed in the button when it's hovered and selected.
        - content_size: is the size of the text and icons of the button.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - mark_side: is the side of the button where the indicator must appear when it's selected. Can be 'left', 'right', 'top' or 'bottom'.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more information.
        - enabled: is a flag saying when the button is enabled or not.
        - selected: is a flag saying when the button is selected or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked.
        """
        # SUPER INITIALIZATION
        super().__init__(
            theme=theme,
            text=text,
            icon=icon,
            hover_icon=hover_icon,
            selected_icon=selected_icon,
            hover_selected_icon=hover_selected_icon,
            content_size=content_size,
            width=width,
            height=height,
            expand=expand,
            enabled=enabled,
            selected=selected,
            data=data,
            action=action
        )
        # VALIDATION
        if not isinstance(mark_side, str):
            raise ClError(
                error="Argument Error: <<mark_side>> must be string."
            )
        elif mark_side not in ("left","right","top","bottom"):
            raise ClError(
                error="Argument Error: <<mark_side>> must be 'left', 'right', 'top' or 'bottom'."
            )
        # INITIALIZATION
        self.mark_side = mark_side
    
    def build(self):

        super().build()

        # BUTTON CONTENT
        if self.selected:
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.color = self.theme.primary_tonal
            if self.text is not None:
                self.button_text.color = self.theme.primary_tonal
                self.button_text.weight = ft.FontWeight.BOLD
        if self.text is not None and self.mark_side in ("left","right"):
            self.button_text.text_align = ft.TextAlign.LEFT if self.mark_side == "left" else ft.TextAlign.RIGHT

        # BUTTON
        self.button.expand = True
        self.button.bgcolor = None
        self.button.gradient = ft.LinearGradient(
            colors=[self.theme.background_one, self.theme.background_one],
            begin={
                "left": ft.alignment.center_left,
                "right": ft.alignment.center_right,
                "top": ft.alignment.top_center,
                "bottom": ft.alignment.bottom_center
            }[self.mark_side],
            end={
                "left": ft.alignment.center_right,
                "right": ft.alignment.center_left,
                "top": ft.alignment.bottom_center,
                "bottom": ft.alignment.top_center
            }[self.mark_side]
        )
        self.button.alignment = {
            "left": ft.alignment.center_left,
            "right": ft.alignment.center_right,
            "top": ft.alignment.center,
            "bottom": ft.alignment.center
        }[self.mark_side]
        self.button.border_radius = None
        self.button.content.alignment = ft.MainAxisAlignment.START if self.mark_side in ("left", "bottom") else ft.MainAxisAlignment.END

        # MARK
        self.mark = ft.Container(
            bgcolor=self.theme.background_two,
            width=0 if self.mark_side in ("left","right") else None,
            height=0 if self.mark_side in ("top","bottom") else None,
            padding=ft.padding.only(top=5, bottom=5) if self.mark_side in ("left","right") else ft.padding.only(left=5, right=5),
            alignment={
                "left": ft.alignment.center_left,
                "right": ft.alignment.center_right,
                "top": ft.alignment.top_center,
                "bottom": ft.alignment.bottom_center
            }[self.mark_side],
            content=ft.Container(
                bgcolor=self.theme.primary_tonal,
                border_radius={
                    "left": ft.border_radius.only(top_right=5, bottom_right=5),
                    "right": ft.border_radius.only(top_left=5, bottom_left=5),
                    "top": ft.border_radius.only(bottom_left=5, bottom_right=5),
                    "bottom": ft.border_radius.only(top_left=5, top_right=5),
                }[self.mark_side]
            ),
            animate=ft.Animation(500, ft.AnimationCurve.ELASTIC_OUT)
        )

        if self.mark_side in ("left","right"):
            return ft.Row(
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[self.mark, self.button] if self.mark_side == "left" else [self.button, self.mark]
            )
        else:
            return ft.Column(
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[self.mark, self.button] if self.mark_side == "top" else [self.button, self.mark]
            )

    def b_hovered(self, e:ft.HoverEvent):
        if not self.selected:
            if self.mark_side in ("left","top"):
                self.button.gradient.colors = [self.theme.background_two, self.theme.background_one] if e.data == "true" else [self.theme.background_one, self.theme.background_one]
            else:
                self.button.gradient.colors = [self.theme.background_one, self.theme.background_two] if e.data == "true" else [self.theme.background_one, self.theme.background_one]
            super().b_hovered(e)
    
    def b_clicked(self, e:ft.TapEvent):
        self.selected = not self.selected
        if self.icon is not None or self.selected_icon is not None:
            self.button_icon.name = self.selected_icon if self.selected else self.icon
            self.button_icon.color = self.theme.primary_tonal if self.selected else self.theme.font_two
        if self.text is not None:
            self.button_text.color = self.theme.primary_tonal if self.selected else self.theme.font_two
            self.button_text.weight = ft.FontWeight.BOLD if self.selected else None
        self.button.gradient.colors = [self.theme.background_two, self.theme.background_one] if self.mark_side in ("left","top") else [self.theme.background_one, self.theme.background_two]
        if self.mark_side in ("left","right"):
            self.mark.width = 3 if self.selected else 0
        else:
            self.mark.height = 3 if self.selected else 0
        self.update()
        if self.action is not None:
            self.action(e)

    def upd(self, theme:ClTheme=None, enabled:bool=None, selected:bool=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        - enabled: a flag saying the new available status of the button.
        - selected: a flag saying the new selection status of the button.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if enabled is not None and not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if selected is not None and not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if theme is not None:
            self.theme = theme
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.color = self.theme.primary_tonal if self.selected else self.theme.font_one
            if self.text is not None:
                self.button_text.color = self.theme.primary_tonal if self.selected else self.theme.font_one
            if self.mark_side in ("left","top"):
                self.button.gradient.colors = [self.theme.background_two, self.theme.background_one] if self.selected else [self.theme.background_one, self.theme.background_one]
            else:
                self.button.gradient.colors = [self.theme.background_one, self.theme.background_two] if self.selected else [self.theme.background_one, self.theme.background_one]
            self.mark.bgcolor = self.theme.background_two
            self.mark.content.bgcolor = self.theme.primary_tonal
        if enabled is not None:
            self.enabled = enabled
            self.button.disabled = not enabled
        if selected is not None:
            self.selected = not self.selected
            if self.icon is not None or self.selected_icon is not None:
                self.button_icon.name = self.selected_icon if self.selected else self.icon
                self.button_icon.color = self.theme.primary_tonal if self.selected else self.theme.font_one
            if self.text is not None:
                self.button_text.color = self.theme.primary_tonal if self.selected else self.theme.font_one
                self.button_text.weight = ft.FontWeight.BOLD if self.selected else None
            if self.mark_side in ("left","top"):
                self.button.gradient.colors = [self.theme.background_two, self.theme.background_one] if self.selected else [self.theme.background_one, self.theme.background_one]
            else:
                self.button.gradient.colors = [self.theme.background_one, self.theme.background_two] if self.selected else [self.theme.background_one, self.theme.background_one]
            if self.mark_side in ("left","right"):
                self.mark.width = 3 if self.selected else 0
            else:
                self.mark.height = 3 if self.selected else 0
        self.update()

# icon button (ok) (ok)
class ClIconButton(ft.UserControl):
    """Represents an icon button to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, icon:str=None, selected_icon:str=None, content_size:int=16, width:int=None,
                 height:int=None, expand:bool|int=None, rounded:bool=True, enabled:bool=True, selected:bool=False,
                 data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button.
        - icon: is the icon to be displayed in the button.
        - selected_icon: is the icon to be displayed in the button when it's selected.
        - content_size: is the size of the text and icons of the button.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more information.
        - rounded: is a flag saying when the button shape is rectangular with rounded corners or circular.
        - enabled: is a flag saying when the button is enabled or not.
        - selected: is a flag saying when the button is selected or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked.
        """
        # VALIDATION BLOCK
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if icon is not None and not isinstance(icon, str):
            raise ClError(
                error="Argument Error: <<icon>> must be string"
            )
        if selected_icon is not None and not isinstance(selected_icon, str):
            raise ClError(
                error="Argument Error: <<selected_icon>> must be string"
            )
        if not isinstance(content_size, int):
            raise ClError(
                error="Argument Error: <<content_size>> must be integer"
            )
        if width is not None and not isinstance(width, int):
            raise ClError(
                error="Argument Error: <<width>> must be integer"
            )
        if height is not None and not isinstance(height, int):
            raise ClError(
                error="Argument Error: <<height>> must be integer"
            )
        if expand is not None and not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean"
            )
        if not isinstance(rounded, bool):
            raise ClError(
                error="Argument Error: <<rounded>> must be boolean"
            )
        if not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )

        # INITIALIZATION BLOCK
        super().__init__()
        self.theme = theme
        self.icon = icon
        self.selected_icon = selected_icon if selected_icon is not None else self.icon
        self.content_size = content_size
        self.width = width
        self.height = height
        self.expand = expand
        self.rounded = rounded
        self.enabled = enabled
        self.selected = selected
        self.data = data
        self.action = action
    
    def build(self):
        
        # BUTTON
        self.button = ft.IconButton(
            data=self,
            width=self.width,
            height=self.height,
            icon=self.icon,
            selected_icon=self.selected_icon,
            icon_size=self.content_size+4,
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: self.theme.font_one,
                    ft.MaterialState.HOVERED: self.theme.font_two,
                    ft.MaterialState.SELECTED: self.theme.font_two
                },
                bgcolor={
                    ft.MaterialState.DEFAULT: self.theme.transparent,
                    ft.MaterialState.HOVERED: self.theme.transparent_05,
                    ft.MaterialState.SELECTED: self.theme.transparent_1
                },
                overlay_color={
                    ft.MaterialState.DEFAULT: self.theme.transparent,
                    ft.MaterialState.HOVERED: self.theme.transparent_05,
                    ft.MaterialState.SELECTED: self.theme.transparent_1
                },
                shadow_color="black",
                animation_duration=200,
                padding=0,
                shape=ft.RoundedRectangleBorder(radius=5) if self.rounded else ft.StadiumBorder()
            ),
            disabled=not self.enabled,
            selected=self.selected,
            autofocus=False,
            on_click=self.b_clicked
        )
        
        return self.button

    def b_clicked(self, e:ft.TapEvent):
        self.selected = not self.selected
        self.button.selected = self.selected
        self.update()
        if self.action is not None:
            self.action(e)

    def upd(self, theme:ClTheme=None, enabled:bool=None, selected=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        - enabled: a flag saying the new available status of the button.
        - selected: a flag saying the new selection status of the button.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if enabled is not None and not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if selected is not None and not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if theme is not None:
            self.theme = theme
            self.button.style.color = {
                ft.MaterialState.DEFAULT: self.theme.font_one,
                ft.MaterialState.HOVERED: self.theme.font_two,
                ft.MaterialState.SELECTED: self.theme.font_two
            }
            self.button.style.bgcolor = {
                ft.MaterialState.DEFAULT: self.theme.transparent,
                ft.MaterialState.HOVERED: self.theme.transparent_05,
                ft.MaterialState.SELECTED: self.theme.transparent_1
            }
            self.button.style.overlay_color = {
                ft.MaterialState.DEFAULT: self.theme.transparent,
                ft.MaterialState.HOVERED: self.theme.transparent_05,
                ft.MaterialState.SELECTED: self.theme.transparent_1
            }
        if enabled is not None:
            self.enabled = enabled
            self.button.disabled = not enabled
        if selected is not None:
            self.selected = selected
            self.button.selected = selected
        self.update()

# nav button (ok) (ok)
class ClNavButton(ft.UserControl):
    """Represents a navigation button to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, label:str, icon:str, selected_icon:str=None, content_size:int=16, 
                 width:int=None, height:int=None, expand:bool|int=None, rounded:bool=True, 
                 enabled:bool=True, selected:bool=False, all_as_button:bool=False, data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button.
        - label: is the text to display under the navigation button.
        - icon: is the icon to be displayed in the button.
        - selected_icon: is the icon to be displayed in the button when it's selected.
        - content_size: is the size of the text and icons of the button.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more information.
        - rounded: is a flag saying when the button shape is rectangular with rounded corners or circular.
        - enabled: is a flag saying when the button is enabled or not.
        - selected: is a flag saying when the button is selected or not.
        - all_as_button: is a flag saying if both elements, label and icon, must be displayed together as an entire button. If is True, ```rounded``` property will be ignored.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked.
        """
        # VALIDATION BLOCK
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if not isinstance(label, str):
            raise ClError(
                error="Argument Error: <<text>> must be string"
            )
        if not isinstance(icon, str):
            raise ClError(
                error="Argument Error: <<icon>> must be string"
            )
        if selected_icon is not None and not isinstance(selected_icon, str):
            raise ClError(
                error="Argument Error: <<selected_icon>> must be string"
            )
        if not isinstance(content_size, int):
            raise ClError(
                error="Argument Error: <<content_size>> must be integer"
            )
        if width is not None and not isinstance(width, int):
            raise ClError(
                error="Argument Error: <<width>> must be integer"
            )
        if height is not None and not isinstance(height, int):
            raise ClError(
                error="Argument Error: <<height>> must be integer"
            )
        if expand is not None and not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean"
            )
        if not isinstance(rounded, bool):
            raise ClError(
                error="Argument Error: <<rounded>> must be boolean"
            )
        if not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if not isinstance(selected, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if not isinstance(all_as_button, bool):
            raise ClError(
                error="Argument Error: <<all_as_button>> must be boolean"
            )
        # INITIALIZATION BLOCK
        super().__init__()
        self.theme = theme
        self.icon = icon
        self.selected_icon = selected_icon if selected_icon is not None else self.icon
        self.label = label
        self.content_size = content_size
        self.width = width
        self.height = height
        self.expand = expand
        self.rounded = rounded
        self.enabled = enabled
        self.selected = selected
        self.all_as_button = all_as_button
        self.data = data
        self.action = action

    def build(self):

        # BUTTON CONTENT
        # - button icon
        self.button_icon = ft.Container(
            bgcolor=self.theme.primary_block if not self.all_as_button and self.selected else self.theme.transparent,
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=10, top=2, right=10, bottom=2) if self.selected else ft.padding.only(left=5, top=2, right=5, bottom=2),
            border_radius=5 if self.rounded else 50,
            animate=ft.Animation(500, ft.AnimationCurve.ELASTIC_OUT),
            content=ft.Icon(
                name=self.icon if not self.selected else self.selected_icon,
                color=self.theme.font_one if not self.selected else self.theme.primary_tonal,
                size=self.content_size+6
            ),
        )
        # - button label
        self.button_label = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Text(
                value=self.label,
                color=self.theme.font_one,
                weight=ft.FontWeight.NORMAL if not self.selected else ft.FontWeight.BOLD,
                size=self.content_size-6,
                text_align=ft.TextAlign.CENTER
            )
        )
        if self.selected:
            self.button_label.content.color = self.theme.primary_tonal if self.all_as_button else self.theme.font_two

        # BUTTON
        self.button = ft.Container(
            data=self,
            width=self.width,
            height=self.height,
            bgcolor=self.theme.primary_block if self.all_as_button and self.selected else self.theme.transparent,
            alignment=ft.alignment.center,
            padding=5,
            border_radius=5,
            animate=100,
            animate_scale=ft.Animation(500, ft.AnimationCurve.ELASTIC_OUT) if self.selected else ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            content=ft.Column(
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[self.button_icon]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[self.button_label],
                    )
                ]
            ),
            on_hover=self.b_hovered,
            on_click=self.b_clicked
        )

        return self.button
    
    def b_hovered(self, e:ft.ControlEvent):
        if not self.selected:
            if self.all_as_button:
                self.button.bgcolor = self.theme.transparent_05 if e.data == "true" else self.theme.transparent
                self.button_icon.content.color = self.theme.font_two if e.data == "true" else self.theme.font_one
                self.button_label.content.color = self.theme.font_two if e.data == "true" else self.theme.font_one
            else:
                self.button_icon.bgcolor = self.theme.transparent_05 if e.data == "true" else self.theme.transparent
                self.button_icon.content.color = self.theme.font_two if e.data == "true" else self.theme.font_one
                self.button_label.content.color = self.theme.font_two if e.data == "true" else self.theme.font_one
            self.update()

    def b_clicked(self, e: ft.TapEvent):
        self.selected = not self.selected
        if self.all_as_button:
            self.button.bgcolor = self.theme.transparent_05 if not self.selected else self.theme.primary_block
            self.button_label.content.color = self.theme.font_two if not self.selected else self.theme.primary_tonal
            self.button.scale = 1 if not self.selected else 1.1
            self.button.animate_scale = ft.Animation(500, ft.AnimationCurve.ELASTIC_OUT) if self.selected else ft.Animation(200, ft.AnimationCurve.EASE_OUT)
        else:
            self.button_icon.bgcolor = self.theme.transparent_05 if not self.selected else self.theme.primary_block
            self.button_icon.padding = ft.padding.only(left=10, top=2, right=10, bottom=2) if self.selected else ft.padding.only(left=5, top=2, right=5, bottom=2)
        self.button_icon.content.color = self.theme.font_two if not self.selected else self.theme.primary_tonal
        self.button_icon.content.name = self.icon if not self.selected else self.selected_icon
        self.button_label.content.weight = ft.FontWeight.NORMAL if not self.selected else ft.FontWeight.BOLD
        self.update()
        if self.action is not None:
            self.action(e)
    
    def upd(self, theme: ClTheme = None, enabled: bool = None, selected=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        - enabled: a flag saying the new available status of the button.
        - selected: a flag saying the new selection status of the button.
        """
        if theme is not None:
            self.theme = theme
            self.button_icon.content.color = self.theme.primary_tonal if self.selected else self.theme.font_one
            if self.all_as_button:
                self.button.bgcolor = self.theme.primary_block if self.selected else self.theme.transparent
                self.button_label.content.color = self.theme.primary_tonal if self.selected else self.theme.font_two
            else:
                self.button_icon.bgcolor = self.theme.primary_block if self.selected else self.theme.transparent
                self.button_label.content.color = self.theme.font_two if self.selected else self.theme.font_one
        if enabled is not None:
            self.enabled = enabled
            if self.all_as_button:
                self.button.disabled = not enabled
            else:
                self.button_icon.disabled = not enabled
        if selected is not None:
            self.selected = selected
            self.button_icon.content.color = self.theme.primary_tonal if self.selected else self.theme.font_one
            self.button_icon.content.name = self.selected_icon if self.selected else self.icon
            self.button_label.content.weight = ft.FontWeight.NORMAL if not self.selected else ft.FontWeight.BOLD
            if self.all_as_button:
                self.button.scale = 1.1 if self.selected else 1
                self.button.animate_scale = ft.Animation(500, ft.AnimationCurve.ELASTIC_OUT) if self.selected else ft.Animation(200, ft.AnimationCurve.EASE_OUT)
                self.button.bgcolor = self.theme.primary_block if self.selected else self.theme.transparent
                self.button_label.content.color = self.theme.primary_tonal if self.selected else self.theme.font_two
            else:
                self.button_icon.padding = ft.padding.only(left=10, top=2, right=10, bottom=2) if self.selected else ft.padding.only(left=5, top=2, right=5, bottom=2)
                self.button_icon.bgcolor = self.theme.primary_block if self.selected else self.theme.transparent
                self.button_label.content.color = self.theme.font_two if self.selected else self.theme.font_one
        self.update()

# window button (ok) (ok)
class ClWinButton(ft.UserControl):
    """Represents a window action button to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, winaction="close", content_size:int=16, width:int=None, height:int=None,
                 expand:bool|int=None, data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button.
        - winaction: is the type of window action of the button. Can be 'close', 'minimize', 'maximize' or 'unmaximize'.
        - content_size: is the size of the text and icons of the button.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more information.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked. If it's None, the executed action will depends on the ```winaction``` by default.
        """
        # VALIDATION BLOCK
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if winaction not in("close", "minimize", "maximize","unmaximize"):
            raise ClError(
                error="Argument Error: <<winaction>> must be 'close', 'minimize', 'maximize' or 'unmaximize'"
            )
        if not isinstance(content_size, int):
            raise ClError(
                error="Argument Error: <<content_size>> must be integer"
            )
        if width is not None and not isinstance(width, int):
            raise ClError(
                error="Argument Error: <<width>> must be integer"
            )
        if height is not None and not isinstance(height, int):
            raise ClError(
                error="Argument Error: <<height>> must be integer"
            )
        if expand is not None and not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean"
            )
        # INITIALIZATION BLOCK
        super().__init__()
        self.theme = theme
        self.winaction = winaction
        self.icon = {
            "close": ft.icons.CLOSE,
            "minimize": ft.icons.MINIMIZE,
            "maximize": ft.icons.SQUARE_OUTLINED,
            "unmaximize": ft.icons.SQUARE
        }[winaction]
        self.content_size = content_size
        self.expand = expand
        self.data = data
        self.action = action

    def build(self):

        # BUTTON
        self.button = ft.IconButton(
            data=self,
            width=self.width,
            height=self.height,
            icon=self.icon,
            icon_size=self.content_size,
            style=ft.ButtonStyle(
                color={
                    ft.MaterialState.DEFAULT: self.theme.font_one,
                    ft.MaterialState.HOVERED: self.theme.font_two
                },
                bgcolor={
                    ft.MaterialState.DEFAULT: self.theme.transparent,
                    ft.MaterialState.HOVERED: self.theme.transparent_05 if self.winaction != "close" else self.theme.cancel,
                },
                overlay_color={
                    ft.MaterialState.DEFAULT: self.theme.transparent,
                    ft.MaterialState.HOVERED: self.theme.transparent_05 if self.winaction != "close" else self.theme.cancel,
                },
                shadow_color="black",
                animation_duration=200,
                padding=5,
                shape=ft.RoundedRectangleBorder(radius=5)
            ),
            autofocus=False,
            on_click=self.b_clicked
        )
        
        return self.button

    def b_clicked(self, e:ft.TapEvent):

        if self.action is not None:
            self.action(e)
        else:
            if self.winaction == "close":
                self.page.window_destroy()
            elif self.winaction == "minimize":
                self.page.window_minimized = True
                self.page.update()
            elif self.winaction == "maximize":
                self.page.window_maximized = True
                self.button.icon = ft.icons.SQUARE
                self.winaction = "unmaximize"
                self.update()
                self.page.update()
            elif self.winaction == "unmaximize":
                self.page.window_maximized = False
                self.button.icon = ft.icons.SQUARE_OUTLINED
                self.winaction = "maximize"
                self.update()
                self.page.update()

    def upd(self, theme:ClTheme=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if theme is not None:
            self.theme = theme
            self.button.style.color = {
                ft.MaterialState.DEFAULT: self.theme.font_one,
                ft.MaterialState.HOVERED: self.theme.font_two
            }
            self.button.style.bgcolor = {
                ft.MaterialState.DEFAULT: self.theme.transparent,
                ft.MaterialState.HOVERED: self.theme.transparent_05 if self.winaction != "close" else self.theme.cancel,
            }
            self.button.style.overlay_color = {
                ft.MaterialState.DEFAULT: self.theme.transparent,
                ft.MaterialState.HOVERED: self.theme.transparent_05 if self.winaction != "close" else self.theme.cancel,
            }
        self.update()

# color button (ok) (ok)
class ClColorButton(ClIconButton):
    """Represents a color selection button to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, color:str="blue", content_size:int=30, width:int=None, height:int=None, 
                 expand:bool|int=None, rounded:bool=True, enabled:bool=True, selected:bool=False, data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button.
        - color: is the color to be displayed in the button.
        - content_size: is the size of the text and icon in the button.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more information.
        - rounded: is a flag saying when the button shape is rectangular with rounded corners or circular.
        - enabled: is a flag saying when the button is enabled or not.
        - selected: is a flag saying when the button is selected or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked.
        """
        # SUPER BLOCK
        super().__init__(
            theme=theme,
            icon=ft.icons.SQUARE_ROUNDED,
            content_size=content_size,
            width=width,
            height=height,
            expand=expand,
            rounded=rounded,
            enabled=enabled,
            selected=selected,
            data=data,
            action=action
        )
        # VALIDATION BLOCK
        if not isinstance(color, str):
            raise ClError(
                error="Argument Error: <<color>> must be string"
            )
        self.color = color
    
    def build(self):
        
        super().build()
        self.button.icon_color = self.color
        self.button.selected_icon_color = self.color
        return self.button

# menu option button (ok) (ok)
class ClOptionButton(ft.UserControl):
    """Represents a menu option button to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, sub_options:list=None, text:str=None, icon:str=None, 
                 hover_icon:str=None, content_size:int=16, width:int=None, height:int=None, expand:bool|int=None, 
                 enabled:bool=True, data=None, action=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button.
        - sub_options: is a list of ```calet_button.ClOptionButton``` objects to display in a submenu.
        - text: is the text to be displayed in the button.
        - icon: is the icon to be displayed in the button.
        - hover_icon: is the icon to be displayed in the button when it's on hover.
        - content_size: is the size of the text and icons of the button.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more information.
        - enabled: is a flag saying when the button is enabled or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - action: is the custom function to execute when the button is clicked.
        """
        # VALIDATION BLOCK
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if text is not None and not isinstance(text, str):
            raise ClError(
                error="Argument Error: <<text>> must be string"
            )
        if icon is not None and not isinstance(icon, str):
            raise ClError(
                error="Argument Error: <<icon>> must be string"
            )
        if hover_icon is not None and not isinstance(hover_icon, str):
            raise ClError(
                error="Argument Error: <<hover_icon>> must be string"
            )
        if content_size is not None and not isinstance(content_size, int):
            raise ClError(
                error="Argument Error: <<content_size>> must be integer"
            )
        if width is not None and not isinstance(width, int):
            raise ClError(
                error="Argument Error: <<width>> must be integer"
            )
        if height is not None and not isinstance(height, int):
            raise ClError(
                error="Argument Error: <<height>> must be integer"
            )
        if expand is not None and not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean"
            )
        if not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean"
            )
        if sub_options is not None:
            if not isinstance(sub_options, list):
                raise ClError(
                    error="Argument Error: <<sub_options>> must be a list of 'calet_button.ClOptionButton' objects"
                )
            else:
                for i in range(len(sub_options)):
                    if not isinstance(sub_options[i], ClOptionButton):
                        raise ClError(
                            error=f"Argument Error: <<sub_options[{i}]>> must be a 'calet_button.ClOptionButton' object"
                        )
        # INITIALIZATION BLOCK
        super().__init__()
        self.theme = theme
        self.sub_options = sub_options
        self.text = text
        self.icon = icon
        self.hover_icon = hover_icon if hover_icon is not None else icon
        self.content_size = content_size
        self.width = width
        self.height = height
        self.enabled = enabled
        self.data = data
        self.action = action
    
    def build(self):

        # BUTTON CONTENT
        # - button icon
        if self.icon is not None:
            self.button_icon = ft.Icon(
                name=self.icon,
                color=self.theme.font_one,
                size=self.content_size+4
            )
        # - button text
        if self.text is not None:
            self.button_text = ft.Text(
                value=self.text,
                color=self.theme.font_one,
                text_align=ft.TextAlign.CENTER,
                size=self.content_size
            )

        # BUTTON
        # - without sub options
        if not self.sub_options:
            self.button = ft.MenuItemButton(
                data=self.data,
                width=self.width,
                height=self.height,
                style=ft.ButtonStyle(
                    bgcolor={
                        ft.MaterialState.DEFAULT: self.theme.transparent,
                        ft.MaterialState.HOVERED: self.theme.transparent_05,
                    },
                    overlay_color={
                        ft.MaterialState.DEFAULT: self.theme.transparent,
                        ft.MaterialState.HOVERED: self.theme.transparent_05,
                    },
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=5,
                    animation_duration=200
                ),
                disabled=not self.enabled,
                focus_on_hover=False,
                on_hover=self.b_hovered,
                on_click=self.action
            )
        # - with sub options
        else:
            self.button = ft.SubmenuButton(
                data=self,
                width=self.width,
                height=self.height,
                style=ft.ButtonStyle(
                    bgcolor={
                        ft.MaterialState.DEFAULT: self.theme.transparent,
                        ft.MaterialState.HOVERED: self.theme.transparent_05,
                    },
                    overlay_color={
                        ft.MaterialState.DEFAULT: self.theme.transparent,
                        ft.MaterialState.HOVERED: self.theme.transparent_05,
                    },
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=5,
                    animation_duration=200
                ),
                menu_style=ft.MenuStyle(
                    bgcolor=self.theme.background_two,
                    surface_tint_color=self.theme.transparent,
                    shadow_color="black",
                    padding=5,
                    elevation=5,
                    shape=ft.RoundedRectangleBorder(radius=5),
                    side=ft.BorderSide(
                        width=1,
                        color=self.theme.divider
                    )
                ),
                disabled=not self.enabled,
                controls=[
                    ft.MenuItemButton(width=0,height=5)
                ]+self.sub_options+[
                    ft.MenuItemButton(width=0,height=5)
                ],
                on_hover=self.b_hovered
            )
        if self.icon is not None and self.text is not None:
            self.button.leading = self.button_icon
            self.button.content = self.button_text
        elif self.icon is not None or self.text is not None:
            self.button.content = self.button_text if self.text is not None else self.button_icon

        return self.button

    # METODOS MANEJADORES DE EVENTOS
    def b_hovered(self, e:ft.HoverEvent):
        if self.icon is not None:
            self.button_icon.name = self.hover_icon if e.data == "true" else self.icon
            self.button_icon.color = self.theme.font_two if e.data == "true" else self.theme.font_one
        if self.text is not None:
            self.button_text.color = self.theme.font_two if e.data == "true" else self.theme.font_one
        self.update()
    
    def upd(self,  theme:ClTheme=None, enabled:bool=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        - enabled: is a flag saying the new enable status of the button.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if enabled is not None and not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if theme is not None:
            self.theme = theme
            if self.icon is not None:
                self.button_icon.color = self.theme.font_one
            if self.text is not None:
                self.button_text.color = self.theme.font_one
            self.button.style.bgcolor = {
                ft.MaterialState.DEFAULT: self.theme.transparent,
                ft.MaterialState.HOVERED: self.theme.transparent_05,
            }
            self.button.style.overlay_color = {
                ft.MaterialState.DEFAULT: self.theme.transparent,
                ft.MaterialState.HOVERED: self.theme.transparent_05,
            }
            if isinstance(self.button, ft.SubmenuButton):
                self.button.menu_style.bgcolor = self.theme.background_one
                self.button.menu_style.side.color = self.theme.font_one
        if enabled is not None:
            self.enabled = enabled
            self.button.disabled = not enabled
        self.update()

# menu button (ok) (ok)
class ClMenuButton(ft.UserControl):
    """Represents a menu button that display a context menu when is clicked
    to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, options:list[ClOptionButton], main_button:ClTextButton=None, main_to_left:bool=True, 
                 text:str=None, icon:str=None, hover_icon:str=None, icon_to_left:bool=True, content_size:int=16, 
                 width:int=None, height:int=None, crystaline:bool=False, expand:bool|int=None, rounded:bool=True, enabled:bool=True, data=None):
        """Use this properties to personalize the button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the button.
        - options: is a list of ```calet_button.ClOptionButton``` buttons to display in the opened menu.
        - main_button: is a text button to display on the side of the menu button.
        - main_to_left: is a flag saying if the main button must be displayed in the left or right side.
        - text: is the text to be displayed in the button.
        - icon: is the icon to be displayed in the button.
        - hover_icon: is the icon to be displayed in the button when it's on hover.
        - icon_to_left: is a flag saying if the main icon of the menu button must be displayed in the left or right side. If no text was given this property will be ignored.
        - content_size: is the size of the text and icons of the button.
        - width: is a custom width for the button.
        - height: is a custom height for the button.
        - crystaline: is a flag saying if the button background color must be semi-transparent or fully transparent.
        - expand: is the responsive expansion of the button in his container. See ```expand``` Flet property for more  information.
        - rounded: is a flag saying when the button shape is rectangular (True) or circular (False).
        - enabled: is a flag saying when the button is enabled or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        """
        # VALIDATION BLOCK
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class."
            )
        if main_button is not None and not isinstance(main_button, ClTextButton):
            raise ClError(
                error="Argument Error: <<main_button>> must be an instance of 'calet_button.ClTextButton' class."
            )
        if not isinstance(main_to_left, bool):
            raise ClError(
                error="Argument Error: <<main_to_left>> must be boolean."
            )
        if text is not None and not isinstance(text, str):
            raise ClError(
                error="Argument Error: <<text>> must be string"
            )
        if icon is not None and not isinstance(icon, str):
            raise ClError(
                error="Argument Error: <<icon>> must be string"
            )
        if hover_icon is not None and not isinstance(hover_icon, str):
            raise ClError(
                error="Argument Error: <<hover_icon>> must be string"
            )
        if not isinstance(icon_to_left, bool):
            raise ClError(
                error="Argument Error: <<icon_to_left>> must be boolean."
            )
        if not isinstance(content_size, int):
            raise ClError(
                error="Argument Error: <<content_size>> must be integer."
            )
        if width is not None and not isinstance(width, int):
            raise ClError(
                error="Argument Error: <<width>> must be integer"
            )
        if height is not None and not isinstance(height, int):
            raise ClError(
                error="Argument Error: <<height>> must be integer"
            )
        if not isinstance(crystaline, bool):
            raise ClError(
                error="Argument Error: <<crystaline>> must be boolean."
            )
        if expand is not None and not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean."
            )
        if not isinstance(rounded, bool):
            raise ClError(
                error="Argument Error: <<rounded>> must be boolean."
            )
        if not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<selected>> must be boolean."
            )
        if not isinstance(options, list):
            raise ClError(
                error="Argument Error: <<options>> must be a list of 'calet_button.ClOptionButton' objects."
            )
        else:
            for i in range(len(options)):
                if not isinstance(options[i], ClOptionButton):
                    raise ClError(
                        error=f"Argument Error: <<options[{i}]>> must be a 'calet_button.ClOptionButton' object."
                    )
        # INITIALIZATION BLOCK
        super().__init__()
        self.theme = theme
        self.options = options
        self.main_button = main_button
        self.main_to_left = main_to_left
        self.text = text
        self.icon = icon
        self.hover_icon = hover_icon if hover_icon is not None else icon
        self.icon_to_left = icon_to_left
        self.content_size = content_size
        self.crystaline = crystaline
        self.expand = expand
        self.rounded = rounded
        self.enabled = enabled
        self.data = data
    
    def build(self):

        # MENU BUTTON CONTENT
        # - expand menu icon
        if self.icon is None and self.text is None:
            self.menu_icon = ft.Icon(
                name=ft.icons.EXPAND_MORE,
                color=self.theme.font_one,
                size=self.content_size+4
            )
        # - menu button icon
        if self.icon is not None:
            self.button_icon = ft.Icon(
                name=self.icon,
                color=self.theme.font_one,
                size=self.content_size+4
            )
        # - menu button text
        if self.text is not None:
            self.button_text = ft.Text(
                value=self.text,
                color=self.theme.font_one,
                size=self.content_size,
                text_align=ft.TextAlign.CENTER
            )
        
        # MENU BUTTON
        self.button = ft.SubmenuButton(
            data=self,
            width=self.width,
            height=self.height,
            style=ft.ButtonStyle(
                bgcolor={
                    ft.MaterialState.DEFAULT: self.theme.transparent if not self.crystaline else self.theme.transparent_1,
                    ft.MaterialState.HOVERED: self.theme.transparent_05 if not self.crystaline else self.theme.transparent_1,
                },
                overlay_color={
                    ft.MaterialState.DEFAULT: self.theme.transparent if not self.crystaline else self.theme.transparent_1,
                    ft.MaterialState.HOVERED: self.theme.transparent_05 if not self.crystaline else self.theme.transparent_1,
                },
                shape=ft.RoundedRectangleBorder(radius=5) if self.rounded else ft.StadiumBorder(),
                padding=5,
                animation_duration=200
            ),
            menu_style=ft.MenuStyle(
                bgcolor=self.theme.background_two,
                surface_tint_color=self.theme.transparent,
                shadow_color="black",
                padding=5,
                elevation=5,
                shape=ft.RoundedRectangleBorder(radius=5),
                side=ft.BorderSide(
                    width=1,
                    color=self.theme.divider
                ),
            ),
            disabled=not self.enabled,
            controls=[
                ft.MenuItemButton(width=0,height=5)
            ]+self.options+[
                ft.MenuItemButton(width=0,height=5)
            ],
            on_hover=self.b_hovered
        )
        if self.text is None:
            self.button.content = self.menu_icon if self.icon is None else self.button_icon
            self.button.width = self.content_size*2
        else:
            self.button.content = self.button_text
            if self.icon is not None and self.icon_to_left:
                self.button.leading = self.button_icon
            elif self.icon is not None:
                self.button.trailing = self.button_icon

        c_button = ft.Container(
            width=self.width,
            height=self.height,
            alignment=ft.alignment.center,
            border_radius=5 if self.rounded else 50,
            content=ft.MenuBar(
                style=ft.MenuStyle(
                    alignment=ft.alignment.center,
                    bgcolor=self.theme.transparent,
                    padding=0,
                    elevation=0,
                    shape=ft.RoundedRectangleBorder(radius=5) if self.rounded else ft.StadiumBorder()
                ),
                controls=[self.button]
            )
        ) 
        return c_button if self.main_button is None else ft.Row(
            spacing=0,
            controls=[self.main_button, c_button] if self.main_to_left else [c_button, self.main_button]
        )
    
    def b_hovered(self, e:ft.HoverEvent):
        if self.icon is None and self.text is None:
            self.menu_icon.color = self.theme.font_two if e.data == "true" else self.theme.font_one
        else:
            if self.icon is not None:
                self.button_icon.color = self.theme.font_two if e.data == "true" else self.theme.font_one
            if self.text is not None:
                self.button_text.color = self.theme.font_two if e.data == "true" else self.theme.font_one
        self.update()

    def upd(self,  theme:ClTheme=None, enabled:bool=None):
        """Update the value of all given properties.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the button.
        - enabled: is a flag saying the new enable status of the button.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if enabled is not None and not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if theme is not None:
            self.theme = theme
            if self.icon is None and self.text is None:
                self.menu_icon.color = self.theme.font_one
            if self.main_button is not None:
                self.main_button.upd(theme=theme)
            self.button.style.bgcolor = {
                ft.MaterialState.DEFAULT: self.theme.transparent if not self.crystaline else self.theme.transparent_1,
                ft.MaterialState.HOVERED: self.theme.transparent_05 if not self.crystaline else self.theme.transparent_1,
            }
            self.button.style.overlay_color = {
                ft.MaterialState.DEFAULT: self.theme.transparent if not self.crystaline else self.theme.transparent_1,
                ft.MaterialState.HOVERED: self.theme.transparent_05 if not self.crystaline else self.theme.transparent_1,
            }
            self.button.menu_style.bgcolor = self.theme.background_one
            self.button.menu_style.side.color = self.theme.font_one
        if enabled is not None:
            self.enabled = enabled
            self.button.disabled = not enabled
            if self.main_button is not None:
                self.main_button.upd(enabled=enabled)
        self.update()

# switch button (ok) (ok)
class ClSwitch(ft.UserControl):
    """Represents a switch button to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, inactive_label:str=None, active_label:str=None,
                 left_label:bool=True, inactive_icon:str=None, active_icon:str=None, 
                 expand:bool=None, active:bool=False, enabled:bool=True, data=None, 
                 activated_action=None, deactivated_action=None):
        """Use this properties to personalize the switch:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the switch.
        - inactive_label: is the text to display near the switch when is inactive.
        - active_label: is the text to display near the switch when is active.
        - left_label: is a flag saying if the label must appear on the left (True) or right (False) side of the switch.
        - inactive_icon: is the icon to display in the switch thumb when is inactive.
        - active_icon: is the icon to display in the switch thumb when is active.
        - expand: is the responsive expansion of the switch in his container. See ```expand``` Flet property for more  information.
        - active: is a flag saying when the switch is active or not.
        - enabled: is a flag saying when the switch is enabled or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - activated_action: is the custom function to execute when the switch is activated.
        - deactivated_action: is the custom function to execute when the switch is deactivated.
        """
        # VALIDATION BLOCK
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if inactive_label is not None and not isinstance(inactive_label, str):
            raise ClError(
                error="Argument Error: <<inactive_label>> must be string"
            )
        if active_label is not None and not isinstance(active_label, str):
            raise ClError(
                error="Argument Error: <<active_label>> must be string"
            )
        if not isinstance(left_label, bool):
            raise ClError(
                error="Argument Error: <<left_label>> must be boolean"
            )
        if inactive_icon is not None and not isinstance(inactive_icon, str):
            raise ClError(
                error="Argument Error: <<inactive_icon>> must be string"
            )
        if active_icon is not None and not isinstance(active_icon, str):
            raise ClError(
                error="Argument Error: <<active_icon>> must be string"
            )
        if expand is not None and not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean"
            )
        if not isinstance(active, bool):
            raise ClError(
                error="Argument Error: <<active>> must be boolean"
            )
        if not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        # INITIALIZATION BLOCK
        super().__init__()
        self.theme = theme
        if inactive_label is None and active_label is None:
            self.inactive_label = inactive_label
            self.active_label = active_label
        else:
            self.inactive_label = inactive_label if inactive_label is not None else active_label
            self.active_label = active_label if active_label is not None else inactive_label
        self.left_label = left_label
        self.inactive_icon = inactive_icon
        self.active_icon = active_icon if active_icon is not None else active_icon
        self.expand = expand
        self.active = active
        self.enabled = enabled
        self.data = data
        self.activated_action = activated_action
        self.deactivated_action = deactivated_action
    
    def build(self):

        # LABEL
        if self.inactive_label is not None:
            self.switch_label = ft.Text(
                value=self.inactive_label if not self.active else self.active_label,
                color=self.theme.font_one,
                text_align=ft.TextAlign.RIGHT if self.left_label else ft.TextAlign.LEFT
            )

        # SWITCH
        self.switch = ft.Switch(
            data=self,
            track_color={
                ft.MaterialState.DEFAULT: self.theme.secondary_block,
                ft.MaterialState.SELECTED: self.theme.primary
            },
            thumb_color={
                ft.MaterialState.DEFAULT: self.theme.secondary,
                ft.MaterialState.SELECTED: self.theme.primary_block,
            },
            focus_color=self.theme.primary_block,
            thumb_icon={
                ft.MaterialState.DEFAULT: self.inactive_icon,
                ft.MaterialState.SELECTED: self.active_icon
            },
            value=self.active,
            disabled=not self.enabled,
            on_change=self.b_changed
        )

        if self.inactive_label is None:
            return self.switch
        else:
            return ft.Row(
                spacing=10,
                controls=[
                    self.switch_label,
                    self.switch
                ] if self.left_label else [
                    self.switch,
                    self.switch_label
                ]
            )
    
    def b_changed(self, e:ft.ControlEvent):
        self.active = self.switch.value
        if self.inactive_label is not None:
            self.switch_label.value = self.inactive_label if not self.active else self.active_label
        self.update()
        if self.active and self.activated_action is not None:
            self.activated_action(e)
        elif self.deactivated_action is not None:
            self.deactivated_action(e)

    def upd(self, theme:ClTheme=None, enabled:bool=None, active:bool=None):
        """Update the value of all given properties of the switch.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the switch.
        - enabled: a flag saying the new available status of the switch.
        - active: a flag saying the new activation status of the switch.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if enabled is not None and not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if active is not None and not isinstance(active, bool):
            raise ClError(
                error="Argument Error: <<active>> must be boolean"
            )
        if theme is not None:
            self.theme = theme
            if self.inactive_label is not None:
                self.switch_label.color = self.theme.font_one
            self.switch.track_color = {
                ft.MaterialState.DEFAULT: self.theme.secondary_block,
                ft.MaterialState.SELECTED: self.theme.primary
            }
            self.switch.thumb_color = {
                ft.MaterialState.DEFAULT: self.theme.secondary,
                ft.MaterialState.SELECTED: self.theme.primary_block
            }
            self.switch.focus_color = self.theme.primary_block
        if enabled is not None:
            self.enabled = enabled
            self.switch.disabled = not enabled
        if active is not None:
            self.active = active
            self.switch.value = active
            if self.inactive_label is not None:
                self.switch_label.value = self.inactive_label if not active else self.active_label
        self.update()

# Experimental custom switch
class ClCustomSwitch(ft.UserControl):
    """Represents a custom switch button to use in Flet Apps"""
    def __init__(self, theme:ClTheme):
        super().__init__()
        self.theme = theme
    
    def build(self):

        # SWITCH
        # - thumb
        self.thumb = ft.Container(
            width=15,
            height=15,
            bgcolor=self.theme.secondary,
            border_radius=50,
            offset=ft.Offset(0,0),
            animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
            animate_offset=ft.Animation(1000, ft.AnimationCurve.ELASTIC_OUT),
            on_hover=self.b_hovered,
        )
        # - switch
        self.switch = ft.Container(
            width=50,
            height=30,
            alignment=ft.alignment.center_left,
            padding=ft.padding.only(left=5, right=2),
            bgcolor=self.theme.secondary_block,
            border=ft.border.all(2, self.theme.secondary),
            border_radius=50,
            animate=100,
            content=self.thumb
        )
        # - hover thumb
        self.hover_thumb = ft.Container(
            visible=False,
            width=35,
            height=35,
            bgcolor=self.theme.transparent_1,
            border_radius=50,
            offset=ft.Offset(-0.1,0),
            animate_offset=ft.Animation(300, ft.AnimationCurve.ELASTIC_OUT),
            on_hover=self.b_hovered,
            on_click=self.b_clicked,
        )
        

        return ft.Stack(
            controls=[
                ft.Column(
                    spacing=0,
                    controls=[
                        ft.Row(expand=1),
                        ft.Row(expand=8, controls=[self.switch]),
                        ft.Row(expand=1)
                    ]
                ),
                ft.Column(
                    spacing=0,
                    controls=[
                        ft.Row(
                            expand=10,
                            controls=[self.hover_thumb]
                        )
                    ]
                )
            ]
        )
    
    def b_hovered(self, e:ft.HoverEvent):
        self.hover_thumb.visible = True if e.data == "true" else False
        self.update()

    def b_clicked(self, e:ft.TapEvent):
        if self.thumb.offset.x == 0:
            self.switch.bgcolor = self.theme.primary
            self.switch.border = ft.border.all(2, self.theme.primary)
            self.hover_thumb.offset = ft.Offset(0.5,0)
            self.thumb.offset = ft.Offset(0.7,0)
            self.thumb.width = 23
            self.thumb.height = 23
            self.thumb.bgcolor = self.theme.transparent_inverse
        else:
            self.switch.bgcolor = self.theme.secondary_block
            self.switch.border = ft.border.all(2, self.theme.secondary)
            self.hover_thumb.offset = ft.Offset(-0.1,0)
            self.thumb.offset = ft.Offset(0,0)
            self.thumb.width = 15
            self.thumb.height = 15
            self.thumb.bgcolor = self.theme.secondary
        self.update()

# radio button (ok) (ok)
class ClRadio(ft.UserControl):
    """Represents a radio button to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, value:str, label:str=None, left_label:bool=True,
                 inversed_colors:bool=False, expand:bool=None, enabled:bool=True, data=None):
        """Use this properties to personalize the radio button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the radio.
        - label: is the text to display near the radio.
        - left_label: is a flag saying if the label must appear on the left (True) or right (False) side of the radio.
        - inversed_colors: is a flag saying if the primary color must be used to paint the fill color or the check color.
        - expand: is the responsive expansion of the radio in his container. See ```expand``` Flet property for more  information.
        - enabled: is a flag saying when the radio is enabled or not.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        """
        # VALIDATION BLOCK
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if not isinstance(value, str):
            raise ClError(
                error="Argument Error: <<value>> must be string"
            )
        if label is not None and not isinstance(label, str):
            raise ClError(
                error="Argument Error: <<label>> must be string"
            )
        if not isinstance(left_label, bool):
            raise ClError(
                error="Argument Error: <<left_label>> must be boolean"
            )
        if not isinstance(inversed_colors, bool):
            raise ClError(
                error="Argument Error: <<inversed_colors>> must be boolean"
            )
        if expand is not None and not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean"
            )
        if not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        # INITIALIZATION BLOCK
        super().__init__()
        self.theme = theme
        self.value = value
        self.label = label
        self.left_label = left_label
        self.inversed_colors = inversed_colors
        self.expand = expand
        self.enabled = enabled
        self.data = data
    
    def build(self):

        # LABEL
        if self.label is not None:
            self.radio_label = ft.Text(
                value=self.label,
                color=self.theme.font_one,
                text_align=ft.TextAlign.RIGHT if self.left_label else ft.TextAlign.LEFT
            )

        # RADIO
        self.radio = ft.Radio(
            data=self,
            value=self.value,
            active_color=self.theme.primary if not self.inversed_colors else self.theme.font_three,
            disabled=not self.enabled
        )

        if self.label is None:
            return self.radio
        else:
            return ft.Row(
                spacing=10,
                controls=[
                    self.radio_label,
                    self.radio
                ] if self.left_label else [
                    self.radio,
                    self.radio_label
                ]
            )

    def upd(self, theme:ClTheme=None, enabled:bool=None):
        """Update the value of all given properties of the radio.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the radio.
        - enabled: a flag saying the new available status of the radio.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if enabled is not None and not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if theme is not None:
            self.theme = theme
            self.radio.active_color = self.theme.primary if not self.inversed_colors else self.theme.font_three
            if self.label is not None:
                self.radio_label.color = self.theme.font_one
        if enabled is not None:
            self.enabled = enabled
            self.radio.disabled = not enabled
        self.update()

# check button (ok) (ok)
class ClCheck(ft.UserControl):
    """Represents a check button to be used in Flet apps.
    """
    def __init__(self, theme:ClTheme, value:bool=False, label:str=None, left_label:bool=True,
                 expand:bool=None, three_states:bool=False, inversed_colors:bool=False, enabled:bool=True, data=None,
                 activated_action=None, deactivated_action=None, limbo_action=None):
        """Use this properties to personalize the check button:\n
        ---
        - theme: is an instance of ```calet_theme.ClTheme``` with the colors set to paint the check.
        - label: is the text to display near the check.
        - left_label: is a flag saying if the label must appear on the left (True) or right (False) side of the check.
        - expand: is the responsive expansion of the check in his container. See ```expand``` Flet property for more information.
        - three_states: is a flag saying if the check can have three different values (True) or only two (False).
        - enabled: is a flag saying when the check is enabled or not.
        - inversed_colors: is a flag saying if the primary color must be used to paint the fill color or the check color.
        - data: is a custom and invisible data to be stored in this object for custom uses.
        - activated_action: is the custom function to execute when the check is activated.
        - deactivated_action: is the custom function to execute when the check is deactivated.
        - limbo_action: is the custom function to execute when the check isn't activated or deactivated in three states mode.
        """
        # VALIDATION BLOCK
        if not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if value is not None and not isinstance(value, bool):
            raise ClError(
                error="Argument Error: <<value>> must be boolean"
            )
        if label is not None and not isinstance(label, str):
            raise ClError(
                error="Argument Error: <<label>> must be string"
            )
        if not isinstance(left_label, bool):
            raise ClError(
                error="Argument Error: <<left_label>> must be boolean"
            )
        if expand is not None and not isinstance(expand, (bool,int)):
            raise ClError(
                error="Argument Error: <<expand>> must be integer or boolean"
            )
        if not isinstance(three_states, bool):
            raise ClError(
                error="Argument Error: <<three_states>> must be boolean"
            )
        if not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if not isinstance(inversed_colors, bool):
            raise ClError(
                error="Argument Error: <<inversed_colors>> must be boolean"
            )
        # INITIALIZATION BLOCK
        super().__init__()
        self.theme = theme
        if not three_states:
            self.value = value if value is not None else False
        else:
            self.value = value
        self.label = label
        self.left_label = left_label
        self.expand = expand
        self.three_states = three_states
        self.enabled = enabled
        self.inversed_colors = inversed_colors
        self.data = data
        self.activated_action = activated_action
        self.deactivated_action = deactivated_action
        self.limbo_action = limbo_action
    
    def build(self):

        # LABEL
        if self.label is not None:
            self.check_label = ft.Text(
                value=self.label,
                color=self.theme.font_one,
                text_align=ft.TextAlign.RIGHT if self.left_label else ft.TextAlign.LEFT
            )

        # CHECK
        self.check = ft.Checkbox(
            data=self,
            active_color=self.theme.primary if not self.inversed_colors else self.theme.font_three,
            check_color=self.theme.font_three if not self.inversed_colors else self.theme.primary,
            tristate=self.three_states,
            disabled=not self.enabled,
            value=self.value,
            on_change=self.b_changed
        )

        if self.label is None:
            return self.check
        else:
            return ft.Row(
                spacing=10,
                controls=[
                    self.check_label,
                    self.check
                ] if self.left_label else [
                    self.check,
                    self.check_label
                ]
            )
    
    def b_changed(self, e:ft.ControlEvent):
        self.value = self.check.value
        if self.value and self.activated_action is not None:
            self.activated_action(e)
        elif not self.value and self.deactivated_action is not None:
            self.deactivated_action(e)
        elif self.limbo_action is not None:
            self.limbo_action(e)
        self.update()
    
    def upd(self, theme:ClTheme=None, enabled:bool=None, value:str=None):
        """Update the value of all given properties of the check.\n
        ---
        - theme: an instance of ```calet_theme.ClTheme``` containing the new colors set for the check.
        - enabled: a flag saying the new available status of the check.
        - value: a string key for the new selection value of the check. Can be 'true' for selected, 'false' for unselected or 'none' for limbo.
        """
        if theme is not None and not isinstance(theme, ClTheme):
            raise ClError(
                error="Argument Error: <<theme>> must be an instance of 'calet_theme.ClTheme' Calet class"
            )
        if enabled is not None and not isinstance(enabled, bool):
            raise ClError(
                error="Argument Error: <<enabled>> must be boolean"
            )
        if value is not None and not isinstance(value, str):
            raise ClError(
                error="Argument Error: <<value>> must be string"
            )
        elif value not in ("true","false","none"):
            raise ClError(
                error="Argument Error: <<value>> must be 'true', 'false' or 'none'"
            )
        elif value == "none" and not self.three_states:
            raise ClError(
                error="Argument Error: <<value>> can not be 'none' because this check button doesn't support three states"
            )
        if theme is not None:
            self.theme = theme
            self.check.active_color = self.theme.primary if not self.inversed_colors else self.theme.font_three
            self.check.check_color = self.theme.font_three if not self.inversed_colors else self.theme.primary
            if self.label is not None:
                self.check_label.color = self.theme.font_one
        if enabled is not None:
            self.enabled = enabled
            self.check.disabled = not enabled
        if value is not None:
            self.value = {"true": True, "false": False, "none": None}[value]
            self.check.value = self.value
        self.update()

if __name__ == "__main__":

    def main(page: ft.Page):

        theme = ClTheme(on_light=ClLightTheme(), mode="light")
        dktheme = ClTheme(on_light=ClLightTheme(), on_dark=ClDarkTheme(), mode="dark")

        # window buttons
        b_minimize = ClWinButton(
            theme=theme,
            winaction="minimize"
        )
        b_maximize = ClWinButton(
            theme=theme,
            winaction="maximize"
        )
        b_close = ClWinButton(
            theme=theme,
            winaction="close"
        )

        # app buttons
        b_text = ClTextButton(
            theme=theme,
            text="Text",
            icon=ft.icons.PEOPLE,
        )
        b_select = ClSelectButton(
            theme=theme,
            text="Select",
            icon=ft.icons.PEOPLE_OUTLINED,
            hover_icon=ft.icons.PEOPLE,
            selected=True
        )
        b_normal = ClButton(
            theme=theme,
            text="Normal",
            icon=ft.icons.PEOPLE_OUTLINED,
            hover_icon=ft.icons.PEOPLE
        )
        b_accept = ClAcceptButton(
            theme=theme,
            text="Accept",
            icon=ft.icons.PEOPLE_OUTLINED,
            hover_icon=ft.icons.PEOPLE
        )
        b_cancel = ClCancelButton(
            theme=theme,
            text="Cancel",
            icon=ft.icons.PEOPLE_OUTLINED,
            hover_icon=ft.icons.PEOPLE
        )
        b_tonal = ClTonalButton(
            theme=theme,
            text="Tonal",
            icon=ft.icons.PEOPLE_OUTLINED,
            hover_icon=ft.icons.PEOPLE,
        )
        b_mode = ClModeButton(
            theme=theme,
            text="Light",
            second_text="Dark",
            icon=ft.icons.LIGHT_MODE_OUTLINED,
            hover_icon=ft.icons.LIGHT_MODE,
            second_icon=ft.icons.DARK_MODE_OUTLINED,
            hover_second_icon=ft.icons.DARK_MODE,
            first_mode=False
        )
        b_icon = ClIconButton(
            theme=theme,
            icon=ft.icons.MENU,
            selected_icon=ft.icons.MENU_OPEN
        )
        b_color = ClColorButton(
            theme=theme,
            color=ft.colors.RED,
        )
        b_switch = ClSwitch(
            theme=theme
        )
        b_custom_switch = ClCustomSwitch(
            theme=theme
        )
        b_radio1 = ClRadio(
            theme=theme,
            value="rd1",
            label="Radio 1"
        )
        b_radio2 = ClRadio(
            theme=theme,
            value="rd2",
            label="Radio 2",
            left_label=False
        )
        b_check1 = ClCheck(
            theme=theme,
            label="Two states:",
        )
        b_check2 = ClCheck(
            theme=theme,
            value=True
        )
        b_check3 = ClCheck(
            theme=theme,
            value=None,
            three_states=True,
            label="Three states",
            left_label=False
        )

        # navigation buttons
        b_filter = ClFilterButton(
            theme=theme,
            text="Tab",
            rounded=False
        )
        b_outlinedfilter = ClOutlineFilterButton(
            theme=theme,
            text="Outlined Tab",
            rounded=False
        )
        b_filledfilter = ClSelectButton(
            theme=theme,
            text="Filled Tab",
            rounded=False
        )
        b_nav = ClNavButton(
            expand=1,
            theme=theme,
            icon=ft.icons.SETTINGS_OUTLINED,
            selected_icon=ft.icons.SETTINGS,
            label="Nav Button",
            rounded=False,
            all_as_button=True
        )
        b_menu = ClMenuButton(
            theme=theme,
            main_button=ClTextButton(
                theme=theme,
                text="Menu"
            ),
            # main_to_left=False,
            # text="Menu",
            # icon=ft.icons.MENU,
            # icon_to_left=False,
            options=[
                ClOptionButton(
                    theme=theme,
                    icon=ft.icons.PERSON,
                    text="Option"
                ),
                ClOptionButton(
                    theme=theme,
                    icon=ft.icons.PERSON_2,
                    text="With Submenu",
                    sub_options=[
                        ClOptionButton(
                            theme=theme,
                            icon=ft.icons.PERSON_3,
                            text="SubOption"
                        )
                    ]
                )
            ]
        )
        b_navtab1 = ClNavTab(
            theme=dktheme,
            text="NavTab 1",
        )
        b_navtab2 = ClNavTab(
            theme=dktheme,
            text="NavTab 2",
            selected=True
        )
        b_navtab3 = ClNavTab(
            theme=dktheme,
            text="NavTab 3"
        )
        b_marktab = ClMarkTab(
            theme=theme,
            text="MarkTab",
            icon=ft.icons.LOCAL_PIZZA_OUTLINED,
            hover_icon=ft.icons.LOCAL_PIZZA,
            selected_icon=ft.icons.LOCAL_PIZZA
        )

        page.padding = 0
        page.window_title_bar_hidden = True

        page.add(
            ft.Container(
                expand=True,
                padding=30,
                bgcolor=theme.background_two,
                alignment=ft.alignment.center,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        ft.Container(
                            expand=1,
                            # bgcolor="purple,0.2",
                            alignment=ft.alignment.center,
                            padding=5,
                            content=ft.Row(
                                spacing=20,
                                controls=[b_minimize, b_maximize, b_close]
                            )
                        ),
                        ft.Container(
                            expand=1,
                            # bgcolor="blue,0.2",
                            alignment=ft.alignment.center,
                            padding=5,
                            content=ft.Row(
                                spacing=20,
                                controls=[b_filter, b_outlinedfilter, b_filledfilter, b_menu]
                            )
                        ),
                        ft.Container(
                            expand=7,
                            # bgcolor="green,0.2",
                            alignment=ft.alignment.center,
                            padding=5,
                            content=ft.Column(
                                spacing=10,
                                controls=[
                                    ft.Row(
                                        expand=1,
                                        spacing=20, 
                                        controls=[b_text, b_normal, b_accept, b_cancel, b_tonal]
                                    ),
                                    ft.Row(
                                        expand=1,
                                        spacing=20, 
                                        controls=[b_select, b_mode, b_icon, b_color]
                                    ),
                                    ft.Row(
                                        expand=1,
                                        spacing=20, 
                                        controls=[
                                            b_switch,
                                            b_custom_switch,
                                            b_check1,
                                            b_check2,
                                            b_check3,
                                            ft.RadioGroup(
                                                value="rd1",
                                                content=ft.Row(
                                                    controls=[b_radio1, b_radio2]
                                                )
                                            )
                                        ]
                                    ),
                                    ft.Container(
                                        expand=1,
                                        alignment=ft.alignment.center,
                                        bgcolor=dktheme.background_one,
                                        padding=0,
                                        content=ft.Row(
                                            expand=1,
                                            spacing=0, 
                                            controls=[b_navtab1, b_navtab2, b_navtab3]
                                        ),
                                    ),
                                    ft.Container(
                                        expand=1,
                                        alignment=ft.alignment.center,
                                        bgcolor=theme.background_one,
                                        padding=0,
                                        content=ft.Row(
                                            expand=1,
                                            spacing=0, 
                                            controls=[b_marktab]
                                        ),
                                    ),
                                    ft.Row(expand=2)
                                ]
                            )
                        ),
                        ft.Container(
                            expand=1,
                            # bgcolor="purple,0.2",
                            alignment=ft.alignment.center,
                            content=ft.Row(
                                spacing=20,
                                controls=[b_nav, ft.Container(expand=14)]
                            )
                        ),
                    ]
                )
            )
        )
    
    ft.app(target=main)