import argparse
import os, time

# Example of argparser and getting parse values
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="The name of the file to be renamed")
parser.add_argument("-r", "--rename", help="The new name of the file")
parser.add_argument("-m", "--mtime", help="Modification time", action="store_true")
parser.add_argument("-s", "--size", help="The size of the file", action="store_true")

args = parser.parse_args()

filename = args.filename
new_name = args.rename

stats = os.stat(filename)
if args.mtime:
    print('Last modified:', time.ctime(stats.st_mtime))
    
if args.size:
    print(f'File size: {(stats.st_size)//(2**20)} MB')

os.rename(filename, new_name)
