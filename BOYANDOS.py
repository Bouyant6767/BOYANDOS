ver = "Ver2026May23"
import os
import time
#######################################
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
        if os.path.isfile(f):
            if os.path.getsize(f) == 0:
                print("Empty File.")
            else:
                with open(f, 'r') as z:
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
    def overwrite(f, d):
        if os.path.isfile(f):
            with open(f, 'w') as z:
                z.write(d)
        else:
            print('File does not exist')
    print("Done defining overwrite.")
    print("Defining appendf...")
    def appendf(f, d, p):
        if os.path.isfile(f):
            with open(f, 'r') as z:
                existing = z.read()
            p = int(p)
            if p < 0 or p > len(existing):
                print(f"Position out of range. File has {len(existing)} characters.")
                return
            new_contents = existing[:p] + d + existing[p:]
            with open(f, 'w') as z:
                z.write(new_contents)
        else:
            print('File does not exist.')
    print("Done defining appendf.")
    print("Defining makefile...")
    def makefile(f, d):
        if not os.path.isfile(f):
            with open(f, 'w') as z:
                z.write(d)
        else:
            print('File already exists.')
    print("Done defining makefile.")
    print("Defining makefol...")
    def makefol(n):
        if not os.path.isdir(n):
            os.makedirs(n)
        else:
            print('Folder already exists.')
    print("Done defining makefol.")
    print("Defining delfile...")
    def delfile(f):
        if os.path.isfile(f):
            os.remove(f)
        else:
            print('File does not exist.')
    print("Done defining delfile.")
    print("Defining delfol...")
    def delfol(f):
        if os.path.isdir(f):
            os.rmdir(f)
        else:
            print("Folder does not exist.")
    print("Done defining delfol.")
    print("Defining pythonmode...")
    pymode = False
    def pythonmode():
        global pymode
        pymode = True
        print("""BoyAnMINIPY build 17
        Type exitpymode() to exit BoyAnMINIPY.""")
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
        if eval(str(ifcon), {'__builtins__': {}}, allowed):
            exec(str(ifbody), {'__builtins__': {}}, allowed)
        elif elifcon and eval(str(elifcon), {'__builtins__': {}}, allowed):
            exec(str(elifbody), {'__builtins__': {}}, allowed)
        else:
            exec(str(elsebody), {'__builtins__': {}}, allowed)
    print("Done defining if_elif_else.")
    print("Defining if_else...")
    def if_else(ifcon, ifbody, elsebody = ''):
        if eval(str(ifcon), {'__builtins__': {}}, allowed):
            exec(str(ifbody), {'__builtins__': {}}, allowed)
        else:
            exec(str(elsebody), {'__builtins__': {}}, allowed)
    print('Done defining if_else.')
    print("Defining rep...")
    def rep(inte, body):
        for i in range(eval(str(inte), {'__builtins__': {}}, allowed)):
           exec(str(body), {'__builtins__': {}}, allowed)
    print("Done defining rep.")
    print("Defining repuntil...")
    def repuntil(cond, body):
        while not eval(str(cond), {'__builtins__': {}}, allowed):
            exec(str(body), {'__builtins__': {}}, allowed)
    print("Done defining repuntil.")
    print("Defining load...")
    def load(p):
        if os.path.isfile(p):
            if os.path.getsize(p) == 0:
                print("Empty File.")
            else:
                with open(p, 'r') as z:
                    exec(p, {'__builtins__': {}}, allowed)
        else:
            print('File does not exist')
    print("Done defining load.")
    print("Finishing things up...")
    def exitpymode():
        global pymode
        pymode = False
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
                a = input(f"{os.name}!BOYANDOS@~")
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
                a = input(f"{os.name}!MINIPY@~")
                while len(a) > 0:
                    p = f"""{p}
{a}"""
                    a = input('...')
                exec(p, {'__builtins__': __builtins__, 'exitpymode': exitpymode})
            except Exception as e:
                print(f"Bad command with error: {e}")
