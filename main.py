import json
import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from pystyle import Colors, Colorate, Center, Box
import os
import urllib.parse
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

with open("config.json", "r") as file:
    config = json.load(file)
    whatsapp = config.get("whatsapp") # https://rapidapi.com/airaudoeduardo/api/whatsapp-data1/pricing get from here

def main():
 os.system('cls')

 banner = """
        _                 _                 
       | |               (_)                
  _ __ | |__   ___  _ __  _ _   _ _ __ ___  
 | '_ \| '_ \ / _ \| '_ \| | | | | '_ ` _ \ 
 | |_) | | | | (_) | | | | | |_| | | | | | |
 | .__/|_| |_|\___/|_| |_|_|\__,_|_| |_| |_|
 | |                                        
 |_|                                        
-----------------------------------------------------
            1. Search Phone Number
            2. Formatting Information 
            3. Exit"""
 print((Colorate.Vertical(Colors.blue_to_purple, banner,1)))
 option = input(Colors.blue + "input > ")
 if option == "1":
  phone_number = input(Colors.purple + "Phone Number: ")
  parsed_number = phonenumbers.parse(phone_number)
        
  country = geocoder.region_code_for_number(parsed_number)
  location = geocoder.description_for_number(parsed_number, "en")
        
  phone_carrier = carrier.name_for_number(parsed_number, "en")
        
  timezones = timezone.time_zones_for_number(parsed_number)
        
  is_valid = phonenumbers.is_valid_number(parsed_number)
        
  is_possible = phonenumbers.is_possible_number(parsed_number)
  print(Colors.pink + "Phone Number Information")      
  print(Colors.purple + "-----------------------------------------------------")
  print(Colors.pink + f"Country: {country}")
  print(Colors.pink + f"Location: {location}")
  print(Colors.pink + f"Phone Carrier: {phone_carrier}")
  print(Colors.pink + f"Timezones: {timezones}")
  print(Colors.pink + f"Validation: {is_valid}")
  print(Colors.purple + "-----------------------------------------------------")
  results = bing_search(phone_number)
        
  if results:
    dorks = {}
    for idx, url in enumerate(results, 1):
        dorks[idx] = url  
    else:
     print("")

  print(Colors.pink + "Google Dorks")
  print(Colors.purple + "-----------------------------------------------------")
  print(Colors.pink + "\n".join([f"{key}: {value}" for key, value in dorks.items()]))
  print(Colors.purple + "-----------------------------------------------------\n")



  headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
}

  json_data = {
    'flow_token': 'g;174216975781989414:-1742169834411:7Mw2FG5FuO3BTkP2efReVRdc:1',
    'subtask_inputs': [
        {
            'subtask_id': 'PasswordResetBegin',
            'enter_text': {
                'text': f'{phone_number}',
                'link': 'next_link',
            },
        },
    ],

}

  response = requests.post('https://api.x.com/1.1/onboarding/task.json', headers=headers, json=json_data)
  if response == "200":
    twitter =  f"Twitter | Valid | {phone_number}"
  else:
    twitter = f"Twitter | Invalid | {phone_number}"



  params = {
    'v': '5.245',
    'client_id': '7913379',
}

  data = {
    'phone': f'{phone_number}',
    'supported_ways': 'call_in',
    'supported_ways_settings': 'callreset_preview_enabled',
    'sid': '',
    'super_app_token': '',
    'device_id': 'Rf6rzquyU8xC4pJBTid1q',
    'external_device_id': '',
    'service_group': '',
    'lang': 'en',
    'auth_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzaWQiOiJOR1kxWkRkaU5UWmxPVEUwWldKak4yVXlPVEUzWlRVMCIsImhhc2giOiI5MThjOTkyNjEzNDM2N2EzIiwiZXhwIjoxNzQyMTc1Njk1fQ.50X3Wu0DlCgeU0thE3_E-HhGZavzU3CxPWlN6WgtmF8',
    'allow_callreset': '1',
    'access_token': '',
}

  response = requests.post('https://api.vk.com/method/auth.validatePhone', params=params, data=data)
  if "Invalid phone number" in response.json():
    vk = f"VK | Valid | {phone_number}"
  else:
    vk = f"VK | Invalid | {phone_number}"

  json_data = {
    'operationName': 'verifyPrivateCredentialIceGql',
    'variables': {
        'clientInfo': {
            'ipAddress': '',
            'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            'ctxId': 'AAFrWW27KXt_0lQ4ym8jg9U8OjHzmW8tQTjC03dxv-rb4EWMgLtVOEXKUvLROd0yO6_dKUpB8jtVAQgJO1D20YU=',
            'fnId': '409c2b4e39ff4d10894facda92410197',
            'tenant': 'VENMO',
            'rData': '%7B%22fn_sync_data%22%3A%22%257B%2522SC_VERSION%2522%253A%25222.0.4%2522%252C%2522syncStatus%2522%253A%2522data%2522%252C%2522f%2522%253A%2522409c2b4e39ff4d10894facda92410197%2522%252C%2522s%2522%253A%2522ICE_VENMO_LOGIN_PUBLIC_PAGE%2522%252C%2522chk%2522%253A%257B%2522ts%2522%253A1742173295346%252C%2522eteid%2522%253A%255B12091660924%252C4640414558%252C5598850264%252C1959267190%252C19974998887%252C-6751128671%252C3316050543%252C477798967%255D%252C%2522tts%2522%253A165%257D%252C%2522dc%2522%253A%2522%257B%255C%2522screen%255C%2522%253A%257B%255C%2522colorDepth%255C%2522%253A24%252C%255C%2522pixelDepth%255C%2522%253A24%252C%255C%2522height%255C%2522%253A1440%252C%255C%2522width%255C%2522%253A2560%252C%255C%2522availHeight%255C%2522%253A1392%252C%255C%2522availWidth%255C%2522%253A2560%257D%252C%255C%2522ua%255C%2522%253A%255C%2522Mozilla%252F5.0%2520(Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F134.0.0.0%2520Safari%252F537.36%255C%2522%257D%2522%252C%2522wv%2522%253Afalse%252C%2522web_integration_type%2522%253A%2522WEB_REDIRECT%2522%252C%2522cookie_enabled%2522%253Atrue%252C%2522d%2522%253A%257B%2522rDT%2522%253A%252226763%252C25687%252C25616%253A37007%252C35935%252C35862%253A31881%252C30816%252C30739%253A16509%252C15451%252C15370%253A6261%252C5208%252C5124%253A47243%252C46195%252C46108%253A6257%252C5214%252C5124%253A52362%252C51324%252C51231%253A6254%252C5219%252C5124%253A21622%252C20590%252C20493%253A42109%252C41088%252C40986%253A26739%252C25722%252C25617%253A52352%252C51340%252C51230%253A47227%252C46221%252C46110%253A42103%252C41100%252C40985%253A26733%252C25733%252C25616%253A11363%252C10366%252C10247%253A36977%252C35983%252C35862%253A11361%252C10370%252C10247%253A21605%252C20620%252C20493%253A17958%252C44%2522%257D%257D%22%7D',
        },
        'credentials': {
            'publicCredential': {
                'credentialValue': f'{phone_number}',
                'credentialType': 'PHONE',
            },
            'credentialValue': 'awrwabtaTBAFWGBAWBTaty',
            'credentialType': 'PASSWORD',
        },
    },
    'query': 'mutation verifyPrivateCredentialIceGql($clientInfo: ClientDetailsInput!, $credentials: PrivateCredentialsInput!) {\n  login {\n    verifyPrivateCredential(clientInfo: $clientInfo, credentials: $credentials) {\n      accessToken\n      fnId\n      idToken\n      rememberedUser\n      visitorId\n      returnUri {\n        href\n        rel\n        method\n        __typename\n      }\n      ctxId\n      identityChallenges {\n        id\n        type\n        status\n        errorCode\n        choices {\n          id\n          cardType\n          phoneType\n          value\n          unmaskedValue\n          answerChoices\n          questionId\n          text\n          countryCode\n          pin\n          __typename\n        }\n        canAddPhone\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
}

  response = requests.post('https://id.venmo.com/idapps/graphql', headers=headers, json=json_data)
  if "failed" or "missing" in response.json():
    venmo = f"Venmo | Invalid | {phone_number}"
  else:
    venmo = f"Venmo | Valid | {phone_number}"
  
  number = phone_number.lstrip("+")
  url = f"https://whatsapp-data1.p.rapidapi.com/number/{number}"

  headers = {
	"x-rapidapi-key": f"{whatsapp}",
	"x-rapidapi-host": "whatsapp-data1.p.rapidapi.com"
}

  response = requests.get(url, headers=headers)

  if "isBusiness" in response.json():
    whatsappx = f"WhatsApp | Valid | {phone_number}"
    wuser = response.json()["pushname"]
    wprofile = response.json()["profilePic"]
    wabout = response.json()["about"]
  else:
    whatsappx = f"WhatsApp | Invalid | {phone_number}"
    wuser = "User | NONE"
    wprofile = "Profile | NONE"
    wabout = "About | NONE"
    

  print(Colors.pink + "Social Media")
  print(Colors.purple + "-----------------------------------------------------")
  print(Colors.pink + twitter)
  print(Colors.pink + vk)
  print(Colors.pink + venmo)
  print(Colors.pink + whatsappx)
  print(Colors.purple + "-----------------------")
  print(Colors.purple + wuser)
  print(Colors.purple + wprofile)
  print(Colors.purple + wabout)
  print(Colors.purple + "-----------------------")
  print(Colors.purple + "-----------------------------------------------------\n")

  input("Press Enter To Return to menu ")
  main()
         




 if option == "2":
  print(Colors.purple + "To input the phone number in proper format please do it like so")
  print(Colors.purple + "[+countrycode][first3][second3][last4]")
  print(Colors.pink + "ex. +18255665543")
  input(Colors.blue + "Press Enter To Return To Main Menu ")
  main()
 if option == "3":
  os.system('exit')


def bing_search(query):

    query = urllib.parse.quote(query)
    url = f"https://www.bing.com/search?q={query}"

    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        search_results = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('http') or href.startswith('www'):
                search_results.append(href)

        return search_results
    else:
        print(f"Error: {response.status_code}")
        return []

if __name__ == "__main__":
 main()