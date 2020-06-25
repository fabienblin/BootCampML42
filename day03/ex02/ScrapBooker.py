import numpy as np
import matplotlib as mpl
import matplotlib.image as mpimg

class ScrapBooker:
    def crop(self, array: np.array, dimensions, position=(0,0)):
        true_dimensions = list(dimensions)
        array = np.copy(array)
        try :
            if array.shape[0] < dimensions[0] + position[0]:
                print("Error : crop is to high.")
                true_dimensions[0] -= dimensions[0] - position[0] - array.shape[0]
            if array.shape[1] < dimensions[1] + position[1]:
                print("Error : crop is to wide.")
                true_dimensions[1] -= dimensions[1] - position[1] - array.shape[1]
           
            a = array[position[0]:true_dimensions[0], position[1]:true_dimensions[1]]
        except Exception as e:
            print("Error on array allocation.", e)
            exit(1)
        return a

    def thin(self, array: np.array, n, axis=0):
        a = np.copy(array)
        try :
            to_delete=[]
            for i in range(a.shape[axis-1]):
                if i % n == 0:
                    to_delete.append(i)
            a = np.delete(array, to_delete, axis-1)
        except Exception as e:
            print("Error deleting.", e)
            exit(1)
        return a

    def juxtapose(self, array: np.array, n, axis=0):
        a = array.copy()
        try:
            for i in range(n-1):
                a = np.concatenate([a, array], axis)
        except Exception as e:
            print(e)
            exit(1)
        return a

    def mosaic(self, array: np.array, dimensions):
        a = np.array(array)
        for axis, dim in enumerate(dimensions):
            a = self.juxtapose(a, round(dim / a.shape[axis])+1, axis)
        a = self.crop(a, dimensions)
        return a


image = mpimg.imread("../ex01/images/opaque.png")
print("image ", str(image.shape))
a = [[10,11,12,13],[20,21,22,23],[30,31,32,33]]

sc = ScrapBooker()
test = sc.crop(image, (100,100))
#test = sc.crop(image, (200,200), (100, 100))
#test = sc.crop(image, (200,200), (300, 300))
#test = sc.thin(a, 2)
#test = sc.thin(a, 2, 1)
#test = sc.juxtapose(a, 3)
test = sc.mosaic(image, (100,200))
print("test ", str(test.shape), "\n", str(test))

