import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageProcessor:
    def load(self, path):
        i = mpimg.imread(path)
        print(i.shape)
        return i

    def display(self, array):
        print(array)

"""
IP = ImageProcessor
image = IP.load("images/opaque.png")
IP.display(image)
"""