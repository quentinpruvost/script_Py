#installer nmap avec pip3 install python-nmap
import nmap
import os
sc = nmap.PortScanner()
print("""
      
  __                   __   
_/  |_  ____   _______/  |_ 
\   __\/ __ \ /  ___/\   __\ 
 |  | \  ___/ \___ \  |  |     
 |__|  \___  >____  > |__|  
           \/     \/        

      """)

def main():
    n = input("1- network scanner\n2- Vulnabilities Detection \n3- Exploit=\nMerci de choisir un chiffre : ")
    
  # Si l'utilisateur Choisie 1 alors executer la commande nmap  
    if n=='1':
        nmap()
    
def nmap():
     print("****************bienvenu sur le Network scanner****************")
     print("***************************************************************")
     ip = input("\n Merci de rentré l'adress IP")
     
     # Affiche les infos sur le scan 
     sc.scan(ip,'1-1024')
     print(sc.scaninfo())
     print(sc[ip]['tcp'].keys())
def vuln():
    print("*************bienvenu sur le Vulnabilities scanner**************")
    print("****************************************************************")
    ip = input("\n Merci de rentré l'adress IP")
    print(os.system('nmap -sV --script=vulscan.nse ' =ip))
# Permet d'exucuter cette fonction par défaut
if __name__ == "__main__":
    main()
