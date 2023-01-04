#!/usr/bin/python3
class LockedClass:
    """ A class that prevents creation of attributes
        except for first name
    """
    def __setattr__(self,attribute,value):
        if attribute == 'first_name':
            super().__setattr__(attribute,value)
        else:
            raise AttributeError
