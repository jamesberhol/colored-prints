from colorama import init,Fore, Back, Style
import sys
init()

def green(word):
 n = list(word)
 d = len(n)
    
 if d == 2:
   sys.stdout.write(Fore.LIGHTGREEN_EX + n[0] + "" + Fore.GREEN + n[1])
 if d == 3:
   sys.stdout.write(Fore.LIGHTGREEN_EX + n[0]+ "" + Fore.GREEN + n[1] +  "" + Fore.LIGHTGREEN_EX + n[2])
 if d == 4:
   sys.stdout.write(Fore.LIGHTGREEN_EX + n[0]+ "" + Fore.GREEN + n[1] + "" + Fore.LIGHTGREEN_EX + n[2] + "" + Fore.GREEN + n[3])
 if d == 5:
   sys.stdout.write(Fore.LIGHTGREEN_EX + n[0]+ "" + Fore.GREEN + n[1] + "" +  Fore.LIGHTGREEN_EX + n[2] + "" + Fore.GREEN + n[3] + "" + Fore.LIGHTGREEN_EX + n[4])
 if d == 6:
   sys.stdout.write(Fore.LIGHTGREEN_EX + n[0]+ "" + Fore.GREEN + n[1] + "" +Fore.LIGHTGREEN_EX + n[2] + "" +Fore.GREEN + n[3] + "" +Fore.LIGHTGREEN_EX + n[4] + "" +Fore.GREEN + "" +Fore.LIGHTGREEN_EX + n[5])
 if d == 7:
    sys.stdout.write(Fore.LIGHTGREEN_EX + n[0]+ "" + Fore.GREEN + n[1] + "" +Fore.LIGHTGREEN_EX + n[2] + "" +Fore.GREEN + n[3] + "" +Fore.LIGHTGREEN_EX + n[4] + "" +Fore.GREEN + n[5] + "" +Fore.LIGHTGREEN_EX + n[6])
 if d == 8:
   sys.stdout.write(Fore.LIGHTGREEN_EX + n[0]+ "" + Fore.GREEN + n[1] + "" +Fore.LIGHTGREEN_EX + n[2] + "" +Fore.GREEN + n[3] + "" +Fore.LIGHTGREEN_EX + n[4] + "" +Fore.GREEN + n[5] + "" +Fore.LIGHTGREEN_EX + n[6] + "" +Fore.GREEN+ n[7])
 if d == 9:
   sys.stdout.write(Fore.LIGHTGREEN_EX + n[0]+ "" + Fore.GREEN + n[1] + "" +Fore.LIGHTGREEN_EX + n[2] + "" +Fore.GREEN + n[3] + "" +Fore.LIGHTGREEN_EX + n[4] + "" +Fore.GREEN + n[5] + "" +Fore.LIGHTGREEN_EX + n[6] + "" +Fore.GREEN + n[7]+ "" +Fore.LIGHTGREEN_EX + n[8])
 if d == 10:
   sys.stdout.write(Fore.LIGHTGREEN_EX + n[0]+ "" + Fore.GREEN + n[1] + "" +Fore.LIGHTGREEN_EX + n[2] + "" +Fore.GREEN + n[3] + "" +Fore.LIGHTGREEN_EX + n[4] + "" +Fore.GREEN + n[5] + "" +Fore.LIGHTGREEN_EX + n[6] + "" +Fore.GREEN + n[7]+ "" +Fore.LIGHTGREEN_EX + n[8]+ "" +Fore.GREEN + n[9])
