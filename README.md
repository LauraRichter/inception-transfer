# inception-transfer
Transfer learning using Tensorflow, retraining the Inception model. [Inception-v3](https://arxiv.org/abs/1512.00567) is a CNN image classification model that was trained using [ImageNet](http://image-net.org/) data in 2012, for the Large Visual Recognition Challenge. 

## 1. Preparation

### Install requirements

```
> pip3 install -r requirements.txt
```

### Clone the full Tensorflow repo

Clone the full Tensorflow repo so we can use the example scripts, which aren't avalable in the pip installed version.

```
> git clone https://github.com/tensorflow/tensorflow
```

### Images

You will need image data sets, containing 200+ images for each category you would like to classify.

Start with a directory named "images", containing sub-directories named after your categories, filled with images of that class. For example:

> images/nelson_mandela

> images/thabo_mbeki

> images/jacob_zuma
  
You can optionally create these data sets by downloading google image search results, either by:

(a) using a plugin like the [Fatkun chrome extension](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en), or

(b) using the [download-google-image-results.py](download-google-image-results.py) script supplied here as follows:

```
> python3 download-google-image-results.py 'nelson mandela' --number 250 --max-height 300
> python3 download-google-image-results.py 'thabo mbeki' --number 250 --max-height 300
> python3 download-google-image-results.py 'jacob zuma' --number 250 --max-height 300
```

If you use the automatic google image download scripts, take a look through the directories and remove images that aren't approptiate for training - pictures that aren't actually of the desired target class, or have objects of more than one of the target classes in them.

---

## 2. Retrain Inception

```
> python tensorflow/tensorflow/examples/image_retraining/retrain.py \
    --bottleneck_dir ./outout/bottlenecks \
    --how_many_training_steps 5000 \
    --model_dir ./output/inception \
    --output_graph ./output/retrained_graph.pb \
    --output_labels ./output/retrained_labels.txt \
    --image_dir ./images/
```

## 3. Use models to label images

Use the model we just trained to label an image that wasn't in the original training set:

```
> python tensorflow/tensorflow/examples/label_image/label_image.py \
    --graph output/retrained_graph.pb \
    --labels output/retrained_labels.txt \
    --image <some_image_to_label> \
    --input_layer Mul \
    --input_height 299 \
    --input_width 299 \
    --output_layer "final_result"
```

And compare this with the output the original Inception model would have given us for this same image:

```
> python tensorflow/tensorflow/examples/label_image/label_image.py \
    --graph output/inception/classify_image_graph_def.pb \
    --labels output/inception/imagenet_synset_to_human_label_map.txt \
    --image <some_image_to_label> \
    --input_layer Mul \
    --input_height 299 \
    --input_width 299 \
    --output_layer "softmax"
```







