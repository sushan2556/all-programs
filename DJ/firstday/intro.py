#django

'''
sql injection -googel  sequrity  /csrf( cross site request frojery)
MVT vs MVC( model view controller- google)


django is free and open source aeb framewqork
it is written in python
it work of Model View Templte(MVT) arctitecture 
it is maintented by django software foundation

statically typed response and dynamiacally typed response -google

#top features of django framework
1)fast
2)fully loaded
3)secure
4)scalability
5)versatile

#django project  vs django appliactaion

1)spam management system ( project)
-a dajango project is a collection of application and configurtion which form a fuyll web appliaction
-django project have atlest 1 aplication so that we can make same funcnality.

bankproject-loan app,custmer app, admin appliaction, insurance.
#####################################################################################
##request respnse working:-



1) googe - www.facebok.com
2)google map the url with  their own url.
3)url hit and request goes towards server.
4)view- is repnsible for conntrolling request respins for each url their is one view funtion present.

model view temaplate
#################################################################################
model- database
view-controller
templte-UI(user interface)


###############################################################
1)create project in django
django-admin startproject bankproject


##################################################################
django folder structure

bank project-MAIN FOLDER(ROOT DIRECTORY)
-BANK PROJECT FOLDER(BASE DIRECTORY/PROJECT LEVEL FILES)
1)_init_.py-this will show thgis is python package.

2)urls.py-project level url written in this

3)settings.py- project setting availbel in this
like-include new app,add static file,database settings like adding external database like postgresql or any.\
(django is having thier own database sqlite.)
-MANAGE.PY= COMMAND LINE UTILITY(WHAT IS COMMAND LINE UTILITUY)

4)wsgi(web server gateway interface)-deploying

5) asgi()asyncronouse gateway interface-deoloyese
#############################################################################################
#how to create a app in django project
#first go into the managy,py file directory
py manage.py startapp loanapp

#application level file
1)_init_.py- python package
2)models.py- database realated things like creating table or inserting and retreving data fron a database using model.
3)admin.py-django have built in django admin interface to intract with  customere.
4)views.py-request and response handele by views,py
5)tests.py
6)app.py

#####################################################################
#start server / run server
py manage.py runserver




googel things:-

1)what is server?
 A server is a computer or system that provides resources, data, services, or programs to other computers, known as clients, over a network. 
 In theory, whenever computers share resources with client machines they are considered servers.

7) what is request and response.
In computer science, request–response or request–reply is one of the basic methods computers use to communicate with each other in a network, 
in which the first computer sends a request for some data and the second responds to the request. More specifically, it is a message exchange 
pattern in which a requestor sends a request message to a replier system, 
which receives and processes the request, ultimately returning a message in response.


8) request and responce cycle
First a user gives a client a URL, the client builds a request for information (or resources) to be generated by a server. 
When the server receives that request, it uses the information included in the request to build a response that contains the 
requested information. Once built, that response is sent back to the client in the requested format, to be rendered to the user.

2)what is model in website

3) what is form in website
Form is a place where user enters the data and sends it to us for review 

4)what are the functnality provided by admin.
Provides the highest access to your website. Admin allows administrator of the website to manage its 
configurations, settings, content, and features and carry out oversight functions critical to the business

5)MVT vs MVC
Model view controller                       model view template 


6)static  and dyanamic response

9)create project in django

10) create app in django
11) project level  files
12)app level files
13)add app in your project level settings
14)run django server .
15)role of web server.








'''