'''
author : nima aram
'''
html = ''
def aboutTemplate():
    return '<!--This file generated by Pyhtml-->'
html_array = [aboutTemplate()]
def runHTML():
    html = ''
    for html5 in html_array:
	    html += html5
    return html
def buildHTML():
    htmlFile = ''
    for html5 in html_array:
        htmlFile += html5
    Hfile = open('Pyhtml.html','w')
    Hfile.write(htmlFile)
    Hfile.close()