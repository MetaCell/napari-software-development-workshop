"""Provides a widget for segmenting cells from calcium imaging data."""
import logging
from typing import TYPE_CHECKING

import numpy as np
from magicgui import magic_factory
from napari.qt.threading import thread_worker
from napari.utils.notifications import show_info
from skimage import color, filters, morphology

if TYPE_CHECKING:
    import napari


@thread_worker
def segment(
    image: "napari.types.Image",
    blur_sigma: float = 2.0,
    disk_size: int = 4,
    classes: int = 3,
):
    image_data = np.asarray(image.data)
    image_data = blur_and_gray_image(image_data, blur_sigma)
    yield (f"{image.name}_blurred", image_data, True)
    labels = initial_segment(image_data, classes)
    yield (f"{image.name}_rough_segmented", labels, False)
    labels = smooth_labels(labels, disk_size)
    yield (f"{image.name}_segmented", labels, False)


def blur_and_gray_image(
    image: "napari.types.ImageData", sigma: float = 2.0
) -> "napari.types.ImageData":
    image = np.asarray(image)
    if len(image.shape) >= 3 and image.shape[-1] in [3, 4]:
        image = color.rgb2gray(image)
    return filters.gaussian(image, sigma)


def initial_segment(
    image: "napari.types.ImageData", classes: int = 3
) -> "napari.types.LabelsData":
    image = np.asarray(image)
    thresholds = filters.threshold_multiotsu(image, classes=classes)
    return np.digitize(image, thresholds)


def smooth_labels(
    labels: "napari.types.LabelsData", disk_size: int = 4
) -> "napari.types.LabelsData":
    labels = np.asarray(labels)
    return filters.rank.mean(labels, morphology.disk(disk_size))


def display_layer(viewer: "napari.Viewer", args) -> None:
    logging.debug(args)
    name, data, as_image = args
    if name in viewer.layers:
        show_info(f"Updating {name} with new data")
        viewer.layers[name].data = data
    else:
        show_info(f"Adding {name} to viewer")
        (
            viewer.add_image(data, name=name)
            if as_image
            else viewer.add_labels(data, name=name)
        )

@magic_factory(persist=True)
def segmentation_widget(
    viewer: "napari.Viewer",
    image: "napari.layers.Image",
    blur_sigma: float = 2.0,
    disk_size: int = 4,
    classes: int = 3,
):
    """Segment cells from calcium image max projection.

    1. Grayscale and blur the image.
    2. Perform a multiotsu to separate the image into three classes:
        background, non-cell tissue, and cells.
    3. Smooth the multiotsu segmentation via disks.

    Parameters
    ----------
    viewer : napari.Viewer
        A viewer instance from napari
    image : napari.layers.Image
        The image to segment from. Can be one channel or more.
        If more than one channel, is converted to grayscale.
    blur_sigma : float, optional
        The standard deviation of the gaussian blur to be applied.
        A higher sigma indicates more blur.
        By default 2.0.
    disk_size : int, optional
        The size of the disk in pixels for smoothing.
        A higher disk_size indicates more smoothing.
        By default 4.
    classes : int, optional
        The number of classes to segment into.
        One of the classes will be background.
        By default 3. Going past 5 classes is not recommended for speed.

    """
    def inner_display_layer(args) -> None:
        display_layer(viewer, args)


    worker = segment(image, blur_sigma, disk_size, classes)
    worker.yielded.connect(inner_display_layer)
    worker.start()

    return worker
