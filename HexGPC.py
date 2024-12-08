import os
from hexgpc import process_file

def main():
    file_path = input("Enter the path of the file (image or video): ").strip().strip('"').strip("'")
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

    max_frames_input = input("Enter maximum number of frames to process (default 20): ").strip()
    max_frames = int(max_frames_input) if max_frames_input.isdigit() else 20

    try:
        c_code = process_file(file_path, invert, max_frames)
    except Exception as e:
        print(f"Error processing file: {e}")
        return

    base = os.path.splitext(os.path.basename(file_path))[0]
    output_file = f"{base}.gpc"
    with open(output_file, "w") as file:
        file.write(c_code)

    print(f"Hexadecimal values have been saved to {output_file}.")

if __name__ == "__main__":
    main()
