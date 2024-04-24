import requests
import random
from django.shortcuts import render
from django.http import HttpResponse


# ------------------Home view-----------------#

# ---------------------------------------------------------
# path to home or index page
def index(request):
   return render(request, 'templates/index.html')


# ------------------Random Fact view-----------------#

# ---------------------------------------------------------
fact_count=0
def fact_view(request):
   res_fact = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
   fact_data = res_fact.json()
   fact = fact_data['text']
   return render(request, 'templates/randomfact.html', 
                 {
                   'fact': fact,
                  }
                )
def generate_facts(request):
  global fact_count
  fact_count +=1
  res_fact = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  fact_data = res_fact.json()
  fact = fact_data['text']
  return render(request, 'templates/randomfact.html', 
                          { 'fact': fact,
                          "fact_count":fact_count})


# ------------------Random dog Pic view-----------------#
# path to random dog pictures page 
# ---------------------------------------------------------
pic_count=0
def dog_view(request):
    res_dog = requests.get('https://dog.ceo/api/breeds/image/random')
    dog_data = res_dog.json()
    dog = dog_data['message']
    return render(request, 'templates/randompic.html',
                  {'dog': dog})
def generete_dog(request):
  global pic_count
  pic_count +=1
  res_dog = requests.get('https://dog.ceo/api/breeds/image/random')
  dog_data = res_dog.json()
  dog = dog_data['message']
  return render(request, 'templates/randompic.html',
                          { 'dog': dog, "pic_count":pic_count })
                           

                  

# ------------------Random Student view-----------------#
# defned a variable countr to keep track 
# of the times that i refresh to get another randomdetail
# ---------------------------------------------------------

refresh_count = 0
# function to fetch details from the api
def fetch_random_student():
    api_url = 'https://freetestapi.com/api/v1/students'
    response = requests.get(api_url)
  # cheaching if we can acces the link b4 returning geting json details from the response
    if response.status_code == 200:
        students = response.json()
        return random.choice(students)
    else:
        return None
# Function to perform randomizing
def random_student(request):
  return render(request, 'templates/randomstudent.html',
                {'refresh_count': refresh_count})

def generate_random_student(request):
  global refresh_count
  random_student = fetch_random_student()
  refresh_count += 1
  if random_student:
      return render(request, 'templates/randomstudent.html', 
                    {'student': random_student, 
                     'refresh_count': refresh_count})
  else:
      error_message = "Failed to fetch student data from the API"
      return render(request, 'error.html', {'error_message': error_message})








