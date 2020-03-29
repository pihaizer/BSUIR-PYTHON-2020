# Merge sort in outer memory module
import tempfile
import linecache


def sort(input_file_name: str, output_file_name: str):
    try:
        with open(input_file_name, 'r') as input_file:
            with open(output_file_name, 'w') as output_file:
                print("Starting to sort")
                __sortStep(input_file, output_file)
                print("Sorting finished")
    except IOError:
        print("Wrong file name")
        return


def lines_count(file):
    print("Counting lines in " + file.name)
    file.seek(0)
    num_lines = sum(1 for line in file)
    print("Lines in " + file.name + ": " + str(num_lines))

    return num_lines


def copy_lines(from_file, to_file, from_line_index, to_line_index):
    print("Copying lines " + str(from_line_index) + "-" + str(to_line_index) + " from " +
          from_file.name + " to file " + to_file.name)
    for i in range(from_line_index+1, to_line_index+1):
        line = linecache.getline(from_file.name, i)
        to_file.write(line)


def get_line_int(file, line_index):
    print("Trying to get line " + str(line_index) + " from " + file.name)

    file.seek(0)
    for i, line in enumerate(file):
        if i == line_index:
            number = int(line)
            return number

    return None


def __sortStep(input_file, output_file):
    if lines_count(input_file) <= 1:
        print(input_file.name + " is final. Starting to reverse sorting")
        return

    middle = lines_count(input_file)//2

    print("Creating left temp file")
    left_file = tempfile.NamedTemporaryFile("w+", prefix="left_")
    copy_lines(input_file, left_file, 0, middle)
    print("Left temp file created. Name: " + left_file.name)

    print("Creating right temp file")
    right_file = tempfile.NamedTemporaryFile("w+", prefix="right_")
    copy_lines(input_file, right_file, middle, lines_count(input_file))
    print("Right temp file created. Name: " + right_file.name)

    print("Starting to sort left temp file " + left_file.name)
    __sortStep(left_file, left_file)
    print("Left temp file " + left_file.name + " is sorted")

    print("Starting to sort right temp file " + right_file.name)
    __sortStep(right_file, right_file)
    print("Right temp file " + right_file.name + " is sorted")

    output_file.seek(0)
    output_file.truncate()

    left_file_length = lines_count(left_file)
    right_file_length = lines_count(right_file)

    left_pointer = right_pointer = 0

    closestLeft = get_line_int(left_file, left_pointer)
    closestRight = get_line_int(right_file, right_pointer)

    while left_pointer < left_file_length and right_pointer < right_file_length:
        if closestLeft <= closestRight:
            print("Appending line from left temp file to output")
            output_file.write(str(closestLeft) + '\n')
            left_pointer += 1
            closestLeft = get_line_int(left_file, left_pointer:=left_pointer)
        else:
            print("Appending line from right file to output")
            output_file.write(str(closestRight) + '\n')
            right_pointer += 1
            closestRight = get_line_int(right_file, right_pointer)

    print("Appending the rest of the lines from left temp file " + left_file.name)
    while left_pointer < left_file_length:
        output_file.write(str(closestLeft) + '\n')
        left_pointer += 1
        closestLeft = get_line_int(left_file, left_pointer)

    print("Appending the rest of the lines from right temp file " + right_file.name)
    while right_pointer < right_file_length:
        output_file.write(str(closestRight) + '\n')
        right_pointer += 1
        closestRight = get_line_int(right_file, right_pointer)

    print("Closing temp files " + left_file.name + " and " + right_file.name)
    left_file.close()
    right_file.close()
    print("Temp files closed")
