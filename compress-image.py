#!/usr/local/bin/python3

import io
import math
import sys
from PIL import Image
import requests
from io import BytesIO


def JPEGSaveWithTargetSize(im, filename, target):
    """Save the image as JPEG with the given name at best quality that makes less than "target" bytes"""
    # Min and Max quality
    Qmin, Qmax = 25, 96
    # Highest acceptable quality found
    Qacc = -1

    s = 0
    while Qmin <= Qmax:
        m = math.floor((Qmin + Qmax) / 2)

        # Encode into memory and get size
        buffer = io.BytesIO()
        im.save(buffer, format="JPEG", quality=m)
        s = buffer.getbuffer().nbytes

        if s <= target:
            Qacc = m
            Qmin = m + 1
        elif s > target:
            Qmax = m - 1

    # Write to disk at the defined quality
    if Qacc > -1:
        im.save(filename, format="JPEG", quality=Qacc)
        w, h = im.size
        print("Final image measurements...")
        print("Bytes:", s)
        print("Width:", w)
        print("Height:", h)
    else:
        print("Image is too big, reducing size to 90% to try again...", file=sys.stderr)
        try:
            w, h = im.size
            print('width:  ', w)
            print('height: ', h)
            if w >= h:
                # width
                w = w * 0.9
                maxsize = (w, w)
                im.thumbnail(maxsize, Image.Resampling.LANCZOS)
            else:
                # height
                h = h * 0.9
                maxsize = (h, h)
                im.thumbnail(maxsize, Image.Resampling.LANCZOS)
                # im.save("temp-file.jpg", "JPEG")
            JPEGSaveWithTargetSize(im, filename, target)
        except IOError:
            print("ERROR: Error resizing image!", file=sys.stderr)


################################################################################
# main
################################################################################

imageOrigin = sys.argv[1]
originalImapePath = sys.argv[2]
# 200000
targetFile = sys.argv[3]
targetSize = sys.argv[4]

# Load sample image
if imageOrigin == "system":
    im = Image.open(originalImapePath)
    JPEGSaveWithTargetSize(im, targetFile, int(targetSize))

if imageOrigin == "url":
    response = requests.get(originalImapePath)
    im = Image.open(BytesIO(response.content))
    JPEGSaveWithTargetSize(im, targetFile, int(targetSize))
