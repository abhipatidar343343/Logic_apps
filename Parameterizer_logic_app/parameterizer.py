import sys
from pathlib import Path
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


NOTEBOOK_NAME = "convertor.ipynb"


def run_notebook(notebook_path, input_file, output_file):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    # Inject input/output variables
    inject_cell = nbformat.v4.new_code_cell(
        f"""
input_path = r"{input_file}"
output_path = r"{output_file}"
"""
    )

    nb.cells.insert(0, inject_cell)

    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")

    ep.preprocess(nb, {"metadata": {"path": str(notebook_path.parent)}})


def main():

    if len(sys.argv) != 2:
        print("Usage:")
        print("python3 parameterizer.py <folder_path>")
        sys.exit(1)

    folder = Path(sys.argv[1]).resolve()

    if not folder.exists():
        print("Folder does not exist")
        sys.exit(1)

    notebook_path = Path(__file__).parent / NOTEBOOK_NAME

    json_files = [
        f for f in folder.iterdir()
        if f.suffix == ".json" and not f.name.endswith("_template.json")
    ]

    if not json_files:
        print("No JSON files found")
        return

    for file in json_files:

        output_file = file.with_name(f"{file.stem}_template.json")

        print(f"Processing {file.name}")

        try:
            run_notebook(notebook_path, file, output_file)
            print(f"Created {output_file.name}")
        except Exception as e:
            print(f"Failed {file.name}")
            print(e)

    print("Finished.")


if __name__ == "__main__":
    main()