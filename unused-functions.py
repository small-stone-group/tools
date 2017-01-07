import os
import sys
import re
import glob

def main():
    args = sys.argv
    folder = args[1]

    for filename in glob.iglob('{0}/**/*.cfc'.format(folder)):
        with open(filename, 'r') as file:
            lineNumber = 0
            for line in file:
                lineNumber += 1
                match = re.search('<cffunction[\s\S]*name="([\S]+)"', line)
                if match:
                    name = match.group(1)
                    used = False
                    for script in glob.iglob('{0}/**/*.*'.format(folder)):
                        with open(script, 'r') as s:
                            for line in s:
                                if re.search(name, line):
                                    used = True
                                    break
                    if not used:
                        print(filename, lineNumber, name)

if __name__ == '__main__':
    main()
