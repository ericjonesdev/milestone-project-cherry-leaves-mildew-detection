import sys
sys.path.append('/workspaces/milestone-project-cherry-leaves-mildew-detection/')

from eval_model import load_and_compile_model

#from eval_model import load_and_compile_model
from pkg_resources import parse_version
from src.data_management import load_pkl_file
from PIL import Image
from tensorflow.keras.models import load_model
import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st



def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'infected': 0, 'healthy': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    width = int(image_shape[1])
    height = int(image_shape[0])
    img_resized = img.resize((width, height), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


# model URL
model_url = 'https://drive.google.com/uc?id=1jMOU1eHCgkZsEHF5_VBiPm916xVl2gqn'

# Load and compile the model using the imported function
model = load_and_compile_model(model_url)


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'infected': 1, 'healthy': 0}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.write(
        f"The predictive analysis indicates the sample leaf is "
        f"**{pred_class.lower()}**.")

    return pred_proba, pred_class
