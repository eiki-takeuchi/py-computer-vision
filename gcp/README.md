# GCP Vision AI

### Image Annotation

Image annotation is to put labels to the given image. It is also called image classification. 
Google Cloud Vision provides image annotation API. 
The `image_annotation.py` is a wrapper command-line interface to process image annotation. 

```
# Image annotation basic usage. 
$ python image_annotation.py --image-uri [image uri]

# Display barplot visualization.
$ python image_annotation.py --image-uri [image uri] --graph

# Extract specified number of top confidence data. 
$ python image_annotation.py --image-uri [image uri] --top-confidence 10
```
