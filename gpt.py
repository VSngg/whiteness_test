import PySimpleGUI as sg
import cv2
import numpy as np
import csv
import os

def process_images(filenames):
    for filename in filenames:
        img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
        Lchannel = img[:,:,1]
        mean_brightness = np.mean(Lchannel)
        name = os.path.basename(filename)
        data = [name, mean_brightness]
        with open('output.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)

layout = [[sg.Text('Select image(s) to process')],
          [sg.FilesBrowse()],
          [sg.Button('Submit'), sg.Exit()]]

window = sg.Window('Image Processing', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event == 'Submit':
        filenames = values['Browse'].split(';')
        process_images(filenames)
        sg.popup('готово!')

window.close()
