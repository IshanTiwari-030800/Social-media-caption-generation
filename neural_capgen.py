from models.vit_gpt2 import model, feature_extractor, tokenizer
from typing import Union
from pathlib import Path
import torch
from PIL import Image

device = torch.device('cuda')

# Hyperparameter setting
max_length = 100
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

model = model.to(device)


def pred_step(
        image_path: Union[Path, str]
    ):

    """
    Generate the default caption for the given image

    Args - 
        1. image_path = path to the image file

    return - Generated default caption 
    """

    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert(mode='RGB')

    inputs = feature_extractor(images=[image],
                                return_tensors='pt').pixel_values.to(device)

    output_ids = model.generate(inputs, **gen_kwargs)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)

    return preds[0].strip()

