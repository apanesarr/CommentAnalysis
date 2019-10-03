# CommentAnaylsis
Analyzes code to find the total number of multi line comments and single line comments.


## How Does It Work ? 

This solution uses regex patterns instead of looping through each line. You can try out one of the regex patterns here: https://regex101.com/r/XaIcIC/

You can also view all the FSM diagrams on: https://drive.google.com/open?id=1x7be1wmcNn8PDAvUc2HWPSJZMeuE3foA


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Deployment

To deploy run main.py along with one argument file

```
python main.py somefile.py

```

## Unit Test
To run tests run the respective unit test file for each module.
```
python singleUnitTest.py

```



### Assumptions
The following lists the assumptions made while creating this project.

```
-> The file size is not larger then the onboard ram of the computer the program is running on

-> Comments such as 

'''
Hello
'''
#World
#!

are counted as two seperate comment blocks rather then one whole block

```

### Support

Current support of program files includes: 

```
-> Java

-> Python

-> JavaScript

```

If you would like more support then all you need to do is add the extension file and respective symbols in regex.py with escaped characters.

Example
```
{"cpp":"\/\/"}

```




