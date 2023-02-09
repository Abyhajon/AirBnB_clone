#!/usr/bin/python3
'''
custom base class to define common attributes and methods for entire project
'''


import uuid
from datetime import datetime


class BaseModel:
    '''
    Base for all the classes in the entire project

    Attributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prins the class name, id and creates dictionary
        representations of the input values
        save(self): returns the dictionary values of the instance obj

    '''
    def __init__(self):
        '''
        public attributes initialization
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of __dict__ of the
        instance.
        '''
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
