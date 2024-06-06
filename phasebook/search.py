from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    
    # new container for searched items
    search_list = []
    
    # temporary containers of search results per filter
    search_filters = {
        "id" : [],
        "name": [],
        "age": [],
        "occupation": []
    }
    
    

    # loop through users data
    for item in USERS:
        
        # loop through url args
        for key, val in args.items():
            
            if key  == "id":
                if args[key] == str(item[key]):
                    # if not is_included(item['id'], searched_byID):
                        search_filters['id'].append(item)
                        
                        
            elif key == "age":
                if int(args[key]) >= item["age"] - 1 and int(args[key]) <= item["age"] + 1:
                    # if not is_included(item['id'], searched_byAge):
                        search_filters['age'].append(item)
                        
                        
            elif key == "name":
                if item[key].find(args[key]) >= 0:
                    # if not is_included(item['id'], searched_byName):
                        search_filters['name'].append(item)
                        
                        
            elif key == "occupation":
                if item[key].find(args[key]) >= 0:
                    # if not is_included(item['id'], searched_byOccupation):
                        search_filters['occupation'].append(item)
                        

    # loop through args to sort the result by priority
    # arg index is equals to sort priority order
    for arg in args:
        
        # loop through the temporary containers
        for key, val in search_filters.items():
            if key == arg:
                for item in search_filters[arg]:
                    # validate if item is already appended in the search_list
                    if not is_included(item['id'], search_list):
                        search_list.append(item)
            
    return search_list


def is_included(id, given_list):
    
    for item in given_list:
        
        if str(item['id']) == str(id):
            
            return True
        
    return False

    
