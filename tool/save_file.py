# Save the file (file name, content)
def save_to_file(path_file_name, contents):
    fh = open(path_file_name, 'w')
    fh.write(contents)
    fh.close()

