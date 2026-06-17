import sqlite3
from pathlib import Path
import csv
def main():
    p = Path("db") / "customers_db.db"
    
    csv_file = "MOCK_DATA.csv"
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        final_data = list(reader)
    
    # C'est pas si nul !!
    # conn = sqlite3.connect(p)
    

    with sqlite3.connect(p) as conn:
        sql = "INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) VALUES(?,?,?,?,?)"
        cur = conn.cursor()
        for data in final_data:
            del data['id']
            data.values()
            cur.execute(sql,list(data.values()))
            
    
    conn.close()


if __name__=='__main__':
    main()
