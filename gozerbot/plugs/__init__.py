# gozerbot basic plugins
#
#

""" register all .py files """

__copyright__ = 'this file is in the public domain'

import os

(f, tail) = os.path.split(__file__)
__all__ = []

for i in os.listdir(f):
    if i.endswith('.py'):
        __all__.append(i[:-3])
    elif os.path.isdir(f + os.sep + i):
        __all__.append(i)
__all__.remove('__init__')
__plugs__ = __all__

del f, tail
