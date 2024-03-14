# VisionFrame

[![Downloads](https://static.pepy.tech/badge/visionframe)](https://pepy.tech/project/visionframe)
[![Downloads](https://static.pepy.tech/badge/visionframe/month)](https://pepy.tech/project/visionframe)
[![Downloads](https://static.pepy.tech/badge/visionframe/week)](https://pepy.tech/project/visionframe)



Empower Your Computer Vision Projects with VisionFrame: Seamlessly Handle Video and Image


## Table of Contents

1. [Installations](#installations)
2. [Video To Frame](#video-to-frame)

---

### Installations
You can  simply use pip to install the latest version of visionframe

```bash
pip install visionframe
```

### Video To Frame

To extract frames from videos, simply import the FrameExtractor class from visionframe and create an instance with the desired parameters. Then, call the extract_frames() method:

```python
from visionframe import FrameExtractor

VIDEO_DIR_PATH = "/path/to/videos"
IMAGE_DIR_PATH = "/path/to/images"
FRAME_STRIDE = 1 # every frame in the video will be extracted

frame_extractor = FrameExtractor(video_dir_path=VIDEO_DIR_PATH, image_dir_path=IMAGE_DIR_PATH, frame_stride=FRAME_STRIDE)
frame_extractor.extract_frames()
```

Replace VIDEO_DIR_PATH with the directory path where your videos are located, IMAGE_DIR_PATH with the directory path where you want to save the extracted frames, and adjust FRAME_STRIDE as needed


