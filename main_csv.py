from pprint import pprint


def main():

    csv_file = "MOCK_DATA.csv"

# split
# slicing
# zip
    with open(csv_file) as f:
        data = f.readlines()
        header = data[0].strip().split(",")
        all_data = data[1:]
        final_data = []

        for line in all_data:
            data_line = line.strip().split(",")
            d = dict(zip(header, data_line))

            # d={}
            # for i in range(len(header)):
            #     print(i)
            #     d[header[i]] = data_line[i]
            final_data.append(d)

    pprint(final_data, sort_dicts=False)


if __name__ == '__main__':
    main()
