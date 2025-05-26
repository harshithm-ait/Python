print("Harshith Nayaka M ")
print("1AY24AI043 ")
print(" M ")
def print_table(data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    for row in data:
        print(' '.join(str(item).rjust(width) for item, width in zip(row, col_widths)))
table_data = [['apples', 'oranges'], ['Alice', 'Bob']]
print_table(table_data)