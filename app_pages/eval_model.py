import requests
from keras.models import load_model
from io import BytesIO
from tempfile import NamedTemporaryFile

def load_and_compile_model (model_url):
    """
    Load and compile the Keras model from a hosted URL.
    """
    
    # model url
    
    model_url = 'https://drive.google.com/uc?id=1jMOU1eHCgkZsEHF5_VBiPm916xVl2gqn'
    
    # Download the model file from the URL
    response = requests.get(model_url)
    
    # Create a temporary file to save the model
    with NamedTemporaryFile(delete=False, suffix=".h5") as tmp_file:
        tmp_file.write(response.content)
        tmp_file_path = tmp_file.name
    
    # Load the Keras model from the temporary file
    model = load_model(tmp_file_path, compile=False)
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    return model 
