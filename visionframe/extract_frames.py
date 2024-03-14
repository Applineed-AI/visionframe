# visionframe/extract_frames.py
import supervision as sv
from tqdm import tqdm
import cv2

class FrameExtractor:
    def __init__(self, video_dir_path, image_dir_path, frame_stride=1):
        self.video_dir_path = video_dir_path
        self.image_dir_path = image_dir_path
        self.frame_stride = frame_stride

    def extract_frames(self):
        video_paths = sv.list_files_with_extensions(
            directory=self.video_dir_path,
            extensions=["mov", "mp4"])
        
        print("Extracting frames from videos...")
        for video_path in tqdm(video_paths):
            video_name = video_path.stem
            print(f"Processing video: {video_name}")
            image_name_pattern = video_name + "-{:05d}.png"
            with sv.ImageSink(target_dir_path=self.image_dir_path, image_name_pattern=image_name_pattern) as sink:
                for image in sv.get_video_frames_generator(source_path=str(video_path), stride=self.frame_stride):
                    sink.save_image(image=image)
        print("Frame extraction completed!")
