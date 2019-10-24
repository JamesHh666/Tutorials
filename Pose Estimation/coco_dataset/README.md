Here are something you might need to use [COCO](http://cocodataset.org/#home) with python.

# Use [coco API](https://github.com/cocodataset/cocoapi)
Install pycocotools:
1. ubuntu:
```
pip install pycocotools
```
2. window:
```
pip3 install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"
```
# Deal with `.json`
The annotations from coco `.json` is in one line, which is hard to read:broken_heart:. You can use the code below to make it more readable (but the size of the output file can be much larger)
``` python
import json

# The path to .json files
path = './'
# The file to be pretty printed
file_name = 'person_keypoints_val2017.json'

json1_file = open(path + file_name)
json1_str = json1_file.read()
data = json.loads(json1_str)

with open(file_name[:-5] + '_prettyPrinted.json', 'w') as fp:
    json.dump(data, fp, indent=4)  # , sort_keys=True)
```
