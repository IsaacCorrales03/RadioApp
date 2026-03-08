import flet as ft
from typing import cast
from src.core.Colors import Colors
from src.ui.MainPanel import MainPanel  # tu clase base

class MusicPlayerPanel(MainPanel):
    """
    Controls de MusicPlayerPanel: \n
    0: Nombre de la canción(Text) \n
    1: Artista(Text) \n
    2: Barra de progreso (Container) \n
    3: Barra de controles (anterior, play/pause, siguiente) (Row) \n
    4: Control de volumen (Row) \n
    """
    def __init__(self, width: int, height: int):
        super().__init__(title="Reproductor", width=width, height=height)

        # Reemplazar el contenido vacío del cuerpo
        # body_container es ft.Container
        body_container = cast(ft.Container, self.controls[1])
        # body_column es ft.Column dentro del container
        body_column = cast(ft.Column, body_container.content)  
        body_column.controls = [
            # Nombre de la canción
            ft.Text("Nombre de la canción", size=24, color=Colors.TEXT_PRIMARY, weight=ft.FontWeight.BOLD),

            # Artista
            ft.Text("Artista", size=18, color=Colors.TEXT_SECONDARY),

            # Barra de progreso (solo visual)
            ft.Container(
                content=ft.Slider(value=0, min=0, max=100, width=width-20),
                padding=ft.padding.symmetric(horizontal=10)
            ),

            # Barra de controles (anterior, play/pause, siguiente)
            ft.Row(
                controls=[
                    ft.IconButton(ft.Icons.SKIP_PREVIOUS, icon_size=36, bgcolor=Colors.BUTTON_SECONDARY, icon_color=Colors.TEXT_PRIMARY),
                    ft.IconButton(ft.Icons.PLAY_ARROW, icon_size=48, bgcolor=Colors.BUTTON_PRIMARY, icon_color=Colors.TEXT_PRIMARY),
                    ft.IconButton(ft.Icons.SKIP_NEXT, icon_size=36, bgcolor=Colors.BUTTON_SECONDARY, icon_color=Colors.TEXT_PRIMARY),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),

            # Control de volumen
            ft.Row(
                controls=[
                    ft.Icon(ft.Icons.VOLUME_DOWN, color=Colors.TEXT_SECONDARY),
                    ft.Slider(value=50, min=0, max=100, width=width-80),
                    ft.Icon(ft.Icons.VOLUME_UP, color=Colors.TEXT_SECONDARY)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            )
        ]