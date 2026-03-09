from src.audio.MusicLoader import MusicLoader

loader = MusicLoader("dardos.mp3")
metadata = loader.getMetadata()
print(metadata)
