import os
import re

def parse_line(line):
    line = line.rstrip('\n')
    # Replace tree drawing characters with spaces
    # Replace any occurrences of '├── ', '└── ', '│   ' with '    '
    line = re.sub(r'[│├└][─]*\s*', '    ', line)
    # Now count the leading spaces
    leading_spaces = len(line) - len(line.lstrip(' '))
    depth = leading_spaces // 4
    item_name = line.strip()
    return depth, item_name

def create_structure(input_string):
    lines = input_string.strip().split('\n')
    stack = []
    for line in lines:
        depth, item_name = parse_line(line)
        # Adjust the stack to the current depth
        while len(stack) > depth:
            stack.pop()
        if item_name.endswith('/'):
            # It's a directory
            item_name = item_name.rstrip('/')
            stack.append(item_name)
            path = os.path.join(*stack)
            os.makedirs(path, exist_ok=True)
        else:
            # It's a file
            path = os.path.join(*stack, item_name)
            # Ensure the directory exists
            os.makedirs(os.path.dirname(path), exist_ok=True)
            # Create an empty file
            with open(path, 'w') as f:
                pass

def main():
    print("Enter the directory structure (end with an empty line):")
    lines = []
    while True:
        try:
            line = input()
            if line == '':
                break
            lines.append(line)
        except EOFError:
            break
    input_string = '\n'.join(lines)
    create_structure(input_string)
    print("Directory structure created successfully.")

if __name__ == "__main__":
    main()

# given something like this:

# flask_erp/
# ├── app/
# │   ├── __init__.py
# │   ├── models.py
# │   ├── forms.py
# │   ├── routes.py
# │   ├── templates/
# │   │   ├── base.html
# │   │   ├── login.html
# │   │   ├── inventory.html
# │   │   ├── transactions.html
# │   │   ├── receive_stock.html
# │   │   ├── deliver_stock.html
# │   │   ├── sellout_stock.html
# │   │   ├── import_inventory.html
# │   ├── static/
# │       ├── styles.css
# │       ├── bootstrap.min.css
# ├── setup.py
# ├── run.py
# ├── requirements.txt
#

# it will make the folders locally (on windows)
# take note of the extra blank line to mark the end
