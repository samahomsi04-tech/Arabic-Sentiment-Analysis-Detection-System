
import nbformat
import glob

# Fix all notebooks
for path in glob.glob("**/*.ipynb", recursive=True):
    nb = nbformat.read(path, as_version=4)
    if "widgets" in nb.metadata:
        for widget in nb.metadata.widgets.values():
            if "state" not in widget:
                widget["state"] = {}
        nbformat.write(nb, path)
        print(f"Fixed: {path}")