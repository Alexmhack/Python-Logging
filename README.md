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

