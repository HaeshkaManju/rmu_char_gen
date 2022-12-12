# Class File: Statistics
# Model for Flask-SQLAlchemy
'''
    The purpose of this file is to house the "stats" used by RMU characters.
    The stats are as follows:
        (AG)ility
        (CO)nstitution
        (EM)pathy
        (IN)tuition
        (ME)mory
        (PR)esence
        (QU)ickness
        (RE)asoning
        (SD)- Self Discipline
        (ST)rength

        Values can be integers ranging from 1 to 100.
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
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
##############################################################################
#                              Class: Statistics                             #
##############################################################################
class Statistics(db.Model):
    '''
        This should be the primary point where individual stats are 
            identified.
        UNKNOWN: I currently don't know if actions to be applied to a stat
            should take place here, or happen in the place where its approp
            table is housed. (see def: stat_gain)
    '''
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    abbrev = db.Column(db.String(80), unique=True, nullable=False)
    potential = db.Column(db.Integer, unique=False, nullable=True)
    temporary = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f'Statistics\("{self.name}","{self.abbrev}"\)'

    def __str__(self):
        return f("This stat is: {self.name}, it is abbreviated as: {self.abbrev}.")

    def stat_gain(self):
        '''
            When a character either levels or pays to increase a stat, this is
                called a stat gain.
            Stat gains use a chart to determine by how much to increase.
        '''
        return None

##############################################################################
#                          Class: Statistics Range Bonus                     #
##############################################################################
class StatisticsRangeBonus(db.Model):
    '''
        To create the table to house the process for describing how much
            bonus a given statistic is worth.
    '''
    __tablename__ = 'stat_bonus'
    id = db.Column(db.Integer, primary_key=True)
    min_range = db.Column(db.Integer, unique=True, nullable=False)
    max_range = db.Column(db.Integer, unique=True, nullable=False)
    bonus = db.Column(db.Integer, unique=False, nullable=False)
    adjective = db.Column(db.String(80), unique=False, nullable=True)

    def display_bonus(self, stat):
        result = 'stat_bonus'.query.filter(stat>=min_range & stat<=max_range).first()
        return result
    

##############################################################################
#                            Class: Statistics Gains                         #
##############################################################################
class StatisticsGains(db.Model):
    '''
        To create the table to house the process for describing how much
            a given statistic will increase from a stat gain request.
    '''
    __tablename__ = 'stat_gain'
    id = db.Column(db.Integer, primary_key=True)
    min_range = db.Column(db.Integer, unique=True, nullable=False)
    max_range = db.Column(db.Integer, unique=True, nullable=False)
    die_type = db.Column(db.Integer, unique=False, nullable=False)
    die_mod = db.Column(db.Integer, unique=False, nullable=True)

    def display_bonus(self, stat):
        result = 'stat_bonus'.query.filter(stat>=min_range & stat<=max_range).first()
        return result
    




