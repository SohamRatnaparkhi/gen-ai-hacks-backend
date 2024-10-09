import cv2
from PIL import Image
import numpy as np


def embed_image_within_bbox(base_image_path, embedding_image_path, bbox):
    # Load base image and the image to be embedded
    base_image = cv2.imread(base_image_path)
    embedding_image = Image.open(embedding_image_path)

    # Bounding box coordinates (x, y, width, height)
    x, y, bbox_width, bbox_height = bbox

    # Check if the bounding box is wider than it is tall
    if bbox_width > bbox_height and embedding_image.height > embedding_image.width:
        # Rotate the embedding image if needed (make it landscape)
        embedding_image = embedding_image.rotate(90, expand=True)

    # Get dimensions of the embedding image
    img_width, img_height = embedding_image.size

    # Calculate scale factor to fit the image within the bounding box while maintaining aspect ratio
    scale_factor = min(bbox_width / img_width, bbox_height / img_height)

    # Resize the embedding image without distorting (keeping aspect ratio)
    new_width = int(img_width * scale_factor)
    new_height = int(img_height * scale_factor)
    resized_embedding_image = embedding_image.resize((new_width, new_height), Image.LANCZOS)

    # Calculate center position for image to be placed in bounding box
    offset_x = x + (bbox_width - new_width) // 2
    offset_y = y + (bbox_height - new_height) // 2

    # Convert resized image to OpenCV format
    resized_embedding_image_cv = cv2.cvtColor(np.array(resized_embedding_image), cv2.COLOR_RGB2BGR)

    # Overlay the resized image on the base image
    base_image[offset_y:offset_y+new_height, offset_x:offset_x+new_width] = resized_embedding_image_cv

    # Save the result or display it
    cv2.imwrite('output_image.jpg', base_image)
    # cv2.imshow('Result', base_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# Example usage
# bbox = (100, 50, 200, 350)  # Example bounding box coordinates
# embed_image_within_bbox('back.jpg', 'product.jpg', bbox)
