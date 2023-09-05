
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from ._reader import read_numpy_file, napari_get_reader
from ._widget import segmentation_widget

# this is the list of things that are imported with
# from napari_workshop_plugin import *
__all__ = (
    "segmentation_widget"
    "read_numpy_file",
    "napari_get_reader"
)
