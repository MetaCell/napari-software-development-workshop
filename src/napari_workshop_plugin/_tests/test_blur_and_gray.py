import numpy as np
import pytest

from .._widget import blur_and_gray_image


# Fixture to create a mock "napari.types.Image" object
@pytest.fixture
def mock_napari_image():
    class MockNapariImage:
        def __init__(self, data, name):
            self.data = data
            self.name = name

    return MockNapariImage(np.random.random((100, 100, 3)), "MockImage")

# Unit test for blur_and_gray_image function
def test_blur_and_gray_image(mock_napari_image):
    input_image = mock_napari_image.data
    sigma = 2.0

    # Call the function
    result = blur_and_gray_image(input_image, sigma)

    # Check if the result is of the correct type
    assert isinstance(result, np.ndarray)

    # Check if the result is 2D (grayscale)
    assert result.ndim == 2
    assert input_image.shape[:2] == result.shape[:2]


# Run the tests
if __name__ == "__main__":
    pytest.main()
