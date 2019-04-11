# Ryan Beck | MCS 275 | Project 3 | December 5, 2018

# Create a one-table SQLite database of the file Public_Passenger_Vehicle_Licenses.csv using SQLite with Python, where each column corresponds to the column in the file. In addition, using either SQLite commands alone, or in combination with Python, answer the following questions. 

# 1. How large is the database in kilobytes? (You don't need to use SQL or Python for this)
    # A. 901 KB
# 2. What percent of the cars are hybrid fuel based? 
    # A. 48.7%
# 3. How old is the average car (in years), based on vehicle model year? 
    # A. 34.856 years old
# 4. How many different vehicle models are there?
    # A. 197 models
# 5. What is the most common vehicle model?
    # A. Camry
# 6  Aside from Chicago, what is the second most common city/town of origin of these cars? 
    # A. Elmhurst
# 7. What zip code contains the most registered public passenger vehicles?  
    # A. 60618


# ======================================================================================================
import sqlite3
# ======================================================================================================
# Vehicle Type,Status,Vehicle Make,Vehicle Model,Vehicle Model Year,Vehicle Color,Vehicle Fuel Source,Wheelchair Accessible,City,State,ZIP Code
def create_db_and_table():
    conn = sqlite3.connect("ppvl.db")
    cursor = conn.cursor()
    sql = "CREATE TABLE public_passenger_vehicle_licenses_table (vehicle_type text, status text, vehicle_make text, vehicle_model text, vehicle_model_year int, vehicle_color text, vehicle_fuel_source text, wheelchair_accessible text, city text, state text, zip_code int)"
    cursor.execute(sql)
    cursor.close()
# ======================================================================================================
def add_public_passenger_data_to_database():
   
    conn = sqlite3.connect("ppvl.db")
    cursor = conn.cursor()

    with open("Public_Passenger_Vehicle_Licenses.csv", "r") as f:
         for line in f:
             if not line.startswith("Vehicle Type"):
                L = line.split(",")
                vehicle_type = L[0]
                status = L[1]
                vehicle_make = L[2]
                vehicle_model = L[3]
                vehicle_model_year = L[4]
                vehicle_color = L[5]
                vehicle_fuel_source = L[6]
                wheelchair_accessible = L[7]
                city = L[8]
                state = L[9]
                zip_code = L[10]
                
                sql = "INSERT INTO public_passenger_vehicle_licenses_table  (vehicle_type, status, vehicle_make, vehicle_model, vehicle_model_year, vehicle_color, vehicle_fuel_source, wheelchair_accessible, city, state, zip_code) VALUES (:vehicle_type, :status, :vehicle_make, :vehicle_model, :vehicle_model_year, :vehicle_color, :vehicle_fuel_source, :wheelchair_accessible, :city, :state, :zip_code)"
                cursor.execute(sql, {"vehicle_type":vehicle_type, "status":status, "vehicle_make":vehicle_make, "vehicle_model":vehicle_model, "vehicle_model_year":vehicle_model_year, "vehicle_color":vehicle_color, "vehicle_fuel_source":vehicle_fuel_source, "wheelchair_accessible":wheelchair_accessible, "city":city, "state":state, "zip_code":zip_code})     
                conn.commit()
    cursor.close()
# ======================================================================================================
def display_all_db_data():
    conn = sqlite3.connect('ppvl.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM public_passenger_vehicle_licenses_table" # * shorthand for all columns of the table
    columns = cursor.execute(sql)
    all_entries = columns.fetchall()
    for entry in all_entries:
        print(entry)  
# ======================================================================================================
def count_hybrids():
    conn = sqlite3.connect('ppvl.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM public_passenger_vehicle_licenses_table WHERE vehicle_fuel_source == 'Hybrid'"
    fuel_column = cursor.execute(sql)
    all_fuel = fuel_column.fetchall()
    hybrid_count = 0
    for x in all_fuel:
        hybrid_count += 1
        # print(x)
    # print("hybrid_count: ", hybrid_count)
    sql = "SELECT vehicle_fuel_source FROM public_passenger_vehicle_licenses_table"
    fuel_column = cursor.execute(sql)
    all_fuel = fuel_column.fetchall()
    total_count = 0
    for x in all_fuel:
        total_count += 1
    print("The percentage of hybrids is:", hybrid_count/total_count)
# =====================================================================================================
def find_average_age():
    conn = sqlite3.connect('ppvl.db')
    cursor = conn.cursor()
    sql3 = "SELECT SUM(vehicle_model_year) FROM public_passenger_vehicle_licenses_table"
    year_sum = cursor.execute(sql3).fetchone()[0]

    sql = "SELECT vehicle_model_year FROM public_passenger_vehicle_licenses_table"
    year_column = cursor.execute(sql)
    all_years = year_column.fetchall()
    num_years = 0
    for x in all_years:
        num_years += 1

    print("The average age of a car is", 2018 - (year_sum/num_years), "years.")
# ======================================================================================================
# I wish I figured out the count function earlier on!
def count_unique_models():
    conn = sqlite3.connect('ppvl.db')
    cursor = conn.cursor()
    sql = "SELECT COUNT(DISTINCT vehicle_model) FROM public_passenger_vehicle_licenses_table"
    num_models = cursor.execute(sql).fetchone()[0]
    print("The number of unique car models is: ", num_models)
# ======================================================================================================
def find_most_common_model():
    conn = sqlite3.connect('ppvl.db')
    cursor = conn.cursor()
    sql = "SELECT vehicle_model, COUNT(vehicle_model) AS amount FROM public_passenger_vehicle_licenses_table GROUP BY vehicle_model ORDER BY amount DESC"
    model_name = cursor.execute(sql).fetchone()[0]
    print("The most common car model is: ", model_name)
# ======================================================================================================
def find_most_common_city():
    conn = sqlite3.connect('ppvl.db')
    cursor = conn.cursor()
    sql = "SELECT city, COUNT(city) AS amount FROM public_passenger_vehicle_licenses_table WHERE city !='CHICAGO' GROUP BY city ORDER BY amount DESC"
    most_city = cursor.execute(sql).fetchone()[0]
    print("The most common city besides Chicago is: ", most_city)
# ======================================================================================================
def find_most_common_zip():
    conn = sqlite3.connect('ppvl.db')
    cursor = conn.cursor()
    sql = "SELECT zip_code, COUNT(zip_code) AS amount FROM public_passenger_vehicle_licenses_table  GROUP BY zip_code ORDER BY amount DESC"
    most_zip = cursor.execute(sql).fetchone()[0]
    print("The most common zip code is: ", most_zip)
# ======================================================================================================
def main():
    
    create_db_and_table()
    add_public_passenger_data_to_database()
    display_all_db_data()
    print("--------------------------------------------------------------------")
    count_hybrids()        
    print("--------------------------------------------------------------------")
    find_average_age()
    print("--------------------------------------------------------------------")
    count_unique_models()
    print("--------------------------------------------------------------------")
    find_most_common_model()
    print("--------------------------------------------------------------------")
    find_most_common_city()
    print("--------------------------------------------------------------------")
    find_most_common_zip()
    print("--------------------------------------------------------------------")
    print_formatted()

main() 