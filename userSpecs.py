class UserSpecs(object):

    def __init__(self):
        self.dice = 0
        self.name = 'null'
        self.country = 'null'
        self.gender = 'null'
        self.age = 0
        self.status = 'null'
        self.electricity = 0
        self.water = 0
        self.less2dollars = 0
        
    ## set methods
    def setDice(self, dice):
        self.dice = dice
        
    def setName(self, name):
        self.name = name
        
    def setCountry(self, country):
        self.country = country
    
    def setGender(self, gender):
        self.gender = gender
    
    def setAge(self, age):
        self.age = age
        
    def setStatus(self, status):
        self.status = status
        
    def setElectricity(self, electricity):
        self.electricity = electricity
    
    def setWater(self, water):
        self.water = water
    
    def setLess2Dollars(self, less2dollars):
        self.less2dollars = less2dollars
     
    ## get methods
    def getDice(self):
        return self.dice
        
    def getName(self):
        return self.name
        
    def getCountry(self):
        return self.country
    
    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age
        
    def getStatus(self):
        return self.status
    
    def getElectricity(self):
        return self.electricity
        
    def getWater(self):
        return self.water
    
    def getLess2Dollars(self):
        return self.less2dollars
    