# Python-Logging
Using Python [Logging](https://docs.python.org/3/library/logging.html) module for collecting useful information and debugging errors for your application

Adding Logging to your Python program is as easy as just importing

```
import logging
```

With logging module imported you can use a ```logger``` to log messages that you want to see.
There are 5 methods through which we can log messages based on the severity of the events. 

1. DEBUG
2. INFO
3. WARNING
4. ERROR
5. CRITICAL

The above methods can be called by simply

**use_loggers.py**
```
logging.debug("this is a debug message")
logging.info("this is a debug message")
logging.warning("this is a debug message")
logging.error("this is a debug message")
logging.critical("this is a debug message")
```

Run the file and you would see the below results 

```
WARNING:root:this is a debug message
ERROR:root:this is a debug message
CRITICAL:root:this is a debug message
```

The output is ordered in severity level. ```:root:``` exists in each of the message 
which is the name the logging module gives to its default logger. 

This format, which shows the level, name, and message separated by a colon (:), is 
the default output format that can be configured to include things like timestamp, 
line number, and other details.

Notice that ```debug()``` and ```info()``` didn't log any messages. This is because 
the logging module logs the messages with a severity level of ```WARNING``` or above

Ofcourse logging module is customizable for changing the log information or the 
severity level to log but it is not recommended since it can cause issues with other
third-party libraries.

# Basic Configurations
```basicConfig()``` from logging helps us in configuring our logs for example 

1. ```level``` The root logger will be set to specified security level.
2. ```filename``` This specifies the file
3. ```filemode``` This specifies the mode in which file is opened **(default is 'a')**
4. ```format``` This is the format of the message.

By using ```level``` with one of the logging constants you can tell logger to log
messages at or above that level

**basic_config.py**
```
import logging 

loggging.basicConfig(level=logging.DEBUG)
logging.debug("Debug messages will also be logged now")
```

Run the file

```
DEBUG:root:Debug messages will also be logged now
```

As expected the ```DEBUG``` and above level messages are also logged.

Similarly we can log this messages into a file instead of the console using the 
attributes ```filename``` and ```format```

**format_log.py**
```
import logging

logging.basicConfig(filename='py.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning("Warning will get logged to file")
```

Open the file ```py.log``` and you should see

```
root - WARNING - Warning will get logged to file

```

**NOTE:** This info won't be shown on console anymore.

If you use [Github](https://github.com) and have a ```.gitignore``` file for 
Python or any other language repo then the ```*.log``` file won't get uploaded to 
github.

**Notice** that we gave ```filemode``` argument to ```w``` or write mode which 
means everytime the file is run the ```py.log``` file will be rewrited with new 
info, the default value for ```filemode``` is ```a``` or append mode.

There are lots more options available for a more customized and advanced root 
logger which can be found at [docs](https://docs.python.org/3/library/
logging.html#logging.basicConfig)

**NOTE:** ```basicConfig()``` function can only be called once in a file that
means we can only configure our root logger once.

**debug(), info(), warning(), error(), and critical() also call basicConfig() 
without arguments automatically if it has not been called before. This means that 
after the first time one of the above functions is called, you can no longer 
configure the root logger because they would have called the basicConfig() 
function internally.**

To see this in action you can simply

**format_log.py**
```
import logging

logging.warning("Warning will get logged to file")
logging.basicConfig(filename='py.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
```

change the order in which code is written and filemode to append to not rewrite 
the previous messages and run the file

```
WARNING:root:Warning will get logged to file
```

The log info is shown in console and not been appended in file

# Formatting The Output
Logging can accept any string as a message and log it but you it also has so many
more variables already with it, you can log the process id using

**format_output.py**
```
import logging

logging.basicConfig(format='%(process)s - %(levelname)s - %(message)s')
logging.warning("This is a warning")
```

Run the file and you should see the process id in console.

```
1304 - WARNING - This is a warning
```

The entire list of available variables can be found [here](https://docs.python.org/3/library/logging.html#logrecord-attributes)

For example we can use ```asctime``` to log the date and time when [logRecord](https://docs.python.org/3/library/logging.html#logging.LogRecord) was
created

```
# using asctime
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
```

```asctime``` is human readable format of time which is preferred over 
```created``` which returns in ```time.time()``` format

```
# using created
logging.basicConfig(format='%(created)s - %(levelname)s - %(message)s')

# Result
1536984287.9202418 - WARNING - This is a warning
```

Well ```asctime``` has a nice format but you can even change that using 
```datefmt``` like this

**format_output.py**
```
import logging

logging.basicConfig(
	format='%(asctime)s - %(levelname)s - %(message)s',
	datefmt='%d-%b-%y %H:%M:%S'
)
logging.warning("Admin logged in")
```

```
15-Sep-18 09:38:23 - WARNING - Admin logged in
```

Some more options that I found useful are ```lineno```

```
import logging

logging.basicConfig(
	format='%(asctime)s - %(levelname)s - %(message)s - %(lineno)s',
	datefmt='%d-%b-%y %H:%M:%S'
)
logging.warning("Admin logged in")
```

```
# RESULT
15-Sep-18 09:41:54 - WARNING - Admin logged in - 7
```

and ```pathname```

```
import logging

logging.basicConfig(
	format='%(asctime)s - %(levelname)s - %(message)s - %(pathname)s',
	datefmt='%d-%b-%y %H:%M:%S'
)
logging.warning("Admin logged in")
```

```
# RESULT
15-Sep-18 09:40:27 - WARNING - Admin logged in - format_output.py
```

```pathname``` gives the path of the file or if you just want the module you can
use ```module``` which gives ```format_output``` as result.

```lineno``` gives the number of souce code from which log has occured.

# Logging Variable Data
You can also log the information dynamically using string formatting with log call

**log_variables.py**
```
import logging

name = "Alex"

logging.warning(f"{name} is causing some issues")
```

```
WARNING:root:Alex is causing some issues
```

# Capturing Stack Traces
Logging module also has features to log full stack information from your app.
Exception information can be captured if ```exc_info``` is set to ```True```
and logging functions are called like this

```
import logging 

a = 'logger'
b = 0

try:
	b = int(a)
except Exception as e:
	logging.error("Exception Occured", exc_info=True)
```

```
ERROR:root:Exception Occured
Traceback (most recent call last):
  File "capture_exc.py", line 7, in <module>
    b = int(a)
ValueError: invalid literal for int() with base 10: 'logger'
```

This is much more useful info as compared to ```ERROR:root:Exception Occured```

A more precise way to log exceptions is using ```exception``` with logging

```
import logging

a = 'logger'
b = 0

try:
	b = int(a)
except Exception as e:
	logging.exception("Exception Occured")
```

```logging.exception("Exception Occured")``` is equivalent to 
```logging.error("Exception Occured", exc_info=True)``` and ```exception``` shows
log at ```ERROR``` level. You can also use any other level by calling the level 
with ```exc_info=True``` passed as argument.

```
logging.debug("Exception Occured", exc_info=True)
```

# Classes And Logging
Till now we have just used logging in simplest and not effiecient way possible. 
But the recommended way is to create your own logger by creating an object of 
Logger class.

The most commonly used classes in logging module are 

1. **Logger**: This is the class whose objects will be used in the application code directly to call the functions.

2. **LogRecord**: Loggers automatically create LogRecord objects that have all the information related to the event being logged, like the name of the logger, the function, the line number, the message, and more.

3. **Handler**: Handlers send the LogRecord to the required output destination, like the console or a file. Handler is a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. These subclasses send the logging outputs to corresponding destinations, like sys.stdout or a disk file.

4. **Formatter**: This is where you specify the format of the output by specifying a string format that lists out the attributes that the output should contain.

Again, unlike the root logger, a custom logger can’t be configured using 
basicConfig(). You have to configure it using Handlers and Formatters.

# Using Handlers
Handlers come into action when you want to configure your own loggers to send
the log to multiple places. Handlers send the log messages to configured 
destinations which can also include your email using [SMTP](https://github.com/
Alexmhack/python_intermediate)

**custom_logger.py**
```
import logging

# create a custom logger
logger = logging.getLogger(__name__)
```

Just like we did before, create a custom logger using ```getLogger``` and pass it
the ```__name__``` keyword that python assigns with the file name. Which means
we are giving our logger the name of the file.
