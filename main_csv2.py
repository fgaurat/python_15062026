import csv
import json
from pprint import pprint


def main():
    csv_file = "MOCK_DATA.csv"
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        final_data = list(reader)
    
    pprint(final_data,sort_dicts=False)
    
    with open("data.json","w") as f:
        json.dump(final_data,f,indent=4)

if __name__=='__main__':
    main()
