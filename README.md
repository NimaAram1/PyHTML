# PyHTML
A module that you can use to create HTML pages with Python code🐍
## How to use?
First, create the file you want to write next to the utils folder.  forexample generate.py
then,
Enter the following code in your file
```python
from utils.tags import *
from utils.run import *
```
Then add the following code to your file.
```python
@headTag
@styleTag
def head():
	return '''div{color:red}'''
@h1Tag
def header():
	return 'hello'
@h2Tag	
def aside():
	return 'this is a aside'
@divTag
def footer():
	return 'this is a my footer'
@divTag
def end():
	return '''<h2>i come with pyhtml</h2>
	<h3> we in a div!</h3>
	'''
@freeTag
def comment():
	return '''
	<!--check my github for new fuetres!-->
	<!--fork me please!-->'''
html_array += [
	head(),
	header(),
	aside(),
	footer(),
	end(),
	comment(),
]
mycode = runHTML()
print(mycode)
buildHTML()
```
then , open generator.py or yourfilename.py
in your directory Pyhtml file is created, open it!
result:
![result](http://s5.picofile.com/file/8397114292/Pyhtml_html_Google_Chrome_25_02_1399_04_44_43_%D8%A8_%D8%B8.png)
## write your first tags
