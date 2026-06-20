"""
Mini Project: File Organizer
Project Integration Phase

A practical utility script that organizes files in a directory 
based on their file extensions.
Demonstrates working with the pathlib module and file system operations.
"""

import shutil
from pathlib import Path
from typing import Dict


def get_category_mapping() -> Dict[str, str]:
    """Returns a mapping of file extensions to folder names."""
    return {
        ".txt": "Documents",
        ".md": "Documents",
        ".pdf": "Documents",
        ".jpg": "Images",
        ".png": "Images",
        ".mp4": "Videos",
        ".py": "Scripts",
        ".csv": "Data",
    }


def organize_directory(target_dir: str) -> None:
    """
    Scans the target directory and moves files into subfolders
    based on their extensions.
    """
    path = Path(target_dir)

    if not path.exists() or not path.is_dir():
        print(f"Error: Directory '{target_dir}' does not exist.")
        return

    category_map = get_category_mapping()
    moved_count = 0

    print(f"Scanning directory: {path.absolute()}")

    for file_path in path.iterdir():
        if file_path.is_file():
            # Get extension (e.g., '.txt')
            extension = file_path.suffix.lower()

            # Determine target folder name (default to 'Others')
            folder_name = category_map.get(extension, "Others")

            # Create target folder if it doesn't exist
            target_folder = path / folder_name
            target_folder.mkdir(exist_ok=True)

            # Define destination path
            destination_path = target_folder / file_path.name

            # Move file
            shutil.move(str(file_path), str(destination_path))
            print(f"Moved: {file_path.name} -> {folder_name}/")
            moved_count += 1

    print(f"\nOrganization complete! Moved {moved_count} files.")


def main() -> None:
    print("--- File Organizer ---")
    print("WARNING: This will move files within the target directory.")
    target = input("Enter the path of the directory to organize (or 'q' to quit): ")

    if target.lower() != "q":
        organize_directory(target)


if __name__ == "__main__":
    main()
