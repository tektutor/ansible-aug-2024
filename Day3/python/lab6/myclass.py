#!/usr/bin/python3

class Parent:
    def __init__(self):
        print( "Parent constructor ...")

    def publicMethod(self):
        print ( "Parent public method ...")

    def _protectedMethod(self):
        print ( "Parent protected method ...")

    def __privateMethod(self):
        print ( "Parent private method ..." )

#Child class is inheriting from Parent class
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print( "Child constructor ...")

    def _protectedChildMethod(self):
        print ( "Protected Child Method ...")

    def __privateChildMethod(self):
        print ( "Private child method ...")

    def publicChildMethod(self):
        print ( "Public child method ...")
        Parent.publicMethod(self) # the public methods of Parents are accessible to child as well
        Parent._protectedMethod(self) # - the protected methods of Parents are inherited by child, hence this should work
        #Parent._privateMethod(self) - the private methods of Parent aren't inherited/accessible to child
        self.__privateChildMethod()


if __name__ == "__main__":
    child = Child()

    child.publicChildMethod()
    child._protectedChildMethod()
    #child.__privateChildMethod()
