import numpy as np
from PIL import Image
from collections import Counter

def get_top_colors(file, num_colors=10):
    image = Image.open(file)
    image = image.resize((200, 200))  
    image = image.convert('RGB')
    image_array = np.array(image)
    image_array = image_array.reshape((image_array.shape[0] * image_array.shape[1], 3))

    colors, counts = zip(*Counter(tuple(rgb) for rgb in image_array).items())
    sorted_indices = np.argsort(counts)[::-1][:num_colors]
    
    top_colors = [(colors[i], counts[i]) for i in sorted_indices]
    return top_colors
