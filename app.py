import streamlit as st
import numpy as np
from PIL import Image
from api_tokens import HUGGING_FACE
import torch
from diffusers import StableDiffusionImg2ImgPipeline

@st.cache_resource
class AvatarGenerator:
    def __init__(self):
        self.pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        "nitrosocke/Ghibli-Diffusion", torch_dtype=torch.float32, use_safetensors=True
        )
        # self.pipe.save_pretrained("./ghibli_diffusion")

    def generate_avatar(self, text_prompt, image):
        image = Image.open(image).convert("RGB")
        image = image.resize((512, 512))
        generator = torch.Generator().manual_seed(1024)
        image = self.pipe(prompt=text_prompt, image=image, strength=0.5, guidance_scale=7.5, generator=generator, negative_prompt="nsfw").images[0]
        image.save(f"./{text_prompt}.jpg")
        return image


app = AvatarGenerator()

# Create a Streamlit app
st.title("🧑🏽‍🎨 Avatar Generator")

# Allow users to upload an image
image_file = st.file_uploader("Upload an image")

# Get the text prompt from the user
text_prompt = st.text_input("Enter a text prompt: ")

# Submit button
submit_button = st.button("Generate Avatar")

# Check if the user has provided both an image and a text prompt
if image_file is None or text_prompt == "":
    st.error("Please provide both an image and a text prompt.")
    exit()

# Generate the avatar image when the user clicks the submit button
if submit_button:
    avatar = app.generate_avatar(f"ghibli style, {text_prompt}", image_file)

    # Display the avatar image
    st.image(avatar)