class Usuario:
    def __init__(self,Nombre:str,VolatileAcidity: float, FixedAcidity: float, CitricAcid: float, 
                FreeSulfurDioxide: float, Chlorides: float, Density: float, TotalSulfurDioxide: float,
                PH: float, Sulphates: float, Alcohol: float, Quality: float, IdProductor: int):
        self.Nombre=Nombre,
        self.VolatileAcidity=VolatileAcidity,
        self.FixedAcidity=FixedAcidity,
        self.CitricAcid=CitricAcid,
        self.FreeSulfurDioxide=FreeSulfurDioxide,
        self.Chlorides=Chlorides,
        self.Density=Density,
        self.TotalSulfurDioxide=TotalSulfurDioxide,
        self.PH=PH,
        self.Sulphates=Sulphates,
        self.Alcohol=Alcohol,
        self.Quality=Quality
        self.IdProductor=IdProductor
    def __json__(self):
        return {"Nombre":self.Nombre[0],"VolatileAcidity":self.VolatileAcidity[0],
                "FixedAcidity":self.FixedAcidity[0],"CitricAcid":self.CitricAcid[0],
                "FreeSulfurDioxide":self.FreeSulfurDioxide[0],"Chlorides":self.Chlorides[0],
               "Density":self.Density,"TotalSulfurDioxide":self.TotalSulfurDioxide,"PH":self.PH,
               "Sulphates":self.Sulphates,"Alcohol":self.Alcohol,"Quality":self.Quality,"IdProductor":self.IdProductor}
    

    