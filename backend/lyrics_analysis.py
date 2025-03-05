from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.cuda.amp import autocast
import torch


# Clear GPU memory
torch.cuda.empty_cache()

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B", device_map="auto")

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token


def generate_visual_prompt(lyrics):
    try:
        # Add a contextual instruction to the prompt
        prompt_template = f"""
        Generate a visual prompt for a music video based on the following song lyrics:
        {lyrics}

        The visual prompt should describe a scene that matches the mood, theme, and story of the song.
        """

        # Tokenize input with truncation and padding
        inputs = tokenizer(prompt_template, return_tensors="pt", truncation=True, max_length=512, padding=True)

        # Move inputs to the same device as the model
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

        # Generate text with mixed precision (FP16)
        with autocast():
            outputs = model.generate(**inputs, max_length=250)

        # Decode and return the output
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        print(f"Error generating visual prompt: {e}")
        return "A mysterious scene with glowing lights and shadows."


# Example usage
if __name__ == "__main__":
    lyrics = "I'm walking through the shadows, chasing fireflies"
    prompt = generate_visual_prompt(lyrics)
    print(prompt)