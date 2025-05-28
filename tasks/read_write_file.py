# task 1 : write a code to read helloworld.txt and then write it back message : hello world in french language program title : read_write_file.py

def read_and_write_file(filename):
    # Read the original content
    try:
        with open(filename, 'r') as file:
            original_content = file.read()
            print("Original content:")
            print(original_content)
    except FileNotFoundError:
        print(f"{filename} not found. Proceeding to write the French message.")

    # Write the French translation
    french_message = "Bonjour le monde"
    with open(filename, 'w') as file:
        file.write(french_message)
        print(f"\nNew content written to {filename}.")


if __name__ == "__main__":
    read_and_write_file("helloworld.txt")

