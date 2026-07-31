def doi_tien(gia, tienkhach):
    tienthua = tienkhach - gia
    menhgia = [20, 10, 5, 2, 1]
    soto = 0

    for m in menhgia:
        soto += tienthua // m
        tienthua %= m

    return so_to


gia, tienkhach = map(int, input().split())
print(doi_tien(gia, tienkhach))