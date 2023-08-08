import os
import sys
from PIL import Image

# Append the location of student's file to the system path
sys.path.insert(1, '/home/codio/workspace')

# Import student's function
from exerc import combine

def test_combine_function():
    # Define test inputs
    prompt1 = "a night sky"
    prompt2 = "a plane flying at night"
   
    # Delete the image file if it already exists
    if os.path.isfile('final_blended.png'):
        os.remove('final_blended.png')

    # Call the student's function
    combine(prompt1, prompt2)

    # Check if the image file is created
    assert os.path.isfile('final_blended.png'), "The 'combine' function did not create an image file."

    # Check if the image file is non-empty
    img = Image.open('final_blended.png')
    width, height = img.size
    assert width > 0 and height > 0, "The created image is empty."

    print("All tests passed!")

# Run the test
test_combine_function()
