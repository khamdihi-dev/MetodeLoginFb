# -----------[ AUTHOR ] ----------#
Author    = "Khamdihi"
Instagram = "khamdihi_dev"
WhatsApp  = "0857-2941-6714"
Github    = 'https://github.com/khamdihi-dev'

#-----------[ MODULE ]-------------#
import re, requests, time, os, random
from time import time

#--------[ HOST MOBILE, TYPE VALIDATE ]---------#
class Mobile:

   def __init__(self,userid, pwek):
       self.session = requests.Session()
       self.user = userid
       self.pswd = pwek
       self.nunu()

   def nunu(self):
       self.link = self.session.get(f'https://mobile.facebook.com/login?locale=id_ID&rdr=1&access_token=None&_rdc=2&_rdr&refsrc=deprecated')
       self.head = {
         "Host": "m.facebook.com",
         "content-length": "73",
         "cache-control": "max-age=0",
         "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
         "sec-ch-ua-mobile": "?1",
         "sec-ch-ua-platform": '"Android"',
         "upgrade-insecure-requests": "1",
         "origin": "https://m.facebook.com",
         "content-type": "application/x-www-form-urlencoded",
         "user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
         "sec-fetch-site": "same-origin",
         "sec-fetch-mode": "navigate",
         "sec-fetch-user": "?1",
         "sec-fetch-dest": "document",
         "referer": "https://m.facebook.com/login?locale=id_ID&rdr=1&access_token=None&refsrc=deprecated&_rdc=3&_rdr",
         "accept-encoding": "gzip, deflate, br",
         "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
       }
       self.name = ["lsd","jazoest","Gabut Doang Gw:(","Tutor Jadi Idaman mu :-"]
       self.data = {
         "lsd":re.search(f'name="{self.name[0]}" value="(.*?)"', str(self.link.text)).group(1),
         "jazoest":re.search(f'name="{self.name[1]}" value="(.*?)"', str(self.link.text)).group(1),
         "uid":self.user,
         "next":"https://m.facebook.com/login/save-device/",
         "flow":"login_no_pin",
         "encpass":f"#PWD_BROWSER:0:{int(time())}:{self.pswd}"
       }
       self.kuki = (";").join([self.key+'='+self.value for self.key, self.value in self.session.cookies.get_dict().items()])
       self.nfnf = self.session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=self.data, headers=self.head, cookies={'cookie':self.kuki}, allow_redirects=False)
       if "c_user" in self.session.cookies.get_dict():
           self.fika = (";").join([self.key+'='+self.value for self.key, self.value in self.session.cookies.get_dict().items()])
           print(f'\n > Login berhasil, cookie kamu ada di bawah ini\n > Cookie : {self.fika}')
           exit(None)

       elif "checkpoint" in self.session.cookies.get_dict().keys():
           print('\n > Akun anda terkena "checkpoint"')
           exit(None)

       else:
           print('\n > Kata sandi salah atau "SPAM"')
           exit(None)

#--------[ HOST M FACEBOOK, TYPE ASYNC ]-------#
class Async:

   def __init__(self,username, password):
       self.session = requests.Session()
       self.user = username
       self.pswd = password
       self.nunu()

   def nunu(self):
       self.link = self.session.get('https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1')
       self.head = {
         "Host": "m.facebook.com",
         "content-length": "2076",
         "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(self.link.text)).group(1),
         "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
         "content-type": "application/x-www-form-urlencoded",
         "sec-ch-ua-mobile": "?1",
         "user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
         "sec-ch-ua-platform": '"Android"',
         "accept": "*/*",
         "origin": "https://m.facebook.com",
         "sec-fetch-site": "same-origin",
         "sec-fetch-mode": "cors",
         "sec-fetch-dest": "empty",
         "referer": "https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1",
         "accept-encoding": "gzip, deflate, br",
         "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
       }
       self.fika = ['m_ts','li','jazoest','Woy','GabutBangetCok','LahKNTL','MiripSiTapiGakPercayaGw!']
       self.data = {
         "m_ts":re.search(f'name="{self.fika[0]}" value="(.*?)"',str(self.link.text)).group(1),
         "li":re.search(f'name="{self.fika[1]}" value="(.*?)"',str(self.link.text)).group(1),
         "try_number":"0",
         "unrecognized_tries":"0",
         "email":self.user,
         "prefill_contact_point":None,
         "prefill_source":None,
         "prefill_type":None,
         "first_prefill_source":None,
         "first_prefill_type":None,
         "had_cp_prefilled":False,
         "had_password_prefilled":False,
         "is_smart_lock":False,
         "bi_xrwh":"0",
         "bi_wvdp":'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
         "encpass":f"#PWD_BROWSER:0:{int(time())}:{self.pswd}",
         "fb_dtsg":None,
         "jazoest":re.search(f'name="{self.fika[2]}" value="(.*?)"',str(self.link.text)).group(1),
         "lsd":self.head["x-fb-lsd"]
       }
       nnu = self.session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=self.data, headers=self.head, allow_redirects=True)
       if "c_user" in self.session.cookies.get_dict():
           self.fika = (";").join([self.key+'='+self.value for self.key, self.value in self.session.cookies.get_dict().items()])
           print(f'\n > Login berhasil, cookie kamu ada di bawah ini\n > Cookie : {self.fika}')
           exit(None)

       elif "checkpoint" in self.session.cookies.get_dict().keys():
           print('\n > Akun anda terkena "checkpoint"')
           exit(None)

       else:
           print('\n > Kata sandi salah atau "SPAM"')
           exit(None)

