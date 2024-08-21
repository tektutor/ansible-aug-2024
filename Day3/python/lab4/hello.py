#!/usr/bin/python3

# Python doesn't have an entry point function unlike many programming languages ( main )

def sayHello(message):
    print ( message )


# This is equivalent to main entrypoint used in most programming languages
if __name__ == "__main__":
    sayHello( 'Hello Python!' )
