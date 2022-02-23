import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(f"{Fore.GREEN}green is one of the colors, there are many other colors!")
List_of_hydrophobic_residues = ['G','A','V','L','I','P','F','M','W']
List_of_polar_residues = ['S','T','C','N','Q','Y']
List_of_Acidic_residues = ['D','E']
List_of_Basic_residues = ['R','K','H']
x = input("Enter your residue: ")
if x in List_of_hydrophobic_residues:
    print(f"{Fore.GREEN}"+x+" is a hydrphobic residue.")
else:
    if x in List_of_polar_residues:
        print(f"{Fore.RED}"+x+" is a polar residue.")
if x in List_of_Acidic_residues:
        print(f"{Fore.BLUE}"+x+" is an acidic residue.")
if x in List_of_Basic_residues:
        print(f"{Fore.WHITE}"+x+" is a basic residue.")
