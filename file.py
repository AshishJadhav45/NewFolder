import os

directory = 'C:/Users/SAM/OneDrive/Desktop/Assignment/Python Assignment'
filename = 'Neo.txt'


file_path = os.path.join(directory, filename)


with open(file_path, 'w') as file:
    file.write("This is a new file.")

print(f"New file '{filename}' created in directory: '{directory}'.")
