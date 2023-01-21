import cv2
import numpy as np
import csv
import os
import sys

def process_images(filenames):
    for filename in filenames:
        img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
        Lchannel = img[:,:,1]
        mean_brightness = np.mean(Lchannel)
        name = os.path.basename(filename)
        data = [name, mean_brightness]
        # with open('output.csv', 'a') as file:
        #     writer = csv.writer(file)
        #     writer.writerow(data)
        print(data)

print(sys.argv[1:])
process_images(sys.argv[1:])
