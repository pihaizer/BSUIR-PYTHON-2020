import tempfile

def _merge(temp_files, dst_file_path):
    for (file_a, file_b) in zip(temp_files[::2], temp_files[1::2]):
        new_file = tempfile.TemporaryFile('w+t')
        value_a = file_a.readline()
        value_b = file_b.readline()
        while True:
            if value_a and not value_b:
                new_file.write(value_a)
                value_a = file_a.readline()
                continue
            if value_b and not value_a:
                new_file.write(value_b)
                value_b = file_b.readline()
                continue
            if not value_a and not value_b:
                break
            if int(value_a) < int(value_b):
                new_file.write(value_a)
                value_a = file_a.readline()
            else:
                new_file.write(value_b)
                value_b = file_b.readline()
        new_file.seek(0)
        a_index = temp_files.index(file_a)
        # closing temp files
        temp_files[a_index].close()
        temp_files[a_index + 1].close()
        temp_files[a_index:a_index + 2] = [new_file]      
    if len(temp_files) > 1:
        _merge(temp_files, dst_file_path)
    else:
        with open(dst_file_path, 'w') as result_file:
            lines = temp_files[0].readlines()
            result_file.writelines(lines)
            temp_files[0].close()

def _write_to_tmp(temp_buffer, temp_files, clear_buffer = True):
    temp_file = tempfile.TemporaryFile('w+t')
    for value in map(str, temp_buffer):
         temp_file.write(value + '\n')
    temp_file.seek(0)
    temp_files.append(temp_file)
    temp_buffer.clear()

def sort(src_file_path, dst_file_path, chunk_size):
    temp_files = [] # contains descriptors of temporary files
    with open(src_file_path) as file:
        temp_buffer = []
        size = 0
        while True:
            value = file.readline()
            if not value:
                temp_buffer.sort()
                _write_to_tmp(temp_buffer, temp_files) 
                break
            temp_buffer.append(int(value))
            size += 1
            if size % chunk_size == 0:
                temp_buffer.sort()
                _write_to_tmp(temp_buffer, temp_files)
                size = 0
        _merge(temp_files, dst_file_path)