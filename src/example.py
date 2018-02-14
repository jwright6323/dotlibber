#!/usr/bin/env python

import os
import sys
import shutil
here = os.path.dirname(os.path.abspath(__file__))

# You may need to append your python path to be able to import dotlibber
# sys.path.insert(0, os.path.join(os.path.dirname(here) ... )
import dotlibber

libdir = os.path.join(os.path.dirname(here),"output")

def file_namer(lib, corner):
    return os.path.join(libdir, dotlibber.default_library_namer(lib, corner) + ".lib")

try:
    shutil.rmtree(libdir)
except:
    pass

dotlibber.read_library_json("../conf/test.json", "../conf/corners.json").write_all(file_namer)
