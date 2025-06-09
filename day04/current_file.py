#basic import - best practice
import hello as ho

ho.say_hello()
print(ho.x)


#specific import
from hello import say_hello, x, y

print(x, y)
say_hello()

#import with alias

ho.say_hello()

#import from package
import package.module_01 as pm1
pm1.say_hello()

#specific nested import
from package.module_01 import say_hello
say_hello()