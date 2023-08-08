# CODIO SOLUTION BEGIN
import os
import openai
import secret
from PIL import Image, ImageChops
from io import BytesIO
import requests

openai.api_key = secret.api_key

# Function to generate an image using DALL-E
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

# Function to download the image
def download_image(image_url, x):
    response = requests.get(image_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    with open(x+'.png', 'wb') as handler:
        handler.write(img_data)
    return img

# Function to blend the images
def custom_blend(image1, image2):
    return ImageChops.add_modulo(image1, image2).point(lambda x: x // 2)

# The required function that combines the above operations
def combine(prompt1, prompt2):
    # Generate the images
    image1_url = generate_base_image(prompt1)
    image2_url = generate_base_image(prompt2)

    # Download and open the generated images
    image1 = download_image(image1_url, 'image1')
    image2 = download_image(image2_url, 'image2')

    # Blend the images
    result = custom_blend(image1, image2)

    # Save the final image
    result.save('final_blended.png')

# Call the combine function with two prompts

# CODIO SOLUTION END 