from shapely import wkb

ENVELOPES = (
    ("none",0),
    ("xy",32),
    ("xyz",48),
    ("xym",48),
    ("xyzm",64)
)

def decode(b):
    # Magic bytes
    assert(b[:2].decode() == "GP")

    # Weird version byte
    version = b[2]

    # Bit-flags
    flags = format(b[3],"08b")

    # Parsing bit flags
    meta = {
        "gpbType": "ext" if int(flags[2]) is "1" else "std",
        "empty": bool(int(flags[3])),
        "envelope": ENVELOPES[int(f"0b{flags[4:7]}",2)],
        "endianness": "little" if int(flags[7]) else "big"
    }

    # If there is a geometry
    if not meta["empty"]:
        envname,envlength = meta["envelope"]
        headerLength = 8 + envlength 

        g = wkb.loads(b[headerLength:])

        return g
    else:
        return None

        
    

