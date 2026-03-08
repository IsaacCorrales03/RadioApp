import flet as ft
from src.ui.MainPanel import MainPanel
from src.ui.MusicPlayerPanel import MusicPlayerPanel

from src.core.Colors import Colors

def main(page: ft.Page):
    page.title = "RadioApp"
    page.bgcolor = Colors.BACKGROUND
    page.padding = 10

    panel_width = int(page.window.width * 0.32) # type: ignore
    panel_height = int(page.window.height * 0.8) # type: ignore
    panel_spacing = int(page.window.width * 0.01) # type: ignore
    # Tres paneles
    musica_panel = MainPanel("Música", panel_width, panel_height)
    player_panel = MusicPlayerPanel(panel_width, panel_height)
    dispositivos_panel = MainPanel("Dispositivos", panel_width, panel_height)

    # Colocarlos en fila
    row = ft.Row(
        controls=[musica_panel, player_panel, dispositivos_panel],
        alignment=ft.MainAxisAlignment.START,
        spacing=panel_spacing,
    )

    page.add(row)


if __name__ == "__main__":
    ft.run(main)