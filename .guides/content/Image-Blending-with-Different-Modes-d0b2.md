### Image Blending

We will explore image blending, which involves combining two images using various blending modes to create unique visual effects and styles. This will allow you to further enhance your image compositions and unlock even more creative possibilities with the DALL-E 2 API and PIL.

### Blending Modes
**Blending modes** determine how the colors of two images interact with each other when combined. Some common blending modes include:
|||
**Normal**: The top image simply covers the bottom image.
**Multiply**: The color values of the top and bottom images are multiplied, resulting in a darker image.
**Screen**: The color values of the top and bottom images are inverted, multiplied, and then inverted again, resulting in a lighter image.
**Overlay**: Combines Multiply and Screen modes, preserving the highlights and shadows of the bottom image.
|||

PIL provides a built-in method called `blend()` for blending two images using the normal blending mode. However, to use other blending modes, we need to use the `ImageChops` module.

We will blend two images using various blending modes to demonstrate their effects on the final composition. 
```python
# Blend the images using the Multiply mode
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')
multiply_blend = ImageChops.multiply(image1, image2)
multiply_blend.save('multiply_blend.jpg')
```
{Try it!}(python3 imageGen.py 4)


[Click here to refresh your 1st  image](close_file image1.jpg panel=1; open_file image1.jpg panel=1)
[Click here to refresh your 2nd  image](close_file image2.jpg panel=1; open_file image2.jpg panel=1)

[Click here to refresh your multiply blend  image](close_file multiply_blend.jpg panel=1; open_file multiply_blend.jpg panel=1)
[Click here to refresh your composite_custom_mask  image](close_file composite_custom_mask.jpg panel=1; open_file composite_custom_mask.jpg panel=1)
Now let's try looking at it with our moon and night sky images. 
Your original composition pic of the moon and night sky might look like this:
![night_sky_with_moon-copy](night_sky_with_moon-copy.jpg)
But using a `blend` you can get more of an image that looks like this.
![multiply_blend-copy](multiply_blend-copy.jpg)

```python 
# Blend the images using the Multiply mode
image3 = Image.open('moon_image.jpg')
image4 = Image.open('night_sky.jpg')
multiply_blend = ImageChops.multiply(image3, image4)
multiply_blend.save('multiply_blend2.jpg')
```
{Try it!}(python3 imageGen.py 5)

[Click here to refresh your multiply moon blend image](close_file multiply_blend2.jpg panel=1; open_file multiply_blend2.jpg panel=1)

### Custom Blend Modes

You can also create custom blend modes by defining your own functions that take the color values of the top and bottom images and return a new color value. This allows you to achieve unique and creative blending effects that may not be available with the built-in blending modes.

Here's an example of creating a custom blend mode that calculates the average of the color values of the top and bottom images:
```python
from PIL import ImageChops

def average_blend(image1, image2):
    return ImageChops.add(image1, image2, scale=0.5)

# Use the custom blend mode to blend two images
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')
average_blend_result = average_blend(image1, image2)
average_blend_result.save('average_blend.jpg')
```
{Try it!}(python3 imageGen.py 6)
[Click here to refresh your average blend image](close_file average_blend.jpg panel=1; open_file average_blend.jpg panel=1)

Creating custom blend modes can be a powerful way to achieve a unique look and feel for your image compositions. Experimenting with different blending functions can lead to interesting and unexpected results, allowing you to further enhance your compositions and unlock even more creative possibilities with the DALL-E 2 API and PIL.


{Check It!|assessment}(multiple-choice-2654498946)
