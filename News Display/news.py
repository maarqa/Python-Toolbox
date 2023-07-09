import requests

data = input(
  "Please Choose One of The Following \n 1.Headlines    2.Weather    3.Sports     4.War    5.Science      6.Technology  7. Any other topic: ")

if data == "1":
  no = input("Write the amount of news you want to see:.     ")
  response = requests.get(
    "https://newsapi.org/v2/top-headlines?country=us&apiKey=bd2a4ba27bf8437195d5d67ec7c305fb"
  )
  print("\n")
  for i in range(int(no)):
    print(response.json()["articles"][i]["title"], "\n")
    print(response.json()["articles"][i]["description"], "\n ------------")

else:
   if data== "2" :
          topic = "Weather"
   elif data== "3"  :
       topic = "Sports"
   elif data== "4" : 
       topic = "War" 
   elif data== "5"  :
       topic = "Science"
   elif data== "6":
       topic = "Technology" 
   elif data== "7":
       topic = input("Please Input The Topic:      ")
   
   no = input("Write the amount of news you want to see:.     ")
  
   response = requests.get(
    f"httpimport requests

data = input(
  "Please Choose One of The Following \n 1.Headlines    2.Weather    3.Sports     4.War    5.Science      6.Technology  7. Any other topic: ")

if data == "1":
  no = input("Write the amount of news you want to see:.     ")
  response = requests.get(
    "https://newsapi.org/v2/top-headlines?country=us&apiKey=bd2a4ba27bf8437195d5d67ec7c305fb"
  )
  print("\n")
  for i in range(int(no)):
    print(response.json()["articles"][i]["title"], "\n")
    print(response.json()["articles"][i]["description"], "\n ------------")

else:
   if data== "2" :
          topic = "Weather"
   elif data== "3"  :
       topic = "Sports"
   elif data== "4" : 
       topic = "War" 
   elif data== "5"  :
       topic = "Science"
   elif data== "6":
       topic = "Technology" 
   elif data== "7":
       topic = input("Please Input The Topic:      ")
   
   no = input("Write the amount of news you want to see:.     ")
  
   response = requests.get(
    f"https://newsapi.org/v2/everything?q={topic.lower()}&apiKey=bd2a4ba27bf8437195d5d67ec7c305fb"
  )
   print("\n")
   for i in range(int(no)):
    print(response.json()["articles"][i]["title"], "\n")
    print(response.json()["articles"][i]["description"], "\n ------------")

s://newsapi.org/v2/everything?q={topic.lower()}&apiKey=bd2a4ba27bf8437195d5d67ec7c305fb"
  )
   print("\n")
   for i in range(int(no)):
    print(response.json()["articles"][i]["title"], "\n")
    print(response.json()["articles"][i]["description"], "\n ------------")

