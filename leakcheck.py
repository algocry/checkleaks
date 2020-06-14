import requests
from bs4 import BeautifulSoup as scrapper
import sys

class bcolors:
    HEADER = '\033[1m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

headers = {
    'Host': 'pwndb2am4tzkvold.onion.pet',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '69',
    'Origin': 'http://pwndb2am4tzkvold.onion.pet',
    'Connection': 'close',
    'Referer': 'http://pwndb2am4tzkvold.onion.pet/',
    'Upgrade-Insecure-Requests': '1',
}

'''
def purpose(purpose_input, input):
    if purpose_input == 'mail':

    else if purpose_input == 'password':
    else:
        print('input type not defined')
    return data
'''

def main(item_type, supply):
    if item_type == "0":
        #data for search_by_email
        raw_data = str(supply).split('@')
        data = 'luser='+ raw_data[0] + '&domain=' + raw_data[1] +'&luseropr=0&domainopr=0&submitform=em'
    elif item_type == "1":
        #data for search_password
        data = 'password='+ str(supply) +'&submitform=pw'
    else:
        print(bcolors.FAIL + 'Input not defined' + bcolors.ENDC)
        exit(0)

    response = requests.post('http://pwndb2am4tzkvold.onion.pet/', headers=headers, data=data)

    soup = scrapper(response.content, 'html.parser')
    lists = soup.findAll('section')[3]
    try:
        return lists.text
    except:
        return soup.text
    #print(sys.argv[1])


def mech():
    
    item = {0: 'mail', 1: 'password'}
    
    try:
        choice = int(input(bcolors.OKBLUE + 'Enter the option no. of data: \n [0] Mail \n [1] Password\n [2] Exit\nOption:' + bcolors.ENDC))
        try:
            pass_data = input(bcolors.OKBLUE + 'Enter the ' + str(item[choice]) + ' to check: ' + bcolors.ENDC)
        except:
            exit(0)

        data = main(str(choice), pass_data)
        print(bcolors.OKGREEN + data + bcolors.ENDC)
        print(bcolors.OKBLUE + ' [0] Dump data in a file \n [1] Go back \n [2] Exit' + bcolors.ENDC)
        choice_ = input(bcolors.OKBLUE +'Option: ' + bcolors.ENDC)

        if choice_ == '0':
            raw_filename = input(bcolors.OKBLUE + 'File name to save: '+ bcolors.ENDC)
            filename = raw_filename + '_' + str(item[choice]) + '.txt'
            file = open(filename, 'w')         
            file.write(data)
            file.close()
            print(bcolors.OKGREEN + 'File is saved in same directory with name {}.'.format(raw_filename) + bcolors.ENDC)
            print()

        elif choice_ == '1':
            print()
            print()
            mech()

        else:
            exit(0)

    except Exception as e:
        print(bcolors.FAIL + e + bcolors.ENDC)
        exit(0)

def banner():
    print(bcolors.HEADER + 'CheckLeaks v0.1' + bcolors.ENDC)
    print(bcolors.HEADER + 'coded by: 0x0is1 (https://github.com/0x0is1)'+ bcolors.ENDC)
    print(bcolors.HEADER +'With StrinTH (https://github.com/StrinTH)'+ bcolors.ENDC)
    print('')
    print('')

if __name__ == "__main__":
    try:
        if sys.argv[1] is '-v' or '--version':
            banner()
    except:
        banner()
        while True:
            mech()
