import os

# Create a folder if it doesn't exist
folder_name = 'artifact-folder'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Specify the path to the file inside the folder
file_path = os.path.join(folder_name, 'example.txt')

# Open a file in write mode ('w') inside the folder
with open(file_path, 'w') as file:
    file.write('Hello, this is a sample text.\n')
    file.write('This is another line of text.\n')
    file.write('And one more line for good measure.\n')
