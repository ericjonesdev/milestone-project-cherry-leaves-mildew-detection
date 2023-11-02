# Cherry Leave Mildew Detector App

The "Powdery Mildew Detector" is a sophisticated application engineered for the purpose of discerning the health status of cherry leaves. It excels in its capacity to perform predictions with remarkable precision, leveraging the visual cues present in images of cherry leaves to discern between states of robust health and infection by powdery mildew.

At its core, this application embodies the principles of supervised machine learning, a foundational paradigm within the realm of artificial intelligence. It operates as a single-label, binary classification model, a construct characterized by its profound ability to delineate two distinct categories. In the context of our application, this binary classifier is harnessed to elucidate the underlying state of the cherry leaves under scrutiny, making a pivotal distinction between 'healthy' and 'infected' labels. This predictive capability is the result of a meticulous training process, where the model learns from a rich dataset, ultimately becoming proficient in classifying cherry leaves with exceptional accuracy.

[View Live Project Here](https://cherry-mildew-detection-app-b96ff905e47b.herokuapp.com/)

![title image](https://res.cloudinary.com/dxla1usfm/image/upload/v1698917391/Project%205/umkm3abr54rkxejapmnf.png)

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). 

* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is also concerned about supplying the market with a compromised quality product.

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

### Page 1: Project Summary

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

* It will answer business requirement 1
  * Checkbox 1 - Difference between average and variability image
  * Checkbox 2 - Differences between average mildew and average uninfected leaves
  * Checkbox 3 - Image Montage

### Page 3: Mildew Detector

* Business requirement 2 information - "The client is interested in positively identifying whether a particular cherry leaf is infected with mold or not."
* Link to download a set of mildew-contained and uninfected laaf images for live prediction.
* User Interface with a file uploader widget. The user should upload multiple cherry leaf images. It will display the image and a prediction statement, indicating if the leaf is infected or not with mildew and the probability associated with this statement.
* Table with the image name and prediction results.
* Download button to download table.

### Page 4: Project Hypothesis and Validation

### Page 5: ML Performance Metrics

* Label Frequencies for Train, Validation and Test Sets
* Model History - Accuracy and Losses
* Model evaluation result

## Unfixed Bugs

* TBD

## Deployment

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 

## Main Data Analysis and Machine Learning Libraries

* numpy==1.19.2
* pandas==1.1.2
* matplotlib==3.3.1
* seaborn==0.11.0
* plotly==4.12.0
* streamlit==0.85.0
* scikit-learn==0.24.2
* tensorflow-cpu==2.6.0
* keras==2.6.0
* protobuf==3.20
* altair<5

## Credits

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- TBD

### Media

- TBD

## Acknowledgements (optional)

* TBD