def red(word):
 n = list(word)
 d = len(n)
    
 if d == 2:
   sys.stdout.write(Fore.LIGHTRED_EX + n[0] + "" + Fore.RED + n[1])
 if d == 3:
   sys.stdout.write(Fore.LIGHTRED_EX + n[0]+ "" + Fore.RED + n[1] +  "" + Fore.LIGHTRED_EX + n[2])
 if d == 4:
   sys.stdout.write(Fore.LIGHTRED_EX + n[0]+ "" + Fore.RED + n[1] + "" + Fore.LIGHTRED_EX + n[2] + "" + Fore.RED + n[3])
 if d == 5:
   sys.stdout.write(Fore.LIGHTRED_EX + n[0]+ "" + Fore.RED + n[1] + "" +  Fore.LIGHTRED_EX + n[2] + "" + Fore.RED + n[3] + "" + Fore.LIGHTRED_EX + n[4])
 if d == 6:
   sys.stdout.write(Fore.LIGHTRED_EX + n[0]+ "" + Fore.RED + n[1] + "" +Fore.LIGHTRED_EX + n[2] + "" +Fore.RED + n[3] + "" +Fore.LIGHTRED_EX + n[4] + "" +Fore.RED + "" +Fore.LIGHTRED_EX + n[5] + "" +Fore.RED + n[6])
 if d == 7:
    sys.stdout.write(Fore.LIGHTRED_EX + n[0]+ "" + Fore.RED + n[1] + "" +Fore.LIGHTRED_EX + n[2] + "" +Fore.RED + n[3] + "" +Fore.LIGHTRED_EX + n[4] + "" +Fore.RED + n[5])
 if d == 8:
   sys.stdout.write(Fore.LIGHTRED_EX + n[0]+ "" + Fore.RED + n[1] + "" +Fore.LIGHTRED_EX + n[2] + "" +Fore.RED + n[3] + "" +Fore.LIGHTRED_EX + n[4] + "" +Fore.RED + n[5] + "" +Fore.LIGHTRED_EX + n[6] + "" +Fore.RED+ n[7])
 if d == 9:
   sys.stdout.write(Fore.LIGHTRED_EX + n[0]+ "" + Fore.RED + n[1] + "" +Fore.LIGHTRED_EX + n[2] + "" +Fore.RED + n[3] + "" +Fore.LIGHTRED_EX + n[4] + "" +Fore.RED + n[5] + "" +Fore.LIGHTRED_EX + n[6] + "" +Fore.RED + n[7]+ "" +Fore.LIGHTRED_EX + n[8])
 if d == 10:
   sys.stdout.write(Fore.LIGHTRED_EX + n[0]+ "" + Fore.RED + n[1] + "" +Fore.LIGHTRED_EX + n[2] + "" +Fore.RED + n[3] + "" +Fore.LIGHTRED_EX + n[4] + "" +Fore.RED + n[5] + "" +Fore.LIGHTRED_EX + n[6] + "" +Fore.RED + n[7]+ "" +Fore.LIGHTRED_EX + n[8]+ "" +Fore.RED + n[9])

