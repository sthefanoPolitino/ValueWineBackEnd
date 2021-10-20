import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import linear_model
#conseguir un conujunto de datos de prueba
#cargamos los datos de entrada 
data = pd.read_csv("../Resources/winequality-red.csv")
data.shape
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
XY_train=np.array(conjuntoDatosParaPrediction)
z_train=filtered_data["quality"].values
regr = linear_model.LinearRegression() #modelo de regresion lineal
        # Entrenamos nuestro modelo
regr.fit(XY_train, z_train) #este modelo genera un ecuacion 
        #de la recta, donde la variable predictora seria el conjunto XY y z la variable de respuesta
        # Dicha recta muestra la relacion lineal entre estos dos conjuntos
prediction = regr.predict(XY_train)
result = regr.predict([[7.4,0.7,0.0,1.9,0.076,11.0,34.0,0.9978,3.51,0.56,9.4	
]])
print(int(result),'resultado')
