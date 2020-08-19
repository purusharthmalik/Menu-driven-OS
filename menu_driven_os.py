import os 


# Funnction for the menu
def menu():

    print("\n\nHello and welcome to your Python-driven Linux(OS) menu!\n")
    print("Please select the command you want to execute by selecting its number.\n")
    print("1-Open Google Chrome")
    print("2-Make a text file and write in it")
    print("3-Install a Python module")
    print("4-Look at some basic commands of your Linux Terminal")
    print("5-Open Spotify")
    print("6-Make a new folder(directory)")
    print("7-Rename a folder")
    print("8-Remove a folder(directory)")
    print("9-Open VS Code")
    print("10-Open File Manager")
    print("11-Open a new terminal")
    print("12-Open your TeX editor(Texstudio)")
    print("13-Make a Python file(.py)")
    print("14-Open a local file")
    print("15-Take a look at all your environment vaiables")
    print("16-Close a running application")
    print("17-Open Settings")
    print("18-See all the installed python modules")
    print("19-Uninstall an application")
    print("20-Install an application")
    execute()


# All the tasks are executed here
def execute():

    kill = 0
    num = choice()
    while num not in range(1,21) and kill == 0:
        print("\nSorry, invalid choice!\nPlease enter a number from the menu!\n")
        print("\nIf you want to terminate the program, choose 0")
        num = choice()
        if num == 0:
            kill = 1
    
    if num == 1:
        os.system('''gnome-terminal -x sh -c "google-chrome|less"''')
    
    elif num == 2:
        name = input("Enter a name for your text file(without .txt): ")
        print("Start typing the content now and press ctrl+D when you're done.")
        print(f"The file will be saved in {os.getcwd()}")        
        os.system(f"cat > {name}.txt")
    
    elif num == 3:
        name = input("Enter the name of the Python module you want to install: ")
        os.system(f"pip install {name}")
        
    elif num == 4:
        commands()

    elif num == 5:
        os.system('''gnome-terminal -x sh -c "spotify|less"''')

    elif num == 6:
        name = input("Enter the name of the new folder: ")
        add = input(f"Where do you want to save your folder?(Use the first slash also) \n(write 'same' if you want to save in {os.getcwd()}): ")
        if add.lower() == 'same':
            os.system(f"mkdir {name}")
        else:
            os.system(f"cd {add} && mkdir {name}")

    elif num ==7:
        name = input("Enter the name of the folder you want to rename: ")
        new = input("Enter a new name: ")
        ren = input(f"Where have you saved that folder?(Use the first slash also)\n(write 'same' if you have saved it in {os.getcwd()}): ")
        if ren.lower() == 'same':
            os.system(f"mv {name} {new}")
        else:
            os.system(f"cd {ren} && rmdir {name}")

    elif num == 8:
        name = input("Enter the name of the folder you want to delete: ")
        dele = input(f"Where do you want to delete your folder from?(Use the first slash also)\n(write 'same' if you want to delete from {os.getcwd()}): ")
        if dele.lower() == 'same':
            os.system(f"rmdir {name}")
        else:
            os.system(f"cd {dele} && rmdir {name}")

    elif num == 9:
        os.system('''gnome-terminal -x sh -c "code|less"''')

    elif num == 10:
        os.system("xdg-open .")

    elif num == 11:
        os.system("gnome-terminal")

    elif num == 12:
        os.system('''gnome-terminal -x sh -c "texstudio|less"''')

    elif num == 13:
        name = input("Enter the name of your file: ")
        os.system(f"touch {name}.py")
        print("File created successfully!")

    elif num == 14:
        name = input(f"Enter the name of file that you want to open(Provide the compplete path if it is not in {os.getcwd()}): ")
        os.system(f"xdg-open {name}")

    elif num == 15:
        os.system("printenv")

    elif num == 16:
        name = input("Which application do you want to close?(e.g Discord) ")
        os.system(f"pkill {name}")

    elif num == 17:
        os.system('''gnome-terminal -x sh -c "gnome-control-center|less"''')

    elif num == 18:
        os.system("pip list")

    elif num == 19:
        name = input("Enter the name of the application that you want to uninstall: ")
        os.system(f"sudo apt-get remove {name}")
        os.system(f"snap remove {name}")

    elif num == 20:
        name = input("Enter the name of the application that you want to uninstall: ")
        os.system(f"sudo apt-get install {name}")
        os.system(f"snap install {name}")


# Takes in User's choice
def choice():
    c = int(input("\nEnter your choice(1-20) : "))
    return c


# Basic Linux commannds
def commands():
    print('''\n
    Basic Ubuntu Commands For Beginner:\n
    1- sudo -> sudo (SuperUser DO) Linux command allows you to run programs or other commands with administrative privileges.
    2- pwd -> To know which directory you are in, you can use the “pwd” command.
    3- ls -> Use the "ls" command to know what files are in the directory you are in. You can see all the hidden files by using the command “ls -a”.
    4- cd -> Use the "cd" command to go to a directory.
    5- mkdir -> Use the mkdir command when you need to create a folder or a directory.
    6- rmdir -> Use the mkdir command when you need to create a folder or a directory.
    7- rm -> Use the rm command to delete files and directories.
    8- touch -> The touch command is used to create a file.
    9- man -> To know more about a command and how to use it, use the man command.
    10- locate -> The locate command is used to locate a file in a Linux system, just like the search command in Windows.
    ''')



if __name__ == "__main__":
    menu()

    # Repeat the program
    re = input("Do you want to run another task?(yes[y] or no[n]) \n")
    
    while re.lower() == 'y' or re.lower() == 'yes':
        menu()

    print("Good bye!")