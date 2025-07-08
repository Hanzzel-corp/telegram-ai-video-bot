import torch
from diffusers import StableDiffusionPipeline, StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video
from PIL import Image
import os
import traceback

def text_to_video_workflow(prompt: str, output_path: str = "output/final_video.mp4"):
    """
    Genera un video a partir de un prompt de texto en un proceso de 2 pasos.
    1. Genera una imagen con Stable Diffusion.
    2. Anima esa imagen con Stable Video Diffusion.
    """
    print(f"\n🚀 Iniciando flujo de trabajo completo para: '{prompt}'")
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    print(f"🔩 Usando dispositivo: {device} con dtype: {dtype}")
    print("⚠️ Este proceso descargará nuevos modelos y puede tardar bastante la primera vez.")

    # --- PASO 1: TEXTO A IMAGEN ---
    print("\n--- PASO 1: Generando imagen base desde el texto ---")
    
    # Usamos un modelo estándar de Stable Diffusion 1.5
    pipe_txt2img = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=dtype)
    pipe_txt2img.to(device)

    image = pipe_txt2img(prompt).images[0]
    
    # Guardar la imagen intermedia (opcional)
    if not os.path.exists("output"):
        os.makedirs("output")
    image.save("output/initial_image.png")
    print("✅ Imagen base generada: output/initial_image.png")

    # Liberar memoria de la GPU si es posible
    del pipe_txt2img
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    # --- PASO 2: IMAGEN A VIDEO ---
    print("\n--- PASO 2: Animando la imagen para crear el video ---")
    
    # Usamos el pipeline de SVD que ahora recibirá una imagen real
    pipe_img2vid = StableVideoDiffusionPipeline.from_pretrained("stabilityai/stable-video-diffusion-img2vid", torch_dtype=dtype)
    pipe_img2vid.to(device)

    # Redimensionar la imagen al tamaño que SVD espera
    image = image.resize((1024, 576))

    generator = torch.manual_seed(42)
    frames = pipe_img2vid(image, decode_chunk_size=8, generator=generator).frames[0]

    # Guardar los fotogramas como un video
    print(f"🎬 Guardando video final en: {output_path}")
    export_to_video(frames, output_path, fps=7)
    
    print(f"🎉 ¡ÉXITO! Video generado en: {output_path}")


if __name__ == "__main__":
    try:
        prompt = "un bebe cantando"
        text_to_video_workflow(prompt=prompt)
        print("\nProceso finalizado.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error durante la ejecución: {e}")
        traceback.print_exc()






















































