def yellow(word):
 n = list(word)
 d = len(n)
    
 if d == 2:
   sys.stdout.write(Fore.LIGHTYELLOW_EX + n[0] + "" + Fore.YELLOW + n[1])
 if d == 3:
   sys.stdout.write(Fore.LIGHTYELLOW_EX + n[0]+ "" + Fore.YELLOW + n[1] +  "" + Fore.LIGHTYELLOW_EX + n[2])
 if d == 4:
   sys.stdout.write(Fore.LIGHTYELLOW_EX + n[0]+ "" + Fore.YELLOW + n[1] + "" + Fore.LIGHTYELLOW_EX + n[2] + "" + Fore.YELLOW + n[3])
 if d == 5:
   sys.stdout.write(Fore.LIGHTYELLOW_EX + n[0]+ "" + Fore.YELLOW + n[1] + "" +  Fore.LIGHTYELLOW_EX + n[2] + "" + Fore.YELLOW + n[3] + "" + Fore.LIGHTYELLOW_EX + n[4])
 if d == 6:
   sys.stdout.write(Fore.LIGHTYELLOW_EX + n[0]+ "" + Fore.YELLOW + n[1] + "" +Fore.LIGHTYELLOW_EX + n[2] + "" +Fore.YELLOW + n[3] + "" +Fore.LIGHTYELLOW_EX + n[4] + "" +Fore.YELLOW + "" +Fore.LIGHTYELLOW_EX + n[5] + "" +Fore.YELLOW + n[6])
 if d == 7:
    sys.stdout.write(Fore.LIGHTYELLOW_EX + n[0]+ "" + Fore.YELLOW + n[1] + "" +Fore.LIGHTYELLOW_EX + n[2] + "" +Fore.YELLOW + n[3] + "" +Fore.LIGHTYELLOW_EX + n[4] + "" +Fore.YELLOW + n[5])
 if d == 8:
   sys.stdout.write(Fore.LIGHTYELLOW_EX + n[0]+ "" + Fore.YELLOW + n[1] + "" +Fore.LIGHTYELLOW_EX + n[2] + "" +Fore.YELLOW + n[3] + "" +Fore.LIGHTYELLOW_EX + n[4] + "" +Fore.YELLOW + n[5] + "" +Fore.LIGHTYELLOW_EX + n[6] + "" +Fore.YELLOW+ n[7])
 if d == 9:
   sys.stdout.write(Fore.LIGHTYELLOW_EX + n[0]+ "" + Fore.YELLOW + n[1] + "" +Fore.LIGHTYELLOW_EX + n[2] + "" +Fore.YELLOW + n[3] + "" +Fore.LIGHTYELLOW_EX + n[4] + "" +Fore.YELLOW + n[5] + "" +Fore.LIGHTYELLOW_EX + n[6] + "" +Fore.YELLOW + n[7]+ "" +Fore.LIGHTYELLOW_EX + n[8])
 if d == 10:
   sys.stdout.write(Fore.LIGHTYELLOW_EX + n[0]+ "" + Fore.YELLOW + n[1] + "" +Fore.LIGHTYELLOW_EX + n[2] + "" +Fore.YELLOW + n[3] + "" +Fore.LIGHTYELLOW_EX + n[4] + "" +Fore.YELLOW + n[5] + "" +Fore.LIGHTYELLOW_EX + n[6] + "" +Fore.YELLOW + n[7]+ "" +Fore.LIGHTYELLOW_EX + n[8]+ "" +Fore.YELLOW + n[9])

def blue(word):
 n = list(word)
 d = len(n)
    
 if d == 2:
   sys.stdout.write(Fore.LIGHTBLUE_EX + n[0] + "" + Fore.BLUE + n[1])
 if d == 3:
   sys.stdout.write(Fore.LIGHTBLUE_EX + n[0]+ "" + Fore.BLUE + n[1] +  "" + Fore.LIGHTBLUE_EX + n[2])
 if d == 4:
   sys.stdout.write(Fore.LIGHTBLUE_EX + n[0]+ "" + Fore.BLUE + n[1] + "" + Fore.LIGHTBLUE_EX + n[2] + "" + Fore.BLUE + n[3])
 if d == 5:
   sys.stdout.write(Fore.LIGHTBLUE_EX + n[0]+ "" + Fore.BLUE + n[1] + "" +  Fore.LIGHTBLUE_EX + n[2] + "" + Fore.BLUE + n[3] + "" + Fore.LIGHTBLUE_EX + n[4])
 if d == 6:
   sys.stdout.write(Fore.LIGHTBLUE_EX + n[0]+ "" + Fore.BLUE + n[1] + "" +Fore.LIGHTBLUE_EX + n[2] + "" +Fore.BLUE + n[3] + "" +Fore.LIGHTBLUE_EX + n[4] + "" +Fore.BLUE + "" +Fore.LIGHTBLUE_EX + n[5])
 if d == 7:
    sys.stdout.write(Fore.LIGHTBLUE_EX + n[0]+ "" + Fore.BLUE + n[1] + "" +Fore.LIGHTBLUE_EX + n[2] + "" +Fore.BLUE + n[3] + "" +Fore.LIGHTBLUE_EX + n[4] + "" +Fore.BLUE + n[5] + "" +Fore.LIGHTBLUE_EX + n[6])
 if d == 8:
   sys.stdout.write(Fore.LIGHTBLUE_EX + n[0]+ "" + Fore.BLUE + n[1] + "" +Fore.LIGHTBLUE_EX + n[2] + "" +Fore.BLUE + n[3] + "" +Fore.LIGHTBLUE_EX + n[4] + "" +Fore.BLUE + n[5] + "" +Fore.LIGHTBLUE_EX + n[6] + "" +Fore.BLUE+ n[7])
 if d == 9:
   sys.stdout.write(Fore.LIGHTBLUE_EX + n[0]+ "" + Fore.BLUE + n[1] + "" +Fore.LIGHTBLUE_EX + n[2] + "" +Fore.BLUE + n[3] + "" +Fore.LIGHTBLUE_EX + n[4] + "" +Fore.BLUE + n[5] + "" +Fore.LIGHTBLUE_EX + n[6] + "" +Fore.BLUE + n[7]+ "" +Fore.LIGHTBLUE_EX + n[8])
 if d == 10:
   sys.stdout.write(Fore.LIGHTBLUE_EX + n[0]+ "" + Fore.BLUE + n[1] + "" +Fore.LIGHTBLUE_EX + n[2] + "" +Fore.BLUE + n[3] + "" +Fore.LIGHTBLUE_EX + n[4] + "" +Fore.BLUE + n[5] + "" +Fore.LIGHTBLUE_EX + n[6] + "" +Fore.BLUE + n[7]+ "" +Fore.LIGHTBLUE_EX + n[8]+ "" +Fore.BLUE + n[9])

