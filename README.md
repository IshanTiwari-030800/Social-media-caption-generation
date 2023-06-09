# Social Media Caption Generation
This project aims to generate a social media caption given an image. Leveraged a Vision Encoder Decoder Model to generate descriptive image captions the output of which were later fed to Chat-GPT (GPT 3.5 turbo backbone) with tuned prompts for final results.

## Introduction
This repo presents an end-to-end approach for providing an instagram like caption for a given input image. Code demo along with a working app has been provided in the further sections of this repository. 

The basic pipeline for the project goes like this - 
- Extracting a descriptive representation for the input images in form of text
- Passing the extracted text to Chat-GPT with tuned prompts for the final results.

#### Image Caption Generation
A Vision encoder decoder model has been used for extracting the descriptive captions for the input images. The full hugging face implementation for the code can been accessed from [here.](https://huggingface.co/docs/transformers/model_doc/vision-encoder-decoder)

#### Social Media Caption Conversion
The output of the previous model is then fed to Chat-GPT for producing social media style captions. The repo also has options for generating hashtags, long captions or short ones with or wihout the emojis.

## Sample Results
The three sample test images that were given have been added for reference
![here](https://github.com/IshanTiwari-030800/Social-media-caption-generation/blob/main/results.png)

## Installation and Quick Start
To use the repo and run inferences, please follow the guidelines below

- Cloning the Repository: 

        $ git clone https://github.com/IshanTiwari-030800/Social-media-caption-generation
        
- Entering the directory: 

        $ cd Social-media-caption-generation/
        
- Setting up the Python Environment with dependencies:

        $ pip install virtualenv
        $ virtualenv venv
        $ source venv/bin/activate
        $ pip install -r requirements.txt
        
- CLI Command

        $ python demo.py --image-file Image path --option (caption, hashtag) --caption_options (Long, short)

A Streamlit application for the same has been provided hosted in Google Colab. 
