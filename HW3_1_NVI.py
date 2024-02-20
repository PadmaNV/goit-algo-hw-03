from pathlib import Path
import shutil

def copy_files(source_dir: Path, dest_dir: Path) -> None:
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                copy_files(item, dest_dir)
            elif item.is_file():
                extension = item.suffix[1:]
                (dest_dir / extension).mkdir(parents=True, exist_ok=True)
                shutil.copy(item, dest_dir / extension / item.name)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    source_path = Path(input("Введіть вхідну папку: "))
    dest_path = Path(input("Введіть папку призначення (press Enter for default 'dist'): ") or 'dist')

    if not source_path.exists():
        print("Source directory does not exist.")
        return
    if not source_path.is_dir():
        print("Source path should be a directory.")
        return

    if not dest_path.exists():
        dest_path.mkdir(parents=True, exist_ok=True)

    copy_files(source_path, dest_path)
    print("Files copied and sorted successfully.")

if __name__ == "__main__":
    main()
