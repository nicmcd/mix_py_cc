from Foo import *

if __name__ == '__main__':
  foo = Foo()
  foo.bar()
  print('4+5={}'.format(foo.add(4, 5)))
  print('4+-1={}'.format(foo.add(4, -1)))
