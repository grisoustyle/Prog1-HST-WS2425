def alphabet(string):
    geteilt = []
    for zeichen in string:
        if zeichen not in geteilt:
            geteilt.append(zeichen)

    return sorted(geteilt)

print(alphabet("hstmeanstuasmeanshst"))
