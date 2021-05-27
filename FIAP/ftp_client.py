from ftplib import *

ftp = FTP ('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario = input('Type your user: ')
senha = input('Type password: ')

ftp.login(usuario, senha)
print("Current working directory: ", ftp.pwd())
ftp.cwd('pub')
print("Current directory: ", ftp.pwd())
print(ftp.retrlines('LIST'))

ftp.quit()

