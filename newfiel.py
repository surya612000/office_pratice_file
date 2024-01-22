import csv
import re

# Your data
data = """
 {
    id: null
    firstName: DIVAS BY
    lastName: MITAL PATEL
    address: 25 PUSHPADHANWA BUNGALOW GATE NYAY MARG PUSHPADHANWA BUNGALOWS GATE 2 VASTRAPUR AHMEDABAD.
    city: 98
    zipCode: 380015
    phone1: 9979873649
    email1: DIVAS@GMAIL.COM
}



 {
    id: null
    firstName: Mascot
    lastName: Mascot
    address: Sidcul Ranipur Haridwar Uttarakhand
    249403
    city: 698
    zipCode: 249403
    phone1: 1234567890
    email1: Info@mascot.in
}


{
    id: null
    firstName: PROMAX
    lastName: OFIICRE
    address: KASTURBA NAGAR BLR
    city: 155
    zipCode: 560026
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}






{
    id: null
    firstName: Spark
    lastName: Spark
    address: Dalmill compound opp.j.k petrol pump
    Purna Village Bhiwandi 421302
    Maharashtra
    city: 455
    zipCode: 421302
    phone1: 1234567890
    email1: Info@spark.in
}

{
    id: null
    firstName: DEXZONE
    lastName: OFFICE
    address: DODDA NA NAGAR BLR
    city: 155
    zipCode: 560091
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

{
    id: null
    firstName: SSS
    lastName: UNIQUE
    address: HAFIZET HYD
    city: 36
    zipCode: 500049
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

{
    id: null
    firstName: SSS
    lastName:  UNIQUE
    address: hafuzet hyd
    city: 36
    zipCode: 500049
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

{
    id: null
    firstName: crafto
    lastName: office
    address: villgae bom
    city: 455
    zipCode: 421302
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

 {
    id: null
    firstName: GREEEN
    lastName: OFFI E
    address: AMMAN ANAGAR MAA
    city: 38
    zipCode: 600095
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

 {
    id: null
    firstName: SPICA
    lastName: OFFICE
    address: TANJAH APAET MAA
    city: 38
    zipCode: 600081
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

 {
    id: null
    firstName: MANSOON
    lastName: OFFICE
    address: MADIVALI BLR
    city: 155
    zipCode: 560068
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

{
    id: null
    firstName: FATHER
    lastName: LITAS
    address: RAMNAGAR BLR
    city: 155
    zipCode: 562107
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

{
    id: null
    firstName: GOOGLE
    lastName: OFFICE
    address: KRISHNA PURAM HOBLIBLR
    city: 155
    zipCode: 560037
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

 {
    id: null
    firstName: MR DESING
    lastName: OFFICE
    address: BESANT NAGAR MAA
    city: 38
    zipCode: 600090
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

 {
    id: null
    firstName: SATISH
    lastName: NAGAR
    address: GAHT HOBTOR WEST BOM
    city: 142
    zipCode: 400086
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}

{
    id: null
    firstName: RADHE
    lastName: OFFICE
    address: PRIGANT MUSLIM  PNQ
    city: 153
    zipCode: 411015
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRIC.COM
}


{
    id: null
    firstName: EXTRA
    lastName: OFFICE
    address: ASHOK NAGAR MAA
    city: 38
    zipCode: 600083
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRI.COM
}

 {
    id: null
    firstName: ISIST
    lastName: OFFICE
    address: KACHALLLI BLR
    city: 155
    zipCode: 560091
    phone1: 9811111111
    email1: RESPONCE@RESPONCEFABRI.COM
}

 {
  id: null
  firstName: BANTI KUMAR SAINI
  lastName: AJAY SINI
  address: Mumbai airport
  city: 142
  zipCode: 400099
  phone1: 9610436613
  email1: info@jmd.com
}

 {
  id: null
  firstName: BANTI KUMAR SAINI
  lastName: AJAY SAINI
  address: Mumbai airport
  city: 142
  zipCode: 400099
  phone1: 9610436613
  email1: info@jmd.com
}

{
  id: null
  firstName: Ajanta
  lastName: Pharma
  address: Gut No.11/12/14/15, Paithan Road,
  Chitegaon
  Chhatrapati Sambhajinagar
  city: 134
  zipCode: 431105
  phone1: 9052300223
  email1: treddy@iclscm.com
}

 {
  id: null
  firstName: Linux
  lastName: life Science
  address: Rs no 241?1 to 241/5, Kalitheenthal Kuppam Noolagadipel inolen 605107
  city: 1
  zipCode: 605001
  phone1: 9052300223
  email1: treddy@iclscm.com
}

 {
  id: null
  firstName: a
  lastName: b
  address: sd
  city: 38
  zipCode: 600005
  phone1: 1111111111
  email1: response.fabric@gmail.com
}

"""

# Extract individual records using a regex pattern
records = re.findall(r'{(.*?)}', data, re.DOTALL)

# Define the headers for the CSV file
headers = ["id", "firstName", "lastName", "address", "city", "zipCode", "phone1", "email1"]

# Specify the CSV filename
csv_filename = "output.csv"

# Write data to CSV file
with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write headers to CSV file
    writer.writerow(headers)
    
    for record in records:
        # Split each record into key-value pairs
        key_value_pairs = re.findall(r'(\w+):\s*([^,\n]+)', record)
        
        # Create a dictionary from the key-value pairs
        record_dict = dict(key_value_pairs)
        
        # Write data to CSV file
        writer.writerow([record_dict.get(header, "") for header in headers])

print(f"CSV file '{csv_filename}' has been created.")
