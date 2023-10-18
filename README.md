# Cherry Leave Mildew Detector App

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). 

* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

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

  


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

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
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.
