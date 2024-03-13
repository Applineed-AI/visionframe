# visionframe

visionframe is a Python package that allows you to easily extract frames from videos using OpenCV and supervision.

## Installation

You can install visionframe via pip:

pip install visionframe

## Usage

To use visionframe, you need to import it into your Python script and use the `extract_frames` function. Here's a basic example:

```python
import visionframe

VIDEO_DIR_PATH = "/path/to/your/video/directory"
IMAGE_DIR_PATH = "/path/to/where/you/want/to/save/images"
FRAME_STRIDE = 1

visionframe.extract_frames(VIDEO_DIR_PATH, IMAGE_DIR_PATH, FRAME_STRIDE)
```

Replace VIDEO_DIR_PATH with the directory path where your videos are located, IMAGE_DIR_PATH with the directory path where you want to save the extracted frames, and adjust FRAME_STRIDE as needed