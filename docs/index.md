# Simple documentation

Here is a simple documentation for a simple project.

The main components of the documentation are:

1. `mkdocs.yml` - the configuration file
    - This specifies the theme, the website layout, and the plugins used. Of note are the `mkdocstrings` plugin, which is used to build the API reference from the code docstrings, and the `search` plugin, which is used to build the search index.
2. `docs/` - the documentation folder
    - This folder contains all the markdown files that make up the documentation. The `index.md` file is the homepage, and the `reference.md` file is the API reference. The `about.md` file is a simple page that describes the MkDocs project.
    - This also holds extra css files that are used to style the documentation via the `mkdocs.yml` file in the `extra_css` section.
3. `.github/workflows/build_docs.yml` - the GitHub action deployment
    - This file specifies the GitHub action that builds the documentation and deploys it to GitHub Pages. It is triggered on every push to the `main` branch.

## Building the documentation locally

To build the documentation locally, you need to install the dependencies. Run the following from the main directory of this project:

```bash
pip install .[docs]
```

Then you can build and view the documentation. Run the following from the main directory of this project:

```bash
mkdocs serve
```
