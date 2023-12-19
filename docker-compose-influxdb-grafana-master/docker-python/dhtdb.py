import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import Adafruit_DHT as adht
import time

token = "rhPXftGjpVFgDaVPvL7dmPDuWaYBuMGV1KWmeRDvPvaPbUgIL7RmoAjra0yr7hynsxI6SXx6bu9l2yysD17uLA=="
org = "boobry"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="szopipi"
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

while True:     
    h,t = adht.read_retry(adht.DHT22, 4)    
    p = Point("Szopa").tag("location", "parter").field("temperature", h)
    write_api.write(bucket=bucket, record=p)
    p = Point("Szopa").tag("location", "parter").field("humidity", t)
    write_api.write(bucket=bucket, record=p)




