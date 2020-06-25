import matplotlib.pyplot as plt
from ImageProcessor import ImageProcessor

class ColorFilter:
    def invert(self, array):
        pass

    def to_blue(self, array):
        pass

    def to_green(self, array):
        return array[:, :, 0]

    def to_red(self, array):
        return array[:, :, 0]

    def celluloid(self, array):
        pass

    def to_greyscale(self, array):
        pass


IP = ImageProcessor()
CF = ColorFilter()
image = IP.load("blackhole.png")
#i = IP.display(image)
image = CF.to_red(image)
plt.imshow(image)
plt.show()