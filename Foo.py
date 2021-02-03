import ctypes
import os

import sys
print(sys.version)

# this hack assumes the first path ends with 'main.runfiles' and that the
#  shared library is one directory upward
# TODO(nicmcd): find a stable way to do this
path_dirs = os.path.split(os.environ.get('PYTHONPATH').split(':')[0])
assert path_dirs[-1] == 'main.runfiles'
lib_path = os.path.join(*path_dirs[0:-1], 'libcc_Foo.so')
libFoo = ctypes.cdll.LoadLibrary(lib_path)

class Foo(object):
  def __init__(self):
    self._obj = libFoo.Foo_new();

  def bar(self):
    libFoo.Foo_bar(self._obj)

  def add(self, a, b):
    return libFoo.Foo_add(self._obj, ctypes.c_int64(a), ctypes.c_int64(b));
