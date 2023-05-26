# from models import vit_gpt2, chat_gpt
from models.vit_gpt2 import model, feature_extractor, tokenizer
from models.chat_gpt import generate_response_chatgpt
import argparse
import torch
from PIL import Image
import requests
from io import BytesIO

def parse_args():
    parser = argparse.ArgumentParser(description="Demo")
    parser.add_argument('--image-file', type=str, help='Path to the image file. Can be local or a url.')
    parser.add_argument('--gpu-id', type=int, help='GPU to be used')
    parser.add_argument('--options', 
                        type=str, 
                        help='Choose whether to generate caption or hashtags'
                        'for the image.')
    
    parser.add_argument('--caption_options', 
                        type=str, 
                        help='Choose the type of caption needed. (Long or short).')
    
    args = parser.parse_args()
    return args

# Generate captions
args = parse_args()

# Push the model on the specified gpu 
gpu_id = args.gpu_id
device = torch.device(f"cuda:{gpu_id}" if torch.cuda.is_available() else "cpu")
model.to(device)

# Generate the predictions for the image caption model
max_length = 100
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

image_paths = args.image_file
def predict_step(image_paths):
  
  # Read the image
  images = []
  for image_path in image_paths:

    if(image_path.startswith('http')):
        response = requests.get(image_path)
        i_image = Image.open(BytesIO(response.content))
    else:
        i_image = Image.open(image_path)

    if i_image.mode != "RGB":
      i_image = i_image.convert(mode="RGB")

    images.append(i_image)

  pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
  pixel_values = pixel_values.to(device)

  output_ids = model.generate(pixel_values, **gen_kwargs)

  preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
  preds = [pred.strip() for pred in preds]

  return preds

# Mode
mode = args.options
flag = False
if(mode == 'caption'):
  option = args.caption_options
  option = option.lower()

  if(option == 'long'):
    prompt = '\nRewrite the text above as an instagram caption and add emojis. Elaborate the caption and describe it in detail.'
  elif(option == 'short'):
    prompt = '\nRewrite the text above as an instagram caption and add emojis. Keep the caption short and concise.'
  else:
    print("Wrong option, please choose something from (long, short)")
    flag = True

elif(mode == 'hashtag'):
  prompt = '\nGenerate hashtags like an instagram caption for the text above.'

else:
  print("Wrong option, please choose something from (caption, hashtag)")
  flag = True

if(not flag):

  #Generate the caption and print it
  print("Generating caption..........")
  pred = predict_step([image_paths])
  question = pred[0] + prompt
  message = [{'role':'user', 'content':question}]
  response_gpt = generate_response_chatgpt(message)

  print(response_gpt)