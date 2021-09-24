import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

#cargamos los datos de entrada
data = pd.read_csv("../Resources/winequality-red.csv")
#veamos cuantas dimensiones y registros contiene
data.shape
data.describe()
filtered_data=data
conjuntoEntrada=filtered_data[["fixed acidity"]]
conjuntoEntrada["volatile acidity"]=filtered_data[["volatile acidity"]]
conjuntoEntrada["citric acid"]=filtered_data[["citric acid"]]
conjuntoEntrada["residual sugar"]=filtered_data[["residual sugar"]]
conjuntoEntrada["chlorides"]=filtered_data[["chlorides"]]
conjuntoEntrada["free sulfur dioxide"]=filtered_data[["free sulfur dioxide"]]
conjuntoEntrada["total sulfur dioxide"]=filtered_data[["total sulfur dioxide"]]
conjuntoEntrada["density"]=filtered_data[["density"]]
conjuntoEntrada["pH"]=filtered_data[["pH"]]
conjuntoEntrada["sulphates"]=filtered_data[["sulphates"]]
conjuntoEntrada["alcohol"]=filtered_data[["alcohol"]]
print(conjuntoEntrada)
XY_train=np.array(conjuntoEntrada)
z_train=filtered_data["quality"].values
regr = linear_model.LinearRegression()
# Entrenamos nuestro modelo
regr.fit(XY_train, z_train)
z_pred = regr.predict(XY_train)
result = regr.predict([[6.6,0.61,0,1.6,0.069,4,8,0.99396,3.33,0.37,10.4]])
print(int(result))