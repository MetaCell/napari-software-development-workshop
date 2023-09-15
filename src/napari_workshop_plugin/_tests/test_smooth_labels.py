import numpy as np
import pytest

from .._widget import smooth_labels


# Fixture to create a mock "napari.types.ImageData" object
@pytest.fixture
def mock_napari_image_data():
    return np.random.random((32, 32))

# Fixture to create a mock "napari.types.LabelsData" object
@pytest.fixture
def mock_napari_labels_data(mock_napari_image_data):
    shape = mock_napari_image_data.shape[:2]
    return np.random.randint(0, 3, shape)

# Unit test for smooth_labels function
def test_smooth_labels(mock_napari_labels_data):
    disk_size = 4

    # Use pytest.warns to suppress warnings
    with pytest.warns(UserWarning):
        # Call the function
        result = smooth_labels(mock_napari_labels_data, disk_size)

    # Check if the result is of the correct type
    assert isinstance(result, np.ndarray)
    assert result.ndim == 2
    assert mock_napari_labels_data.shape[:2] == result.shape[:2]
    assert issubclass(result.dtype.type, np.integer)
    assert result.max() <= mock_napari_labels_data.max()
