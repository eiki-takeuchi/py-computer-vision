#!/usr/bin/env python
# coding: utf-8


from google.cloud import vision
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from google.cloud import storage
import argparse


def vision_client():
    """Create vision client."""
    return vision.ImageAnnotatorClient()

    
def annotate_image(vision_client, image_uri, log=False):
    """
    Image annotation. 
    
    Arguments
    ---------
    vision_client : GCP vision client. 
    image_uri     : str
        Call vision API.
        Image resource can be specified only in 3 ways. 
        1. Google Storage
        2. base64 data.
        3. HTTP uri. 
    """

    response = vision_client.annotate_image({
      'image': {
          'source': {
              'image_uri': image_uri
          }
      }
    })
    
    if log:
        print("response : ", response)
        
    return response


def visualization(response):

    # Preprocessing for visualization. 
    descriptions = []
    scores = []
    for label in response.label_annotations:
        descriptions.append(label.description)
        scores.append(label.score)

    dic = {"description": descriptions, "score": scores}

    # Visualization with seaborn. 
    sns.set(style="whitegrid")
    tips = sns.load_dataset("tips")
    sns.barplot(y="description", x="score", data=dic)
    plt.show()
    

def extract_top_confidences(response, num=1, display=True):
    """Extract top confident annotations.
    
    Arguments
    ---------
    response : google.cloud.vision_v1.types.AnnotateImageResponse
    num      : int
    
    Return
    ------
    top_annotations : tuple list (description, confidence)
    """
    print(type(response))
    top_annotations = []
    for label in response.label_annotations[:num]:
        t = (label.description, label.score)
        top_annotations.append(t)
        
    index = 1;
    for description, confidence in top_annotations:
        print("Index        : ", index)
        print("Descriptions : ", description)
        print("Confidence   : ", round(confidence * 100, 2), "%")
        print("---------------")
        index += 1
        
    return top_annotations


if __name__ == "__main__":
    description="""
        Image annotation command line interface.
        
        Example
        -------
        $ python image_annotation.py --image-uri [image uri]
        
        # Display barplot.
        $ python image_annotation.py --image-uri [image uri] --graph
        
        # Extract specified number of top confidence data. 
        $ python image_annotation.py --image-uri [image uri] --top-confidence 10
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--image-uri", type=str, help="Put image URI.")
    parser.add_argument("--top-confidence", type=int, default=1, help="Number of top confidence data to display.")
    parser.add_argument("--graph", action="store_const", const=True, help="Display barplot.")

    # Set parameters.
    args = parser.parse_args()
    image_uri = args.image_uri
    top_confidence = args.top_confidence

    # Call API.
    client = vision_client()    
    response = annotate_image(vision_client=client, image_uri=image_uri)

    # Extract top confidecne data.
    extract_top_confidences(response, num=top_confidence)

    # Display barplot graph.
    if args.graph:
        visualization(response)



