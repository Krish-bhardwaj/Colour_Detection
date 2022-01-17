import argparse
import cv2
import pandas as pd

# argparse is use to take the value through command line
ap = argparse.ArgumentParser(description="Image Color Detection")
ap.add_argument('-i', '--image', required=True, help="Image Path")

# vars is a function which returns value in dictionary
args = vars(ap.parse_args())
# print(args)
img_path = args['image']

# print(img_path)
# Reading image with opencv
img = cv2.imread(img_path)

# Global varibale decelaration
clicked = False
r = g = b = xpos = ypos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("colors.csv", names=index, header=None)
# print(csv.head)

# Function to get x,y coordinates of mouse double click


def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r, g, b, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        #print(r, g, b)

# Function to calculate minimum distance from all colors and get the most matching color


def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G -
                                                int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))

        if(d <= minimum):
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


cv2.namedWindow('image')
# Mousecallback function requires user defined function for call back
# Note:- Function created for mousecallback requires 5 parameters so we have defined draw_function with 5 params
cv2.setMouseCallback('image', draw_function)


while(1):
    # TO display the image continuosly unless ESC key is pressed
    cv2.imshow("image", img)
    if clicked:

        # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = getColorName(r, g, b) + ' R=' + str(r) + \
            ' G=' + str(g) + ' B=' + str(b)

        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8,
                    (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if(r+g+b >= 600):
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
