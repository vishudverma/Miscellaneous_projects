import os
import shutil
import datetime
import time
import schedule  # pyright: ignore

source_dir = os.getcwd()
destination_dir = "/var/home/fauji/Desktop/Backups"
# Use the entire folder name don't use shortcuts or it crashes


def copy_folder_to_directory(source: str, dest: str) -> None:
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in {dest}.")


if __name__ == "__main__":
    schedule.every().day.at("6:55").do(
        lambda: copy_folder_to_directory(source_dir, destination_dir)
    )  # The time is in 24 Hour format, remember that.
    while True:
        schedule.run_pending()
        time.sleep(60)
