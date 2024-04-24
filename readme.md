#### Hackathon Instructions

Make sure to use the comments in the files to complete the hackathon


# Description
 This project is a random generator for dog pictures, student details, and interesting facts. It is built using Django  on Replit.

# How to Run Locally
To run this project locally, follow these steps:

# 1. Clone the Repository
  git clone https://github.com/amuybar/ApiBuilding.git

#2. Install Dependencies
Ensure you have Python and pip installed on your system. Then, navigate to the project directory and install the required packages:

  pip install django
  pip install requests

# 3. Run the Server
    python manage.py runserver

 
# Structure of the Assignment
It contains [5] pages  

  [Error.html] ---->this is a error fallback page such that when we cant fetch the desired page we fall back to this page.  
    
  [ Index.html ] --->this is the core page of this project with buttons to Navigate to differet pages.  
    
  [Randomfact.html] --->This page Display our **fact quote** together with a **button** to **generate random fact** and a{ **count card** }which shows the number of time we have generated our **facts**.  
    
  [Randompic.html]  ---> This Display our Random image card with a button to generate different our pctures and at the bottom is a cout card to keep track of the number of time weve generated.  
    
  [Randomstudent.html] ---> Our last page which displays a card of student details displayed at random.It alse have a generate button and a count card to keep track of number of time we generated.


#Screenshot of the Index Page
<div style="display: flex; align-items: center;">
  <img src="/static/readme_images/image.png" alt="Index Page" width="400" style="margin-right: 20px;">
  <p>This is the core page of the project.</p>
</div>

#Screenshot of the Random Dog Page
<div style="display: flex; align-items: center;">
  <img src="/static/readme_images/image_2.png" alt="Random Dog Page" width="400" style="margin-right: 20px;">
  <p>This page displays random dog images.</p>
</div>

#Screenshot of the Random Student Page
<div style="display: flex; align-items: center;">
  <img src="/static/readme_images/image_3.png" alt="Random Student Page" width="400" style="margin-right: 20px;">
  <p>This page displays random student details.</p>
</div>
