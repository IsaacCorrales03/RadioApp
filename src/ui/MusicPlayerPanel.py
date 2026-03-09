import flet as ft
from typing import cast
from pathlib import Path
from src.core.Colors import Colors
from src.ui.MainPanel import MainPanel
from src.audio.PlaySong import PlaySong
import threading
import time


class MusicPlayerPanel(MainPanel):
    def __init__(self, width: int, height: int):
        super().__init__(title="Reproductor", width=width, height=height)

        # Estado del reproductor
        self.currentSong: Path = None
        self.songPlayer: PlaySong = None
        self.isPlaying: bool = False

        # UI references
        bodyContainer = cast(ft.Container, self.controls[1])
        self.bodyColumn = cast(ft.Column, bodyContainer.content)

        self.durationText = ft.Text("0:00", size=14, color=Colors.TEXT_SECONDARY)
        self.elapsedText = ft.Text("0:00", size=12, color=Colors.TEXT_SECONDARY)

        # Botones y sliders
        self.playButton = ft.IconButton(
            ft.Icons.PLAY_ARROW,
            icon_size=48,
            bgcolor=Colors.BUTTON_PRIMARY,
            icon_color=Colors.TEXT_PRIMARY,
            mouse_cursor=ft.MouseCursor.CLICK
        )
        self.playButton.on_click = self.togglePlayPause

        self.volumeSlider = ft.Slider(value=100, min=0, max=100, width=width-80)
        self.volumeSlider.on_change = self.changeVolume

        self.progressSlider = ft.Slider(value=0, min=0, max=100, width=width-20)

        # Construir UI
        self.bodyColumn.controls = [
            ft.Text("Nombre de la canción", size=24, color=Colors.TEXT_PRIMARY, weight=ft.FontWeight.BOLD),
            ft.Text("Artista", size=18, color=Colors.TEXT_SECONDARY),
            ft.Text("Album", size=14, color=Colors.TEXT_SECONDARY),
            ft.Column(
                controls=[
                    ft.Container(content=self.progressSlider, padding=ft.padding.symmetric(horizontal=10)),
                    ft.Row(
                        controls=[self.elapsedText, ft.Row(expand=True), self.durationText],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ]
            ),
            ft.Row(
                controls=[
                    ft.IconButton(ft.Icons.SKIP_PREVIOUS, icon_size=36, bgcolor=Colors.BUTTON_SECONDARY, icon_color=Colors.TEXT_PRIMARY, mouse_cursor=ft.MouseCursor.CLICK),
                    self.playButton,
                    ft.IconButton(ft.Icons.SKIP_NEXT, icon_size=36, bgcolor=Colors.BUTTON_SECONDARY, icon_color=Colors.TEXT_PRIMARY, mouse_cursor=ft.MouseCursor.CLICK),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            ft.Row(
                controls=[
                    ft.Icon(ft.Icons.VOLUME_DOWN, color=Colors.TEXT_SECONDARY),
                    self.volumeSlider,
                    ft.Icon(ft.Icons.VOLUME_UP, color=Colors.TEXT_SECONDARY)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            )
        ]

        # Hilo de progreso visual
        threading.Thread(target=self.progressThread, daemon=True).start()

    def updateMetadata(self, metadata: dict):
        """Actualizar UI y cargar canción"""
        self.bodyColumn.controls[0].value = metadata.get("title", "Desconocido")
        self.bodyColumn.controls[1].value = metadata.get("artist", "Desconocido")
        self.bodyColumn.controls[2].value = metadata.get("album", "Desconocido")
        self.songDuration = metadata.get("duration", 0)
        minutes = self.songDuration // 60
        seconds = self.songDuration % 60
        self.durationText.value = f"{minutes}:{seconds:02d}"
        self.elapsedText.value = "0:00"
        self.progressSlider.value = 0
        self.bodyColumn.update()

        songPath = metadata.get("path", None)
        if songPath:
            self.currentSong = songPath
            self.songPlayer = PlaySong(self.currentSong)
            self.songPlayer.setVolume(self.volumeSlider.value)
            self.isPlaying = False
            self.playButton.icon = ft.Icons.PLAY_ARROW
            self.playButton.update()

    def togglePlayPause(self, e):
        if not self.songPlayer:
            return

        if self.isPlaying:
            self.songPlayer.pause()
            self.isPlaying = False
            self.playButton.icon = ft.Icons.PLAY_ARROW
        else:
            self.songPlayer.play()
            self.isPlaying = True
            self.playButton.icon = ft.Icons.PAUSE

        self.playButton.update()

    def changeVolume(self, e):
        if self.songPlayer:
            self.songPlayer.setVolume(int(self.volumeSlider.value))

    def progressThread(self):
        while True:
            time.sleep(0.5)
            if self.songPlayer and self.isPlaying:
                elapsed = self.songPlayer.getTime()
                if elapsed >= self.songDuration:
                    self.isPlaying = False
                    self.playButton.icon = ft.Icons.PLAY_ARROW
                    elapsed = self.songDuration
                self.progressSlider.value = (elapsed / self.songDuration) * 100 if self.songDuration else 0
                minutes = int(elapsed) // 60
                seconds = int(elapsed) % 60
                self.elapsedText.value = f"{minutes}:{seconds:02d}"
                self.progressSlider.update()
                self.elapsedText.update()
                self.playButton.update()