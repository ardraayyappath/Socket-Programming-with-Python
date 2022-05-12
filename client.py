# Import socket module
import socket               

# Create a socket object
s = socket.socket()         
port = 5206               
s.connect(('127.0.0.1', port))
res = "EECE7374 INTR 002172340"
s.send(res.encode( 'utf-8'))

# receive data from the server
exp = s.recv(4096).decode( 'utf-8' )
exp = exp.encode()
while exp.startswith(b'EECE7374 SUCC')|exp.startswith(b'EECE7374 RSLT')|exp.startswith(b'EECE7374 EXPR'):
#while s.startswith("EECE7374 SUCC")|s.startswith("EECE7374 RSLT")|s.startswith("EECE7374 EXPR"):


    if (exp.startswith(b'EECE7374 SUCC')):
        print(exp)
        break
    
    
    #exp = exp.encode()
    exp=exp.split(b' ')[2:] 
    #exp = exp.decode()
    mystr=""
    for x in exp:
        x = x.decode()
        mystr+=x
    
    # printing original string
    #print("The original string is : " + test_str)
    
    # Expression evaluation in String
    # Using eval()
    res = eval(mystr)
   # "EECE7374 RSLT".append(res)
     
    res = "EECE7374 RSLT "+str(res)
    s.send(res.encode( 'utf-8'))
    exp = s.recv(4096)
    try:
        exp = exp.decode()
    except (UnicodeDecodeError, AttributeError):
        pass
    # printing result
    #print("The evaluated result is : " + str(res))

# close the connection
s.close()           