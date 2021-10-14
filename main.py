from scipy.spatial import distance as dist
import pytesseract as Ptec
from selenium import webdriver as wb
import cv2 as cv
import numpy as np
import imutils as imu
import argparse as ag
import time

def ScrollPageFF():#we need to use this to move the snipping tool through long pages to collect data in bulk loads ,, used with Firefox
    browse = wb.Firefox()
    browse.get()
    browse.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    browse.close()
    print()

def ScrollPageGC():  # we need to use this to move the snipping tool through long pages to collect data in bulk loads,, used with Chrome
    browse = wb.Chrome()
    browse.get()
    browse.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    browse.close()
    print()
def ScrollPageIE():  # we need to use this to move the snipping tool through long pages to collect data in bulk loads,, used with Internet Explorer
    browse = wb.Ie()
    browse.get()
    browse.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    browse.close()
    print()

def ScrollPageEdge():  # we need to use this to move the snipping tool through long pages to collect data in bulk loads,, used with Edge
    browse = wb.Edge()
    browse.get()
    browse.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    browse.close()
    print()

def ScrollPageSafari():  # we need to use this to move the snipping tool through long pages to collect data in bulk loads,, used with safari
    browse = wb.Safari()
    browse.get()
    browse.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    browse.close()
    print()
def ScrollPageOP():  # we need to use this to move the snipping tool through long pages to collect data in bulk loads,, used with Opera
    browse = wb.Opera()
    browse.get()
    browse.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    browse.close()
    print()
def autologon():#log into the agresource automatically if it is not logged in
    print()



def CalImg():#we need to use this function to collect data from the right side and centre of the page but not the left
    print()





def snipIMG():#to actually capture and save the image we use this function
    print()





def PullText(pic):
    Ptec.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'#link to the tesseract program
    print(Ptec.image_to_string(pic))#parse image into string
#cv.destroyAllWindows()





def destroyImg(pic): #this will be used to clear the cache by destroying the image once it has been used
    print()





def sendRep():# we will send the text that we have collected via email to the agresource group
    print()




PullText('Capture1.PNG')