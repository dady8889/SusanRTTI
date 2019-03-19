# ClassInformer python
# Nicolas Guigo / NCC Group
# Tyler Colgan / NCC Group
# 03/2017

import idaapi
idaapi.require("utils")
idaapi.require("msvc")
idaapi.require("gcc")
idaapi.require("classdiagram")
from idaapi import autoIsOk
from msvc import run_msvc
from gcc import run_gcc
from classdiagram import ClassDiagram

def show_classes(classes, vtables):
    c = ClassDiagram("Class Diagram", classes, vtables)
    c.Show()

def isGcc():
    gcc_info = FindText(0x0, SEARCH_CASE|SEARCH_DOWN, 0, 0, "N10__cxxabiv117__class_type_infoE")
    return gcc_info != BADADDR

def main():
    print "Starting ClassInformerPython"
    if autoIsOk():
        vtables = {}

        if isGcc():
          classes = run_gcc()
        else:
          classes, vtables = run_msvc()

        print "VTables:"
        print vtables
        print "Classes:"
        print classes

        show_classes(classes, vtables)
    else:
        print "Take it easy, man"
    print "Done"

if __name__ == '__main__':
    main()
