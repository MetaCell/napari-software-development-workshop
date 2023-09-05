try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from ._reader import napari_get_reader, read_numpy_file
from ._widget import segmentation_widget
from ._sample_data import load_sample_data

# this is the list of things that are imported with
# from napari_workshop_plugin import *
__all__ = (
    "segmentation_widget",
    "read_numpy_file",
    "napari_get_reader",
    "load_sample_data",
)
