import sys, os, codecs, csv

input_folder_path, csv_path, file_list, new_filename_list, rename_list = None, None, [], [], []
success, fail = int(0), int(0)

def print_debug_infos():
    print("\nDebug infos:")
    print(f"input_folder_path: {input_folder_path}")
    print(f"csv_path: {csv_path}")
    print("file_list:")
    for i, file in enumerate(file_list, 1):
        print(f"#{i}: {file}")
    print("new_filename_list:")
    for new_filename in new_filename_list:
        print("#" + new_filename["IntFileNumber"] + ": " + new_filename["NewFilename"])
    print("rename_list:")
    for file_to_rename in rename_list:
        print(f"{file_to_rename[0]} -> {file_to_rename[1]}")

def press_enter_to_continue(error_message):
    print(f"\n{error_message}")
    input("Press Enter to continue...\n")

def change_input_path(setup = False):
    global input_folder_path
    if setup:
        if len(sys.argv) > 1:
            input_folder_path = sys.argv[1].strip()
            if os.path.isdir(input_folder_path):
                input_folder_path = remove_dot(input_folder_path)
                print(f"Selected folder: {input_folder_path}")
                return
    while True:
        input_folder_path = input("Enter folder path: ").strip()
        if os.path.isdir(input_folder_path):
            input_folder_path = remove_dot(input_folder_path)
            break
        else:
            input_folder_path = None
            press_enter_to_continue("Incorrect path, enter again")

def change_csv_path(setup = False):
    global csv_path
    if setup:
        if len(sys.argv) > 2:
            csv_path = sys.argv[2].strip()
            if os.path.isfile(csv_path):
                csv_path = remove_dot(csv_path)
                print(f"Selected csv: {csv_path}")
                return
        while True:
            ans = input("Do you want to use default csv location? (Y/N): ").lower()
            if ans == "y" or ans == "yes":
                csv_path = f"{os.path.dirname(os.path.abspath(__file__))}/rename.csv"
                print(f"Selected default csv: {csv_path}")
                return
            elif ans == "n" or ans == "no":
                break
            else:
                press_enter_to_continue("Unknown operation")
    while True:
        csv_path = input("Enter csv path: ").strip()
        if os.path.isfile(csv_path):
            csv_path = remove_dot(csv_path)
            break
        else:
            csv_path = None
            press_enter_to_continue("File not found, enter again")

def remove_dot(path: str):
    while path[-1:] == ".":
        path = path[:-1]
    return path

def update_file_list():
    global file_list
    temp = os.listdir(input_folder_path)
    for i in temp:
        if os.path.isfile(os.path.join(input_folder_path, i)):
            file_list.append(i)
    if not file_list:
        sys.exit(f"0 file found at {input_folder_path}, program ended")

def load_rename_csv():
    global csv_path, new_filename_list
    new_filename_list.clear()
    while True:
        if not csv_path:
            csv_path = input("Enter csv path: ").strip()
        try:
            with codecs.open(csv_path, "r", "utf-8") as rename_csv:
                csv_reader = csv.DictReader(rename_csv)
                for row in csv_reader:
                    int(row["IntFileNumber"])
                    new_filename_list.append(row)
                return
        except FileNotFoundError:
            csv_path = None
            press_enter_to_continue(f"csv file not found, enter again")
        except ValueError:
            csv_path = None
            press_enter_to_continue(f"csv format incorrect, update the csv file and try again")
        except KeyError:
            csv_path = None
            press_enter_to_continue(f"csv format incorrect, update the csv file and try again")

def update_rename_list():
    global file_list, new_filename_list, rename_list
    rename_list.clear()
    for new_filename in new_filename_list:
        index = int(new_filename["IntFileNumber"])-1
        if index >= len(file_list):
            continue
        rename_list.append((file_list[index], new_filename["NewFilename"]))

def show_rename_list():
    print("\nFiles to be rename:")
    for file_to_rename in rename_list:
        print(f"\"{file_to_rename[0]}\" -> \"{file_to_rename[1]}\"")

def rename_file():
    global success, fail
    for file_to_rename in rename_list:
        try:
            os.rename(os.path.join(input_folder_path, file_to_rename[0]), os.path.join(input_folder_path, file_to_rename[1]))
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
    change_input_path(True)
    change_csv_path(True)
    rename_list_setup()

def rename_list_setup():
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
        elif ans == "csv":
            change_csv_path()
            print("Updating rename file...")
            rename_list_setup()
        elif ans == "update":
            print("Updating rename list...")
            rename_list_setup()
        elif ans == "y" or ans == "yes":
            rename_file()
            sys.exit(f"Rename completed with {success} success and {fail} fail")
        elif ans == "n" or ans == "no":
            sys.exit("Rename aborted, program ended")
        else:
            press_enter_to_continue("Unknown operation")

    # print_debug_infos()