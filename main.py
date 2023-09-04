import cv2
import fitz
import os

class Coordinate:
    def __init__(self, x, y, get_label):
        self.x = x
        self.y = y
        self.get_label = get_label
        self.label = self.set_label()

    def set_label(self):
        if self.get_label:
            print('Enter a label for this coordinate:')
            return input('> ')
        print('Coordinate stored.')
        return None
        
    def print_coordinate(self):
        print(f'({self.x}, {self.y})', end = '')
        if self.label is not None: 
            print(f' : {self.label}')
        else: 
            print()


def get_file_path():
    print('Enter a pdf file path to determine coordinates for:')
    file_path = input('> ')
    # file_path may be surrounded by "", which must be removed.
    if file_path[0] == file_path[-1] == '\"':
        file_path = file_path[1:][:-1]
    return file_path


def get_adjustment():
    print('Enter an integer value to be added to each coordinate:')
    adjustment = input('> ')
    try:
        adjustment = int(adjustment)
    except ValueError:
        adjustment = 0
    finally:
        return adjustment


def collect_coordinates(img_file_name, coordinates, adjustment, get_label):
    os.system('cls')
    print('Your file has been opened.')
    if get_label: print('You will be prompted to label each coordinate.')
    print('\tLEFT CLICK:   collects coordinate\n',
          '\tRIGHT CLICK:  collects coordinate but keept previous y value\n',
          '\tBACKTICK (`): closes the file and prints coordinates')
    # Open image and store coordinates until backtick is pressed.
    img = cv2.imread(img_file_name, 1)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click, 
                         param = (coordinates, adjustment, get_label))
    while True:
        key = cv2.waitKey(0)
        if key == ord('`'): 
            cv2.destroyAllWindows() 
            break


def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        param[0].append(Coordinate(x + param[1], y + param[1], param[2]))

    if event==cv2.EVENT_RBUTTONDOWN:
        param[0].append(Coordinate(x + param[1], param[0][-1].y, param[2]))


def print_coordinates(coordinates):
    os.system('cls')
    print('Collected coordinates:')
    for coordinate in coordinates:
        coordinate.print_coordinate()


pdf_file_path = get_file_path()
img_file_name = 'Coordinate_Finder_Temp.png'

try:
    # Convert pdf to a temporary image file.
    pdf = fitz.open(pdf_file_path)
    pdf_to_image = pdf[0].get_pixmap()
    pdf_to_image.save(img_file_name)
except Exception as ex:
    print(f'ERROR:\n{ex}\nExiting program.')
else:
    adjustment = get_adjustment()
    coordinates = []
    get_label = False

    print('Would you like to label each coordinate? (y/n):')
    if input('> ') == 'y': 
        get_label = True

    collect_coordinates(img_file_name, coordinates, adjustment, get_label)
    os.remove(img_file_name)
    print_coordinates(coordinates)
