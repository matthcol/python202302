def sizeHumanReadable(size, unit="o", kilo = 2**10):
    """convert size in bytes in human readable form
        return str human readable size
        K: 1024, i.e 2**10
        M: 2**20
        G: 2**30
        T: 2**40
        P: 2**50
        E: 2**60
        Z: 2**70
        Y: 2**80
    """
    prefixes = ['','K','M','G','T','P','E','Z','Y']
    lastunit = True
    for p in prefixes[:-1]:
        if size < kilo:
            lastunit = False
            break
        size /= kilo
    if lastunit:
        p = prefixes[-1]
    return f"{size:.3f} {p}{unit}"