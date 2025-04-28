# sort_dream.py

def sort_dream_file(filename="daydream.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Strip trailing newlines, sort the lines alphabetically
        lines = [line.strip() for line in lines if line.strip()]
        lines.sort()

        # Add a blank line after each line
        formatted_lines = [line + '\n\n' for line in lines]

        # Write the formatted lines back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(formatted_lines)

        print(f"Sorted '{filename}' and added blank lines between each line.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    sort_dream_file()
    sort_dream_file(filename="understood.txt")
