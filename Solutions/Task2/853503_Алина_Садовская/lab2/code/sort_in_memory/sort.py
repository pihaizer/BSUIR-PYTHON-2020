import os
import tempfile


class NotNumber(Exception):
    def __init__(self, text):
        self.txt = text


class MergeSort:
    def __init__(self, file_name, result_path):
        if not (os.path.exists(file_name)):
            raise FileNotFoundError('file not found')
        self.first_file = file_name
        with open(self.first_file, 'r') as file:
            self.amount_element = sum(1 for line in file)

        result = self.sort(0, self.amount_element)
        with open(result_path, 'w+') as file_output:
            for line in result:
                if line == '':
                    break
                number = int(line)
                file_output.write(str(number) + '\n')

    def merge_sort(self, temp_file_1, temp_file_2):
        str1 = temp_file_1.readline()
        str2 = temp_file_2.readline()
        if str1 != "":
            num_1 = int(str1)
            first_is_ok = True
        else:
            num_1 = 0
            first_is_ok = False

        if str2 != "":
            num_2 = int(str2)
            second_is_ok = True
        else:
            second_is_ok = False
            num_2 = 0

        result_file = tempfile.TemporaryFile()

        while first_is_ok is True and second_is_ok is True:
            if num_1 <= num_2:
                result_file.write(bytes(str(num_1) + '\n', 'utf-8'))
                try:
                    num_1 = int(temp_file_1.readline())
                    first_is_ok = True
                except:
                    first_is_ok = False
                    num_1 = 0
            else:
                result_file.write(bytes(str(num_2) + '\n', 'utf-8'))
                try:
                    num_2 = int(temp_file_2.readline())
                    second_is_ok = True
                except:
                    second_is_ok = False
                    num_2 = 0

        if first_is_ok is False and second_is_ok is False:
            result_file.seek(0)
            return result_file

        if first_is_ok:
            right_bound = temp_file_1
            result_file.write(bytes(str(num_1) + '\n', 'utf-8'))
        else:
            right_bound = temp_file_2
            result_file.write(bytes(str(num_2) + '\n', 'utf-8'))

        still_numbers = True

        while still_numbers:
            try:
                num = int(right_bound.readline())
                still_numbers = True
            except:
                still_numbers = False
                num = 0
            if still_numbers:
                result_file.write(bytes(str(num) + '\n', 'utf-8'))

        result_file.seek(0)
        return result_file

    def sort(self, left, right):
        if right - left <= 10 ** 5:
            sorted_data = self.sort_array(left, right)
            temp_file = tempfile.TemporaryFile()
            for item in sorted_data:
                temp_file.write(bytes(str(item) + '\n', 'utf-8'))
            temp_file.seek(0)
            return temp_file
        else:
            middle = left + (right - left) // 2
            temp_file_l = self.sort(left, middle)
            temp_file_r = self.sort(middle + 1, right)
            return self.merge_sort(temp_file_l, temp_file_r)

    def sort_array(self, l_bound, r_bound):
        data = []
        if r_bound >= self.amount_element:
            r_bound = self.amount_element - 1
        with open(self.first_file, 'r') as fp:
            for l_number in range(l_bound):
                next(fp)
            for l_number in range(r_bound - l_bound + 1):
                line = fp.readline()
                try:
                    number = int(line)
                    data.append(number)
                except ValueError:
                    raise NotNumber('Not a number')
        data.sort()
        return data


if __name__ == '__main__':
    # with open('numbers.txt', 'w') as f: f.writelines(
    #   '{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000000))
    MergeSort().initialize('../../tests/sort/numbers.txt', '../../tests/sort/number_sort.txt')
