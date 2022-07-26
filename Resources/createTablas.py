createTablaVino = '''CREATE TABLE Vino(
            Id INT NOT NULL AUTO_INCREMENT,
            IdProductor INT NOT NULL,
            PRIMARY KEY (`Id`),
             FOREIGN KEY (IdProductor)
             REFERENCES Usuario(id)
            ON DELETE CASCADE
            )'''
createTablaUsuario = '''CREATE TABLE Usuario(
        id INT NOT NULL AUTO_INCREMENT,
        Email VARCHAR(30) NOT NULL,
        PRIMARY KEY (`id`)
        )'''
