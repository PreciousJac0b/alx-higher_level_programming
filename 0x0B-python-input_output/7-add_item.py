#!/usr/bin/python3

"""adds all arguments to a list and saves them to a file"""

if __name__ == '__main__':
    import json
    import sys
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        new_list = load_from_json_file('add_item.json')
    except:
        new_list = []
    finally:
        new_list.extend(sys.argv[1:])
        save_to_json_file(new_list, 'add_item.json')
