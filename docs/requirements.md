# Dependencias del Proyecto

Este documento describe las dependencias utilizadas en el sistema de cabina de radio y su propósito dentro del proyecto.

---

## Flet

Interfaz gráfica del sistema.

Permite desarrollar una UI moderna y multiplataforma para la aplicación de cabina.  
Se utiliza para construir los controles de reproducción, visualización de canciones, cola de reproducción y control de dispositivos.

---

## sounddevice

Motor de audio principal.

Permite reproducir audio, capturar entrada de micrófono y seleccionar dispositivos de entrada y salida utilizando la librería PortAudio.

---

## soundfile

Lectura de archivos de audio.

Se utiliza para cargar archivos de audio desde la biblioteca local y procesarlos para reproducción.

---

## ffmpeg-python

Interfaz de Python para FFmpeg.

Permite convertir y procesar archivos de audio, además de soportar formatos comunes como MP3, WAV y OGG.

Requiere que **FFmpeg esté instalado en el sistema**.

---

## yt-dlp

Descarga de contenido de audio desde internet.

Se utiliza para obtener música desde fuentes externas y almacenarla en la biblioteca local del sistema.

---

## SQLAlchemy

ORM para la persistencia de datos.

Permite gestionar la base de datos del sistema, donde se almacenan canciones, playlists y configuraciones.

---

## Mutagen

Lectura de metadatos de archivos de audio.

Se utiliza para obtener información de las canciones como:

- título
- artista
- álbum
- duración

---

## python-dotenv

Gestión de variables de entorno.

Permite cargar configuraciones del sistema desde archivos `.env`, evitando hardcodear valores dentro del código.

---