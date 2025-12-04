
AUBAU_ORDER = [
    ('1s',2),
    ('2s',2), ('2p',6),
    ('3s',2), ('3p',6),
    ('4s',2), ('3d',10), ('4p',6),
    ('5s',2), ('4d',10), ('5p',6),
    ('6s',2), ('4f',14), ('5d',10), ('6p',6),
    ('7s',2), ('5f',14), ('6d',10), ('7p',6)
]


EXCEPTIONS = {
    24: [('1s',2),('2s',2),('2p',6),('3s',2),('3p',6),('4s',1),('3d',5)],
    29: [('1s',2),('2s',2),('2p',6),('3s',2),('3p',6),('4s',1),('3d',10)],
    47: [('1s',2),('2s',2),('2p',6),('3s',2),('3p',6),('4s',2),('3d',10),('4p',6),('5s',1),('4d',10)],
    79: [('1s',2),('2s',2),('2p',6),('3s',2),('3p',6),('4s',2),('3d',10),('4p',6),('5s',2),('4d',10),('5p',6),('6s',1),('4f',14),('5d',10)],
}

def config(Z):
    if Z in EXCEPTIONS:
        return EXCEPTIONS[Z]
    rem = Z
    out = []
    for sub, cap in AUBAU_ORDER:
        if rem <= 0:
            break
        take = min(cap, rem)
        out.append((sub, take))
        rem -= take

    n = 8
    while rem > 0:
        take = min(2, rem)
        out.append((f"{n}s", take))
        rem -= take
        n += 1
    return out

def config_text(cfg):
    return " ".join(f"{s}{c}" for s,c in cfg)

BOHR_CAPS = [2,8,18,32,18,8,2]

def bohr_distribution(Z):
    rem = Z
    shells = []
    for cap in BOHR_CAPS:
        if rem <= 0:
            shells.append(0)
        else:
            take = min(cap, rem)
            shells.append(take)
            rem -= take
    return shells