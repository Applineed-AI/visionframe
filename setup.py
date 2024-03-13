from setuptools import setup, find_packages

setup(
    name="visionframe",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "tqdm",
        "opencv-python",
        "supervision==0.9.0"
    ],
    author="Md Faruk Alam",
    author_email="farukalampro@gmail.com",
    description="A package for extracting frames from videos using OpenCV and supervision.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Applineed-AI/visionframe",
    license="MIT",
)
