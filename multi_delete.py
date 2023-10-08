import os
import argparse
import send2trash


def batch_delete_files(directory, file_extension, recursive, silent):
    """
    Batch delete files in a directory with options.

    Args:
        directory (str): The directory to delete files from.
        file_extension (str): The file extension to target.
        recursive (bool): Enable recursive deletion if True.
        silent (bool): Enable silent mode (no progress messages) if True.
    """

    def delete_file(file_path):
        """
        Delete a file and send it to the trash.

        Args:
            file_path (str): The path to the file to be deleted.
        """
        try:
            send2trash.send2trash(file_path)
            if not silent:
                print(f"Sent to trash: {file_path}")
        except OSError as e:
            if not silent:
                print(f"Error sending {file_path} to trash: {e}")

    def process_files_in_directory(path):
        """
        Recursively process files in a directory and delete those matching the file extension.

        Args:
            path (str): The path to the directory to process.
        """
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if file.endswith(file_extension):
                delete_file(file_path)
            elif recursive and os.path.isdir(file_path):
                process_files_in_directory(file_path)

    if recursive:
        process_files_in_directory(directory)
    else:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if file.endswith(file_extension):
                delete_file(file_path)


def parse_arguments():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: The parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Batch delete files with options.")
    parser.add_argument("-d", "--directory", help="The directory to delete files from.")
    parser.add_argument("-e", "--extension", help="The file extension to target.")
    parser.add_argument(
        "-r", "--recursive", action="store_true", help="Enable recursive deletion."
    )
    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        help="Enable silent mode (no progress messages).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    directory_path = args.directory
    file_extension = args.extension
    recursive = args.recursive
    silent = args.silent

    if os.path.exists(directory_path):
        batch_delete_files(directory_path, file_extension, recursive, silent)
    else:
        print(f"Directory '{directory_path}' does not exist.")
