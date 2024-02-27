# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:06:02 2023

@author: Dell
"""

capitals={
 "France":"Paris",
 "Germany":'Berlin'   
}
capitals

travel_log={
"France":["Paris","Lillie","Dijon"],
"Germany":["Berlin","Hamburg","Stuttgart"]    

}

travel_log

travel_details={
"France":{"cities_visited":["Paris","Lillie","Dijon"],"total_visits":12},
"Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5}    
    
}
travel_details
################################
#nested dictinaries inside list
travel_details=[
{
 "country":"France",
 "cities_visited":["Paris","Lillie","Dijon"],
 "total_visits":12
 },
{
 "country":"Germany",
 "cities_visited":["Berlin","Hamburg","Stuttgart"],
 "total_visits":5
 }    
    
]
travel_details
##########################################
#write a method which will add new dictionary in travel_details which 
#comrises of country :Rassia,cities_visited:Moskow,saint Petersburg
#total_visits:7

def add_new_country(country_visited,cities_visited,total_visits):
    new_country={}
    new_country["country"]=country_visited
    new_country["cities_visited"]=cities_visited
    new_country["total_visits"]=total_visits
    travel_details.append(new_country)
    
    
add_new_country("Russia",["Moscow","Saint Petersburg"],7)  
travel_details 
#####################################
number=int(input("Enter the number "))
if (number % 2==0):
    print("The number is even")
else:
    print("The number is odd")    
    
    
    
    
    
    
    
    