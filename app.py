import streamlit as st
from models.chat_gpt import generate_response_chatgpt
from caption_generator import predict_step
from PIL import Image
import requests
from io import BytesIO
import os

# Define the main function that processes the video and outputs a list of numbers
def prompt_generate(option):
    if option == 'long caption':
        prompt = 'Rewrite the text above as an instagram caption and add emojis. Elaborate the caption and describe it in detail.'

    elif option == 'short caption':
        prompt = 'Rewrite the text above as an instagram caption and add emojis. Keep the caption short and concise.'
        
    else:
        prompt = 'Generate hashtags like an instagram caption for the text above.'

    # Return the output prompt
    return prompt

# Define the page for processing a video and outputting a list of numbers
def image_page():

    # Set Background Image
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://www.google.com/imgres?imgurl=https%3A%2F%2Fimage.slidesdocs.com%2Fresponsive-images%2Fbackground%2Fgradient-light-effect-business-purple-paper-texture-solid-color-powerpoint-background_b6c386e391__960_540.jpg&tbnid=cd37xSdzC--nhM&vet=12ahUKEwjbtqmx993-AhWn6HMBHYpMAIUQMyhFegQIARBp..i&imgrefurl=https%3A%2F%2Fslidesdocs.com%2Fbackground%2Fgradient-light-effect-business-purple-paper-texture-solid-color-powerpoint-background_b6c386e391&docid=gROl-qsSrdAjKM&w=960&h=540&q=light%20purple%20pink%20color%20gradient&ved=2ahUKEwjbtqmx993-AhWn6HMBHYpMAIUQMyhFegQIARBp");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Set the title of the page
    st.title("Generate Captions!")

    # Add a file uploader widget to allow the user to upload a video file
    image_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"]) 

    option = st.selectbox('Choose the type for caption you want to generate',
    ('long caption', 'short caption', 'hashtag'))

    # If the user has uploaded a video file, process it and display the output list
    if image_file is not None:
        image = Image.open(image_file)
        col1, col2 = st.columns([0.5,0.5])

        with col1:
          st.markdown('<p style="text-align: center;">Input image</p>',unsafe_allow_html=True)
          st.image(image,width=300)

        with col2:
          if st.button('Generate'):
              pred = predict_step(image_file)
              prompt = prompt_generate(option)
              question = pred[0] + prompt
              message = [{'role':'user', 'content':question}]
              response_gpt = generate_response_chatgpt(message)
              if response_gpt is not None:
                  st.write(response_gpt)

# Define the Streamlit app
def main():

    # Set the background color and image of the page
    st.set_page_config(
        page_title="Social Media Caption Generation",
        page_icon=":sunglasses:",
        layout="wide"
        )

    # Add a dropdown menu to allow the user to navigate between pages
    pages = {
        "Demo": image_page
    }
    page = st.sidebar.selectbox("Select a Page", list(pages.keys()))

    # Display the selected page
    pages[page]()

# Run the Streamlit app
if __name__ == "__main__":
    main()
