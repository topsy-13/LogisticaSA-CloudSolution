from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import random

# Crear la aplicación FastAPI
app = FastAPI()

# Modelo Pydantic para representar un registro con las nuevas columnas
class Record(BaseModel):
    VendorID: int
    tpep_pickup_datetime: str
    tpep_dropoff_datetime: str
    passenger_count: int
    trip_distance: float
    RatecodeID: int
    store_and_fwd_flag: str
    PULocationID: int
    DOLocationID: int
    payment_type: int
    fare_amount: float
    extra: float
    mta_tax: float
    tip_amount: float
    tolls_amount: float
    improvement_surcharge: float
    total_amount: float
    congestion_surcharge: float
    airport_fee: float

# Función para conectar con la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect("./data_wrangling/nyc_taxi.db")
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint para obtener un registro aleatorio
@app.get("/random")
def get_random_record():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()
    conn.close()
    if not records:
        raise HTTPException(status_code=404, detail="No records found.")
    random_record = random.choice(records)
    return {
        "VendorID": random_record["VendorID"],
        "tpep_pickup_datetime": random_record["tpep_pickup_datetime"],
        "tpep_dropoff_datetime": random_record["tpep_dropoff_datetime"],
        "passenger_count": random_record["passenger_count"],
        "trip_distance": random_record["trip_distance"],
        "RatecodeID": random_record["RatecodeID"],
        "store_and_fwd_flag": random_record["store_and_fwd_flag"],
        "PULocationID": random_record["PULocationID"],
        "DOLocationID": random_record["DOLocationID"],
        "payment_type": random_record["payment_type"],
        "fare_amount": random_record["fare_amount"],
        "extra": random_record["extra"],
        "mta_tax": random_record["mta_tax"],
        "tip_amount": random_record["tip_amount"],
        "tolls_amount": random_record["tolls_amount"],
        "improvement_surcharge": random_record["improvement_surcharge"],
        "total_amount": random_record["total_amount"],
        "congestion_surcharge": random_record["congestion_surcharge"],
        "airport_fee": random_record["airport_fee"]
    }

# Endpoint para obtener un número específico de registros
@app.post("/records")
def get_specific_number_of_records(count: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()
    conn.close()
    if not records:
        raise HTTPException(status_code=404, detail="No records found.")
    if count > len(records):
        raise HTTPException(status_code=400, detail="Requested count exceeds available records.")
    selected_records = random.sample(records, count)
    return [{
        "VendorID": record["VendorID"],
        "tpep_pickup_datetime": record["tpep_pickup_datetime"],
        "tpep_dropoff_datetime": record["tpep_dropoff_datetime"],
        "passenger_count": record["passenger_count"],
        "trip_distance": record["trip_distance"],
        "RatecodeID": record["RatecodeID"],
        "store_and_fwd_flag": record["store_and_fwd_flag"],
        "PULocationID": record["PULocationID"],
        "DOLocationID": record["DOLocationID"],
        "payment_type": record["payment_type"],
        "fare_amount": record["fare_amount"],
        "extra": record["extra"],
        "mta_tax": record["mta_tax"],
        "tip_amount": record["tip_amount"],
        "tolls_amount": record["tolls_amount"],
        "improvement_surcharge": record["improvement_surcharge"],
        "total_amount": record["total_amount"],
        "congestion_surcharge": record["congestion_surcharge"],
        "airport_fee": record["airport_fee"]
    } for record in selected_records]