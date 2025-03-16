from PIL import Image
import pytesseract
import os

# Constants
RESIZE_DIMENSIONS = (100, 100)

def edit_image(image_path, operations):
    """
    Edit an image based on the specified operations.

    :param image_path: Path to the image file.
    :param operations: List of operations to perform on the image.
                       Supported operations: 'rotate', 'resize'.
    :return: Path to the edited image.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")

    img = Image.open(image_path)
    for operation in operations:
        if operation == 'rotate':
            img = img.rotate(90)
        elif operation == 'resize':
            img = img.resize(RESIZE_DIMENSIONS)
        else:
            raise ValueError(f"Unsupported operation: {operation}")

    img.save(image_path)
    return image_path

def ocr_image(image_path):
    """
    Perform OCR on an image to extract text.

    :param image_path: Path to the image file.
    :return: Extracted text from the image.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")

    return pytesseract.image_to_string(Image.open(image_path))