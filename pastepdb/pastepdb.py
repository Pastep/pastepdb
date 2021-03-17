# imports
from os import walk, mkdir, remove
from json import loads, dumps
import pastepdb.config as module_config
from betterlog import log


# variables


# classes 

class pastepdb:

    def __init__(self, database_folder, database_config):
        self.database_folder = database_folder
        self.database_config = database_config

    def __read_config(self):
        file = open(self.database_config, 'r', encoding='utf-8')
        return loads(file.read())

    def __get_type(self, value):
        if type(value) == int:
            return "int"
        return "string"

    def __list_files(self, path):
        items = []
        for (dirpath, dirnames, filenames) in walk(path):
            items.extend(filenames)
            break
        return items

    @property
    def database_folder(self):
        return self.__database_folder

    @database_folder.setter
    def database_folder(self, new_data):
        self.__database_folder = new_data

    @property
    def database_config(self):
        return self.__database_config

    @database_config.setter
    def database_config(self, new_data):
        if '.json' in new_data:
            self.__database_config = new_data

    def migrate(self):
        config = self.__read_config()
        if not config:
            raise SystemExit(module_config.database_config['database_config_empty'])
        files = []
        for (dirpath, dirnames, filenames) in walk(self.database_folder):
            files.extend(filenames)
            files.extend(dirnames)
            break
        if files:
            raise SystemExit(module_config.database_folder['directory_not_empty'])

        for table in config:
            try:
                mkdir(f"{self.database_folder}/{table}")
                log(f"Directory {table} created at {self.database_folder}/{table}").info()
            except:
                raise SystemExit(f"ERROR: Failed to create {table} folder, Check permissions and etc.")
        log('Database structures successfully created.').success()

    def insert(self, target_database, data):
        value = data
        if not type(value) == dict:
            raise SystemExit(module_config.database_crud['value_isnot_dict'])
        config = self.__read_config()
        config = config[target_database]["values"]
        counter = 0
        for (dirpath, dirnames, filenames) in walk(f"{self.database_folder}/{target_database}"):
            try:
                counter = int(filenames[-1].replace('.txt', '')) + 1
            except:
                counter = 0
            break

        default_data = {}
        for item in config:
            default_data[item] = config[item]['default']
        for item in value:
            if not config[item]['type'] == self.__get_type(value[item]):
                raise SystemExit(f"ERROR: DataType of {item} is not same as config file.")
            default_data[item] = value[item]
        file = open(f"{self.database_folder}/{target_database}/{counter}.txt", "w", encoding="utf-8")
        file.write(dumps(default_data))
        file.close()

        return True

    def read(self, database, values):
        items = self.__list_files(path=f"{self.database_folder}/{database}")
        result = []
        for item in items:
            file = open(f"{self.database_folder}/{database}/{item}", 'r', encoding='utf-8')
            data = loads(file.read())
            for value in values:
                if values[value] == data[value]:
                    result.append(data)
            file.close()
        return result

    def get(self, database, where):
        result = self.read(database, where)
        if not len(result) == 1:
            raise LookupError("ERROR: There's more than 1 item with same values, use pastepdb.read instead of get method to get a list of items.")
        
        return result[0]
    
    def update(self, database, where, new_values):

        if 'id' in where:
            try:
                file_path = f"{self.database_folder}/{database}/{where['id']}.txt"
                file = open(file_path, 'r', encoding='utf-8')
                data = loads(file.read())
                file.close()
                file = open(file_path, 'w', encoding='utf-8')
                for new_value in new_values:
                    data[new_value] = new_values[new_value]
                file.write(dumps(data))
                return True
            except FileNotFoundError:
                raise SystemExit(f"ERROR: No such file or directory: '{where['id']}.txt'")
        elif 'params' in where:
            where = where['params']
            items = self.__list_files(path=f"{self.database_folder}/{database}")
            result = []
            for item in items:
                file = open(f"{self.database_folder}/{database}/{item}", 'r', encoding='utf-8')
                data = loads(file.read())
                for value in where:
                    if where[value] == data[value]:
                        result.append(item)
            file.close()
            if result:
                if len(result) == 1:
                    result = result[0]
                    result = f"{self.database_folder}/{database}/{result}"
                    file = open(result, 'r', encoding='utf-8')
                    data = loads(file.read())
                    for new_value in new_values:
                        data[new_value] = new_values[new_value]
                    file.close()
                    file = open(result, 'w', encoding='utf-8')
                    file.write(dumps(data))
                    file.close()
                    return True
                else:
                    raise LookupError("ERROR: There's more than 1 data that has same params.")
            else:
                raise LookupError(f"ERROR: There's no data that has {where} in it...")
        else:
            raise SystemExit(f"ERROR: No Parameters as target_data (id or params)")

    def delete(self, database, where):

        if 'id' in where:
            try:
                file_path = f"{self.database_folder}/{database}/{where['id']}.txt"
                remove(file_path)
                return True
            except FileNotFoundError:
                raise SystemExit(f"ERROR: No such file or directory: '{where['id']}.txt'")
        elif 'params' in where:
            where = where['params']
            items = self.__list_files(path=f"{self.database_folder}/{database}")
            result = []
            for item in items:
                file = open(f"{self.database_folder}/{database}/{item}", 'r', encoding='utf-8')
                data = loads(file.read())
                for value in where:
                    if where[value] == data[value]:
                        result.append(item)
            file.close()
            if result:
                if len(result) == 1:
                    result = result[0]
                    result = f"{self.database_folder}/{database}/{result}"
                    remove(result)
                    return True
                else:
                    raise LookupError("ERROR: There's more than 1 data that has same params.")
            else:
                raise LookupError(f"ERROR: There's no data that has {where} in it...")
        else:
            raise SystemExit(f"ERROR: No Parameters as target_data (id or params)")