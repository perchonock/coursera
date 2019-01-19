import os
import tempfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()

if args.key:
    key = args.key
else:
    key = None

if args.val:
    value = args.val
else:
    value = None


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.isfile(storage_path):
    with open(storage_path, 'w') as f:
        f.write('')
if key and value:
    with open(storage_path, 'a') as f:
        pair = key + ':' + value
        f.write(pair + '\n')
elif key:
    with open(storage_path, 'r') as f:
        values = []
        for line in f.readlines():
            cur_key, cur_val = line.split(':')
            cur_val = cur_val.rstrip(os.linesep)
            if cur_key == key:
                values.append(cur_val)
    if len(values) > 0:
        print(", ".join(values))
    else:
        print('')