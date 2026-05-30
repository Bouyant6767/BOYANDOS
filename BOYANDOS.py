ver = "Ver2026May29"
pyver = "28"
usr = "LiveUser"
#WORK IN PROCESS:
#   all done 
#   why are u staring here
import os
import time
import mimetypes
#######################################
os.system('cls' if os.name == 'nt' else 'clear')
print("Installation of BOYANDOS", ver)
print("~~~")
print("Welcome to the installation of BOYANDOS!")
options = ['1','2','3']
option = ''
while not option in options:
    print("Select your options to install...")
    print("1. Use without installation.")
    print("2. Install BOYANDOS to computer")
    print("3. Exit the installer")
    option = input()
    if not option in options:
        os.system('cls' if os.name == 'nt' else 'clear')
########################################
if option == '1':
    print('Getting things ready...')
    import time
    import mimetypes
    helpdata = []
    def printhelp(a, p = 1):
        if p == 1:
            print(a)
        if not a in helpdata:
            helpdata.append(a)
    printhelp("version() - Returns the current version of BOYANDOS", 0)
    printhelp("load(p) - Loads a .burger program (p)", 0)
    printhelp("echo(a) - Prints something (a) on the screen", 0)
    printhelp("halt(t) - Waits for t seconds", 0)
    printhelp("contents(f) - Shows the contents of a file (f)", 0)
    printhelp("clear() - Clears everything on the screen.", 0)
    printhelp("goodbye() - Exits the terminal.", 0)
    printhelp("overwrite(f, d) - Replace all data in the file (f) with new data (d)", 0)
    printhelp("appendf(f, d, p) - Add data (d) at character position (p) to file (f)", 0)
    printhelp("makefile(f, d) - Creates a file (f) with data (d)", 0)
    printhelp("delfile(f) - Deletes a file (f)", 0)
    printhelp("pythonmode() - Switches into Python", 0)
    printhelp("pythonrun(c) - Runs a Python command (c)", 0)
    printhelp("systemrun(c) - Runs a command (c) in a subshell", 0)
    printhelp("cd(q) - Change directory to (q).")
    printhelp("ls() - Prints out the list of files and folders in the current directory.")
    printhelp("if_elif_else(ifcondition, ifbody, elifcondition, elifbody, elsebody) - If-elif-else command", 0)
    printhelp("if_else(ifcondition, ifbody, elsebody) - If-else command", 0)
    printhelp("rep(int, body) - Repeat for an amount of times", 0)
    printhelp("repuntil(condition, body) - Repeat until a condition is met.", 0)
    def _help(a = ''):
        if a == '' :
            print("List of commands:")
            printhelp("version() - Returns the current version of BOYANDOS")
            printhelp("load(p) - Loads a .burger program (p)")
            printhelp("echo(a) - Prints something (a) on the screen")
            printhelp("halt(t) - Waits for t seconds")
            printhelp("contents(f) - Shows the contents of a file (f)")
            printhelp("clear() - Clears everything on the screen.")
            printhelp("goodbye() - Exits the terminal.")
            print()
            print("DANGEROUS COMMANDS:")
            printhelp("overwrite(f, d) - Replace all data in the file (f) with new data (d)")
            printhelp("appendf(f, d, p) - Add data (d) at position (p) to file (f)")
            printhelp("makefile(f, d) - Creates a file (f) with data (d)")
            printhelp("makefol(n) - Creates a folder named (n).")
            printhelp("delfile(f) - Deletes a file (f)")
            printhelp("delfol(f) - Deletes a folder (f)") 
            printhelp("pythonmode() - Switches into Python")
            printhelp("pythonrun(c) - Runs a command (c) in Python")
            printhelp("systemrun(c) - Runs a command (c) in a subshell")
            printhelp("cd(q) - Change directory to (q).")
            printhelp("ls() - Prints out the list of files and folders in the current directory.")
            print()
            print("Loops and condition-checking commands (beta):")
            printhelp("if_elif_else(ifcondition, ifbody, elifcondition, elifbody, elsebody) - If-elif-else command")
            printhelp("if_else(ifcondition, ifbody, elsebody) - If-else command", 0)
            printhelp("rep(int, body) - Repeat for an amount of times")
            printhelp("repuntil(condition, body) - Repeat until a condition is met.")
            print("WARNING: all bodies and conditions must be a string!")
            print()
            print("If you are struggling with a command, please run _help('keyword').")
            print("More commands soon!")
        else:
            h_searchdata = []
            print("Searching...")
            for i in helpdata:
                if a in i:
                    h_searchdata.append(i)
            if len(h_searchdata) > 0:
                for i in h_searchdata:
                    print(i)
            else:
                print("Nothing found!")
    print("Done defining _help.")
    print("Defining version...")
    def version():
        print(ver)
    print("Done defining version.")
    print("Defining echo...")
    def echo(a):
        print(a)
    print("Done defining echo.")
    print("Defining halt...")
    def halt(t):
        time.sleep(t)
    print("Done defining halt.")
    print("Defining contents...")
    def contents(f):
        
        a = os.path.join(d, f)
        if os.path.isfile(a):
            if os.path.getsize(a) == 0:
                print("Empty File.")
            else:
                with open(a, 'r') as z:
                    y = z.read()
                    f_contents = y.splitlines()
                for i in f_contents:
                    print(i)
        else:
            print('File does not exist')
    print("Done defining contents.")
    print("Defining clear...")
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    print("Done defining clear.")
    print("Defining goodbye...")
    def goodbye():
        exit()
    print("Done defining goodbye.")
    print("Defining overwrite...")
    def overwrite(f, h):
        
        a = os.path.join(d, f)
        if os.path.isfile(a):
            with open(a, 'w') as z:
                z.write(h)
        else:
            print('File does not exist')
    print("Done defining overwrite.")
    print("Defining appendf...")
    def appendf(f, h, p):
        
        a = os.path.join(d, f)
        if os.path.isfile(a):
            with open(a, 'r') as z:
                existing = z.read()
            p = int(p)
            if p < 0 or p > len(existing):
                print(f"Position out of range. File has {len(existing)} characters.")
                return
            new_contents = existing[:p] + h + existing[p:]
            with open(a, 'w') as z:
                z.write(new_contents)
        else:
            print('File does not exist.')
    print("Done defining appendf.")
    print("Defining makefile...")
    def makefile(f, h):
        
        a = os.path.join(d, f)
        if not os.path.isfile(a):
            with open(a, 'w') as z:
                z.write(h)
        else:
            print('File already exists.')
    print("Done defining makefile.")
    print("Defining makefol...")
    def makefol(n):
        
        a = os.path.join(d, n)
        if not os.path.isdir(a):
            os.makedirs(a)
        else:
            print('Folder already exists.')
    print("Done defining makefol.")
    print("Defining delfile...")
    def delfile(f):
        
        a = os.path.join(d, f)
        if os.path.isfile(a):
            os.remove(a)
        else:
            print('File does not exist.')
    print("Done defining delfile.")
    print("Defining delfol...")
    def delfol(f):
        
        a = os.path.join(d, f)
        if os.path.isdir(a):
            os.rmdir(a)
        else:
            print("Folder does not exist.")
    print("Done defining delfol.")
    print("Defining pythonmode...")
    pymode = False
    def pythonmode():
        global pymode
        pymode = True
        print(f"BoyAnMINIPY build {pyver}\nType exitpymode() to exit BoyAnMINIPY.")
    print("Done defining pythonmode.")
    print("Defining pythonrun...")
    def pythonrun(c):
        exec(c)
    print("Done defining pythonrun.")
    print("Defining systemrun...")
    def systemrun(c):
        os.system(c)
    print("Done defining systemrun.")
    print("Defining if_elif_else...")
    allowed = {}
    def if_elif_else(ifcon, ifbody, elifcon = False, elifbody = '', elsebody = ''):
        if eval(str(ifcon), {'__builtins__': __builtins__}, allowed):
            exec(str(ifbody), {'__builtins__': {}}, allowed)
        elif elifcon and eval(str(elifcon), {'__builtins__': __builtins__}, allowed):
            exec(str(elifbody), {'__builtins__': {}}, allowed)
        else:
            exec(str(elsebody), {'__builtins__': {}}, allowed)
    print("Done defining if_elif_else.")
    print("Defining if_else...")
    def if_else(ifcon, ifbody, elsebody = ''):
        if eval(str(ifcon), {'__builtins__': __builtins__}, allowed):
            exec(str(ifbody), {'__builtins__': {}}, allowed)
        else:
            exec(str(elsebody), {'__builtins__': {}}, allowed)
    print('Done defining if_else.')
    print("Defining rep...")
    def rep(inte, body):
        for i in range(eval(str(inte), {'__builtins__': __builtins__}, allowed)):
           exec(str(body), {'__builtins__': {}}, allowed)
    print("Done defining rep.")
    print("Defining repuntil...")
    def repuntil(cond, body):
        while not eval(str(cond), {'__builtins__': __builtins__}, allowed):
            exec(str(body), {'__builtins__': {}}, allowed)
    print("Done defining repuntil.")
    print("Defining load...")
    def load(p):
        a = os.path.join(os.getcwd(), p)
        if os.path.isfile(a):
            if os.path.getsize(a) == 0:
                print("Empty File.")
            else:
                with open(a, 'r') as z:
                    exec(z.read(), {'__builtins__': {}}, allowed)
        else:
            print('File does not exist')
    print("Done defining load.")
    print("Defining cd...")
    def cd(q):
        try:
            os.chdir(q)
        except Exception as e:
            print("Uh oh, looks like you've messed something up! Please check your spelling.")
            print(f"Specific details about the error: {e}")
    print("Done defining cd.")
    print("Defining ls...")
    def ls():
            import mimetypes
            try:
                with os.scandir(os.getcwd()) as entries:
                    for entry in entries:
                        file_type = "Directory: " if entry.is_dir() else ""
                        print(f"{file_type}{entry.name}")
            except Exception as e:
                print(f"Could not list directory: {e}")
    print("Done defining ls.")
    print("Finishing things up...")
    def exitpymode():
        global pymode
        pymode = False
    pymode_globals = {'__builtins__': __builtins__, 'exitpymode': exitpymode}
    allowed = {
    'echo': echo,
    'load': load,
    'halt': halt,
    'version': version,
    'clear': clear,
    'contents': contents,
    'overwrite': overwrite,
    'appendf': appendf,
    'makefile': makefile,
    'makefol': makefol,
    'delfile': delfile,
    'delfol': delfol,
    'pythonmode': pythonmode,
    'exitpymode': exitpymode,
    'pythonrun': pythonrun,
    'systemrun': systemrun,
    '_help': _help,
    'if_elif_else': if_elif_else,
    'if_else': if_else,
    'rep': rep,
    'repuntil': repuntil,
    'ls': ls,
    'cd': cd,
    'goodbye': goodbye
    }
    ###########################################################################
    input("All done! Press [Enter] to enter BOYANDOS.")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Welcome to BOYANDOS {ver}!")
    print("To get help, please type _help() then press enter two times.")
    while True:
        if not pymode:
            try:
                p = ''
                a = input(f"{usr}_BOYANDOS:{os.getcwd()}$")
                while len(a) > 0:
                    p = f"""{p}
{a}"""
                    a = input('...')
                exec(p, {'__builtins__': {}}, allowed)
            except Exception as e:
                print(f'Uh oh, you typed a command that BOYANDOS hates looking at. Because it has a secret "{e}" inside it.')
        else:
            try:
                p = ''
                a = input(f"{usr}!MINIPY@~")
                while len(a) > 0:
                    p = f"""{p}
{a}"""
                    a = input('...')
                exec(p, pymode_globals)
            except Exception as e:
                print(f"Bad command with error: {e}")