##########################################################
elif option == '2':
    print(f"Welcome to the BOYANDOS {ver} Installation wizard!")
    print("What is your name?")
    usrname = input('>>>')
    if usrname.lower() in ["bùi hải hà", "dalo", "daly"]:
        print("womp womp :'(")
        print("I'LL KICK YOU OUT IN 5 SECONDS")
        import time
        time.sleep(5)
        exit()
    installtodir = input(f"Please enter the directory to install BOYANDOS (If you leave it blank, it will be saved to the main OS' disk): ")
    if len(installtodir) == 0:
        if os.name == "nt":
            installtodir = r"C:\\"
        else:
            installtodir = r"/"
    while not os.path.isdir(installtodir):
        installtodir = input(f"Invalid directory, please enter it again: ")
        if len(installtodir) == 0:
            if os.name == "nt":
                installtodir = r"C:\\"
            else:
                installtodir = r"/"
    confirm_opts = ["y", "Y", "n", "N"]
    confirm = "sixsevennn"
    while not confirm in confirm_opts: 
        print("Confirm installation?")
        print("[y/n]")
        confirm = input()
        if not confirm in confirm_opts:
            os.system('cls' if os.name == 'nt' else 'clear')
    if confirm in ['n', 'N']:
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
        with open(os.path.join(dosdir, "main.py"), 'w') as z:
            z.write(f'usr = "{usrname}"\nver = "{ver}"\n' +
            r"""print('Getting things ready...')
import os
import time
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
    if os.path.isfile(f):
        if os.path.getsize(f) == 0:
            print("Empty File.")
        else:
            with open(f, 'r') as z:
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
def overwrite(f, d):
    if os.path.isfile(f):
        with open(f, 'w') as z:
            z.write(d)
    else:
        print('File does not exist')
print("Done defining overwrite.")
print("Defining appendf...")
def appendf(f, d, p):
    if os.path.isfile(f):
        with open(f, 'r') as z:
            existing = z.read()
        p = int(p)
        if p < 0 or p > len(existing):
            print(f"Position out of range. File has {len(existing)} characters.")
            return
        new_contents = existing[:p] + d + existing[p:]
        with open(f, 'w') as z:
            z.write(new_contents)
    else:
        print('File does not exist.')
print("Done defining appendf.")
print("Defining makefile...")
def makefile(f, d):
    if not os.path.isfile(f):
        with open(f, 'w') as z:
            z.write(d)
    else:
        print('File already exists.')
print("Done defining makefile.")
print("Defining makefol...")
def makefol(n):
    if not os.path.isdir(n):
        os.makedirs(n)
    else:
        print('Folder already exists.')
print("Done defining makefol.")
print("Defining delfile...")
def delfile(f):
    if os.path.isfile(f):
        os.remove(f)
    else:
        print('File does not exist.')
print("Done defining delfile.")
print("Defining delfol...")
def delfol(f):
    if os.path.isdir(f):
        os.rmdir(f)
    else:
        print("Folder does not exist.")
print("Done defining delfol.")
print("Defining pythonmode...")
pymode = False
def pythonmode():
    global pymode
    pymode = True

    print('''BoyAnMINIPY build 17
    Type exitpymode() to exit BoyAnMINIPY.''')
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
    if eval(str(ifcon), {'__builtins__': {}}, allowed):
        exec(str(ifbody), {'__builtins__': {}}, allowed)
    elif elifcon and eval(str(elifcon), {'__builtins__': {}}, allowed):
        exec(str(elifbody), {'__builtins__': {}}, allowed)
    else:
        exec(str(elsebody), {'__builtins__': {}}, allowed)
print("Done defining if_elif_else.")
print("Defining if_else...")
def if_else(ifcon, ifbody, elsebody = ''):
    if eval(str(ifcon), {'__builtins__': {}}, allowed):
        exec(str(ifbody), {'__builtins__': {}}, allowed)
    else:
        exec(str(elsebody), {'__builtins__': {}}, allowed)
print('Done defining if_else.')
print("Defining rep...")
def rep(inte, body):
    for i in range(eval(str(inte), {'__builtins__': {}}, allowed)):
       exec(str(body), {'__builtins__': {}}, allowed)
print("Done defining rep.")
print("Defining repuntil...")
def repuntil(cond, body):
    while not eval(str(cond), {'__builtins__': {}}, allowed):
        exec(str(body), {'__builtins__': {}}, allowed)
print("Done defining repuntil.")
print("Defining load...")
def load(p):
    if os.path.isfile(p):
        if os.path.getsize(p) == 0:
            print("Empty File.")
        else:
            with open(p, 'r') as z:

                exec(p, {'__builtins__': {}}, allowed)
    else:
        print('File does not exist')
print("Done defining load.")
print("Finishing things up...")
def exitpymode():
    global pymode
    pymode = False
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
            a = input(f"{usr}!BOYANDOS@~")
            while len(a) > 0:
                p = f'''{p}
{a}'''
                a = input('...')
            exec(p, {'__builtins__': {}}, allowed)
        except Exception as e:
            print(f'Uh oh, you typed a command that BOYANDOS hates looking at. Because it has a secret "{e}" inside it.')
    else:
        try:
            p = ''
            a = input(f"{usr}!MINIPY@~")
            while len(a) > 0:
                p = f'''{p}
{a}'''
                a = input('...')
            exec(p, {'__builtins__': __builtins__, 'exitpymode': exitpymode})
        except Exception as e:
            print(f"Bad command with error: {e}")
"""
            )
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
