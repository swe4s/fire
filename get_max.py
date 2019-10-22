from utils import file_io


file_name = "amazon.tsv"
col_nums = [3]

data = file_io.get_file_columns(file_name, col_nums)

print(max(data[0]))
