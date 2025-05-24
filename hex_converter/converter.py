import struct

def swap_mid_endian(b):
    # Pentru 4 bytes: ABCD -> CDAB
    if len(b) == 4:
        return b[2:4] + b[0:2]
    # Pentru 8 bytes: ABCDEFGH -> GHEFCDAB
    elif len(b) == 8:
        return b[4:8] + b[0:4]
    else:
        return b

def to_ascii(b):
    return ''.join([chr(x) if 32 <= x <= 126 else '.' for x in b])

def get_conversions(hexstr: str):
    hexstr = hexstr.replace(" ", "").replace("0x", "")
    if len(hexstr) % 2 != 0:
        hexstr = "0" + hexstr
    b = bytes.fromhex(hexstr)
    n = len(b)

    big = b
    little = b[::-1]
    mid = swap_mid_endian(b)

    result = {}

    # 8 bit
    if n >= 1:
        result["Unsigned 8-bit"] = (big[-1], "-", little[-1])
        result["Signed 8-bit"] = (
            big[-1]-256 if big[-1] > 127 else big[-1],
            "-",
            little[-1]-256 if little[-1] > 127 else little[-1]
        )

    # 16 bit
    if n >= 2:
        result["Unsigned 16-bit"] = (
            int.from_bytes(big[-2:], "big"),
            "-",
            int.from_bytes(little[-2:], "little")
        )
        result["Signed 16-bit"] = (
            int.from_bytes(big[-2:], "big", signed=True),
            "-",
            int.from_bytes(little[-2:], "little", signed=True)
        )

    # 32 bit
    if n >= 4:
        # Extrage corect cei 4 bytes pentru fiecare interpretare
        b4_big = big[-4:]
        b4_little = little[-4:]
        b4_mid = swap_mid_endian(b4_big)

        result["Unsigned 32-bit"] = (
            int.from_bytes(b4_big, "big"),
            int.from_bytes(b4_mid, "big"),
            int.from_bytes(b4_little, "little")
        )
        result["Signed 32-bit"] = (
            int.from_bytes(b4_big, "big", signed=True),
            int.from_bytes(b4_mid, "big", signed=True),
            int.from_bytes(b4_little, "little", signed=True)
        )
        # Floats
        try:
            f_big = struct.unpack(">f", b4_big)[0]
        except:
            f_big = "-"
        try:
            f_mid = struct.unpack(">f", b4_mid)[0]
        except:
            f_mid = "-"
        try:
            f_little = struct.unpack("<f", b4_little)[0]
        except:
            f_little = "-"
        result["Float 32-bit"] = (f_big, f_mid, f_little)

    # 64 bit
    if n >= 8:
        b8_big = big[-8:]
        b8_little = little[-8:]
        b8_mid = swap_mid_endian(b8_big)
        result["Unsigned 64-bit"] = (
            int.from_bytes(b8_big, "big"),
            int.from_bytes(b8_mid, "big"),
            int.from_bytes(b8_little, "little")
        )
        result["Signed 64-bit"] = (
            int.from_bytes(b8_big, "big", signed=True),
            int.from_bytes(b8_mid, "big", signed=True),
            int.from_bytes(b8_little, "little", signed=True)
        )
        try:
            d_big = struct.unpack(">d", b8_big)[0]
        except:
            d_big = "-"
        try:
            d_mid = struct.unpack(">d", b8_mid)[0]
        except:
            d_mid = "-"
        try:
            d_little = struct.unpack("<d", b8_little)[0]
        except:
            d_little = "-"
        result["Float 64-bit"] = (d_big, d_mid, d_little)

    # ASCII pentru tot hexul (toate variantele)
    result["ASCII"] = (to_ascii(big), to_ascii(mid), to_ascii(little))
    result["Hex"] = (big.hex().upper(), mid.hex().upper(), little.hex().upper())
    return result
    