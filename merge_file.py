import os
# from pprint import pprint

class MergeFile:

    def __init__(self, directory):
        self.dir = directory
        self.files = [file for file in os.listdir(directory)]

    def merge(self):
        files_dict = {}
        file_in_lines = {}
        for file in self.files:
            with open(f'{self.dir}/{file}', 'r', encoding='utf-8') as text_file:
                count_lines = 0
                for line in text_file:
                    count_lines += 1
                    if files_dict.get(file):
                        files_dict[file] += [line[:-1]]
                    else:
                        files_dict[file] = [line[:-1]]
                if files_dict.get(file):
                    # <--- Проверка повторения количества строк --->
                    if file_in_lines.get(count_lines):
                        file_in_lines[count_lines] += [file]
                    else:
                        file_in_lines[count_lines] = [file]
                else:
                    file_in_lines[count_lines] = ''
        with open('all_files_in_one.txt', 'w', encoding='utf-8') as new_file:
            for count_line in sorted(list(file_in_lines.keys())):
                for one_count_line in file_in_lines[count_line]:
                    new_file.write(f'{one_count_line}\n')
                    new_file.write(f'{count_line}\n')
                    for line in files_dict[one_count_line]:
                        new_file.write(f'{line}\n')


general_file = MergeFile('files')
general_file.merge()
