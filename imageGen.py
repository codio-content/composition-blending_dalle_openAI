# CODIO SOLUTION BEGIN
import os
import openai
import secret
from PIL import Image, ImageOps,ImageChops
from io import BytesIO
import requests

openai.api_key = secret.api_key

# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']
from PIL import Image
from io import BytesIO
import requests

def download_image(image_url,x):
    response = requests.get(image_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    with open(x+'.jpg', 'wb') as handler:
      handler.write(img_data)
    return img


"""
moon_image_url = generate_base_image('moon')
night_sky_image_url = generate_base_image('night sky with stars')

img_data = requests.get(moon_image_url).content
with open('moon_image.jpg', 'wb') as handler:
    handler.write(img_data)
img_data = requests.get(night_sky_image_url).content
with open('night_sky.jpg', 'wb') as handler:
    handler.write(img_data)

"""
"""


# Generate two images using the DALL-E 2 API
image1_url = generate_base_image('forest')
image2_url = generate_base_image('sunset')

# Download and open the generated images
image1 = download_image(image1_url,'image1')
image2 = download_image(image2_url,'image2')
"""



# Blend the images using the Multiply mode
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')
# Blend the images using the Multiply mode
image3 = Image.open('moon_image.jpg')
image4 = Image.open('night_sky.jpg')

def custom_blend(image1, image2):
    return ImageChops.add_modulo(image1, image2).point(lambda x: x // 2)



# Blend the images using the custom blend mode
result = custom_blend(image1, image2)
result2= custom_blend(image3, image4)
# Save the blended image to a file
result.save('custom_blend.jpg')
result2.save('custom_blend2.jpg')

# CODIO SOLUTION END