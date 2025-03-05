from diffusers import StableDiffusionPipeline
import torch
import cv2
import os
import gc


# Clear GPU and CPU memory
torch.cuda.empty_cache()
gc.collect()

# Load the Stable Diffusion model with mixed precision (FP16)
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe.to("cuda")

def generate_video(prompt, output_path="output.mp4", num_frames=12, height=512, width=512):
    try:
        # Create a temporary directory to store frames
        os.makedirs("temp_frames", exist_ok=True)

        # Generate images (frames)
        for i in range(num_frames):
            # Generate an image
            image = pipe(prompt).images[0]

            # Resize the image to the desired resolution
            image = image.resize((width, height))

            # Save the image as a frame
            frame_path = f"temp_frames/frame_{i:04d}.png"
            image.save(frame_path)

        # Combine frames into a video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, 24, (width, height))

        for i in range(num_frames):
            frame_path = f"temp_frames/frame_{i:04d}.png"
            frame = cv2.imread(frame_path)
            out.write(frame)

        out.release()

        # Clean up temporary frames
        for i in range(num_frames):
            frame_path = f"temp_frames/frame_{i:04d}.png"
            os.remove(frame_path)
        os.rmdir("temp_frames")

        print(f"Video saved to: {output_path}")
    except Exception as e:
        print(f"Error generating video: {e}")

# Example usage
if __name__ == "__main__":
    prompt = "A dark forest with glowing fireflies"
    generate_video(prompt)