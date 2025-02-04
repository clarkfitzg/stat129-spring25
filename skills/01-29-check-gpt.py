#!/usr/bin/env python3
# chatGPT generated checking code

import os
import subprocess

def check_directory_exists(path):
    return os.path.isdir(path)

def check_file_exists(path):
    return os.path.isfile(path)

def check_q3_content():
    q3_path = os.path.expanduser('~/skills/01-29/q3.txt')
    if not check_file_exists(q3_path):
        return False
    
    expected_output = subprocess.run(['ls', '/stat129/class/'], capture_output=True, text=True).stdout.strip()
    with open(q3_path, 'r') as f:
        file_content = f.read().strip()
    
    return file_content == expected_output

def main():
    home = os.path.expanduser('~')
    skills_path = os.path.join(home, 'skills')
    skills_subdir = os.path.join(skills_path, '01-29')
    q3_file = os.path.join(skills_subdir, 'q3.txt')
    
    checks = {
        "Skills directory exists": check_directory_exists(skills_path),
        "01-29 directory exists": check_directory_exists(skills_subdir),
        "q3.txt exists": check_file_exists(q3_file),
        "q3.txt content matches expected": check_q3_content()
    }
    
    for desc, result in checks.items():
        print(f"{desc}: {'PASSED' if result else 'FAILED'}")

if __name__ == "__main__":
    main()
