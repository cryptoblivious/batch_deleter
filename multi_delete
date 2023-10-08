import os
import send2trash
import sys

def batch_delete_files(directory, file_extension, recursive):
    if recursive:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    try:
                        send2trash.send2trash(file_path)
                        print(f"Sent to trash: {file_path}")
                    except Exception as e:
                        print(f"Error sending {file_path} to trash: {e}")
    else:
        for file in os.listdir(directory):
            if file.endswith(file_extension):
                file_path = os.path.join(directory, file)
                try:
                    send2trash.send2trash(file_path)
                    print(f"Sent to trash: {file_path}")
                except Exception as e:
                    print(f"Error sending {file_path} to trash: {e}")

if len(sys.argv) != 4:
    print("Usage: python script_name.py directory_path file_extension recursive")
else:
    directory_path = sys.argv[1]
    file_extension = sys.argv[2]
    recursive_flag = sys.argv[3].lower() == "true"

    if os.path.exists(directory_path):
        batch_delete_files(directory_path, file_extension, recursive_flag)
    else:
        print(f"Directory '{directory_path}' does not exist.")
