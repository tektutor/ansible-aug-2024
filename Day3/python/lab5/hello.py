#!/usr/bin/python3

class Hello:

    # Constructor - special function used to initialize member variables 
    # will be called automatically when we create an instance of this Hello class
    # self is equivalent to this pointer used in most programming lanaguages
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname  = lastname

    def display(self): 
        print ( "Welcome,", self.firstname, self.lastname, "!" )

if __name__ == "__main__":
    hello = Hello("Bruce", "Lee")
    hello.display()

