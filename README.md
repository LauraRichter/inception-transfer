# inception-transfer

Examples around the topic of transfer learning using Tensorflow, by retraining the Inception model. [Inception-v3](https://arxiv.org/abs/1512.00567) is a CNN image classification model that was trained using [ImageNet](http://image-net.org/) data, for the Large Visual Recognition Challenge. 

* Example 1: **Transfer learning** - Transfer learning from the Inception model
* Example 2: **Building a CNN** - Building an Inception style model from scratch
* Example 3: **What are these convolutions you speak of?** - Playing with convolutions

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
