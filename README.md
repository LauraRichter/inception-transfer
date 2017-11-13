# inception-transfer
Transfer learning using Tensorflow

## Preparation

### Images

You will need image data sets, containing 200+ images for each category you would like to classify.

Start with a directory named "images", containing sub-directories named after your categories, filled with images of that class. For example:
> images/pandas
> images/penguins
> images/people
  
You can optionally create these data sets by downloading google image search results, using [download-google-image-results.py](download-google-image-results.py) as follows:

> python3 download-google-image-results.py 'african penguin' --number 300
