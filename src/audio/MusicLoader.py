from mutagen._file import File
from pathlib import Path
from typing import Optional


class MusicLoader:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.metadata = {}
        self.duration = 0
        self._load()

    def _load(self):
        if not self.file_path.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {self.file_path}")

        audio = File(self.file_path, easy=True)
        if audio is None:
            raise ValueError("Formato de audio no soportado")

        # Nombre de la canción
        self.metadata['title'] = audio.get('title', [self.file_path.stem])[0]
        # Artista
        self.metadata['artist'] = audio.get('artist', ['Desconocido'])[0]
        # Álbum (opcional)
        self.metadata['album'] = audio.get('album', [''])[0]
        # Duración en segundos
        self.duration = int(audio.info.length)

    def getMetadata(self) -> dict:
        """
        Devuelve un diccionario con:
        - title
        - artist
        - album
        - duration (segundos)
        """
        return {
            'title': self.metadata['title'],
            'artist': self.metadata['artist'],
            'album': self.metadata['album'],
            'duration': self.duration,
            'path': self.file_path
        }