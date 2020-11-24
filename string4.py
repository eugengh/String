cnp=str(input("CNP: "))
nr=5
if len(cnp) ==13:
    for i in cnp:
        if (ord(i)<=57) and (ord(i)>=48):
            nr=0
        else:
            nr=1
else:
    print("error")
if nr==0:
    print("Da")
elif nr==1:
    print("Nu")