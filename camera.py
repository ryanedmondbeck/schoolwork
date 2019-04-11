
import sqlite3

#ADDRESS,CAMERA ID,VIOLATION DATE,VIOLATIONS,X COORDINATE,Y COORDINATE,LATITUDE,LONGITUDE,LOCATION
#7738 S WESTERN,CHI065,07/08/2014,65,,,,,

def create_db_and_table():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "CREATE TABLE speed_camera_violations_table (address text, cameraid text, day int, month int, year int, violations int)"
    cursor.execute(sql)
    cursor.close()

def add_speed_violation_data_to_database():
   
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    with open("Speed_Camera_Data.csv", "r") as f:
         for line in f:
             if not line.startswith("ADDRESS"):
                L = line.split(",")
                address = L[0]
                cameraid = L[1]
                date = L[2].split("/")
                month = int(date[0])
                day = int(date[1])
                year = int(date[2])
                violations = L[3]
                sql = "INSERT INTO speed_camera_violations_table  (address, cameraid, day, month, year, violations) VALUES (:address, :cameraid, :day, :month, :year, :violations)"
                cursor.execute(sql, {"address":address, "cameraid":cameraid, "day":day, "month":month, "year":year, "violations":violations})     
                conn.commit()
    cursor.close()

def display_all_db_data():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM speed_camera_violations_table" # * shorthand for all columns of the table
    columns = cursor.execute(sql)
    all_entries = columns.fetchall()
    for entry in all_entries:
        print(entry)  

def display_all_addresses():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql = "SELECT address FROM speed_camera_violations_table" # * shorthand for all columns of the table
    address_column = cursor.execute(sql)
    all_addresses = address_column.fetchall()
    for address in all_addresses:
        print(address)

def display_min_max_total_number_of_violations():
    #we can use Python to manipulate the data or we can use native SQL functions
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql1 = "SELECT MIN(violations) FROM speed_camera_violations_table"
    sql2 = "SELECT MAX(violations) FROM speed_camera_violations_table"
    sql3 = "SELECT SUM(violations) FROM speed_camera_violations_table"
    lowest_number = cursor.execute(sql1).fetchone()[0]
    highest_number = cursor.execute(sql2).fetchone()[0]
    total_number = cursor.execute(sql3).fetchone()[0]
    print(lowest_number, highest_number, total_number)


def main():
    
    create_db_and_table()
    add_speed_violation_data_to_database()
    display_all_db_data()
    print("-------")
    display_all_addresses()
    print("-------")
    display_min_max_total_number_of_violations()
main() 