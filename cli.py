import sys
from hex_converter.converter import get_conversions
from hex_converter.utils import pretty_print_conversions

def main():
    if len(sys.argv) > 1:
        hexstr = sys.argv[1]
    else:
        hexstr = input("Introduceți hex string: ")
    conv = get_conversions(hexstr)
    pretty_print_conversions(conv)
    print("\nHex representations:")
    print(f"Big endian:        {conv['Hex'][0]}")
    print(f"Mid-little endian: {conv['Hex'][1]}")
    print(f"Little endian:     {conv['Hex'][2]}")

if __name__ == "__main__":
    main()
    