# Cherry Leave Mildew Detector App

The "Cherry Leaf Mildew Detector App" is a sophisticated application engineered for the purpose of discerning the health status of cherry leaves. It excels in its capacity to perform predictions with remarkable precision, leveraging the visual cues present in images of cherry leaves to discern between states of robust health and infection by powdery mildew.

At its core, this application embodies the principles of supervised machine learning, a foundational paradigm within the realm of artificial intelligence. It operates as a single-label, binary classification model, a construct characterized by its profound ability to delineate two distinct categories. In the context of our application, this binary classifier is harnessed to elucidate the underlying state of the cherry leaves under scrutiny, making a pivotal distinction between 'healthy' and 'infected' labels. This predictive capability is the result of a meticulous training process, where the model learns from a rich dataset, ultimately becoming proficient in classifying cherry leaves with exceptional accuracy.

[View Live Project Here](https://cherry-mildew-detection-app-b96ff905e47b.herokuapp.com/)

![title image](https://res.cloudinary.com/dxla1usfm/image/upload/v1698917391/Project%205/umkm3abr54rkxejapmnf.png)

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). 

* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is also concerned about supplying the market with a compromised quality product.

![health cherry leaves Kaggle](https://res.cloudinary.com/dxla1usfm/image/upload/v1699114657/Project%205/healthy_cherry_pusdw2.png)
![unhealthy cherry leaves](https://res.cloudinary.com/dxla1usfm/image/upload/v1699114657/Project%205/powdery_mildew_cherry_leaves_yub8n2.png)

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a serious challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

* We suspect that infected cherry leaves, containing powdery mildew, contrast starkly from non-infected leave specimines.
  * An average image study can help to investigate it.


## The rationale to map the business requirements to the Data Visualisations and ML tasks

* Business Requirment 1: Data Visualization
  * We will display the "mean" and "standard deviation" images for mildewed and healthy cherry leaves.
  * We will display the difference between an average mildewed leaf and an average uninfected leaf.
  * We will display an image montage for either mildewed or uninfected leaves.
* Business Requirement 2: Classification
  * We want to predict if a given leaf is infected, or not, with powdery mildew.
  * We want to build a binary classifier and generate reports.


## ML Business Case

### MildewCherryLeavesCLF

* We want an ML model to predict if a cherry leaf is infected with mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
* Our ideal outcome is to provide the Marianne McGuineys and her team a faster and more reliable diagnostic for the detection of the fungal disease on Farmy & Foods cherry tree crops.
* The model success metrics are
  * Accuracy of 70% or above on the test set.
* The model output is defined as a flag, indicating if the cherry leaf has mildew or not and the associated probability of being infected or not. The botanical staff will do the visual inspection workflow as usual and upload the picture to the App. The prediction is made on the fly (not in batches).
* Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish infected and uninfected cherry leaves. A sample is collected and examined under the microscope. Visual criteria are used to detect fungal infection. It leaves room to produce inaccurate diagnostics due to human error. On top of that, some specific farming facilities with fungal detection equipment need more, trained staff and expertise and are typically understaffed.
* The training data to fit the model come from the National Institutes of Health (NIH) Website. This dataset contains about 26+ thousand images. We have extracted a subset of 5643 images from this dataset and saved it to Kaggle dataset directory for quicker model training. 
  * Train data - target: infected or not; features: all images

## Dashboard Design (Streamlit App User Interface)

### Wireframe

![Streamli App Wirefram](https://res.cloudinary.com/dxla1usfm/image/upload/v1699192463/Project%205/Cherry_Leaves_WireFrame_Image_xz2rte.png)

### Page 1: Project Summary

![Project Summary](https://res.cloudinary.com/dxla1usfm/image/upload/v1699180231/Project%205/project_Summary_yjqfxr.png)

* Quick Project Summary
  * Powdery mildew on cherry leaves is primarily caused by a group of fungi, with one common species being Podosphaera clandestina.
  * Controlling powdery mildew often involves a combination of cultural practices, such as pruning to improve air circulation, and fungicide applications. Selecting cherry varieties with resistance to powdery mildew can also help prevent infection.
  * Cherry powdery mildew typically infects young leaves. The exact reason for this preference is not always clear, but it may be related to the thinner cuticle on older leaves, which can provide some resistance to fungal penetration.
  * According to Penn State University The fungus attacks leaves and twigs, producing symptoms much like powdery mildew on apples. Infected leaves curl upward.
* Project Dataset
  * The available dataset contains 4208 images, divided evenly, between infected and uninfected cherry leaves.
* Addition information:
* Business Requirements
  * The client is interested to have a study to visually differentiate between infected and uninfected cherry leaves.
  * The client is interested in positively identifying whether a particular cherry leaf is infected with mold or not.

### Page 2: Leaf Visualizer

![Leaf Visualizer](https://res.cloudinary.com/dxla1usfm/image/upload/v1699182131/Project%205/Leaf_visualizer_huunw4.png)

* It will answer business requirement 1
  * Checkbox 1 - Difference between average and variability image

![Average Variability](https://res.cloudinary.com/dxla1usfm/image/upload/v1699182131/Project%205/Leaf_visualizer_huunw4.png)

  * Checkbox 2 - Differences between average mildew and average uninfected leaves

![Difference between infected and healthy leaves](https://res.cloudinary.com/dxla1usfm/image/upload/v1699184891/Project%205/difference_between_averagemildew_healthy_leaves_cpotfr.png) 

  * Checkbox 3 - Image Montage

![Healthy Montage](https://res.cloudinary.com/dxla1usfm/image/upload/v1699185108/Project%205/healthy_montage_xo9cjw.png)
![Mildew Montage](https://res.cloudinary.com/dxla1usfm/image/upload/v1699185169/Project%205/powdery_mildew_montage_vifliy.png)


### Page 3: Mildew Detector

![Leaf Mildew Detecotr](https://res.cloudinary.com/dxla1usfm/image/upload/v1699182350/Project%205/leaf_mildew_detector_page_bltrvi.png)
![Healthy Detection](https://res.cloudinary.com/dxla1usfm/image/upload/v1699185936/Project%205/healthy_detection_opjmgb.png)

* Business requirement 2 information - "The client is interested in positively identifying whether a particular cherry leaf is infected with mold or not."
* Link to download a set of mildew-contained and uninfected laaf images for live prediction.
* User Interface with a file uploader widget. The user should upload multiple cherry leaf images. It will display the image and a prediction statement, indicating if the leaf is infected or not with mildew and the probability associated with this statement.
* Table with the image name and prediction results.
* Download button to download table.

### Page 4: Project Hypothesis and Validation

![Project Hypothesis and Validation](https://res.cloudinary.com/dxla1usfm/image/upload/v1699183658/Project%205/Project_hypothesis_and_evaluation_qox4jn.png)

### Page 5: ML Performance Metrics

* Label Frequencies for Train, Validation and Test Sets

![Train, Validation, and Test](https://res.cloudinary.com/dxla1usfm/image/upload/v1699183932/Project%205/performance_metrics_a3xgu4.png)
![Train, Validation, and Test](https://res.cloudinary.com/dxla1usfm/image/upload/v1699183933/Project%205/performance_metrics2_pehxbq.png)

* Model History - Accuracy and Losses

![Model History](https://res.cloudinary.com/dxla1usfm/image/upload/v1699183933/Project%205/performance_metrics3_htmasz.png)

* Model evaluation result

![Model Evaluation Result](https://res.cloudinary.com/dxla1usfm/image/upload/v1699183934/Project%205/performance_metrics4_glfoho.png)

## Deployment

### Heroku

* The App live link is: <https://cherry-mildew-detection-app-b96ff905e47b.herokuapp.com/>
* The project was deployed to Heroku using the following steps:

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

# Technologies Utilized

### Languages

Python

### Frameworks and Other Technologies

* **Git:** - Git was used for version control by utilizing the CodeAnywhere virtual environment to commit to Git and Push to GitHub.

* **GitHub:** GitHub is used as the remote repository file hosting.

* **Balsamiq:** Balsamiq was used to create the wireframes for this project.

* **Heroku:** Hosting provider used to deploy this site project.

* **CodeAnywhere:** Virtual programming environment used to interact with the codebase.

## Main Data Analysis and Machine Learning Libraries

* numpy==1.19.2 - NumPy provides an efficient interface for handling numerical arrays and matrices in Python, essential for performing high-level mathematical operations that are ubiquitous in machine learning algorithms.
* pandas==1.1.2 - Pandas is instrumental in data manipulation and analysis, offering data structures and operations for manipulating numerical tables and time series which are foundational in pre-processing for machine learning.
* matplotlib==3.3.1 - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python, serving as a pivotal tool for data exploration and results presentation in machine learning.
* seaborn==0.11.0 - Seaborn extends matplotlib's functionality, providing a high-level interface for drawing attractive and informative statistical graphics, which is crucial for data interpretation in machine learning.
* plotly==4.12.0 - Plotly specializes in creating interactive, web-based graphs and dashboards, enhancing the interpretability and interactivity of machine learning model visualizations.
* streamlit==0.85.0 - Streamlit streamlines the creation of web apps for machine learning projects, enabling rapid sharing and prototyping without the overhead of complex web development.
* scikit-learn==0.24.2 - Scikit-learn is a versatile tool that offers a multitude of algorithms and data processing techniques, integral for implementing standard machine learning tasks such as classification, regression, and clustering.
* tensorflow-cpu==2.6.0 - TensorFlow is a robust framework for large-scale machine learning and neural networks, optimized for performance and scalability on CPUs for computational tasks.
* keras==2.6.0 - Keras serves as a user-friendly interface to TensorFlow, simplifying the construction and training of neural networks and accelerating the experimental cycle.
* protobuf==3.20 - Protocol Buffers is Google's mechanism for serializing structured data, crucial for TensorFlow's efficient storage and exchange of model configurations and parameters.
* altair<5 - Altair offers a declarative statistical visualization library designed for rendering concise and structured visualizations, which are integral to the analytical phase of machine learning workflows.

## Bugs

* Model and Evaluation (eval_model.py):
  * During the process of creating the Model and Evaluation Jupyter notebook  
    the problem of model.h5 size came into play. It was decided to host the .H5
    file on a remote file storage and, as such, a function called
    load_and_compile_model. Originally a script at the head of code was created
    that auto-generated a .py file to the Jupyter Notebooks directory. Due to
    limitations in synchronicity between Jupyter Notebooks and Streamlit, the
    newly-created .py file was not being recognized within the app_pages
    directory, despite several attemps at code configuration changes. Due
    to time constraints it was decided to manually create the eval_mdoel.py file
    within the root directory and then the codebase worked as expected. In
    a future iteration, investigations will be made to determine the exact
    code/module library necessary to enable the function to auto-generate the
    .py file in the root directory.
* Heroku Stack
  * When I initially created the app on Heroku, the stack by default does not support the Python version that I was using, so I had to change the stack of my project from 22 to 20.

## Credits

* Background info:
  * <https://extension.psu.edu/powdery-mildew-of-cherry-and-plum-in-home-fruit-plantings>
* os.path.join() method:
  * <https://www.geeksforgeeks.org/python-os-path-join-method/>
* PIL image resize:
  * <https://www.askpython.com/python-modules/resize-image-pillow-pil>
  * <https://stackoverflow.com/questions/76616042/attributeerror-module-pil-image-has-no-attribute-antialias>
* Slug size management:
  * <https://stackoverflow.com/questions/68464527/heroku-compiled-slug-size-is-too-large-python>
* Main Image:
  * <https://ui.dev/amiresponsiv>
* Choose Activation Function:
  * <https://machinelearningmastery.com/choose-an-activation-function-for-deep-learning/>
* Image hosting:
  * https://console.cloudinary.com/
* H5 model storage:
  * <https://drive.google.com/uc?id=1jMOU1eHCgkZsEHF5_VBiPm916xVl2gqn>
* Writefile:
  * <https://douglatornell.github.io/2014-09-25-ubc/novice/python/06-simple_cmdline.html#:~:text=%25%25writefile%20lets%20you%20output,a%20program%20was%20run%20with.>
* The overall inspiration and structure of this project was adapted from the Malaria
  Detector App, originally done by Code Institute:
  * <https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/07a3964f7a72407ea3e073542a2955bd/29ae4b4c67ed45a8a97bb9f4dcfa714b/>
* Wireframe:
  * <https://balsamiq.com/wireframes/?gad=1&gclid=Cj0KCQjw-pyqBhDmARIsAKd9XIMN7IR9EAmH5WvCZzFNeatFrRQsrA_uAdcwvghTC6vIch73J1yp7k4aAjt5EALw_wcB>
* CodeAnywhere
  * <https://app.codeanywhere.com/>

## Acknowledgements

* I'd like to thank my mentor **Precious Ijege**, **Neil_ci** (community leader), community members, **family** and friends who gave me their support during this process. It was greatly appreciated.
