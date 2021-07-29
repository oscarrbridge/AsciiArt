import cv2
import numpy as np
import sys

symbols_list = ["█", "═", "║", "▓", "░", "o"]
threshold_list = [0, 50, 100, 150, 200]

IMAGE_SCALE = 20


def print_asci(image_array):
    for line in image_array:
        for e in line:
            print(symbols_list[int(e) % len(symbols_list)], end="")
        print("")


def img_to_asci(photo):
    height, width = photo.shape

    new_width = int(width / IMAGE_SCALE + 20)
    new_height = int(height / IMAGE_SCALE)

    resized_image = cv2.resize(photo, (new_width, new_height), )

    image_thresh = np.zeros(resized_image.shape)

    for i, threshold in enumerate(threshold_list):
        image_thresh[resized_image > threshold] = i

    return image_thresh


if __name__ == "__main__":

    if len(sys.argv) > 1:
        print(f"The image being used is '{sys.argv[1]}'")
        image_path = sys.argv[1]

    else:
        print("You need to specify the path to the image, Using default image")
        image_path = "sample_image.jpg"

    image = cv2.imread(image_path, 0)

    new_image = img_to_asci(image)

    print(print_asci(new_image))
