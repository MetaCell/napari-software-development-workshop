import numpy as np
import pytest
import time

from napari_workshop_plugin import segmentation_widget


def create_circle_image(size_x, size_y):
    """Create a circle image."""
    x, y = np.meshgrid(np.linspace(-1, 1, size_x), np.linspace(-1, 1, size_y))
    return (x**2 + y**2) < 1


@pytest.mark.parametrize(
    "size_x, size_y, classes", [(100, 100, 2), (511, 511, 3)]
)
def test_example_magic_widget(
    make_napari_viewer, capsys, size_x, size_y, classes
):
    viewer = make_napari_viewer()
    image = create_circle_image(size_x, size_y)
    viewer.add_image(image, name="circle")
    my_widget = segmentation_widget()

    # if we "call" this object, it'll execute our function
    worker = my_widget(
        image=viewer.layers[0], classes=classes, disk_size=2, blur_sigma=2.0
    )
    ready_count = 0
    def worker_ready():
        nonlocal ready_count
        ready_count += 1
    worker.yielded.connect(worker_ready)

    start_time = time.time()
    timeout = 0
    while ready_count < 4 and timeout < 10:
        time.sleep(1)
        timeout = time.time() - start_time
    if timeout >= 10:
        raise TimeoutError("Timeout while waiting for layers to be added")

    layer = viewer.layers[-1]
    assert layer.name == "circle_segmented"
    assert layer.data.shape == (size_x, size_y)
    assert layer.data.dtype == np.uint8
    assert layer.data.max() == classes - 1

    # read captured output and check that it's as we expected
    captured = capsys.readouterr()
    assert captured.out == (
        "INFO: Adding circle_blurred to the viewer\n"
        "INFO: Adding circle_rough_segmented to the viewer\n"
        "INFO: Adding circle_segmented to the viewer\n"
    )
