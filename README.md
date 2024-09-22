# PDF Coordinate Finder

This script allows the user to find, list, and label the coordinates of any point on a pdf document.

## Installation

Clone the pdf-coordinate-finder [repository](https://github.com/reidspreiter/pdf-coordinate-finder):

```
git clone https://github.com/reidspreiter/pdf-coordinate-finder.git
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

Coordinate values are stored in point units of length (pt).

Provide the script with a PDF file's path. View the [Options](#options) section for additional functionality such as labeling.

```
python main.py [<options>] <path to PDF>
```

The script opens the PDF in a new window. The following controls will assist with collecting coordinates:

- **Left click**: collect coordinate at the current mouse position
- **X**: collect, but keep previous coordinate's x value
- **Y**: collect, but keep previous coordinate's y value
- **>**: navigate to next page
- **<**: navigate to previous page
- **ESC**: close window and output coordinates

By default, the collected coordinates are presented in Python dictionary format for convenient transfer to Python projects.

## Options

**-l**, **--label**

When this option is specified, the user is prompted to label each coordinate, and the labels are included in the final coordinate results.

**-a** \<int>, **--adjustment** \<int>

Increase or decrease coordinate x and y values by the provided amount.

A universal adjustment value is important for scenarios like drawing shapes. For example, PyFPDF circles are anchored to the top left, and coordinates must subtract the circle's radius to center the circle on the desired point.

**-o** \<path>, **--output** \<path>

Output coordinate results to a specific file instead of stdout.

**-j**, **--json**

Format coordinate results as JSON instead of Python.

**-n**, **--no_pretty_print**

Display coordinate results in a single line without indentation or extra spacing.
