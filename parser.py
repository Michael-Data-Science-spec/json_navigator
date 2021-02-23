'''
Lab3 Task2 Mykhailo Kuzmyn
User can either navigate in given json file, or enter one's bearer token
and navigate through
'''
import json
import requests


def twitter_api(name, token="AAAAAAAAAAAAAAAAAAAAAIKvMwEAAAAAGfXtAizYuenmkYuQLZ4qCDL%2F3n8%3D0Bqy4HA6TVWqzcYq7Nk9UK0slRiRyVZvlEBtpyowkdXOupLBNf"):
    base_url = "https://api.twitter.com/"

    bearer_token = token

    search_url = '{}1.1/friends/list.json'.format(base_url)

    search_headers = {
        'Authorization': 'Bearer {}'.format(bearer_token)
    }

    search_params = {
        'screen_name': '@' + str(name),
        'count':15
    }

    response = requests.get(search_url, headers = search_headers, params=search_params)
    return response


def get_json():
    '''
    gets .json object using Twitter API
    returns a dict of this object
    '''
    pass


def is_dict(json_object):
    '''
    gets object type (dict or list)
    returns True if object is a dict
    '''
    if isinstance(json_object, dict):
        return True

    return False


def is_dict_or_list(json_object):
    '''
    gets object type (dict or list)
    returns True if object is a dict
    '''
    if isinstance(json_object, dict) or isinstance(json_object, list):
        return True

    return False


def get_keys(json_dict):
    '''
    gets keys of a dict
    returns keys as a list
    '''
    return json_dict.keys()


def get_len(lst: list):
    '''
    returns length of a list
    '''
    return len(lst)


def dict_navigator(dct: dict):
    '''
    navigates inside the dict
    '''
    keys = get_keys(dct)
    print('following item is a dict\n\
select key you would like to explore from from', keys)
    user_input = input()

    try:
        return navigator(dct[user_input])
    except KeyError:
        print('wrong key, try again')
        return navigator(dct)


def list_navigator(lst: list):
    '''
    navigates inside the list
    '''
    length = get_len(lst)
    print('following item is a list\n\
select index of an element, you would like to explore from 1 to', length)
    user_input = input()

    try:
        return navigator(lst[int(user_input) - 1])

    except IndexError:
        print('wrong index, try again')
        return navigator(lst)

    except ValueError:
        print('type a number, try again')
        return navigator(lst)


def navigator(json_object):
    '''
    navigates inside the json file
    '''
    if is_dict_or_list(json_object):

        if is_dict(json_object):
            return dict_navigator(json_object)

        else:
            return list_navigator(json_object)

    return json_object


def choice():
    '''
    checks if user wants to navigate withing given file
    or Twitter API json file
    '''
    print('if u want to navigate with given file, enter 0\n\
else: enter your bearer token')
    user_input = input()
    if user_input == '0':
        with open('friends_list_AdamMGrant.json', 'r') as f:
            json_obj = json.load(f)

        print(navigator(json_obj))

    else:
        print('enter a twitter username without a @ sign')
        username = input()
        try:
            json_obj = twitter_api(username, user_input).json()
            print(navigator(json_obj))
        except:
            print('wrong bearer token')


choice()
