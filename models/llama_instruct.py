from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from huggingface_hub import login

login('<huggingface_token_here>') # Authenticate huggingface login

model_name = "meta-llama/Llama-3.2-3B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

def postprocess_caption(caption: str, 
                        prompt: str,
                        default_caption: str,
                    ):

    """
    PostProcess the generated caption.
    """
    
    if default_caption in caption:
        caption = caption.replace(default_caption, '')

    if prompt in caption:
        caption = caption.replace(prompt, '')

    if 'You are a helpful ai assistant' in caption:
        caption = caption.replace('You are a helpful ai assistant', '')

    ### Hard coding redundant text, will find a better approach in upcoming versions
    if 'system\n    user\n    \n\nassistant\n     ' in caption:
        caption = caption.replace('system\n    user\n    \n\nassistant\n     ', '')
        
    return caption.strip()

def generate_llama_caption(
        default_caption: str, 
        prompt: str
    ):

    """
    Create caption from the pre generated caption given by vit_gpt2 encoder decoder model.
    """

    system = 'You are a helpful ai assistant'

    chat_prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    {system}<|eot_id|><|start_header_id|>user<|end_header_id|>
    {prompt}\n\n{default_caption}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """

    inputs = tokenizer(chat_prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=150, do_sample=True, 
                                temperature=0.9, top_p=0.95)
    
    caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return postprocess_caption(caption, prompt, default_caption)
