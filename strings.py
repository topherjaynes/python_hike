#!/usr/bin/env python
# encoding: utf-8
"""
strings.py

Playing around with strings

Created by Christopher Jaynes on 2015-09-20.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main(argv):
	#strings slices
	string = argv[1]
	
	print string [:-2]
	print string [::-1]


if __name__ == '__main__':
	main(sys.argv)

