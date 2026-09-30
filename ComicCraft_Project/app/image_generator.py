import os, re
import torch
from diffusers import StableDiffusionPipeline

MODEL_ID = "runwayml/stable-diffusion-v1-5"
OUTPUT_DIR = "static/panels"
os.makedirs(OUTPUT_DIR, exist_ok=True)

_pipe = None

def get_pipeline():
    global _pipe
    if _pipe is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        _pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        _pipe = _pipe.to(device)
    return _pipe

def generate_image(image_prompt, panel_number):
    pipe = get_pipeline()
    safe = re.sub(r"[^a-zA-Z0-9_-]+", "_", image_prompt[:50]).strip("_")
    filename = f"panel_{panel_number}_{safe or 'comic'}.png"
    path = os.path.join(OUTPUT_DIR, filename)

    full_prompt = (
        f"{image_prompt}, comic book illustration, cinematic composition, "
        "detailed characters, expressive faces, vibrant storytelling, no text"
    )
    image = pipe(full_prompt, num_inference_steps=25, guidance_scale=7.5).images[0]
    image.save(path)
    return "/" + path.replace("\\", "/")
