import numpy as np

from napari_workshop_plugin import napari_get_reader, read_numpy_file


# tmp_path is a pytest fixture
def test_reader(tmp_path):
    """An example of how you might test your plugin."""
    # write some fake data using your supported file format
    my_test_file = str(tmp_path / "myfile.npy")
    original_data = np.random.rand(20, 20)
    np.save(my_test_file, original_data)

    # try to read it back in
    reader = napari_get_reader(my_test_file)
    assert callable(reader)

    # make sure we're delivering the right format
    layer_data_list = reader(my_test_file)
    assert isinstance(layer_data_list, list) and len(layer_data_list) > 0
    layer_data_tuple = layer_data_list[0]
    assert isinstance(layer_data_tuple, tuple) and len(layer_data_tuple) > 0

    # make sure it's the same as it started
    np.testing.assert_allclose(original_data, layer_data_tuple[0])


def test_get_reader_pass():
    reader = napari_get_reader("fake.file")
    assert reader is None


def test_napari_get_reader_single_file():
    # Test the napari_get_reader function with a single file path.
    path = "test.npy"
    reader = napari_get_reader(path)
    assert callable(reader)

def test_napari_get_reader_multiple_files():
    # Test the napari_get_reader function with a list of file paths.
    paths = ["test1.npy", "test2.npy"]
    reader = napari_get_reader(paths)
    assert callable(reader)

def test_napari_get_reader_non_npy():
    # Test the napari_get_reader function with a non-npy file path.
    path = "test.txt"
    reader = napari_get_reader(path)
    # assert callable(reader) # to make it fail
    assert reader is None

def test_read_numpy_file_single_file(tmp_path):
    # Test the read_numpy_file function with a single npy file.
    path = str(tmp_path / "test.npy")
    original_data = np.random.rand(20, 20)
    np.save(path, original_data)
    layer_data = read_numpy_file(path)
    assert isinstance(layer_data, list)
    assert len(layer_data) == 1
    data, add_kwargs, layer_type = layer_data[0]
    assert isinstance(data, np.ndarray)
    assert data.shape == original_data.shape
    np.testing.assert_allclose(data, original_data)

def test_read_numpy_file_multiple_files(tmp_path):
    # Test the read_numpy_file function with multiple npy files.
    paths = [str(tmp_path / "test1.npy"), str(tmp_path / "test2.npy")]
    original_data1 = np.random.rand(20, 20)
    original_data2 = np.random.rand(20, 20)
    np.save(paths[0], original_data1)
    np.save(paths[1], original_data2)
    layer_data = read_numpy_file(paths)
    assert isinstance(layer_data, list)
    assert len(layer_data) == 1
    data, add_kwargs, layer_type = layer_data[0]
    assert isinstance(data, np.ndarray)
    assert data.shape == (2, 20, 20)
    np.testing.assert_allclose(data[0], original_data1)
    np.testing.assert_allclose(data[1], original_data2)
