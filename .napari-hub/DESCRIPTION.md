<!-- This file is a placeholder for customizing description of your plugin 
on the napari hub if you wish. The readme file will be used by default if
you wish not to do any customization for the napari hub listing.

If you need some help writing a good description, check out our 
[guide](https://github.com/chanzuckerberg/napari-hub/wiki/Writing-the-Perfect-Description-for-your-Plugin)

-->

This is a demonstration plugin for a software development workshop held in 2023 for the napari community.

It provides the following features:

1. Uploads to PyPI via GitHub actions.
2. Has a conversion to conda-forge in [recipes](https://github.com/seankmartin/napari-software-development-workshop/blob/main/recipes/napari-workshop-plugin/meta.yaml) from grayskull
3. Tests via GitHub actions.
4. Builds and publishes [MkDocs documentation](https://seankmartin.github.io/napari-software-development-workshop/) via GitHub actions.
5. Provides a simple multi-threaded segmentation widget for napari. The widget yields the result of segmentation as a napari layer at each step, to help understand the process.

## Widget functionality

![demo gif of segmentation](https://i.imgur.com/eW4cKsl.gif)

napari-workshop-plugin provides a widget to demonstrate how segmentation works. The widget takes in a 2D grayscale or RGB image, and proceeds to perform a series of segmentation steps, producing a 2D image or labels layer at each step to visualise how the segmentation algorithm works.

Please note, this is not a production-ready segmentation algorithm, but rather a demonstration of how segmentation works.

## Testing

The tests in this package are a good jumping off point for your own plugin development. The main widget is multi-threaded, so it can be a bit challenging to test end-to-end. Instead, the tests are broken down into smaller unit tests for individual functions. The [tests](https://github.com/seankmartin/napari-software-development-workshop/tree/main/src/napari_workshop_plugin/_tests) are run via GitHub actions.

## Other resources

This plugin was generated from the [napari plugin cookiecutter](https://github.com/napari/cookiecutter-napari-plugin). The cookiecutter plugin is also a great jumping off point for your own plugin development. Additionally, some of these concepts are covered in the napari [plugin developer documentation](https://napari.org/dev/plugins/index.html). If you need more support, please reach out on [napari zulip](https://napari.zulipchat.com/), check out the [napari Image.sc](https://forum.image.sc/tag/napari) or [open an issue](https://github.com/napari/napari/issues/new/choose) on the napari repository.

Finally, check out a simple [README template](https://github.com/seankmartin/napari-software-development-workshop/blob/main/template.md) that you can use for your own plugin.
