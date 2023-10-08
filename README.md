# Batch Deleter

Batch Deleter is a versatile Python script that empowers you to delete files with specific extensions from a directory. It offers options for recursive deletion and provides detailed progress updates. This script is designed to work seamlessly on various platforms, including Linux, Windows, and macOS.

## Features

- Efficiently delete files with specific file extensions in bulk.
- Choose between recursive or non-recursive deletion modes.
- Enable verbose mode to receive detailed progress updates during the deletion process.

## Supported Platforms

- Linux
- Windows
- macOS
- Unknown (for unsupported platforms)

## Prerequisites

- Python 3.x installed on your system.
- The `send2trash` Python library, which can be installed using pip:

  ```bash
  pip install send2trash
  ```

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the `batch_deleter.py` script.

4. Execute the script with the following command:

   ```bash
   python batch_deleter.py directory_path file_extension [-r] [-v]
   ```

   Replace the following arguments:

   - `directory_path`: The path to the directory from which you want to delete files.
   - `file_extension`: The file extension of the files you want to delete (e.g., `.txt`, `.jpg`).
   - `-r` (optional): Enable recursive deletion (use this flag if you want to include files in subdirectories).
   - `-v` (optional): Enable verbose mode (progress messages).

## Examples

- Delete all `.txt` files from the current directory:

  ```bash
  python batch_deleter.py . txt
  ```

- Delete all `.jpg` files from a specific directory and its subdirectories:

  ```bash
  python batch_deleter.py /path/to/directory jpg -r -v
  ```

## Important Notes

- Please exercise caution when using this script. Deleted files are moved to the system's trash by default, but there is no guarantee of recovery once the trash is emptied.

- Ensure that you have the necessary permissions to delete files in the specified directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Platform Detection

Batch Deleter automatically identifies the platform you are using (Linux, Windows, macOS, or Unknown) and tailors its output accordingly.

## Contributing

If you encounter any issues or have suggestions for enhancements, we encourage you to open an issue or submit a pull request. Your contributions are welcome!

Happy batch deleting!
