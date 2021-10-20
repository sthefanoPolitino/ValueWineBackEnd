class vino:
    def __init__(self,Nombre:str,Residualsugar:float ,VolatileAcidity:float, FixedAcidity: float, CitricAcid: float, 
                FreeSulfurDioxide: float, Chlorides: float, Density: float, TotalSulfurDioxide: float,
                PH: float, Sulphates: float, Alcohol: float, Quality: int, IdProductor: int,Redwine:bool):
        self.Nombre=Nombre
        self.Residualsugar=Residualsugar
        self.VolatileAcidity=VolatileAcidity
        self.FixedAcidity=FixedAcidity
        self.CitricAcid=CitricAcid
        self.FreeSulfurDioxide=FreeSulfurDioxide
        self.Chlorides=Chlorides
        self.Density=Density
        self.TotalSulfurDioxide=TotalSulfurDioxide
        self.PH=PH
        self.Sulphates=Sulphates
        self.Alcohol=Alcohol
        self.Quality=None
        self.IdProductor=IdProductor
        self.Redwine=Redwine
    def __json__(self):
        return {"Nombre":self.Nombre,"VolatileAcidity":self.VolatileAcidity,
                "FixedAcidity":self.FixedAcidity,"CitricAcid":self.CitricAcid,"Residualsugar":self.Residualsugar,
                "FreeSulfurDioxide":self.FreeSulfurDioxide,"Chlorides":self.Chlorides,
               "Density":self.Density , "TotalSulfurDioxide":self.TotalSulfurDioxide ,"PH":self.PH ,
               "Sulphates":self.Sulphates , "Alcohol":self.Alcohol , "Quality":self.Quality , "IdProductor":self.IdProductor,"Redwine":self.Redwine}
    

    