import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score,precision_score
#conseguir un conujunto de datos de prueba
#cargamos los datos de entrada
data = pd.read_csv("../Resources/winequality-red.csv")
#veamos cuantas dimensiones y registros contiene
data.shape
data.describe()
campoaPredecir=data["quality"]
filtered_data=data
conjuntoDatosParaPrediction=filtered_data[["fixed acidity"]]
conjuntoDatosParaPrediction["volatile acidity"]=filtered_data[["volatile acidity"]]
conjuntoDatosParaPrediction["citric acid"]=filtered_data[["citric acid"]]
conjuntoDatosParaPrediction["residual sugar"]=filtered_data[["residual sugar"]]
conjuntoDatosParaPrediction["chlorides"]=filtered_data[["chlorides"]]
conjuntoDatosParaPrediction["free sulfur dioxide"]=filtered_data[["free sulfur dioxide"]]
conjuntoDatosParaPrediction["total sulfur dioxide"]=filtered_data[["total sulfur dioxide"]]
conjuntoDatosParaPrediction["density"]=filtered_data[["density"]]
conjuntoDatosParaPrediction["pH"]=filtered_data[["pH"]]
conjuntoDatosParaPrediction["sulphates"]=filtered_data[["sulphates"]]
conjuntoDatosParaPrediction["alcohol"]=filtered_data[["alcohol"]]
print(conjuntoDatosParaPrediction)
XY_train=np.array(conjuntoDatosParaPrediction)
z_train=filtered_data["quality"].values
regr = linear_model.LinearRegression() #modelo de regresion lineal
# Entrenamos nuestro modelo
regr.fit(XY_train, z_train) #este modelo genera un ecuacion 
#de la recta, donde la variable predictora seria el conjunto XY y z la variable de respuesta
# Dicha recta muestra la relacion lineal entre estos dos conjuntos
prediction = regr.predict(XY_train)
print(prediction)
result = regr.predict([[6.6,0.61,0,1.6,0.069,4,8,0.99396,3.33,0.37,10.4]])
print(int(result))
print(r2_score(campoaPredecir,prediction), mean_squared_error(campoaPredecir,prediction))