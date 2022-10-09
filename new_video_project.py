import datetime
import os
import shutil

main_folder = datetime.datetime.now()
main_folder = main_folder.strftime("%b-%d-%Y")
raw_folder = fr'C:\Things\InProgress\{main_folder}\Raw'

log_location = r'C:\Things\InProgress\log.txt'


def make_dir():
    os.makedirs(raw_folder)

    # Make log file, Top line is newest, bottom is oldest.
    with open(log_location, 'r') as f:
        old_content = f.readlines()
        f.close()
    with open(log_location, 'w') as f:
        new_content = ''.join([f'{main_folder}\n'] + old_content)
        f.write(new_content)
        f.close()


def move_dir():

    # Open log and find current folder name, it will be the first line.
    with open(log_location, 'r') as f:
        current_project = f.readlines()[0].strip("\n")
        f.close()

    # Move Folders
    origin_dir = fr"C:\Videos\InProgress\{current_project}"
    target_dir = r"D:\Vieos\Completed"
    shutil.move(origin_dir, target_dir)

    # Mark date in log as moved
    with open(log_location, 'r') as f:
        old_content = f.readlines()
        f.close()
    with open(log_location, 'w') as f:
        new_content = ''.join(
            [f'{current_project} - Moved\n']
            + old_content[1:]
            )
        f.write(new_content)
        f.close()


if __name__ == "__main__":
    while True:
        action = input("1 for Make, 2 for move, x to exit: ")
        
        if action in [1, '1']:
            make_dir()
            break
            
        elif action in [2, '2']:
            move_dir()
            break
            
        elif action in ['x', 'X', 'exit', 'esc']:
            break

