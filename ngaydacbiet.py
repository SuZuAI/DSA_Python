def main():
    a = ["02", "20", "22"]
    b = ["2000", "2002", "2020", "2022", "2200", "2202", "2220", "2222"]
    for i in a:
        for j in b:
            print("{}/02/{}".format(i, j))
main()