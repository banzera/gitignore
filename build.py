#!/usr/bin/env python

import sys
import os
from os import path
from glob import glob

basedir = path.dirname(__file__)
genignore = path.abspath(basedir + "/gitignore.gen")


def build():
    print "Building .gitignore file at " + genignore

    if path.exists(genignore):
        yn = raw_input(".gitignore already exists. Overwrite? [n]")
        yn = yn or 'n'

        if yn in ["n", "N"]:
            sys.exit(0)

    gi = open(genignore, "w")
    gi.write("#" * 79 + "\n")
    gi.write("#\n")
    gi.write("# !!Auto-generated file!! Do not edit!!\n")
    gi.write("# See http://github.com/banzera/gitignore for details\n")
    gi.write("#\n")
    gi.write("#" * 79 + "\n")

    files = glob(basedir + "/Global/*.gitignore")
    files.extend(glob(basedir + "/*.gitignore"))

    yn = "n"

    for f in files:
        if not yn == "a":
            yn = raw_input("Include template %s ([y]/n/a/q)? " % f) or "y"

        if yn in ["A", "a", "Y", "y"]:
            ff = open(f, "r")

            gi.write("#" * 79 + '\n')
            gi.write("#\n")
            gi.write("# Imported from %s\n" % f)
            gi.write("#\n")
            gi.write("#" * 79 + '\n')
            for line in ff.readlines():
                gi.write("%s\n" % line)

        if yn in ["Q", "q"]:
            break


def install():
    yn = raw_input("Install new .gitignore? ([y]/n)") or "y"

    if yn in ["Y", "y"]:
        print "Installing generated .gitignore: " + genignore

        os.system("ln -fs %s %s/.gitignore " %
                  (genignore, os.path.expanduser("~")))
        os.system("git config --global core.excludesFile ~/.gitignore")


if __name__ == '__main__':
    build()
    install()
