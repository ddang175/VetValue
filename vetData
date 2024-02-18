from dotenv import find_dotenv, load_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("password")
connection_string = f"mongodb+srv://ddang175:{password}@vetvalue.hj5s8uw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

vetDB = client.vetnextdoor
vetsCollection = vetDB.vets

def create_documents():
  clinic_names = ["Ashworth Road Animal Hospital", "Banfield Pet Hospital", "Animal Care Clinic West & Metro Cat Hospital", "University West Pet Clinic"]
  drNames = [["Dr. Jessica Merk", "Dr. Sara Niemand", "Dr. Samantha Frahm", "Dr. Katherine Wiedmann"], ["Dr. Garlock", "Dr. Trepp", "Dr. Kelsey Stickler", "Dr. Rachel Spah", "Dr. Nareddy"], ["Dr. Kim Bollinger", "Dr. Rebecca Stone", "Dr. Allyson Jacobi", "Dr. Michelle Heyer"], ["Dr. Lori Clark", "Dr. Lisa Takes"]]
  links = ["https://www.ashworthpet.com/", "https://www.banfield.com/en/locations/veterinarians/ia/clive/clv", "https://www.animalcareclinicwest.com/staff", "https://www.universitywestpetclinic.com/staff"]
  phoneNum = ["(515) 337-2643", "(515) 457-1381", "(515) 224-4368", "(515) 223-8185"]
  address = ["5902 Ashworth Rd West Des Moines, IA 50266, US", "11101 University Ave, Clive, IA 50325", "2900 University Ave. Suite 340 West Des Moines, IA50266", "8145 University Blvd. Clive, IA50325"]
  animalsAccepted = [["Dog", "Cat", "Fish", "Bird", "Rodent", "Lizard", "Snake", "Amphibian", "Turtle", "Tortoise", "Rabbit", "Hedgehog", "Invertebrate", "Ferret"],["Dog", "Cat", "Fish", "Bird", "Rodent", "Lizard", "Snake", "Amphibian", "Rabbit"], ["Dog", "Cat", "Hedgehog", "Ferret"], ["Dog", "Cat", "Fish", "Bird", "Rodent", "Lizard", "Snake", "Amphibian", "Rabbit"]] 
  hours = [["M-F: 8:00AM - 6:00PM", "S: 8:00AM - 12:00PM", "SUN: Closed"], ["M-F: 8:00AM - 6:00PM", "S: 8:00AM - 5:00PM", "SUN: Closed"], ["M-F: 7:00AM - 7:00PM", ": Closed"], ["M-F: 7:30AM - 6:00PM", "S: 8:00AM - 12:00PM", "SUN: Closed"]]
  emergencyCare = ["Yes", "Yes", "Yes", "No"]
  starRating = [4.8, 4.1, 4.7, 4.8]
  
  vetInfo = []
  for clinic_names, drNames, links, phoneNum, address, animalsAccepted, hours, emergencyCare, starRating in zip(clinic_names, drNames, links, phoneNum, address, animalsAccepted, hours, emergencyCare, starRating):
    doc = {"clinic_name": clinic_names, "dr_name": drNames, "links": links, "phone_number": phoneNum, "address": address, "animals_accepted": animalsAccepted, "hours": hours, "emergency_care": emergencyCare, "rating": starRating}
    vetInfo.append(doc)
   ## person_collection.insert_one(doc)
  vetsCollection.insert_many(vetInfo)
  
create_documents()

