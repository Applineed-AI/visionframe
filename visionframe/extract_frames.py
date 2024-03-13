# visionframe/extract_frames.py
import supervision as sv
from tqdm import tqdm
import cv2

def extract_frames(VIDEO_DIR_PATH, IMAGE_DIR_PATH, FRAME_STRIDE=1):
    video_paths = sv.list_files_with_extensions(
        directory=VIDEO_DIR_PATH,
        extensions=["mov", "mp4"])

    for video_path in tqdm(video_paths):
        video_name = video_path.stem
        image_name_pattern = video_name + "-{:05d}.png"
        with sv.ImageSink(target_dir_path=IMAGE_DIR_PATH, image_name_pattern=image_name_pattern) as sink:
            for image in sv.get_video_frames_generator(source_path=str(video_path), stride=FRAME_STRIDE):
                sink.save_image(image=image)
