# Colour Detection
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)


In this **Color Detection Python Project**, we can automatically get the name of the color by clicking on them. 

## Approach to solve this problem 
1. Firstly we have dataset that contains the color name and its values
2. After selecting a perticular segment we calculate the distance from each color and find the shortest one.

# About Dataset
Colors are made up of 3 primary colors **red** , **green** , and **blue** . 

In computers, we define each color value within a range of 0 to 255. therefore we can define a colour in 256*256*256 = 16,581,375 ways !

There are approximately 16.5 million different ways to represent a color. Our task is  to map each color’s values with their corresponding names in the dataset . 
But we don’t need to map all the values. We will be using a dataset that contains RGB values with their corresponding names.

## Colors Dataset
The colors.csv file includes 865 color names along with their RGB and hex values.

# Prerequisites
OpenCV, Pandas, and numpy are the Python packages that are necessary for this project in Python. 
To install them, simply run this pip command in your terminal:

```
pip install opencv-python 
pip install numpy 
pip install pandas
```

# The project contains :
- Color_detection.py – main source code of our project.
- Colors.csv – a file that contains our dataset.

# Run Python File

```
python code.py -i 'add your image path here'
```

# Demo & documention ( in progress )

# Future scope 
1. make an API
2. Embede in a big project !

### Author : Krish Bhardwaj
