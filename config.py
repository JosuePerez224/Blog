#This are the configuration of the app
class Config:
    DEBUG = True
    TESTING = True
    
#This is going to be the config when the app is on production
class ProductionCongig(Config):
    DEBUG = False
    
#This is going to be the config when the app is on develop        
class DevelopmentConfig(Config) :    
    SECRET_KEY = "mySecretKey"

