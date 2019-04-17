# Welcome to The Ecommerce web application.

This project is a website that has been created which is a mutipage site.
I have created a multi-page website with a home page and register and login page for users to register aswell
as login to acces bugs, a cart and a profile.

[Here is a link to the live version of my project ]()

#  UX 

This is a data-driven web application created for users, my primary target is to achieve the goal of being able view recipes with ingredients  on avaliablity of recipes. this is shown in the recipes page.

My data-driven web application will be a online cookbook created with  a homepage, a recipes page, my recipes page, and a login form. These pages will allow me to achieve my goals.

* As a user type, I would like to create a reigster page to register users to the database.
* As a user type, I would like to achieve a goal of also being able to log user in on the web application.
* As a user type, I would like to be able to add an feature to the cart.
* As a user type, I would like to be able to add bugs to the site.
* As a user type, I would like to be able to vote on a bug.
* As a user type, I would like to be able to comment on a feature or bug.
* My goal was to make information accessible on the site and user friendly, as shown through the  ecommerce web application I have created.


# Main Features

### User Login

A user can login using the username which is "proxie" and  password which is "password" to be able to login. This username will be used to log in and add, edit and delete a recipe.

###  User Register

A user can register using the username which is created by the user and a password which is also used to be able to login. 

###  bugs 

A user can add, vote and comment  on a bug aswell as set the status. 

###  Features

A user can add, vote and comment  on a bug aswell as set the status but must pay to use this.

###  cart

A user can register using the username which is created by the user and a password which is also used to be able to login. 

###  profile

A user can register using the username which is created by the user and a password which is also used to be able to login. 


## Wire frames 


Here I have included wire frames of diffrent pages such as the home, login, bugs, features and reigster pages.

My design process for me was to draw my wireframes and add them to my project once I had figured out what I needed to create 
an acheviable site.

* wire frame 1 - homepage
* wireframe 2 - login page
* wireframe3 -  register page
* wireframe 4 - bugs page
* wireframe 5 - features page 
* wireframes 6 - cart page
* wireframe 7 - profile page

### Planning 

I decided to plan my website, I looked at google.com at images of diffrent websites that came up in google images that I thought would help me and give me an idea of a layout of what should be included in my page for design of the navbar, the flow of my page and the pages I would include that would tie in my website together

I understood the base of my  web application should include a home page to start with the login function for a user to login and also a register function for new users to be able to sign up.

I decided that I would draw my wire frames with a pen and paper for each of my pages.


### Technologies

#### Technologies I used for this project is:

* [HTML](https://html.com/)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Python](https://www.python.org/)
* [Heroku](https://www.heroku.com)
* [Javascript](https://www.javascript.com/)
* [Startboostrap](https://startbootstrap.com/themes/)
* [Github](https://github.com/)
* [Cloud9](https://c9.io/login)
* [Formatter](https://www.freeformatter.com/html-formatter.html)
* [Validator](https://validator.w3.org/)



### Testing

#### Manual Testing

There were two options of testing my project the first one was by manual testing it by 
making sure the navbar worked by clicking on the recipe button to link to  the login and registration pages and 
that I was able to login using the username and the password that the user created.
I tested each section to see that every link worked correctly as i built the website.

When I installed pillow it wouldnt install  but I recorrected this error,
by using "sudo pip3 install pipenv" and then I created a virtualenv by running this code "pipenv shell" after 
this is reinstalled pillow using this code "pip3 install pillow". I reinstalled my packages in my requirements.txt file using
"pip install -r requirements.txt" it worked straight away and i could install stripe after this. 


              

    
                            login
            
     1.Click on the login button on the right hand corner of the navbar
     2.A login form will pop up like a modal.
     3. The user will see "Username" and "password"
     4. Type 'proxie' where it says username with a line underneath
     5. Type 'password' where it says password with a line underneath
     6. Then press the login button.
     
     
     
                            register
         
     1.Click on the register button on the right hand corner of the navbar
     2.A register form will appear on the page.
     3. The user will see "Username" and "password"
     4. Type 'proxie' where it says username with a box underneath
     5. Type 'password' where it says password with a line underneath
     6. Then press the login button.
     
    
                        Redirect to the home page
                
    1. Press the Happy Cooking logo on the upper left hand corner of the navbar.
    2. This will redirect you back to the home page.
    3. Press Home on the navbar from any of the three pages and it will bring you back to the homepage.
    

                
                         To create an application 
     
        
    1. I opened a terminal
    2. Then I typed in sudo pip3 install django==1.11
    3. It then installed
    2.     
    
                     To set up a requirements.txt file
         
        
    1. I opened a terminal
    2. Then I typed in sudo pip3 install django==1.11
    3. It then installed

        
                          To install stripe
         
    1. 
    2. 
    
    
                         To install django 1.11
    
    1. I opened a terminal
    2. Then I typed in sudo pip3 install django==1.11
    3. It then installed.
    
    
    
                         To run the server 
         
        
    1.I opened a terminal
    2. Then I typed in python3 manage.py runserver $IP:$C9_PORT 
    3. This ran a local server for me to test my code.
    4. It came back as an disallowedhost so i copied the link given in the server page.
    5. I opened up settings.py in ecommerce folder and put the link into allowed hosts and saved it.
    6. I  reran the open link and it came back as the message it worked so I knew it was now succesfully running.
 
#### Automated Testing

Automated testing using django included these tests  

In the terminal I ran my project locally by opening the terminal and the typing in python3 app.py to run the application and this would run my code.


       
### Deployment of my project

My Deployment was done by opening a terminal and then by using the code git status first followed git add (I put in my file or image) git commit -m "message on what the update was" and the git push to the master branch followed by my username and password.

I deployed my page from github through github pages. I went to settings in my github repository and scrolled down to Github pages title and changed my source from disabled to master branch and clicked save. now my website has been deployed.

Heroku was used also to deploy my project i created an new application and called it happy cooking.

### Credit

To start bootstrap website where i got my template for my website.



### Acknowledgements

I got inspiration on google Images I googled on google.com to see different websites and also for my colour scheme and background colour for my pages in my data-driven  web application.
I also got the recipes from Jamie Olivers website and the images too for my website.