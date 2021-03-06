#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tutorials for sample use-cases with pywebcopy.

This modules demos some general use cases when
working with pywebcopy.

You can uncomment the functions which you like and modify 
its arguments to instantly get the results.
"""


import pywebcopy


'''
If you are getting `pywebcopy.exceptions.AccessError` Exception.
then check if website allows scraping of its content.

or

Uncomment the line below.
'''
# pywebcopy.config['bypass_robots'] = True


"""
If you want to overwrite existing files in the directory then
use the over_write config key.

or 

Uncomment the line below.
"""
# pywebcopy.config['over_write'] = True


"""
If you want to change the project name.
use the project_name config key.

or 

Uncomment the line below.
"""
# pywebcopy.config['project_name'] = 'my_project'



"""
Save Single Webpage

Particular webpage can be saved easily using the following 
methods.

For `pywebcopy.exceptions.AccessError` use the code provided on top sections.

choose and uncomment the method which you like to use.
"""

# method_1()
# pywebcopy.save_webpage(project_url='http://google.com', project_folder='c://Saved_Webpages/',)

# :Deprecated in version > 2.x : method 2:
# pywebcopy.config.config['bypass_robots'] = True
# wp = pywebcopy.generators.AssetsGenerator('https://www.bing.com/', 'e://tests/')
# wp.generate_style_map()
# wp.save_to_disk()

# method 3:
pywebcopy.WebPage('http://google.com', 'e://tests/', project_name='Google').save_complete()

# Advanced Features in Test Phase

# :New in version 4: method 4:

# raw html is now also accepted
# HTML = open('c:/users/raja/desktop/test.html').read()

# pywebcopy.WebPage(url='https://google.com/', project_folder='e://tests/pwc4/', HTML=HTML, over_write=True).save_complete()


'''
Whole Websites

Use caution when copying websites as this can overload or damage the
servers of the site and rarely could be illegal, so check everything before
you proceed.


choose method and uncomment the method which you like.
'''

# method 1:
'''
>>> pywebcopy.config.setup_config(project_url='http://localhost:5000/', 'project_folder='e://tests/', project_name='LocalHost')
>>> crawler = pywebcopy.Crawler('http://localhost:5000/')
>>> crawler.crawl()
'''

# method 2:
'''
>>> pywebcopy.save_website(project_url='http://localhost:8000', project_folder='e://tests/')
'''
