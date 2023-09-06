import os, subprocess

'''

Created By Volkan EFE 06.09.2023 15:50

'''

class SimpleOS:
    def __init__(self):
        self.current_directory = "/"
        self.running = False

    def run(self):
        self.running = True
        print("Welcome to SimpleOS!")

        while self.running:
            user_input = input(f"{self.current_directory}> ")
            self.process_input(user_input)

    def process_input(self, user_input):
        if user_input == "exit":
            self.running = False
        elif user_input == "pwd":
            print(self.current_directory)
        elif user_input == "ls":
            self.list_files()
        elif user_input == "open": # elif user_input == "explorer":
            subprocess.run(['open', os.path.realpath(self.current_directory)])
            # if you are using windows operating system replace the word "open" with "explorer"
            # subprocess.run(['explorer', os.path.realpath(self.current_directory)])
        elif user_input.startswith("cd "):
            self.change_directory(user_input[3:])
        else:
            print("Command not found")

    def list_files(self):
        files = os.listdir(self.current_directory)
        for file in files:
            print(file)

    def change_directory(self, new_dir):
        if new_dir.startswith("/"):
            self.current_directory = new_dir
        else:
            self.current_directory = os.path.join(self.current_directory, new_dir)

if __name__ == "__main__":
    os_simulator = SimpleOS()
    os_simulator.run()
