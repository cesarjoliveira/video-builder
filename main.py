import os
import uuid
import requests
from moviepy.editor import *

def download_file(url, path):
    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)

def handler(event):
    print("🟢 Handler iniciado com dados:", event)
    image_urls = event.get("image_urls", [])
    audio_url = event.get("audio_url")

    os.makedirs("tmp", exist_ok=True)

    image_files = []
    for i, url in enumerate(image_urls):
        img_path = f"tmp/image_{i}.jpg"
        download_file(url, img_path)
        image_files.append(img_path)

    audio_path = "tmp/audio.mp3"
    download_file(audio_url, audio_path)

    audio_clip = AudioFileClip(audio_path)
    duration_per_image = audio_clip.duration / len(image_files)

    clips = [ImageClip(img).set_duration(duration_per_image).resize(height=720) for img in image_files]
    video = concatenate_videoclips(clips, method="compose").set_audio(audio_clip)

    output_path = f"tmp/final_{uuid.uuid4().hex}.mp4"
    video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")

    return {"video_path": output_path}
