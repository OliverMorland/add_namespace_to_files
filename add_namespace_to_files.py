import os
import sys
import time


def add_namespace_to_files(directory, namespace_name):
    for filename in os.listdir(directory):
        if filename.endswith(".cs"):  # Assuming you're working with cs files
            filepath = os.path.join(directory, filename)

            # Read the file contents
            with open(filepath, 'r') as file:
                lines = file.readlines()

            # Prepare new content with namespace declaration and closing brace
            new_lines = []
            namespace_added = False
            inside_namespace = False

            for line in lines:
                if line.strip().startswith("public class") and not namespace_added:
                    # Add the namespace line before the class declaration
                    new_lines.append(f'namespace {namespace_name} {{\n')
                    namespace_added = True
                    inside_namespace = True

                if inside_namespace:
                    # Add a tab before the line if inside the namespace
                    new_lines.append(f'\t{line}')
                else:
                    new_lines.append(line)

            if namespace_added:
                # Close the namespace block with '}'
                new_lines.append('}\n')

            # Write the modified content back to the file
            with open(filepath, 'w') as file:
                file.writelines(new_lines)
            print(f"Updated file: {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <namespace_name>")
        sys.exit(1)

    directory_path = sys.argv[1]
    namespace_name = sys.argv[2]

    add_namespace_to_files(directory_path, namespace_name)

    time.sleep(5)
