# with open('week_5_assignment/my_file.txt', 'w+') as file:
    # file.write("Hello \n")
    # file.write("Writing to a file \n")
    # file.write("Adding a number, 16, to the file")
# with open('week_5_assignment/my_file.txt', 'r') as file2:
#     contents = file2.read()
#     print(contents)

def write_and_read():
    try:
        with open(f'week_5_assignment/my_file.txt', 'w+') as file:
            file.write("Hello \n")
            file.write("Writing to a file \n")
            file.write("Adding a number, 16, to the file \n")
        with open(f'week_5_assignment/my_file.txt', 'a') as file:
            file.write("Append line 1 \n")
            file.write("Append line 2 \n")
            file.write("Append line 3")
        with open('week_5_assignment/my_file.txt', 'r') as file2:
            contents = file2.read()
            print(contents)
    except FileNotFoundError:
        print('File Not Found')
    except PermissionError:
        print('You ar not permitted to open')
    finally:
        print("All done")

write_and_read()