#pip install matplotlib
#!pip install streamlit -q
#importing streamlit
import streamlit as st
#image or logo
from PIL import Image
#add photo or logo in website
img = Image.open('girl.jpg')
#tabs row title
st.set_page_config(page_title='RH CLASSIFIER')
st.title(' Welcome to : [RadiantHope Classifier]❤️ ')
# IMPORTING DEPENDENCIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.datasets
from sklearn.datasets import load_breast_cancer
#from google.colab import files
from sklearn.model_selection import train_test_split
# loading the data from sklearn
breast_cancer_dataset = load_breast_cancer()
print(breast_cancer_dataset)
# loading the data to a dataframe
data_frame = pd.DataFrame(breast_cancer_dataset.data, columns = breast_cancer_dataset.feature_names)
#remove 20 columns
data_frame.drop(data_frame.columns[-20:], axis=1, inplace=True)
#adding the 'target' column to the dataframe
data_frame['label'] = breast_cancer_dataset.target
print(data_frame)
#CREATING SCREEN
col1,col2 = st.columns(2)
with col1:
  st.header('BREAST TUMOUR CLASSIFICATION USING DEEP LEARNING')#for Title
  st.error('_WOMEN CARE_')#second title
  st.info('Cure Sometimes, Treat Often, Comfort Always')#for paragraph
with col2:
  st.image(img)#for image
#Creating button and insert dataset in it
dingdong = st.checkbox('DataSet')
if dingdong:
  st.dataframe(data_frame)  
#"""***Building the predictive system***"""
st.header('_Please enter the Values_')
st.subheader("_Input Features_")
col3,col4,col5,col6,col7 = st.columns(5)
with col3:
  mean_radius = st.number_input("Mean Radius", value=20.0)
  mean_texture = st.number_input("Mean Texture", value=16.0)
with col4:
  mean_perimeter = st.number_input("Mean Perimeter", value=85.0)
  mean_area = st.number_input("Mean Area", value=550.0)
with col5:
  mean_smoothness = st.number_input("Mean Smoothness", value=0.1)
  mean_compactness = st.number_input("Mean Compactness", value=0.1)
with col6:
  mean_concavity = st.number_input("Mean Concavity", value=0.1)
  mean_concave_points = st.number_input("Mean Concave Points", value=0.05)
with col7:
  mean_symmetry = st.number_input("Mean Symmetry", value=0.1)
  mean_fractal_dimension = st.number_input("Mean Fractal Dimension", value=0.02)
# print the first 5 rows of the dataframe
data_frame.head()
# print last 5 rows of the dataframe
data_frame.tail()
# number of rows and columns in dataset
#data_frame.shape
# getting some information about the data
data_frame.info()
# Checking the missing values
data_frame.isnull().sum()
# Statistical measures about the data
data_frame.describe()
# Checking the distribution of target value
data_frame['label'].value_counts()
#"""1  ---->  Benign
#0  ---->  Malignant"""
# Grouping values for each label 1 & 0
data_frame.groupby('label').mean()
#"""SEPARATING THE FEATURES AND TARGET"""
X = data_frame.drop(columns= 'label', axis= 1)
Y = data_frame['label']
print(X)
print(Y)
#"""SPLITTING THE DATA INTO TRAINING DATA AND TESTING DATA"""
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print(X.shape, X_train.shape, X_test.shape)
#"""***STANDARDIZE THE DATA***"""
from sklearn.preprocessing import StandardScaler
# Create an instance of the StandardScaler class.
scaler = StandardScaler()
# Fit the scaler to the training data.
X_train_std = scaler.fit_transform(X_train)
# Transform the test data using the fitted scaler.
X_test_std = scaler.transform(X_test)
# Print the shapes of the original data, the training data, and the test data.
print(X_train_std)
#"""**BUILDING THE NEURAL NETWORK**
#![download.png](data:image/png;base64,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)"""
# Importing Tensorflow and Keras
import tensorflow as tf
tf.random.set_seed(3)
from tensorflow import keras
# Setting up the layers of Neural Network
model = keras.Sequential([
                          keras.layers.Flatten(input_shape=(10,)),
                          keras.layers.Dense(20, activation='relu'),
                          keras.layers.Dense(2, activation='sigmoid')
])
# compiling the neural network
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
# training the Neural Network
history = model.fit(X_train_std, Y_train, validation_split=0.1, epochs=10)
#"""***VISUALIZATION OF ACCURACY AND LOSS***"""
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epochs')
plt.legend(['training data', 'validation data'], loc = 'lower right')
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epochs')
plt.legend(['training data', 'validation data'], loc = 'upper right')
#"""***ACCURACY OF THE MODEL ON TEST DATA***"""
loss, accuracy = model.evaluate(X_test_std, Y_test)
#print(accuracy)
print(X_test_std.shape)
print(X_test_std[0])
Y_pred = model.predict(X_test_std)
print(Y_pred.shape)
print(Y_pred[0])
print(X_test_std)
print(Y_pred)
#"""**model.predict() gives me the prediction probability of each class for the data point**"""
# argmax function
my_list = [30, 20, 10]
index_of_max_value = np.argmax(my_list)
print(my_list)
print(index_of_max_value)
# Converting the prediction probability to class labels
Y_pred_labels = [np.argmax(i) for i in Y_pred]
print(Y_pred_labels)
## Put the inputs into a DataFrame
input_data = pd.DataFrame({
    "mean radius": [mean_radius],
    "mean texture": [mean_texture],
    "mean perimeter": [mean_perimeter],
    "mean area": [mean_area],
    "mean smoothness": [mean_smoothness],
    "mean compactness": [mean_compactness],
    "mean concavity": [mean_concavity],
    "mean concave points": [mean_concave_points],
    "mean symmetry": [mean_symmetry],
    "mean fractal dimension": [mean_fractal_dimension]
})
# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)
#reshape the numpy array as we are predicting for one data point
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
# standardize the input_data
input_data_std = scaler.transform(input_data_reshaped)
prediction = model.predict(input_data_std)
print(prediction)
prediction_label = [np.argmax(prediction)]
Predict = st.button('CLASSIFY')
if Predict:
  if(prediction_label[0] == 0):
    st.error(f"The predicted tumor type is: MALIGNANT. You have to take more care about your Breast Health ")
  else:
    st.success(f"The predicted tumor type is: BENIGN. watch the video below to improve your Breast Health ")
#For Video Screening
st.header('_FIVE WAYS TO REDUCE YOUR RISK OF BREAST CANCER_')
bullet_points = [
    "--->  Maintain a Healthy Body Weight",
    "--->  Maintain an Active Lifestyle ",
    "--->  Limit Your Alcohol ",
    "--->  Breastfeed if possible ",
    "--->  Weigh the Risks and Benefits of Hormone Therapy for Menopause Symptoms ",
    "------------------------------------------------------------------------------",
    "***You should be aware of any changes in your breasts***",
    "***When you turn 50 get a mammogram for every 2 years until you're 74***",
    "------------------------------------------------------------------------------"
]
st.write(bullet_points)
video_file = open('Five_Ways_to_Reduce_your_Risk_for_Breast_Cancer(1080p).mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)
