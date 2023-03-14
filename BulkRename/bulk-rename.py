import sys, os, codecs, csv

input_path, file_list, new_filename_list, rename_list = None, [], [], []
success, fail = int(0), int(0)

def print_debug_infos():
    print("\nDebug infos:")
    print(f"input_path: {input_path}")
    print("file_list:")
    for i, file in enumerate(file_list, 1):
        print(f"#{i}: {file}")
    print("new_filename_list:")
    for new_filename in new_filename_list:
        print(f"#{new_filename[0]}: {new_filename[1]}")
    print("rename_list:")
    for file_to_rename in rename_list:
        print(f"{file_to_rename[0]}: {file_to_rename[1]}")

def press_enter_to_continue(error_message):
    print(f"\n{error_message}")
    input("Press Enter to continue...\n")

def change_input_path():
    global input_path
    if len(sys.argv) > 1:
        input_path = sys.argv[1].strip()
        if os.path.isdir(input_path):
            print(f"Selected folder: {input_path}")
            return
    while True:
        input_path = input("Enter folder path: ").strip()
        if os.path.isdir(input_path):
            while input_path[-1:] == ".":
                input_path = input_path[:-1]
            break
        else:
            input_path = None
            press_enter_to_continue("Incorrect path, enter again")

def update_file_list():
    global file_list
    file_list = os.listdir(input_path)
    temp = file_list.copy()
    for i in temp:
        if not os.path.isfile(os.path.join(input_path, i)):
            file_list.remove(i)
    if not file_list:
        sys.exit(f"0 file found at {input_path}, program ended")

def load_rename_csv():
    global new_filename_list
    new_filename_list.clear()
    with codecs.open(f"{os.path.dirname(os.path.abspath(__file__))}/rename.csv", "r", "utf-8") as rename_csv:
        csv_reader = csv.reader(rename_csv)
        for row in csv_reader:
            new_filename_list.append(row)

def update_rename_list():
    global file_list, new_filename_list, rename_list
    rename_list.clear()
    for i in range(len(new_filename_list)):
        if i >= len(file_list):
            break
        rename_list.append((file_list[i], new_filename_list[i][1]))

def show_rename_list():
    print("\nFiles to be rename:")
    for file_to_rename in rename_list:
        print(f"\"{file_to_rename[0]}\" -> \"{file_to_rename[1]}\"")

def rename_file():
    global success, fail
    for file_to_rename in rename_list:
        try:
            os.rename(os.path.join(input_path, file_to_rename[0]), os.path.join(input_path, file_to_rename[1]))
            success += 1
            print(f"\"{file_to_rename[0]}\" renamed to \"{file_to_rename[1]}\"")
        except FileNotFoundError:
            fail += 1
            print(f"File not found: \"{file_to_rename[0]}\"")
        except FileExistsError:
            fail += 1
            print(f"Can't rename \"{file_to_rename[0]}\" to \"{file_to_rename[1]}\", filename already exists")
        except PermissionError:
            fail += 1
            print(f"Can't rename \"{file_to_rename[0]}\", file is being used")

def setup():
    change_input_path()
    update_file_list()
    load_rename_csv()
    update_rename_list()
    show_rename_list()

if __name__ == "__main__":
    setup()
    while True:
        ans = input("Confirm rename above files? (Y/N): ").lower()
        if ans == "list":
            show_rename_list()
        if ans == "update":
            print("Updating rename list...")
            update_file_list()
            load_rename_csv()
            update_rename_list()
            show_rename_list()
        elif ans == "y" or ans == "yes":
            rename_file()
            sys.exit(f"Rename completed with {success} success and {fail} fail")
        elif ans == "n" or ans == "no":
            sys.exit("Rename aborted, program ended")
        else:
            press_enter_to_continue("Unknown operation")

    # print_debug_infos()