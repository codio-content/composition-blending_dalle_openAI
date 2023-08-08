
Before diving into more advanced techniques, let's start with a revision example of image composition. In this example, we will generate two images using the DALL-E 2 API:` a moon` and `a night sky`. Then, we will overlay the moon image on top of the night sky image to create a composite image.


# Generate moon and night sky images
```python
moon_image_url = generate_base_image('moon')
night_sky_image_url = generate_base_image('night sky with stars')
```

### Saving our new images
```python
img_data = requests.get(moon_image_url).content
with open('moon_image.jpg', 'wb') as handler:
    handler.write(img_data)
img_data = requests.get(night_sky_image_url).content
with open('night_sky.jpg', 'wb') as handler:
    handler.write(img_data)

```

{Try it!}(python3 imageGen.py 2)
[Click here to refresh your moon image](close_file moon_image.jpg panel=1; open_file moon_image.jpg panel=1) 
[Click here to refresh your night sky image](close_file night_sky.jpg panel=1; open_file night_sky.jpg panel=1)
After generating your images comment out the code that calls on new images to be generated, so we can keep our base images consistent. 



```python 
#saving our images as variables.
moon_image=Image.open('moon_image.jpg')
night_sky_image=Image.open('night_sky.jpg')


# Resize the moon image to fit the composition
moon_image = moon_image.resize((200, 200), Image.ANTIALIAS)

# Ensure the moon image has the correct mode with an alpha channel
moon_image = moon_image.convert('RGBA')

# Overlay the moon image on top of the night sky image
night_sky_image.paste(moon_image, (150, 100), moon_image)

# Save the composed image to a file
night_sky_image.save('night_sky_with_moon.jpg')
```
{Try it!}(python3 imageGen.py 3)
[Click here to refresh your moon and night sky  image](close_file night_sky_with_moon.jpg panel=1; open_file night_sky_with_moon.jpg panel=1)


{Check It!|assessment}(multiple-choice-2995036391)
