# EastvantageTest
### Task description:
Create an address book application where API users can create, update and delete
addresses.
The address should:
- contain the coordinates of the address.
- be saved to an SQLite database.
- be validated


## Project Setup:
First take clone from repository given below:

Using HTTPS:

```
https://github.com/Ajkumar5686/EastvantageTest.git
```

Using SSH:
```
git@github.com:Ajkumar5686/EastvantageTest.git
```

Install python 3.8 or any latest version of python and Intall python3 virtual environment.

Create Virtual Environment:
```
python3 -m venv eastvantage_env
```

Activate Virtual Environment:
```
source eastvantage_env/bin/activate
```

Run Requirements
```
pip install -r requirements.txt 
```

Run Server:
```
uvicorn main:app --reload
```


Copy below link and paste it to browser url search bar:
```
http://127.0.0.1:8000/docs
```

### Add New Address
URL:
http://127.0.0.1:8000/address/

Method: POST

Payload: 
{
    "coordinates": "19.92108148417044, 96.18268294182562",
    "house_no": 234,
    "street": "new street",
    "city": "New york",
    "country": "USA"
}

### Get List of Address
URL:
http://127.0.0.1:8000/address/

Method: GET

### Update Address
URL:
http://127.0.0.1:8000/address/{address_id}

Method: PUT

Payload: 
{
    "coordinates": "19.92108148417044, 96.18268294182562",
    "house_no": 456,
    "street": "test street",
    "city": "New york",
    "country": "USA"
}

### Delete Address
URL:
http://127.0.0.1:8000/address/{address_id}

Method: DELETE
