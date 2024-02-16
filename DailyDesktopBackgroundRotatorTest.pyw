import os
import random
import ctypes 
import schedule
import time

def set_wallpaper(image_file):

    # Function sets wallpaper, below comments are for my own enrichment.
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_file, 0)
    # The line above is a function that uses the ctypes library to communicate with Windows OS.
    # the SystemParametersInfoW function is responsible for changing the wallpaper
    # parameter 20 is a constant in the user32 library that lets the machine know we need the desktop library to change
    # The second 0 indicates we want the wallpaper changed, the third parameter is the path to the image file we want as wallpaper
    # the fourth zero specifis th positioning o the wallpaper, in this case 0 means the wallpaper should be centered.

def get_image_file(image_directory):
    # Function retrieves random img file from folder, checks if file is an image type before picking a random photo from the directory recieved.
    image_files = [file for file in os.listdir(image_directory) if file.endswith(('.jpg', '.jpeg', '.png'))]
    if image_files:
        return os.path.join(image_directory, random.choice(image_files))
    else:
        return None

def rotate_background(image_directory):
     # Get a random image from the directory
    image_file = get_image_file(image_directory)

    if image_file:
        # Set the image as the desktop wallpaper
        set_wallpaper(image_file)

def main():

    image_directory = 'C:\\Users\\Livvy\\OneDrive\\000\\DesktopImagesforPythonDailyDesktop' # Replace with the path to your image directory

     # Schedule background rotation every 12 hours
    schedule.every(5).seconds.do(rotate_background, image_directory)

    # Run the scheduled tasks indefinitely
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()