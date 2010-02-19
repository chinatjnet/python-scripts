#!/usr/bin/python
# coding=cp936
# python 3.x


##Python获取程序所在目录
##
##解决__file__或sys.argv[0]在py2exe下失效的问题。
##
##选自pathutils模块。
##http://www.voidspace.org.uk/python/pathutils.html#get-main-dir

##############################################################################
# These functions get us our directory name
# Even if py2exe or another freeze tool has been used

import sys
import os

def main_is_frozen():
    """Return ``True`` if we're running from a frozen program."""
    import imp
    return (
        # new py2exe
        hasattr(sys, "frozen") or
        # tools/freeze
        imp.is_frozen("__main__"))

def get_main_dir():
    """Return the script directory - whether we're frozen or not."""
    if main_is_frozen():
        return os.path.abspath(os.path.dirname(sys.executable))
    return os.path.abspath(os.path.dirname(sys.argv[0]))

##############################################################################

##print(get_main_dir())