import sys
from hex_converter.converter import get_conversions
from hex_converter.utils import pretty_print_conversions

def main():
    # Dacă ai dat argument în linia de comandă, îl procesează o dată și apoi intră în loop
    if len(sys.argv) > 1:
        hexstr = sys.argv[1]
        conv = get_conversions(hexstr)
        pretty_print_conversions(conv)
        print("\nHex representations:")
        print(f"Big endian:        {conv['Hex'][0]}")
        print(f"Mid-little endian: {conv['Hex'][1]}")
        print(f"Little endian:     {conv['Hex'][2]}")
        print()

    print("Type a hex string to convert, or type 'exit' to quit.\n")
    while True:
        try:
            hexstr = input("Hex string: ").strip()
            if hexstr.lower() in ("exit", "quit", ""):
                print("Bye!")
                break
            conv = get_conversions(hexstr)
            pretty_print_conversions(conv)
            print("\nHex representations:")
            print(f"Big endian:        {conv['Hex'][0]}")
            print(f"Mid-little endian: {conv['Hex'][1]}")
            print(f"Little endian:     {conv['Hex'][2]}")
            print()
        except Exception as e:
            print(f"Error: {e}\nTry again or type 'exit' to quit.\n")

if __name__ == "__main__":
    main()
