# PastepDB
## _Nosql Based Database_

PastepDB is a fast json database with cool methods.
It makes a seperated file for each data and it can index them quickly

- Fast
- Easily config and migration
- ✨ Magic ✨
- Embedded database

## Features

- Read method
- Get method
- Insert data
- Delete data
- Update data
- Migrate

> PastepDB is used in https://pastep.com and Pastep Discord bot


## Installation

PastepDB requires [Python](https://python.org) v3.6+ to run.

Install PastepDB using PIP

```sh
pip install pastepdb
```

_Dependencies_:
(not needed to install manually, it will install automatically)
```sh
pip install betterlog
```

## Starting a database:
- First setup Database config (it can be fount bellow `Starting a Database` section)
- Setup a folder called `database` (name its changeable...)
- Import `PastepDB` into your project
```py
from pastepdb import pastepdb

pastepdb = pastepdb(database_config='database_config.json', database_folder='database')
```
- Migrate your database for creating folders and etc... using migrate method (After delete it)
```py
pastepdb.migerate()
```


## Config files:
- ### Database config file(Json file)
_This is a sample_
```json
{
    "users": {
        "values": {
            "fname": {
                "type": "string",
                "default": ""
            },
            "lname": {
                "type": "string",
                "default": ""
            },
            "number": {
                "type": "int",
                "default": 900
            }
        }
    },
    "posts": {
        "values": {
            "title": {
                "type": "string",
                "length": 100,
                "default": "Untitled"
            }
        }
    }
}
```
## Methods

Want to use PastepDB? Great!
Here is a tutorial for methods (CRUD)

### Insert Data:

```py
# Inserted data is sample
response = pastepdb.insert(target_database='users', data={
    'fname': 'Pooria',
    'lname': 'Ahmadi',
    'phone_number': "0903333333"
})
print(response) # Will return True if its successfull
```

### Read data:

- #### Read method:
```py
# Filtered data is sample
response = pastepdb.read(database='users', values={
    'fname': 'Pooira'
})
print(response) # Will return a LIST of founded data's
for item in response:
    print(response)
```
- #### Get method:
```py
# Recived data is sample
response = pastepdb.get(database='users', where={
    'fname': 'Pooira'
})
print(response) # Will return a DICT object with data 
```
- #### All method:
```py
# Recived list is sample
response = pastepdb.all(database='users')
print(response) # Will return a list object with data 
```

### Update Data:
- ### Method 1: (Using file id)
```py
# Updated data is sample
response = pastepdb.update(database='users', where={
    'id': 3
}, new_values={
    "fname": "The man who is a man"
})
print(response) # Will return True if operation is successful
```
- ### Method 2: (Using where method):
```py
# Updated data is sample
response = pastepdb.update(database='users', where={
    "params": {
        "fname": "Pooria"
    }
}, new_values={
    "fname": "The man who is a man"
})
print(response) # Will return True if operation is successful
```

### Delete Data:
- ### Method 1: (Using file id)
```py
# Deleted data is sample
response = pastepdb.delete(database='users', where={
    'id': 3
})
print(response) # Will return True if operation is successful
```
- ### Method 2: (Using where method)
```py
# Deleted data is sample
response = pastepdb.delete(database='users', where={
    "params": {
        "fname": "Pooria"
    }
})
print(response) # Will return True if operation is successful
```

## License

MIT

