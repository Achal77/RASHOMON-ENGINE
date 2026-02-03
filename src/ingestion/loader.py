import cv2
import os
import subprocess
from pathlib import Path

class RashomonIngestor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)

    def extract_frames(self, video_path, cam_id):
        print(f"[*] Extracting frames from {cam_id}...")
        save_path = self.output_dir / "processed_frames" / cam_id
        os.makedirs(save_path, exist_ok=True)

        cap = cv2.VideoCapture(str(video_path))
        count = 0
        while True:
            success, image = cap.read()
            if not success: break
            # Save every 30th frame (approx 1 per second)
            if count % 30 == 0:
                cv2.imwrite(str(save_path / f"frame_{count}.jpg"), image)
            count += 1
        print(f"[+] Frames saved to {save_path}")

    def extract_audio(self, video_path, cam_id):
        print(f"[*] Extracting audio from {cam_id}...")
        audio_path = self.output_dir / "audio_logs" / f"{cam_id}.wav"
        os.makedirs(audio_path.parent, exist_ok=True)
        # Using ffmpeg-python wrapper or subprocess
        cmd = f'ffmpeg -i "{video_path}" -ab 160k -ac 2 -ar 44100 -vn "{audio_path}" -y'
        subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def run_pipeline(self):
        videos = list(self.input_dir.glob("*.mp4"))
        if not videos: print("[-] No videos found in raw_footage!"); return
        
        for video in videos:
            self.extract_frames(video, video.stem)
            self.extract_audio(video, video.stem)