from models.vit_gpt2 import model, feature_extractor, tokenizer
from models.chat_gpt import generate_response_chatgpt

import torch
from PIL import Image

# Assign device to model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Generate the predictions for the image caption model
max_length = 100
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

def predict_step(image): 

    # Convert the image to PIL file
    image = Image.open(image)
  
    # Read the image
    images = []

    if image.mode != "RGB":
    image = image.convert(mode="RGB")

    images.append(image)

    pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]

    return preds
