from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class SceneDescriber:
    def __init__(self):
        print("[*] Loading Vision Cortex (BLIP Model)...")
        # Load the pre-trained model from Salesforce
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def describe_frame(self, image_path):
        """
        Takes an image file path, feeds it to the AI, 
        and returns a text description (e.g., 'a man holding a phone').
        """
        try:
            # 1. Open the image
            raw_image = Image.open(image_path).convert('RGB')
            
            # 2. Process it for the AI
            inputs = self.processor(raw_image, return_tensors="pt")
            
            # 3. Generate the caption
            out = self.model.generate(**inputs)
            
            # 4. Decode the math back into English text
            description = self.processor.decode(out[0], skip_special_tokens=True)
            return description
            
        except Exception as e:
            print(f"[!] Vision Error: {e}")
            return "unknown object"