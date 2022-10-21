How to run : First install pycharm IDE
1- open GoogleChrome :
2- go to the link : https://chromedriver.storage.googleapis.com/index.html
3- open new tab and go to the link : chrome://version/
4- check google version like this (Google Chrome:	100.0.4896.88)
5- go back to : https://chromedriver.storage.googleapis.com/index.html
and open folder 100.0.4896.00….
6 - Download chromedriver_win32.zip if you use windows , Or download the right one for your system.
7-  create new folder in C , like this C:\SeleniumDrivers\chromedriver.exe
and extract file chromedriver_win32.zip in this folder.
8- copy this path C:\SeleniumDrivers\chromedriver.exe , and add in cls.driver = webdriver.Chrome("Your Path")
9- copy reports package path and put here
if __name__ == '__main__':
   unittest.main(
       testRunner=HtmlTestRunner.HTMLTestRunner(output='A Path Reports Package'))
10- if you using pycharm IDE open setting , go to the Python Interpreter
select add new , and install pip & selenium .
11- open command line and go to project path :Follow the commands line in order :
- python scenario1.py and [Enter]
- python -m unittest scenario1.py and [Enter]
after everything is working fine
- pip install html-testRunner and [Enter]
- python scenario1.py and [Enter]
Now Running tests………….
Go to the reports package and You will find -> TestResult.html -> Open in Browser -> and you will find Sample report from the output of test cases.
