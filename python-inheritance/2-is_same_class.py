#!/usr/bin/python3

import importlib.util
import sys

def is_same_class(obj, a_class):
    """Devuelve True si obj es exactamente una instancia de a_class, de lo contrario False"""
    return type(obj) is a_class

# Esta parte importaría el archivo dinámicamente
spec = importlib.util.spec_from_file_location("2-is_same_class", "/home/student_jail/student_repo/python-inheritance/2-is_same_class.py")
module = importlib.util.module_from_spec(spec)
sys.modules["2-is_same_class"] = module
spec.loader.exec_module(module)

# Luego puedes usar is_same_class como antes