##########################################################
elif option == '2':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Welcome to the BOYANDOS {ver} Installation wizard!")
    while True:
        print("What is your name?")
        usrname = input('>>>')
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(usrname) > 0:    
            if any(i in usrname.lower() for i in ["bùi_hải_hà","bùi hải hà","bùi_hải hà", "bùi hải_hà", "daly", "dalo"]) :
                print("It is detected that you are Daly.")
                print("Due to special reasons, Daly cannot install BOYANDOS.")
                print("Thank you for choosing BOYANDOS.")
                import time
                time.sleep(5)
                exit()
            else:
                if any(i in usrname for i in [" ", "!", "$", "@", "~", "/", "\\"]):
                    print("Your username must not have one of these characters:")        
                    print("[space], !, $, @, ~, / and \\.")
                    print("Please type your name again.")
                else:
                    break
        else:
            print("Your name cannot be blank.")
    os.system('cls' if os.name == 'nt' else 'clear')
    installtodir = input(f"Please enter the directory to install BOYANDOS (If you leave it blank, it will be saved to the main OS' disk): ")
    if len(installtodir) == 0:
        if os.name == "nt":
            installtodir = r"C:\\"
        else:
            installtodir = r"/"
    while not os.path.isdir(installtodir):
        os.system('cls' if os.name == 'nt' else 'clear')
        installtodir = input(f"Invalid directory, please enter it again: ")
        if len(installtodir) == 0:
            if os.name == "nt":
                installtodir = r"C:\\"
            else:
                installtodir = r"/"
    confirm_opts = ["y", "Y", "n", "N"]
    confirm = "sixsevennn"
    while not confirm in confirm_opts: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Confirm installation?")
        print("[y/n]")
        confirm = input()
        if not confirm in confirm_opts:
            os.system('cls' if os.name == 'nt' else 'clear')
    if confirm in ['n', 'N']:
        os.system('cls' if os.name == 'nt' else 'clear')
        input('Cancelled. Please press enter to exit.')
        exit()
    print("Creating folder named 'BOYANDOS'...")
    try:
        dosdir = os.path.join(installtodir, "BOYANDOS")
        os.makedirs(dosdir)
    except FileExistsError:
        pass
    except Exception as e:
        print(f"Installation error: {e}")
        input("Press [Enter] to exit.")
        exit()
    print("Done.")
    print("Creating file named 'main.py'...")
    try:
        with open(__file__, 'r', encoding='utf-8') as current_file:
            lines = current_file.readlines()
        shell_code = []
        capture = False
        for line in lines:
            if "if option == '1':" in line:
                capture = True
                continue
            if "elif option == '2':" in line:
                capture = False
                break
            if capture:
                shell_code.append(line[4:] if line.startswith("    ") else line)
        with open(os.path.join(dosdir, "main.py"), 'w', encoding='utf-8') as z:
            z.write(f'usr = "{usrname}"\nver = "{ver}"\npyver = "{pyver}"\nimport os\nos.chdir("{dosdir}")\n')
            z.writelines(shell_code)
    except Exception as e:
        print(f"Installation error: {e}")
        input("Press [Enter] to exit.")
        exit()
    print("Done.")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("All done! Just go to ", os.path.join(dosdir, "main.py"), " to open BOYANDOS!")
elif option == '3':
    print("Thank you for choosing BOYANDOS.")
    input("Press ENTER to exit.")
    exit()      
