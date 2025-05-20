# 🖼️ Social Media Caption Generator

A web application that automatically generates rich, creative captions for your images using state-of-the-art vision and language models. Built with a Flask backend and a React + Tailwind CSS frontend.

## 🚀 Features

- 📤 Upload an image through the UI
- 🧠 Generate descriptive captions using `vit-gpt2` from Hugging Face
- 💬 Enhance and stylize captions with `llama-3.2b-instruct` via prompt engineering
- 🎨 Clean and responsive UI built with React and Tailwind CSS

## 🧠 How It Works

1. **Image Upload**: Users upload an image via the web interface.
2. **Image Captioning**: The backend uses the `nlpconnect/vit-gpt2-image-captioning` model to generate a rich descriptor of the image.
3. **Contextual Refinement**: This descriptor is then passed into the `llama3.2-3b-instruct` model with carefully engineered prompts to produce a final, high-quality caption.
4. **Frontend Display**: The caption is returned to the frontend and displayed below the uploaded image.

## 🛠️ Tech Stack

- **Backend**: Flask, Flask-CORS, Hugging Face Transformers
- **Models**:
  - [`nlpconnect/vit-gpt2-image-captioning`](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning)
  - [`meta-llama/Meta-Llama-3-8B-Instruct`](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) *(or your preferred LLaMA model)*
- **Frontend**: React, Tailwind CSS
- **Tunnel**: Pyngrok (for local development and testing)
