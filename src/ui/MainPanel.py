import flet as ft
from src.core.Colors import   Colors


class MainPanel(ft.Column):
    def __init__(self, title: str, width: int, height: int):
        super().__init__()
        self.width = width
        self.height = height
        self.controls = [
            ft.Container(
                content=ft.Text(title, color=Colors.TEXT_PRIMARY, size=20),
                alignment=ft.Alignment.CENTER,
                bgcolor=Colors.BORDER,
                width=width,
                height=40,
            ),
            ft.Container(
                content=ft.Column([]),  # vacío por ahora
                width=width,
                height=height - 40,   # resto del panel
                bgcolor=Colors.BACKGROUND,
                padding=10,
            )
        ]