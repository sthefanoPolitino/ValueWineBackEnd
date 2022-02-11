from logging import debug
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.model_selection import train_test_split
#conseguir un conujunto de datos de prueba
#cargamos los datos de entrada

def prediccion(vino):
    
    if vino["Redwine"]==1:
        data = pd.read_csv("./Resources/winequality-red.csv")
    elif vino["Redwine"]==0:
        data = pd.read_csv("./Resources/winequality-white.csv")
    #veamos cuantas dimensiones y registros contiene
    try:
        data.shape
        campoaPredecir=data["quality"]
        filtered_data=data
        conjuntoDatosParaPrediction=pd.DataFrame()
        conjuntoDatosParaPrediction["fixed acidity"]=filtered_data[["fixed acidity"]]
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
        X_train, X_test, y_train, y_test = train_test_split(XY_train, z_train, test_size=0.2,random_state=0)
        regr = linear_model.LinearRegression() #modelo de regresion lineal
        # Entrenamos nuestro modelo
        regr.fit(X_train, y_train) #este modelo genera un ecuacion 
        #de la recta, donde la variable predictora seria el conjunto XY y z la variable de respuesta
        # Dicha recta muestra la relacion lineal entre estos dos conjuntos
        prediction = regr.predict(X_test)
        result = regr.predict([[vino["FixedAcidity"],
                                vino["VolatileAcidity"],
                                vino["CitricAcid"],
                                vino["ResidualSugar"],
                                vino["Chlorides"],
                                vino["FreeSulfurDioxide"],
                                vino["TotalSulfurDioxide"],
                                vino["Density"],
                                vino["PH"],
                                vino["Sulphates"],
                                vino["Alcohol"]
                                ]])
        
        return int(result)
    except Exception as e:
        return 500