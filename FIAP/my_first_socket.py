import socket

resp = "S"

while (resp == "S"):
    url = input("Input the URL: ")
    ip = socket.gethostbyname(url)
    print("This is IP from of the URL you entered: ", ip)
    res = input("Press <S> to continue or another key to leave : ").upper()