createTablaVino = '''CREATE TABLE Vino(
            Id INT NOT NULL AUTO_INCREMENT,
            IdProductor INT NOT NULL,
            Nombre VARCHAR(40),
            Residualsugar FLOAT,
            VolatileAcidity FLOAT,
            FixedAcidity FLOAT,
            CitricAcid FLOAT,
            FreeSulfurDioxide FLOAT,
            Chlorides FLOAT,
            Density FLOAT,
            TotalSulfurDioxide FLOAT,
            PH FLOAT,
            Sulphates FLOAT,
            Alcohol FLOAT,
            Quality INT,
            Redwine TINYINT,
            PRIMARY KEY (`Id`),
             FOREIGN KEY (IdProductor)
             REFERENCES Usuario(id)
            )'''
createTablaUsuario = '''CREATE TABLE Usuario(
        id INT NOT NULL AUTO_INCREMENT,
        Email VARCHAR(30) NOT NULL,
        Nombre VARCHAR(30),
        Telefono INT,
        Rol TINYINT,
        Direccion VARCHAR (40),
        Password VARCHAR(200),
        PRIMARY KEY (`id`)
        )'''
