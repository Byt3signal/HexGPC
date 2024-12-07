import os, sys, subprocess
try:
    from PIL import Image, ImageOps
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"]) #Installs packages for you
    from PIL import Image, ImageOps

def converter(file_path, invert=False, display_width=128, display_height=64):
    img = Image.open(file_path)
    img = img.convert("L")
    if invert:
        img = ImageOps.invert(img)
    img = img.resize((min(img.width, display_width), min(img.height, display_height)), Image.Resampling.LANCZOS)
    width, height = img.size
    x = (display_width - width) // 2
    y = (display_height - height) // 2
    img = img.convert("1", dither=Image.FLOYDSTEINBERG)
    pixels = list(img.getdata())
    hex_vals = []
    for i in range(0, len(pixels), 8):
        byte = 0
        for bit in range(8):
            if i + bit < len(pixels) and pixels[i + bit] == 0:
                byte |= 1 << (7 - bit)
        hex_vals.append(f"0x{byte:02X}")
    formatted = []
    for i in range(0, len(hex_vals), 16):
        line = ", ".join(hex_vals[i:i+16])
        formatted.append(f"        {line}")
    hex_data = ",\n".join(formatted)
    Form = (
        f"const image picture[] = {{\n"
        f"    {{\n"
        f"        {width}, {height},\n"
        f"{hex_data}\n"
        f"    }}\n"
        f"}};\n\n"
        f"init {{\n"
        f"    cls_oled(OLED_BLACK);\n"
        f"    image_oled({x}, {y}, TRUE, TRUE, picture[0]);\n"
        f"}}"
    )
    return Form

def main():
    file_path = input("Enter Path  of Image; ").strip().strip('"').strip("'")
    if not os.path.isfile(file_path):
        print("Can't find the path🤷‍♂️")
        return
    print("1. Black Logo white background")
    print("2. White logo Black Background")
    choice = input("Choose an option (1 or 2): ").strip()
    if choice == "1":
        invert = False
    elif choice == "2":
        invert = True
    else:
        print("Invalid choice")
        return
    try:
        gpc_script = converter(file_path, invert)
    except Exception as e:
        print(f"Error processing image: {e}")
        return
    base = os.path.splitext(os.path.basename(file_path))[0]
    output_file = f"{base}.gpc"
    with open(output_file, "w") as file:
        file.write(gpc_script)
    print(f"hexadecimal values have been saved to {output_file}.")

if __name__ == "__main__":
    main()
