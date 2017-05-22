# noqa
# coding=utf-8
from __future__ import absolute_import

from io import BytesIO
from StringIO import StringIO

from PIL import Image

from .. import _isimage

CONTENT_TYPE = "image/png"


def format():
    def _format((data, (data_bounds, data_crs)), data_format):
        if not _isimage(data_format):
            raise Exception("Must be an image format")

        out = StringIO()
        im = Image.fromarray(data, data_format.upper())
        im.save(out, "png")

        return (CONTENT_TYPE, out.getvalue())

    return _format