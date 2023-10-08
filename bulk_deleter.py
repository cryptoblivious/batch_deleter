import os
import platform
import argparse
import send2trash


def determine_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "Linux"
    elif os_name == "Windows":
        return "Windows"
    elif os_name == "Darwin":
        return "macOS"
    else:
        return "Unknown"


def bulk_delete_files(directory, file_extension, recursive, verbose):
    """
    Bulk delete files in a directory with options.

    Args:
        directory (str): The directory to delete files from.
        file_extension (str): The file extension to target.
        recursive (bool): Enable recursive deletion if True.
        verbose (bool): Enable verbose mode (progress messages) if True.
    """

    def delete_file(file_path):
        """
        Delete a file and send it to trash.

        Args:
            file_path (str): The path to the file to be deleted.
        """
        try:
            file_name = file_path.split(os.sep)[-1]
            send2trash.send2trash(file_path)
            if verbose:
                print(f"Sent to trash: {file_name}")
            return True
        except OSError as e:
            if verbose:
                print(f"Error sending {file_name} to trash: {e}")
            return False

    def count_total_files(path):
        if recursive:
            total_files = 0
            for root, dirs, files in os.walk(path):
                total_files += len(files)
            return total_files
        else:
            return len(os.listdir(path))

    def process_files_in_directory(path):
        """
        Recursively process files in a directory and delete those matching the file extension.

        Args:
            path (str): The path to the directory to process.
        """
        total_files = count_total_files(path)
        directory_files_count = len(os.listdir(path))
        files_processed = 0
        files_deleted = 0
        path_end = path.split(os.sep)[-1]
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if file.endswith(file_extension) and delete_file(file_path):
                files_deleted += 1
            elif recursive and os.path.isdir(file_path):
                sub_processed, sub_deleted = process_files_in_directory(file_path)
                files_processed += sub_processed
                files_deleted += sub_deleted
            files_processed += 1
            if verbose:
                completion = (files_processed / total_files) * 100
                if files_processed != directory_files_count:
                    print(
                        f"Processed {completion:.2f}% of files in {path_end}{' ' * (64 - len(path_end))}\r",
                        end="",
                    )
                else:
                    print(
                        f"Processed {completion:.2f}% of files in {path_end}{' ' * (64 - len(path_end))} - Done!"
                    )

        return files_processed, files_deleted

    if recursive:
        processed, deleted = process_files_in_directory(directory)
    else:
        processed = 0
        deleted = 0
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if file.endswith(file_extension) and delete_file(file_path):
                deleted += 1
            processed += 1

    return processed, deleted


def parse_arguments():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: The parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Batch delete files with options.")
    parser.add_argument(
        "directory", metavar="directory", help="The directory to delete files from."
    )

    parser.add_argument(
        "extension", metavar="extension", help="The file extension to target."
    )
    parser.add_argument(
        "-r", "--recursive", action="store_true", help="Enable recursive deletion."
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose mode (progress messages).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    directory_path = args.directory
    file_extension = args.extension
    recursive = args.recursive
    verbose = args.verbose
    path_end = directory_path.split(os.sep)[-1]

    current_os = determine_os()

    if os.path.exists(directory_path):
        print(
            f"Processing files in {path_end} to find files ending with {file_extension} in order to send them to the {current_os} trash..."
            if not recursive
            else f"Processing files in {path_end} to find files ending with {file_extension} in order to send them to the {current_os} trash recursively..."
        )

        processed, deleted = bulk_delete_files(
            directory_path, file_extension, recursive, verbose
        )
        print(
            f"\nDone deleting files in {path_end}."
            if not recursive
            else f"\nDone deleting files in '{path_end}' recursively."
        )
        print(f"{processed} files processed, {deleted} files deleted.")

    else:
        print(f"Directory '{directory_path}' does not exist.")
