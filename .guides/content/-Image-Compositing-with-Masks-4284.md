In this section, we will explore image compositing using masks to control the transparency and visibility of different image layers. By mastering the use of masks, you will be able to create complex and visually engaging image compositions using the DALL-E 2 API and PIL.

### Alpha Masks
**Alpha masks** define the transparency of an image, allowing you to control which parts of the image are visible when composited with another image. In the previous example, we used the `paste()` function to overlay the moon image onto the night sky image using its own alpha channel as the mask. This ensures that only the moon's visible pixels are pasted onto the night sky image. When you use an image's own alpha channel as the mask during the compositing process, you're essentially using the transparency information already embedded in the image to dictate where and how the image should be visible when overlaid onto another. This is particularly useful with images that have elements with varying degrees of transparency or complex shapes that would be difficult to manually isolate.



### Custom Masks

You can also create custom masks to apply more advanced compositing techniques or control the visibility of image layers in a more precise manner. Custom masks can be created using the `Image.new()` function with the `'L'` mode, which represents a grayscale image.

Here's an example of creating a custom mask and using it to composite two images. Please note, if you are going to run it multiple time the generation and the download need to be commented out so you can keep your base image consistent.
```
from PIL import Image

# Generate two images using the DALL-E 2 API
image1_url = generate_base_image('forest')
image2_url = generate_base_image('sunset')


# Download and open the generated images
image1 = download_image(image1_url,'image1')
image2 = download_image(image2_url,'image2')

# Create a custom mask (grayscale gradient)
width, height = image1.size
mask = Image.new('L', (width, height))
for y in range(height):
    for x in range(width):
        mask.putpixel((x, y), x)

# Composite the two images using the custom mask
result = Image.composite(image1, image2, mask)

# Save the composited image to a file
result.save('composite_custom_mask.jpg')
```

{Try it!}(python3 imageGen.py 19)
[Click here to refresh your composite_custom_mask  image](close_file composite_custom_mask.jpg panel=1; open_file composite_custom_mask.jpg panel=1)

[Click here to refresh your 1st  image](close_file image1.jpg panel=1; open_file image1.jpg panel=1)
[Click here to refresh your 2nd  image](close_file image2.jpg panel=1; open_file image2.jpg panel=1)

In this example, the custom mask is a grayscale gradient from left (black) to right (white). When using `Image.composite()`, the black areas of the mask will take the corresponding pixels from `image1`, while the white areas will take the pixels from `image2`. Gray areas of the mask will result in a blend of the two images.  

### Advanced Masking Techniques

You can create more complex custom masks using a variety of techniques, such as drawing shapes, adding text, or even using another image as a mask. By combining these techniques, you can create intricate and visually stunning image compositions.

{Check It!|assessment}(multiple-choice-2876945861)
