import os
def list_files_in_folders(folder):
  try:  
      files = os.listdir(folder)
      return files, None
  except FileNotFoundError:
      return None, "Folder not found"
  except PermissionError:
      return None, "Permission Error"
def main():
  folders = input("Enter folders names with spaces: ").split()
for folder in folders:
  files = list_files_in_folders(folder)
    if files:
      print(f"Files in {folder}:")
      for file in files:
        print(file)
     else:
       print(f"Error in {folder_path}: Error")
          
if __name__ == "__main__":
    main()
