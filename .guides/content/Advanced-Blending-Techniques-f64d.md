We will dive deeper into advanced blending techniques, such as creating custom gradient masks and blend modes, to give you greater control and flexibility in image composition. We learned how to create a custom mask for image compositing. Similarly, you can create custom gradient masks to control the blending of two images. By creating masks with varying levels of transparency, you can achieve smooth transitions between the two images.

You can create custom blend modes by defining your own functions that take the color values of the top and bottom images and return a new color value. This allows you to achieve unique and creative blending effects that may not be available with the built-in blending modes.

Before we start we are going to create some variables that we will use in our function. 
```python
# set our images to a variable
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')

image3 = Image.open('moon_image.jpg')
image4 = Image.open('night_sky.jpg')

```
{Try it!}(python3 imageGen.py 18)

```python

def custom_blend(image1, image2):
    return ImageChops.add_modulo(image1, image2).point(lambda x: x // 2)

# Blend the images using the custom blend mode
result = custom_blend(image1, image2)
result2= custom_blend(image3, image4)
# Save the blended image to a file
result.save('custom_blend.jpg')
result2.save('custom_blend2.jpg')
```
{Try it!}(python3 imageGen.py 16)

[Click here to refresh your custom  blend of image 1](close_file custom_blend.jpg panel=1; open_file custom_blend.jpg panel=1)
[Click here to refresh your custom  blend of image 2](close_file custom_blend2.jpg panel=1; open_file custom_blend2.jpg panel=1) 

This is the updated visual of the moon and night sky when using a custom blend.
![custom_blend2-copy](custom_blend2-copy.jpg)

### Custom Blend Function 

The `custom_blend` function returns the resulting image, which is the blended image with the average color value of the two input images.
The `custom_blend` function takes two images, `image1` and `image2`, as inputs. Its purpose is to blend these two images together by calculating the average color value of each corresponding pixel from both images.

`ImageChops.add_modulo(image1, image2)` adds the pixel values of `image1` and `image2` together. It does this by adding the values of corresponding pixels in each image while ensuring that the resulting values don't exceed the maximum allowed value for each color channel. In this case, the maximum allowed value is 255 for an 8-bit image. The `add_modulo` function ensures that if the sum of two pixel values exceed 255, the result wraps around from 0, in a similar fashion to how numbers wrap around when using the modulo operation.

The resulting image from the `add_modulo()` operation has pixel values that are double the average of the original images' pixel values. In order to get the true average, we need to divide these values by 2. We do this using the `point()` function, which applies a given function to each pixel value in the image. In this case, we use a lambda function ` lambda x: x // 2` , which takes an input `x` (the pixel value) and returns the integer division of x by 2 (effectively dividing the pixel value by 2).

{Check It!|assessment}(multiple-choice-1269904246)
