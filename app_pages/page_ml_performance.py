import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")

    
    st.info(

        f"* Train - healthy: 1472 images\n"
        f"* Train - powdery_mildew: 1472 images\n"
        f"* Validation - healthy: 210 images\n"
        f"* Validation - powdery_mildew: 210 images\n"
        f"* Test - healthy: 422 images\n"
        f"* Test - powdery_mildew: 422 images\n"
    )
    st.write("---")

    st.write("### Model History")
    st.info(
        f"The graph below provide a visual representation of the learning cycle for the ML model.\n"
        f" The plot graphs show the loss and accuracy plots as a part of the training process.\n\n"
        f" From these graphs it is apparent that it is a normal learning curve. The model is neither \n"
        f" overfitting or underfitting.\n"
    )

    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

    st.success(
        f"**The general accuracy of ML model is 99% !!** "
    )
    load_test_evaluation(version)
    
    