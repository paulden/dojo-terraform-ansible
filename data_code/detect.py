from pydarknet import Detector, Image
from collections import defaultdict

import cv2
import glob
import json
import os
import sys

TEXT_COLOR = (255, 255, 0)
BOX_COLOR = (255, 0, 0)
BOX_THICKNESS = 2

if len(sys.argv) == 1:
    list_of_files = glob.glob('images/*')
    img_path = max(list_of_files, key=os.path.getctime)
else:
    img_path = sys.argv[1]

img_name = img_path.split('/')[-1].split('.')[0]

img_to_analyze = cv2.imread(img_path)
img_to_analyze_darknet = Image(img_to_analyze)

net = Detector(bytes('cfg/yolov3.cfg', encoding='utf-8'),
               bytes('weights/yolov3.weights', encoding='utf-8'),
               0,
               bytes('cfg/coco.data', encoding='utf-8'))

darknet_detection_results = net.detect(img_to_analyze_darknet)
objects_detected = defaultdict(int)

for cat, score, bounds in darknet_detection_results:
    objects_detected[str(cat.decode('utf-8'))] += 1

    x, y, w, h = bounds
    cv2.rectangle(img_to_analyze,
                  (int(x - w / 2), int(y - h / 2)),
                  (int(x + w / 2), int(y + h / 2)),
                  BOX_COLOR,
                  thickness=BOX_THICKNESS)
    cv2.putText(img_to_analyze, str(cat.decode('utf-8')), (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 1, TEXT_COLOR)

with open('result_reports/{}.json'.format(img_name), 'wb') as output_json:
    formatted_output_dict = json.dumps(objects_detected).encode('utf-8')
    output_json.write(formatted_output_dict)

cv2.imwrite('result_images/{}.jpg'.format(img_name), img_to_analyze)