def magenta(word):
 n = list(word)
 d = len(n)
    
 if d == 2:
   sys.stdout.write(Fore.LIGHTMAGENTA_EX + n[0] + "" + Fore.MAGENTA + n[1])
 if d == 3:
   sys.stdout.write(Fore.LIGHTMAGENTA_EX + n[0]+ "" + Fore.MAGENTA + n[1] +  "" + Fore.LIGHTMAGENTA_EX + n[2])
 if d == 4:
   sys.stdout.write(Fore.LIGHTMAGENTA_EX + n[0]+ "" + Fore.MAGENTA + n[1] + "" + Fore.LIGHTMAGENTA_EX + n[2] + "" + Fore.MAGENTA + n[3])
 if d == 5:
   sys.stdout.write(Fore.LIGHTMAGENTA_EX + n[0]+ "" + Fore.MAGENTA + n[1] + "" +  Fore.LIGHTMAGENTA_EX + n[2] + "" + Fore.MAGENTA + n[3] + "" + Fore.LIGHTMAGENTA_EX + n[4])
 if d == 6:
   sys.stdout.write(Fore.LIGHTMAGENTA_EX + n[0]+ "" + Fore.MAGENTA + n[1] + "" +Fore.LIGHTMAGENTA_EX + n[2] + "" +Fore.MAGENTA + n[3] + "" +Fore.LIGHTMAGENTA_EX + n[4] + "" +Fore.MAGENTA + "" +Fore.LIGHTMAGENTA_EX + n[5])
 if d == 7:
    sys.stdout.write(Fore.LIGHTMAGENTA_EX + n[0]+ "" + Fore.MAGENTA + n[1] + "" +Fore.LIGHTMAGENTA_EX + n[2] + "" +Fore.MAGENTA + n[3] + "" +Fore.LIGHTMAGENTA_EX + n[4] + "" +Fore.MAGENTA + n[5] + "" +Fore.LIGHTMAGENTA_EX + n[6])
 if d == 8:
   sys.stdout.write(Fore.LIGHTMAGENTA_EX + n[0]+ "" + Fore.MAGENTA + n[1] + "" +Fore.LIGHTMAGENTA_EX + n[2] + "" +Fore.MAGENTA + n[3] + "" +Fore.LIGHTMAGENTA_EX + n[4] + "" +Fore.MAGENTA + n[5] + "" +Fore.LIGHTMAGENTA_EX + n[6] + "" +Fore.MAGENTA+ n[7])
 if d == 9:
   sys.stdout.write(Fore.LIGHTMAGENTA_EX + n[0]+ "" + Fore.MAGENTA + n[1] + "" +Fore.LIGHTMAGENTA_EX + n[2] + "" +Fore.MAGENTA + n[3] + "" +Fore.LIGHTMAGENTA_EX + n[4] + "" +Fore.MAGENTA + n[5] + "" +Fore.LIGHTMAGENTA_EX + n[6] + "" +Fore.MAGENTA + n[7]+ "" +Fore.LIGHTMAGENTA_EX + n[8])
 if d == 10:
   sys.stdout.write(Fore.LIGHTMAGENTA_EX + n[0]+ "" + Fore.MAGENTA + n[1] + "" +Fore.LIGHTMAGENTA_EX + n[2] + "" +Fore.MAGENTA + n[3] + "" +Fore.LIGHTMAGENTA_EX + n[4] + "" +Fore.MAGENTA + n[5] + "" +Fore.LIGHTMAGENTA_EX + n[6] + "" +Fore.MAGENTA + n[7]+ "" +Fore.LIGHTMAGENTA_EX + n[8]+ "" +Fore.MAGENTA + n[9])

