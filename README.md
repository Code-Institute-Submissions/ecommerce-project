# Welcome to The Ecommerce web application.

This project is a website that has been created which is a mutipage site.
I have created a multi-page website with a home page and register and login page for users to register aswell
as login to acces bugs, a cart and a profile.

[Here is a link to the live version of my project ](https://ecommerce-project-2019.herokuapp.com/)

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
* [Background Image](https://www.google.com/search?biw=1440&bih=789&tbm=isch&sa=1&ei=L7rBXJbwGouq1fAP7cydwAU&q=pattern+hd+image&oq=pattern+hd+image&gs_l=img.3..0j0i5i30l4j0i8i30l5.83421.88296..88485...3.0..0.121.705.9j1......1....1..gws-wiz-img.......0i7i30j0i7i5i30j0i8i7i30.mIu3VU5om6E#imgrc=d0Xa12HhzygCWM:)


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
    
    
    

                         To create a project
     
        
    1. I opened a terminal
    2. Then I typed in "django-admin startproject ecommerce-project ."
    3. A project was then created
    
                
                         To create an application 
     
        
    1. I opened a terminal
    2. Then I typed in "sudo pip3 install startapp home"
    3. A home application was then created.
    
    
                         To install dj-database-url
     
        
    1. I opened a terminal
    2. I typed in "sudo pip3 install dj-database-url"
    3. Then I typed in "sudo pip3 install psycopg"
    4. pip3 freeze > requirements.txt
    
  

        
                          To install stripe
         
    1. Open terminal in cloud9
    2. Then type "sudo pip3 install stripe"
    3. wait for stripe to install 
    4. Then i typed in "pip3 freeze > requirments.txt" 
    
    
                         To install django 1.11
    
    1. I opened a terminal
    2. Then I typed in sudo pip3 install django==1.11
    3. It then installed the packages
    4. Then i typed in "pip3 freeze > requirments.txt" 
    
    
    
                         To run the server 
         
        
    1.I opened a terminal
    2. Then I typed in python3 manage.py runserver $IP:$C9_PORT 
    3. This ran a local server for me to test my code.
    4. It came back as an disallowedhost so i copied the link given in the server page.
    5. I opened up settings.py in ecommerce folder and put the link into allowed hosts and saved it.
    6. I  reran the open link and it came back as the message it worked so I knew it was now succesfully running.
    
 
#### Automated Testing

## command line
        
        

       
### Deployment of my project

                    deployment of project through github 
                
    1. Go to the terminal 
    2. Typed in git add "filename of what you want to push" and press enter key
    3. Typed in commit -m "type in the message that I would explain about the commit in quotations"
    4. Repeat if neccessary for more files 
    5. Typed in  git push.
    6. Typed in username for github
    7. Typed in password for guthub 
    8. files are now pushed to github


                    
                   
                   deployment of page through github pages
                   
                    
                            
    1.Go to the github repository of happy cooking
    2. Then click on settings up on the right handside of the screen under the watch button
    3. Scroll down to the Github Pages
    4. In the container there is a source heading and a option button that has the word "none" with a little arrow pointing down the right
    5. Click on this and it will give you three options master branch, master branch/docs folder or none.
    6. click the master branch.
                                  
                                  
                  
                  
                  
                            creating up herokua app
            
    1. Log in using username and password
    2. In the personal page click the "NEW" button
    3. Click "Create new app"
    4. This brought me to Create new app page
    5. Type in an app name you want to call the app i called mine happy_cooking
    6. Choose a region united states or europe, i choose europe
    7. Press "create app" button.
    8. The app is now created.
    
                Create a new Git repository
                    
    1. Type in "cd my-project/" in the terminal
    2. Next type in "git init"
    3. After that I typed in "heroku git:remote -a ecommerce-project"     
        
        
    set up Deployment to Heroku in terminal of cloud9
            
    1. Go to the "deploy" page in heroku app
    2. To set up heroku deployment from github to heroku scroll down to "Deploy using Heroku Git" section
    3. Typed in "heroku login" to the terminal of cloud9
    5. Typed in "username" of my heroku username to the terminal of cloud9
    6. Types in "password" of my heroku password to the terminal of cloud9
    



            Commit my code to the repository and deploy it to Heroku using cloud9 terminal 
            
    1. Open terminal
    2. Typed in git add .
    3. Typed in git commit -am "message to explain about the commit you are commiting"
    4. Typed in git push heroku master
    5. Its pushed now.
    





### Credit

To start bootstrap website where i got my template for my website.



### Acknowledgements

I got inspiration on google Images I googled on google.com to see different websites and also for my colour scheme and background colour for my pages in my data-driven  web application.
I also got the recipes from Jamie Olivers website and the images too for my website.