# Class File: Statistics
# Model for Flask-SQLAlchemy 
'''
    Equipment is the generic layer of representation of physical objects.
    - 
'''

'''
    These imports will likely be unecessary at production.
    They are here for testing purposes.
    Establishing a structured flask-app, and placing these files into the 
        models folder will handle the imports and prevent the need for 
        over use of imports.
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

##############################################################################
#                            Class:                          #
##############################################################################
class Equipment(db.Model)
    __tablename__ = 'equipment'
    id = db.Column
##############################################################################
#                            Class:                          #
##############################################################################