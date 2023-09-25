
from setuptools import setup

setup(
    name="avatar-generator",
    version="0.0.1",
    description="Generate avatars from real images using Stable Diffusion v1.5 and Streamlit.",
    author="Abhishek S A",
    author_email="abhishek.s.a2201@gmail.com",
    url="https://github.com/Abhishek-S-A-2201/Avatar_Generator.git",
    license="None",
    install_requires=[
        "streamlit",
        "numpy",
        "PIL",
        "torch",
        "diffusers>=0.5",
    ],
    python_requires=">=3.8",
)