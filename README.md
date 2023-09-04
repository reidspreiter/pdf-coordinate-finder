# PDF Coordinate Finder

## _Introduction_
This program allows the user to view the coordinates of any point on any pdf document. 

My motivation for this program arose during the development of leasing-helper, which uses the PyFPDF library to populate pdfs with text and shapes. The PyFPDF library requires specific x and y coordinates to write to a document. I quickly became frustrated with the daunting task of finding 172 different coordinates on a single document. After researching existing tools online, I realized I needed to develop something more flexible to fit my needs.

## _Advantages_
This program has specific advantages over preexisting tools.
pdf-coordinate-finder can:
- Store each coordinate in one place
- Label each coordinate
- Adjust each coordinate by a specific value
- Align the y values of multiple coordinates

While this list comprises the current functionality of pdf-coordinate-finder, I know there is room for improvement when I work with pdfs again.
In the future, pdf-coordinate-finder could:
- Be implemented with a GUI
- Convert x and y values to different units
- Offer streamlined coordinate alignment
- Gather similar coordinates with less user input
- Label coordinates automatically

## _Usage_
**Coordinate Units**

This program stores coordinate values in point units of length (pt).

**File Path**

Once the program starts, the user is prompted for the file path of the pdf file they wish to edit. The pdf is then converted to an image via the PyMUPDF(fitz) library so it can be accessed by OpenCV-Python(cv2).

**Adjustment**

The user is asked to input an adjustment value to add to each coordinate. If the user enters a posotive integer, all x and y coordinates will be increased by that value. If a negative integer is entered, the coordinates will decrease. If zero is entered, the coordinates will not be adjusted. 

A universal adjustment value is important for specific scenarios like drawing shapes. When a PyFPDF circle is drawn at a specific location, it's center does not align with the location. Consequently, the user has to subtract the circle's radius from both the x and y coordinates to actually center the circle on a specific location. If 100 circles with a radius of 5 need to be drawn at 100 different locations, setting the adjustment value to -5 ensures each coordinate will result in a centered circle.  

**Labeling**

If more than a few coordinates are selected at a time, it can be difficult to remember the location they correspond to. This program gives the user the option to label each coordinate if they desire. 

**Collecting Coordinates**

During this section of pdf-coordinate-finder, an external window is opened via OpenCV-Python(cv2). The user has three control options:
- _Left Click_ - Stores the coordinate of the clicked location
- _Right Click_ - Stores the coordinate of the clicked location, but retains the previous coordinate's y value. This control allows the user to quickly select coordinates for locations aligned horizontally.
- _Backtick(`)_ - Closes the external window and terminates the coordinate collecting process

If the user chose to not label each coordinate, 'Coordinate stored.' will be output to the terminal after each click for visual conformation purposes.

If the user chose to label each coordinate, they will be prompted to enter a label after each click. If a label is not entered after a click, all subsequent clicks will be ignored until a label is entered.

**Printing Coordinates**

All collected coordinates and labels are printed before the program terminates. This allows the coordinates to be quickly transfered to other programs.

## _What I Learned_
This program taught me that writing code can make writing other code much less frustrating. I'm looking forward to developing more smaller projects to assist me with larger projects in the future. 
