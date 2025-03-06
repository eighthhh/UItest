# author: "eight"
# date: 2025/2/27 15:03
import yaml

def get_yaml_data(file_path:str):
    with open(file_path,encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())
'''
if __name__ == '__main__':
    res = get_yaml_data('../config/test.yml')
    print(res)

'''