def cyan(word):
 n = list(word)
 d = len(n)
    
 if d == 2:
   sys.stdout.write(Fore.LIGHTCYAN_EX + n[0] + "" + Fore.CYAN + n[1])
 if d == 3:
   sys.stdout.write(Fore.LIGHTCYAN_EX + n[0]+ "" + Fore.CYAN + n[1] +  "" + Fore.LIGHTCYAN_EX + n[2])
 if d == 4:
   sys.stdout.write(Fore.LIGHTCYAN_EX + n[0]+ "" + Fore.CYAN + n[1] + "" + Fore.LIGHTCYAN_EX + n[2] + "" + Fore.CYAN + n[3])
 if d == 5:
   sys.stdout.write(Fore.LIGHTCYAN_EX + n[0]+ "" + Fore.CYAN + n[1] + "" +  Fore.LIGHTCYAN_EX + n[2] + "" + Fore.CYAN + n[3] + "" + Fore.LIGHTCYAN_EX + n[4])
 if d == 6:
   sys.stdout.write(Fore.LIGHTCYAN_EX + n[0]+ "" + Fore.CYAN + n[1] + "" +Fore.LIGHTCYAN_EX + n[2] + "" +Fore.CYAN + n[3] + "" +Fore.LIGHTCYAN_EX + n[4] + "" +Fore.CYAN + "" +Fore.LIGHTCYAN_EX + n[5])
 if d == 7:
    sys.stdout.write(Fore.LIGHTCYAN_EX + n[0]+ "" + Fore.CYAN + n[1] + "" +Fore.LIGHTCYAN_EX + n[2] + "" +Fore.CYAN + n[3] + "" +Fore.LIGHTCYAN_EX + n[4] + "" +Fore.CYAN + n[5] + "" +Fore.LIGHTCYAN_EX + n[6])
 if d == 8:
   sys.stdout.write(Fore.LIGHTCYAN_EX + n[0]+ "" + Fore.CYAN + n[1] + "" +Fore.LIGHTCYAN_EX + n[2] + "" +Fore.CYAN + n[3] + "" +Fore.LIGHTCYAN_EX + n[4] + "" +Fore.CYAN + n[5] + "" +Fore.LIGHTCYAN_EX + n[6] + "" +Fore.CYAN+ n[7])
 if d == 9:
   sys.stdout.write(Fore.LIGHTCYAN_EX + n[0]+ "" + Fore.CYAN + n[1] + "" +Fore.LIGHTCYAN_EX + n[2] + "" +Fore.CYAN + n[3] + "" +Fore.LIGHTCYAN_EX + n[4] + "" +Fore.CYAN + n[5] + "" +Fore.LIGHTCYAN_EX + n[6] + "" +Fore.CYAN + n[7]+ "" +Fore.LIGHTCYAN_EX + n[8])
 if d == 10:
   sys.stdout.write(Fore.LIGHTCYAN_EX + n[0]+ "" + Fore.CYAN + n[1] + "" +Fore.LIGHTCYAN_EX + n[2] + "" +Fore.CYAN + n[3] + "" +Fore.LIGHTCYAN_EX + n[4] + "" +Fore.CYAN + n[5] + "" +Fore.LIGHTCYAN_EX + n[6] + "" +Fore.CYAN + n[7]+ "" +Fore.LIGHTCYAN_EX + n[8]+ "" +Fore.CYAN + n[9])
