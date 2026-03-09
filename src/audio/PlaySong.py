from pathlib import Path
import vlc
import threading
import time


class PlaySong:
    def __init__(self, path: Path):
        if not path.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {path}")
        self.path = path
        self.player = vlc.MediaPlayer(str(path))
        self._lock = threading.Lock()
        self.isPlaying = False
        self.isPaused = False

    def play(self):
        with self._lock:
            if not self.isPlaying:
                self.player.play()
                self.isPlaying = True
                self.isPaused = False
            elif self.isPaused:
                self.player.play()  # vlc resume
                self.isPaused = False

    def pause(self):
        with self._lock:
            if self.isPlaying and not self.isPaused:
                self.player.pause()
                self.isPaused = True

    def stop(self):
        with self._lock:
            self.player.stop()
            self.isPlaying = False
            self.isPaused = False

    def setVolume(self, volume: int):
        """Volume: 0-100"""
        self.player.audio_set_volume(max(0, min(100, volume)))

    def isPlayingStatus(self) -> bool:
        return self.isPlaying and not self.isPaused

    def getLength(self) -> int:
        """Duración en segundos"""
        length = self.player.get_length()  # milisegundos
        return int(length / 1000) if length > 0 else 0

    def getTime(self) -> int:
        """Tiempo transcurrido en segundos"""
        t = self.player.get_time()  # milisegundos
        return int(t / 1000) if t > 0 else 0