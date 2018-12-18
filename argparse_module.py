# argparse module practice
# https://docs.python.org/3/library/argparse.html
'''
====================================================================================
Compatibility
====================================================================================
ARGPARSE module should work on Python >= 2.3, it was tested on:

2.3, 2.4, 2.5, 2.6 and 2.7
3.1, 3.2, 3.3, 3.4
====================================================================================
Module description:
====================================================================================
- argparse module - makes easier to write user-friendly command-line interfaces
- defines what arguments it requires
- 'argparse' will figure out how to parse those out of 'sys.argv'
- this module also automattically generates help and usage msgs / issues errors when
	gives program invalid arguments. 
====================================================================================
EXAMPLE:
====================================================================================
- Code takes a list of integers and produces either the sum or the max:
'''
import argparse
									#STEPS:
parser = argparse.ArgumentParser(description='Process some integers.')  # <-- (1) Creating a PARSER -- 
									# 	- create an 'ArgumentParser' object
									#	- this obj will hold all the info necessary to 
									#	parse the cmdline into python data types
		
parser.add_argument('integers', metavar='N', type=int, nargs='+', 	#
			help='an integer for the accumulator')		#
									#
parser.add_argument('--sum', dest='accumulate', action='store_const', 	#
			const=sum, default=max,				#
		help='sum the integers (default: find the max)')	#
									#
args=parser.parse_args()						#
print(args.accumulate(args.integers))					#
									#
	
	
	
	













