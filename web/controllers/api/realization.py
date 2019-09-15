from os import walk
from re import compile
from os.path import dirname, realpath

path = dirname(realpath(__file__))
file_list = list()
import_list = list()

for root, dirs, files in walk(path):
    file_list = files
    break

import_module = "from  web.controllers.api import %s"
reg = compile(r'^[\_+]|^(realization)+|pyc$')
for f in file_list:
    if not reg.search(f):
        moudle_name = f[:f.index(".")]
        import_list.append(import_module % moudle_name)
for import_ in import_list:
    exec(import_)