class Reguler:

   def __init__(self, username, password):
       self.session = requests.Session()
       self.user = username
       self.pswd = password
       self.nunu()

   def nunu(self):
       link = self.session.get("https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8&refsrc=deprecated&ref_component=mbasic_footer&_rdr")
       data = {
          "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
          "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
          "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
          "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
          "try_number": "0",
          "unrecognized_tries": "0",
          "email":self.user,
          "masked_cp":f"+628*******{random.randint(100,999)}",
          "pass":self.pswd,
          "login":"Masuk",
          "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1)
       }

       head = {
          "x-requested-with": "mark.via.gp",
          "Host": "m.facebook.com",
          "content-length": f"{str(len(data))}",
          "cache-control": "max-age=0",
          "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
          "sec-ch-ua-mobile": "?0",
          "sec-ch-ua-platform": '"Android"',
          "upgrade-insecure-requests": "1",
          "origin": "https://free.facebook.com",
          "content-type": "application/x-www-form-urlencoded",
          "user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
          "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          "sec-fetch-site": "same-origin",
          "sec-fetch-mode": "navigate",
          "sec-fetch-user": "?1",
          "sec-fetch-dest": "document",
          "referer": "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8&refsrc=deprecated&ref_component=mbasic_footer&_rdr"
       }
       nnu = self.session.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl", data=data, headers=head, allow_redirects=False)
       if "c_user" in self.session.cookies.get_dict():
           self.fika = (";").join([self.key+'='+self.value for self.key, self.value in self.session.cookies.get_dict().items()])
           print(f'\n > Login berhasil, cookie kamu ada di bawah ini\n > Cookie : {self.fika}')
           exit(None)

       elif "checkpoint" in self.session.cookies.get_dict().keys():
           print('\n > Akun anda terkena "checkpoint"')
           exit(None)

       else:
           print('\n > Kata sandi salah atau "SPAM"')
           exit(None)

class Menu:

   def __init__(self):
       os.system('clear')
       print('''
[ List methode login fb from meta ]\n
 1. Tes methode async
 2. Tes methode reguler
 3. Tes methode validate
 4. Penjelasan user agent
 5. Keluar\n ''')
       yxz = input(' > Pilih : ')
       if yxz in ['5','05']:quit()
       elif yxz in ['4','04']:os.system('clear');print('\r [ Apa yang di makzud dengan user agent ]\n\n > Oke, User Agent adalah script yang dikirimkan oleh web browser ke web server yang kita tuju, atau ke setiap situs yang kita kunjungi, jadi setiap situs yang kita kunjungi dapat mengetahui Browser dan sistem operasi yang kita gunakan sehingga konten dapat disesuaikan dengan jenis sistem operasi kita');quit()
       elif yxz in ['3','03']:
            ytta = input('\n > Gunakan tanda | sebagai pemisah contoh username|password\n > data akun : ')
            try:Mobile(ytta.split('|')[0], ytta.split('|')[1])
            except IndexError:exit('\n > Pemisahan salah, anda harus memasukan data seperti ini contoh : 10000004|kata sandi anda')

       elif yxz in ['2','02']:
            ytta = input('\n > Gunakan tanda | sebagai pemisah contoh username|password\n > data akun : ')
            try:Reguler(ytta.split('|')[0], ytta.split('|')[1])
            except IndexError:exit('\n > Pemisahan salah, anda harus memasukan data seperti ini contoh : 10000004|kata sandi anda')

       elif yxz in ['1','01']:
            ytta = input('\n > Gunakan tanda | sebagai pemisah contoh username|password\n > data akun : ')
            try:Async(ytta.split('|')[0], ytta.split('|')[1])
            except IndexError:exit('\n > Pemisahan salah, anda harus memasukan data seperti ini contoh : 10000004|kata sandi anda')

       else:Menu()

if __name__ == '__main__':
   Menu()


# Hi, mau ngapain?
