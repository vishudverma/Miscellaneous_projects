import os
import json
import shutil
from subprocess import PIPE, run
import sys


GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]


def find_all_game_dirs(source: str) -> list[str]:
    game_paths = []

    for _, dirs, _ in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        break
    return game_paths


def get_name_from_paths(paths: list[str], to_strip: str) -> list[str]:
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "").rstrip("_")
        new_names.append(new_dir_name)
    return new_names


def create_dir(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)


def copy_and_overwrite(source: str, dest: str):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)


def make_json_metadata_file(path: str, game_dirs: list[str]):
    data = {
        "gameNames": game_dirs,
        "numberOfGames": len(game_dirs),
    }
    with open(path, "w") as f:
        json.dump(data, f)


def compile_game_code(path: str):
    code_file_name = None
    for _, _, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break
        break
    if code_file_name is None:
        return

    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)


def run_command(command, path: str):
    cwd = os.getcwd()
    os.chdir(path)

    result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)
    print("compile result", result)

    os.chdir(cwd)


def main(source: str, target: str):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_dirs(source_path)
    new_game_dirs = get_name_from_paths(game_paths, "game")

    create_dir(target_path)

    for src, dest in zip(game_paths, new_game_dirs):
        dest_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, dest_path)
        compile_game_code(dest_path)

    json_path = os.path.join(target, "metadata.json")
    make_json_metadata_file(json_path, game_paths)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")

    source, target = args[1:]
    main(source, target)
