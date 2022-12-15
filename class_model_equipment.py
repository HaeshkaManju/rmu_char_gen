# Class File: Statistics
# Model for Flask-SQLAlchemy 
'''
    Equipment is the generic layer of representation of inanimate
        physical objects.
    - Equipment (carried/worn),
    - Weapons,
    - Armor.
    This will not be used to represent animals.
    - Generally, those objects with a personal movement speed need to be
        represented elsewhere.  I don't know where/how, yet.

    I'm not sure if I should call the strength of an item "strength".
        Yes, that's how it is in the book, but it's actually:   
        "Item Durability".  
        It does not possess the characteristics of the strength stat.
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
from flask_appbuilder import Model
####################
#  Configurations  #
####################
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

###############################################################################
#                                Class: Equipment                             #
###############################################################################
class Equipment(db.Model):
    '''
        Equipment shall form the base class for all inanimate objects
            that do not possess a speed of their own.
        This class shall be used to specify "items" such as those that
            would appear in a marketplace or as part of purchasble
            equipment during character generation.
        This shall NOT be used to specify those items which have a
            personal movement stat (such as a Horse or Flying Carpet.)
    '''
    __tablename__ = 'equipment'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    production_time = db.Column(db.Integer, unique=False, nullable=True)
    weight = db.Column(db.Integer, unique=False, nullable=True)
    item_strength = db.Column(db.Integer, unique=False, nullable=True)
    notes = db.Column(db.String(400), unique=False, nullable=True)
    worn = db.Column(db.Boolean, unique=False, nullable=True)
    # move me
    coinage_id = db.Column(db.Integer, unique=False, nullable=True)
    coinage = db.relationship("Coinage", backref="equipment")

    def convert_time_units(self):
        """
            Time should be presented in the lowest common denominator among
                possible options.  Use this method to convert (for display)
                to the most appropriate length of time.
            Hours is the lowest common denominator.
        """
        # Take production time.
        # Determine if less than 24 [hours].
        ## If less: display "{#} hours".
        ## if more: divide/modulo 24, display "{#} days, {#2} hours".
        pass

    def convert_monetary_units(self):
        """
            Money should be presented in the lowest common denominator among
                possible options.  Use this method to convert (for display)
                to the most appropriate length of coinage/currency.
            Tin Pieces (tp) is the lowest common denominator.
        """
        # Take coin amount.
        # Determine if greater than 10 coins.
        ## If less: display "{#} Tin Pieces (tp)".
        ## else: for loop to modulo each final digit,
        ### display #[type], #[type].
        ### See: Class Coinage for details.
        pass

    def convert_mass_units(self):
        """
            Weight should be presented in the lowest common denominator among
                possible options.  Use this method to convert (for display)
                to the most appropriate length of mass/weight.
            Ounces (oz) is the lowest common denominator.
        """
        # Take weight amount.
        # Determine greater than 16 ounces.
        ## If less: display "{#} ounces (oz)".
        ## else: #/16: display "{#} pounds (lb(s))".
        pass
########################################
#     Sub-Class: Armor (Equipment)     #
########################################
class Armor(Equipment):
    '''
        Armor is a subclass of Equipment.
        Armor specifies values that are specific only to armor, such as
            movement and ranged penalties.
        Armors are descriptive rather than prescriptive.  Should Armor
            therefore be a subclass of Armor_Types?  Or should those concepts
            be combined?
    '''
    pass

    def don_armor(self, character):
        '''
            To be used to add Armor from a Character's Inventory to their
                list of armor that is currently worn.
            Purpose: Flag armor as being worn.
        '''
        # If other Armor already has "Worn" flag, send notice to user
        ## "[name] Armor is already worn." then Break.
        # If No other Armor has "Worn" flag, add Flag to selected Armor.
        ## Then, indicate "[name] Armor has been equipped."
        pass
    
    def apply_move_pen(self, character):
        '''
            To be used to assess the Maneuver Penalties of an Armor to
                the character.
            Purpose: Find Worn armor, apply appropriate penalty.
                    Return 0 if Armor is not worn.
            This should almost always be called in conjunction (before)
                with: "Maneuvering in Armor" SKILL.
                If you fail to do this, you'll be an idiot Michael, and 
                    you know damn-well why.
        '''
        # If no Armor has "Worn" flag, Return Penalty = 0 or 0.
        ## Display penalty in appropriate locations as: 0.
        # If Armor has "Worn" flag, lookup associated "maneuv_pen"
        ## Add to all appropriate skill checks with "moving maneuver" type.
        ### Display penalty in appropriate locations as: -X.
        # maybe we just pass this value and don't actually handle display?
        ## If so, change name of this function to "calc" not "apply"
        pass

    def apply_enc_perc(self, character):
        '''
            To be used to assess the weight of an Armor to the character.
            Purpose: Find worn/carried armor, apply appropriate penalty.
                Return 0 if Armor is not worn/carried.
            This should always always be called in conjunction with
                assessing a character's total encumbrance.
            This method shall NOT be used to calculate the total encumbrance
                penalty.  That should be done elsewhere.
        '''
        # If no Armor has "Carried" flag, Return Penalty = 0 or 0.
        ## Display penalty in appropriate location as: 0.
        # If Armor has "Carried" flag, lookup associated "enc_perc"
        ## All to total encumbrance value for character.
        pass

##############################################################################
#                            Class:                          #
##############################################################################

##############################################################################
#                            Class:                          #
##############################################################################

#############################################################################
#                               Class: Coinage                              #
#############################################################################
class Coinage():
    '''
    '''