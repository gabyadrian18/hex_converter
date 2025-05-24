def pretty_print_conversions(conv):
    colw1 = 22
    colw2 = 20
    colw3 = 23
    colw4 = 20

    header = f"{'Type':<{colw1}}{'Big (ABCD)':<{colw2}}{'Mid-Little (CDAB)':<{colw3}}{'Little (DCBA)':<{colw4}}"
    print(header)
    print('-' * (colw1 + colw2 + colw3 + colw4))

    for key, val in conv.items():
        # Format float cu 10 zecimale, tăiate dacă sunt prea lungi
        out = []
        for v in val:
            if isinstance(v, float):
                # Scoate din notația științifică doar dacă e foarte mic/mare
                s = f"{v:.10f}".rstrip('0').rstrip('.') if (1e-4 < abs(v) < 1e10) else f"{v:.10e}"
            else:
                s = str(v)
            if len(s) > colw2 - 2:  # taie dacă e prea lung
                s = s[:colw2-5] + "..."
            out.append(s)
        while len(out) < 3:
            out.append("")
        print(f"{key:<{colw1}}{out[0]:<{colw2}}{out[1]:<{colw3}}{out[2]:<{colw4}}")
        