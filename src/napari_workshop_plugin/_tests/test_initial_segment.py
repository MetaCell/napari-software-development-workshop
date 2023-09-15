import numpy as np
import pytest

from .._widget import initial_segment


# Fixture to create a mock "napari.types.ImageData" object
@pytest.fixture
def mock_napari_image_data():
    return np.random.random((100, 100))

# Unit test for initial_segment function
#expected to work correctly only for grayscale images
def test_initial_segment(mock_napari_image_data):
    classes = 3

    # Call the function
    result = initial_segment(mock_napari_image_data, classes)

    # Check if the result is of the correct type and size (same size)
    assert isinstance(result, np.ndarray)
    assert mock_napari_image_data.shape == result.shape
    assert issubclass(result.dtype.type, np.integer)
    assert result.max() <= classes - 1
