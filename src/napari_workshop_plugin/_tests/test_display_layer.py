import numpy as np
import pytest
from .._widget import display_layer
import time
import sys
from skimage import data

def test_add_layer(make_napari_viewer, capsys):
    viewer = make_napari_viewer()
    name = "test_layer"
    data = np.random.random((100, 100, 3))
    as_image = True
    display_layer(viewer, (name, data, as_image))
    captured = capsys.readouterr()
    assert f"Adding {name} to viewer" in captured.out.strip()

   
def test_update_layer(make_napari_viewer, capsys):
    viewer = make_napari_viewer()
    name = "test_layer"
    data = np.random.random((100, 100, 3))
    as_image = True
    display_layer(viewer, (name, data, as_image))
    display_layer(viewer, (name, data, as_image))
    captured = capsys.readouterr()
    assert f"Updating {name} with new data" in captured.out.strip() 