import os
from hexgpc import converter

def main():
    file_path = input("Enter the path of the image: ").strip().strip('"').strip("'")
    if not os.path.isfile(file_path):
        print("Error: File not found.")
        return

    print("1. Black Logo on White Background")
    print("2. White Logo on Black Background")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        invert = False
    elif choice == "2":
        invert = True
    else:
        print("Invalid choice.")
        return

    try:
        gpc_script = converter(file_path, invert=invert)
    except Exception as e:
        print(f"Error processing image: {e}")
        return

    base = os.path.splitext(os.path.basename(file_path))[0]
    output_file = f"{base}.gpc"
    with open(output_file, "w") as file:
        file.write(gpc_script)
    print(f"Hexadecimal values have been saved to {output_file}.")

if __name__ == "__main__":
    main()
