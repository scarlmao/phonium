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
    # while True avoids recursive calls to main
    while True:
        os.system('cls')
        banner = r"""
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
            3. Exit
            """
        print((Colorate.Vertical(Colors.blue_to_purple, banner, 1)))
        option = input(Colors.blue + "input > ")
        if option == "2":
            print(Colors.purple + "IMPORTANT! The phone number must be input properly for Phonium to work.")
            print(
                Colors.pink + "Start with the country code, then the area code, then the exchange, then the last 4 digits")
            print(Colors.blue + "[countrycode][first3][second3][last4]")
            print(Colors.purple + "ex. 18255665543")
            input(Colors.pink + "Do NOT add any spaces, hyphens or parentheses.")
            input(Colors.blue + "In other words, don't use any non-numeric characters.")
            input(Colors.purple + "Press Enter To Return To Main Menu.")
            continue
        if option == "3":
            print('Thank you for using Phonium! Goodbye.')
            break
        if option =="1":
            phone_number = "+" + input(Colors.purple + "Phone Number: ").lstrip("+")
            # if this works as intended, then the user does not have to enter a + ... but if they do, it'll trim it out
            try:
                parsed_number = phonenumbers.parse(phone_number)
                # Anything is possible, but this phone number might not be.
                is_possible = phonenumbers.is_possible_number(parsed_number)
                if not is_possible:
                    print(Colors.red + "This number is not even structurally valid.\n Try again?")
                    input("Press any key to return to the main menu")
                    continue

                is_valid = phonenumbers.is_valid_number(parsed_number)
                if not is_valid:
                    print(Colors.red + "This number is possible, but not valid.\n Try again?")
                    input("Press any key to return to the main menu")
                    continue
    # if the number is possible and valid, let's find out more!
                # Metadata
                country = geocoder.region_code_for_number(parsed_number)
                location = geocoder.description_for_number(parsed_number, "en")
                phone_carrier = carrier.name_for_number(parsed_number, "en")
                timezones = timezone.time_zones_for_number(parsed_number)
                print(Colors.pink + "Phone Number Metadata")
                print(Colors.purple + "-----------------------------------------------------")
                print(Colors.pink + f"Country: {country}")
                print(Colors.pink + f"Location: {location}")
                print(Colors.pink + f"Phone Carrier: {phone_carrier}")
                print(Colors.pink + f"Timezones: {timezones}")
                print(Colors.pink + f"Validation: {is_valid}")
                print(Colors.purple + "-----------------------------------------------------")
                print(Colors.pink + "Google (Bing) Dorks")
                print(Colors.purple + "-----------------------------------------------------")
                print(
                    Colors.blue + "Use with discretion and some salt: These are just web hits containing this number string \n")


                results = bing_search(phone_number)
                if results:
                    dorks = {}
                    for idx, url in enumerate(results, 1):
                        dorks[idx] = url
                else:
                    print("No dorks found. Maybe just a few nerds.")
                print(Colors.pink + "\n".join([f"{key}: {value}" for key, value in dorks.items()]))
                print(Colors.purple + "-----------------------------------------------------\n")
                headers = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',}
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
                # --- Twitter ---
                response = requests.post('https://api.x.com/1.1/onboarding/task.json', headers=headers, json=json_data)
                if response.status_code == 200:
                    twitter = f"Twitter | Valid | {phone_number}"
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
           # --- VK ---
                response = requests.post('https://api.vk.com/method/auth.validatePhone', params=params, data=data)
                vk_response = response.json()
                if "Invalid phone number" in str(vk_response):
                    vk = f"VK | Invalid | {phone_number}"
                else:
                    vk = f"VK | Valid | {phone_number}"
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
                'query': 'mutation verifyPrivateCredentialIceGql($clientInfo: ClientDetailsInput!, $credentials: PrivateCredentialsInput!) {\n  login {\n    verifyPrivateCredential(clientInfo: $clientInfo, credentials: $credentials) {\n      accessToken\n      fnId\n      idToken\n      rememberedUser\n      visitorId\n      returnUri {\n        href\n        rel\n        method\n        __typename\n      }\n      ctxId\n      identityChallenges {\n        id\n        type\n        status\n        errorCode\n        choices {\n          id\n          cardType\n          phoneType\n          value\n          unmaskedValue\n          answerChoices\n          questionId\n          text\n          countryCode\n          pin\n          __typename\n        }\n        canAddPhone\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',}
                # --- Venmo ---
                response = requests.post('https://id.venmo.com/idapps/graphql', headers=headers, json=json_data)
                #venmo_json = response.json()
                if "failed" in str(response) or "missing" in str(response):
                    venmo = f"Venmo | Invalid | {phone_number}"
                else:
                    venmo = f"Venmo | Valid | {phone_number}"
                # --- WhatsApp ---
                #number = phone_number
                url = f"https://whatsapp-data1.p.rapidapi.com/number/{phone_number.lstrip('+')}"

                headers = {
                    "x-rapidapi-key": f"{whatsapp}",
                    "x-rapidapi-host": "whatsapp-data1.p.rapidapi.com"
                }
                response = requests.get(url, headers=headers)
                whatsapp_data = response.json()
                print(whatsapp_data)  # added the print statement for troubleshooting
                if whatsapp_data.get("isUser"):
                    if whatsapp_data.get("isBusiness"):
                        whatsappx = f"WhatsApp | Valid (Business) | {phone_number}"
                    else:
                        whatsappx = f"WhatsApp | Valid (Personal) | {phone_number}"
                    wuser = whatsapp_data.get("pushname") or "User | NONE"
                    wprofile = whatsapp_data.get("profilePic", "Profile | NONE")
                    wabout = whatsapp_data.get("about", "About | NONE")
                else:
                    whatsappx = f"WhatsApp | Invalid | {phone_number}"
                    wuser = "User | NONE"
                    wprofile = "Profile | NONE"
                    wabout = "About | NONE"

                print(Colors.pink + "Social Media Affiliated with this number")
                print(Colors.purple + "-----------------------------------------------------")
                print(Colors.pink + twitter)
                print(Colors.pink + vk)
                print(Colors.pink + venmo)
                print(Colors.pink + whatsappx)
                print(Colors.purple + "-----------------------")
                print(Colors.purple + wuser)
                print(Colors.purple + "-----------------------")
                print(Colors.purple + f"User profile pic url:\n {wprofile}")
                print(Colors.purple + wabout)
                print(Colors.purple + "-----------------------")
                print(Colors.purple + "-----------------------------------------------------\n")

                print(Colors.pink + "Press Enter To Return to menu")
                _ = input()
                continue

            except phonenumbers.NumberParseException:
                print(Colors.red + "Could not parse the number. Please enter a valid number.")
                input("Press Enter to return to the main menu.")
                continue


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