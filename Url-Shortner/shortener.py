import requests

def shorten_url(url):
     url = url
     api = "YOUR_API_KEY"
     api_url = f"https://cutt.ly/api/api.php?key={api}&short={url}"#&name=htpdpco"
     data = requests.get(api_url).json()["url"]
     if data["status"] == 7:
         # OK, get shortened URL
         shortened_url = data["shortLink"]
         print("\nShortened URL:", shortened_url , "\n")
     else:
         print("[!] Error Shortening URL:", data)

def expand_url(url):
     response = requests.get(url)
     print(response.url)
while True:
     print('''Url Shortener 👨‍💻
---------------------
1.Shorten a Url
2. Expand Url
3.Exit''')
     opt = input()
     if opt =="1":
          url =input("Enter the url:")
          shorten_url(url)
     elif opt =="2":
          url =input("Enter the url:")
          expand_url(url)
     else:
          print("Exiting")
          break
     
     
