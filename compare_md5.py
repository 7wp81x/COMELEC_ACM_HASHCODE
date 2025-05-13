import pandas as pd
import sys
import os
import re

def normalize_path(path):
    # remove (/phl-acm.../ in path)
    path = re.sub(r'^(?:\./|[^/]+-v?\d+\.\d+\.\d+/)', '', path)
    return f'./{path.strip()}'

def compare_csv(old_csv, new_csv):
    df_old = pd.read_csv(old_csv)
    df_new = pd.read_csv(new_csv)

    df_old['filename'] = df_old['filename'].apply(normalize_path)
    df_new['filename'] = df_new['filename'].apply(normalize_path)

    old_dict = dict(zip(df_old['filename'], df_old['md5hash']))
    new_dict = dict(zip(df_new['filename'], df_new['md5hash']))

    modified_files = []
    new_files = []

    for filename, new_hash in new_dict.items():
        old_hash = old_dict.get(filename)
        if old_hash is None:
            new_files.append((filename, new_hash))
        elif old_hash != new_hash:
            modified_files.append((filename, old_hash, new_hash))

    return modified_files, new_files

def display_results(modified, new):
    print("\033[1;96m==== Modified Files =====\033[0m")
    for filename, old_hash, new_hash in modified:
        print(f"\033[1;91m{filename}\n  \033[0mOld Hash: \033[1;93m{old_hash}\n \033[0m New Hash: \033[1;92m{new_hash}\n")

    print("\033[1;96m===== New Files =====\033[0m")
    for filename, new_hash in new:
        print(f"\033[1;91m{filename}\n\033[0m  Hash: \033[1;92m{new_hash}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_md5_csv.py <csv_one>.csv <csv_two>.csv")
        sys.exit(1)

    old_csv = sys.argv[1]
    new_csv = sys.argv[2]

    modified, new = compare_csv(old_csv, new_csv)
    display_results(modified, new)
