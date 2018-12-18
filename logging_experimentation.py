#logging experimentation


'''
LOGGING:
- helps develop better understanding of the flow of a prgm / discover scenarios
you might not have thought were developing
- extra set of eyes, constantly looking at the flow that an application is
going through
- capabilities:
    -- store info --> which user or IP accessed the application
    -- if error occurs --> provide more insights than a stack trace by telling
    what the state of the program was before it arrived at the line of code
    where the error occurred
- logging useful data in right places --> can debug errors easily & use data 
to analyze the performance of the application to plan for scaling or look at
usage patterns to plan for marketing
'''


# ================
# Logging Module
# ================
'''
- module provides a default logger --> can get started without much configuration
- by default, there are 5 standard lvls indicating severity of events.
	-- DEBUG
	-- INFO
	-- WARNING
	-- ERROR
	-- CRITICAL

- corresponding methods for each lvl can be called as shown in these examples:
	-- output shows the severity level before each msg along with 'root'
'''
import logging

logging.debug('this is a debug msg')
logging.info('this is an info msg')
logging.warning('this is a warning msg')
logging.error('this is an error msg')
logging.critical('this is a critical msg')

'''
=================
commonly used parameters for basicConfig() are:
- level: the root logger will be set to the specified severity level
- filename: specifies the file.
- filemode: if filename given, file is opened in this mode. The default is 'a', means append
- format: This is the format of the log msg
=================
'''


logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')





