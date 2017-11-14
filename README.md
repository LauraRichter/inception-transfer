# inception-transfer
Transfer learning using Tensorflow

## Preparation

### Install requirements

> pip3 install -r requirements.txt

### Images

You will need image data sets, containing 200+ images for each category you would like to classify.

Start with a directory named "images", containing sub-directories named after your categories, filled with images of that class. For example:

> images/nelson_mandela

> images/thabo_mbeki

> images/jacob_zuma
  
You can optionally create these data sets by downloading google image search results, using [download-google-image-results.py](download-google-image-results.py) as follows:

> python3 download-google-image-results.py 'nelson mandela' --number 250 --max-height 300

> python3 download-google-image-results.py 'thabo mbeki' --number 250 --max-height 300

> python3 download-google-image-results.py 'jacob zuma' --number 250 --max-height 300

Take a look through the directories and remove images that aren't approptiate for training - pictures that aren't actually of the desired target class, or have objects of more than one of the target classes in them.

