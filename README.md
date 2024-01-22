# Compress Image
## Overview

compress-image is a Python script designed to compress images either from the local system or from the internet, allowing users to specify the compression parameters and the maximum size of the resulting image file.
Installation

To use compress-image, make sure you have Python installed. Then, you can install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using the following command:

```bash
python compress-image.py arg1 arg2 arg3 arg4
```

## Arguments

    arg1: Specify the source of the image. Use system for local system images and url for images from the internet.
    arg2: Provide the path or URL of the image accordingly.
    arg3: Specify the path and name of the file to save the compressed result.
    arg4: Set the maximum size in bytes for the final compressed image.

## Examples
### Compressing a local image:

```bash
python compress-image.py system /path/to/local/image.jpg /path/to/save/compressed_image.jpg 500000
```

### Compressing an image from the internet:

```bash
python compress-image.py url https://example.com/image.jpg /path/to/save/compressed_image.jpg 500000
```

### Notes

    The script utilizes the specified compression parameters and ensures that the resulting image file does not exceed the specified maximum size.
    Adjust the arg4 parameter to control the compression level and achieve the desired file size.
    Ensure a stable internet connection when compressing images from URLs.

Feel free to contribute, report issues, or suggest improvements!

Happy compressing!