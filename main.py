import cv2
import numpy as np

base_img = cv2.imread('base.png', 0)
text_diff_img = cv2.imread('altered.png', 0)
bg_color_changed_img = cv2.imread('bg-color-changed.png', 0)


def img_diff(img1, img2, caption):
    """Prints the difference in two imported images in percentage

    Args:
                    img1: First OpenCV imported image
                    img2: Second OpenCV imported image
    """
    # Take the absolute difference of the images
    res = cv2.absdiff(img1, img2)

    # Convert the result to integer type
    res = res.astype(np.uint8)

    # Find percentage difference based on number of pixels that are not zero
    percentage = (np.count_nonzero(res) * 100) / res.size

    output = f"{caption} Percentage: {percentage}"
    print(output)


# Diff the first
img_diff(base_img, base_img, "Comparing to self")
img_diff(base_img, text_diff_img, "Comparing to slightly changed text")
img_diff(base_img, bg_color_changed_img,
         "Comparing to changed background color")
