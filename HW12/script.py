from PIL import Image
import numpy as np

class QuadTreeNode:
    def __init__(self, value=None, children=None):
        self.value = value 
        self.children = children 

def build_quadtree(image_array, threshold=10):

    if image_array.size == 0:
        return None

    if image_array.shape[0] == 1 and image_array.shape[1] == 1:
        return QuadTreeNode(value=image_array[0, 0])

    avg_value = np.mean(image_array)
    max_deviation = np.max(image_array) - np.min(image_array)

    if max_deviation <= threshold:
        return QuadTreeNode(value=avg_value)

    h, w = image_array.shape
    mid_h, mid_w = max(1, h // 2), max(1, w // 2)

    children = [
        build_quadtree(image_array[:mid_h, :mid_w], threshold),  
        build_quadtree(image_array[:mid_h, mid_w:], threshold),
        build_quadtree(image_array[mid_h:, :mid_w], threshold), 
        build_quadtree(image_array[mid_h:, mid_w:], threshold), 
    ]

    return QuadTreeNode(children=children)

def decompress_quadtree(node, shape):

    if node.value is not None:
        return np.full(shape, node.value, dtype=np.uint8)

    mid_h, mid_w = shape[0] // 2, shape[1] // 2
    top_left = decompress_quadtree(node.children[0], (mid_h, mid_w))
    top_right = decompress_quadtree(node.children[1], (mid_h, shape[1] - mid_w))
    bottom_left = decompress_quadtree(node.children[2], (shape[0] - mid_h, mid_w))
    bottom_right = decompress_quadtree(node.children[3], (shape[0] - mid_h, shape[1] - mid_w))

    # Combine the four quadrants into a single array
    return np.vstack((np.hstack((top_left, top_right)), np.hstack((bottom_left, bottom_right))))

image_path = "./data/sample.bmp" 
image = Image.open(image_path).convert("L")
image_array = np.array(image)

quadtree_root = build_quadtree(image_array)

compressed_image_array = decompress_quadtree(quadtree_root, image_array.shape)

decompressed_image = Image.fromarray(compressed_image_array)

decompressed_image_path = "./data/decompressed_image.bmp"
decompressed_image.save(decompressed_image_path)
print("Original image shape: ", image_array)
print("Compressed image shape: ", compressed_image_array) 
print("Decompressed image shape: " + decompressed_image)
