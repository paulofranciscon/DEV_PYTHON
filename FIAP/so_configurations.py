import platform
import getpass
from datetime import datetime

print("Hostname:....................", platform.node())
print("Architecture:................", platform.architecture())
print("Operational System:..........", platform.system())
print("Version OS:..................", platform.release())
print("Processor:...................", platform.processor())
print("Machine:.....................", platform.machine())
print("Version:.....................", platform.version())
print("Version Python:..............", platform.python_version())
print("Date machine is: ............", datetime.now())
usuario = getpass.getuser()
senha = getpass.getpass("Digite your password: ")


if usuario == "paulo.franciscon" and senha == '1234':
    print("Bem Vindo: ", usuario)
else:
    print("Usuario ou senha inválidos")

