# Powdery Mildew Detection in Cherry Leaves

Live Project can be accessed here - <https://cherry-leaf-detect-mildew-cdc5a7b829c7.herokuapp.com/>

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* I expect that leaves affect by powdery mildew would be easily identifiable from an image based on white patches
    * I can try to validate this with an average image study as well as visual comparison of montages


## The rationale to map the business requirements to the Data Visualisations and ML tasks

### User Stories
* Business Requirement 1: Data Visualization
      * As the client, I can average images for healthy and mildew affected leaves, in order to try to pick out identifiable characteristics
      * As the client, I can view the difference between the average images, in order to try to pick out identifiable characteristics
      * As the client, I can choose to see a montage of either healthy or powdery mildew leaves, in order to review them against my expectations

* Business Requirement 2: Classification
      * As the client I can upload an image(s) to predict if a leaf is healthy or affected by powdery mildew
      * As the client I can generate and download csv reports based on batches of images, in order to quickly and easily review thmm

## ML Business Case
* I want an ML model to predict if a leave is affected by powdery mildew or not, based on images provided the client. It is a 2-class, single label, supervised classfication model
* Ideally, this will redice the time and cost of identifying and treating diseased trees and maintain crop quality
* Success metric is >90% accutacy on the test set
* The current process requires an employee to spend around 30 minutes inspecting each tree and applying treatment if the tree is diseased. The ML model could drastically speed up the identification process
* The data is provided by the client
  * Train data - target: powder mildew or not; features: all images


## Dashboard Design

### Page 1: Quick Project Summary

* Quick project summary
  * General Information
    * Powdery mildew is a fungal problem that affects cherry trees and the cherries they produce.
    * The leaves need to be carefully inspected and can take an employee around 30 minutes.
  * Project Dataset
    * The available dataset contains +4 thousand images taken from the client's crop fields
  * Link to additional information
  * Business requirements
    * The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
    * The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: Leaves Visualizer

* It will answer business requirement 1
  * Checkbox 1 - Difference between average and variability image
  * Checkbox 2 - Differences between average powdery mildew and average healthy leaves
  * Checkbox 3 - Image Montage

### Page 3: Mildew Detection

* Business requirement 2 information - "The client is interested in telling whether a given leaf contains powdery mildew or not."
* Link to download images for live prediction.
* User Interface with a file uploader widget. The user should upload multiple cherry leaf images. It will display the image and a prediction statement, indicating if the leaf is affected bymildew or not and the probability associated with this statement.
* Table with the image name and prediction results.
* Download button to download table.

### Page 4: Project Hypothesis

* The affected leaves have clear white markings on them, however the average images and difference did not provide actionable visibilty. Perhaps this could be better if images could be transformed to have leaves in the same position and orientation

### Page 5: ML Performance Metrics

* Label Frequencies for Train, Validation and Test Sets:
* Model History - Accuracy and Losses
* Model evaluation result

## Unfixed Bugs
* I had problems with Makrdown cells in the jupyter notebooks that when processed would not match even the text in those cells at times - this resulted in completing and saving these multiple times
* I had an issue where the v1 of the model had not saved properly and had to resave it

## Deployment
### Heroku

* The App live link is: <https://cherry-leaf-detect-mildew-cdc5a7b829c7.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries

* Numpy: It is an open-source, python library used for working with arrays. NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines.
* Pandas: It is an open-source, python package used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.
* Matplotlib: It is a cross-platform, data visualization and graphical plotting library for python.
* Seaborn: It is Python data visualization library based on Matplotlib. It will be used to visualize random distributions.
* Plotly: It is an interactive, open-soource, and browser-based gra6. Tensorflow: It is an open-sourec machine learning platform focused on deep neural networks.phing library. Used to create visualisations within Jupyter notebooks to present the data.
* Tensorflow: It is an open-source machine learning platform focused on deep neural networks.
* Shutil: Used form file copying and removal.
* Streamlit: It is used to create web apps for data science and machine learning.
* Joblib: It is a set of tools to provide lightweighting pipelining in Python.
* PIL: Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

## Credits 

* Relied heavily upon the Malaria Detection Walkthrough project - https://github.com/Code-Institute-Solutions/WalkthroughProject01
* Also used <https://github.com/olleholmgren/mildew-detection> for some inspiraion on the README
