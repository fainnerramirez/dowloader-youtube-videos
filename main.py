
import yt_dlp
import os

def descargar_video(url):
    carpeta = "Videos descargados"
    os.makedirs(carpeta, exist_ok=True)

    opciones = {
    "format": "bestvideo+bestaudio/best",
    "outtmpl": "Videos descargados/%(title)s.%(ext)s",
    "merge_output_format": "mp4",
    "noplaylist": True,

    # Reanudar descargas interrumpidas
    "continuedl": True,
    "nopart": False,

    # Reintentos automáticos
    "retries": 20,
    "fragment_retries": 50,
    "file_access_retries": 10,

    # Esperar entre fragmentos
    "sleep_interval": 2,
    "max_sleep_interval": 5,

    # JavaScript
    "js_runtimes": {
        "deno": {}
    },

    "progress": True,
}

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])

        print("\n¡Descarga completada!")

    except Exception as error:
        print(f"\nError al descargar: {error}")

if __name__ == "__main__":
    print("=== DESCARGADOR DE YOUTUBE ===")
    url = input("Introduce el enlace del video de YouTube: \n Url del Video:")

    if url.strip():
        descargar_video(url)
    else:
        print("Debes introducir un enlace válido.")
