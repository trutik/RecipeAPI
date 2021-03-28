from sqlalchemy.sql import exists


class Storage:
    """
    A layer of abstraction between the higher level API code in routes.py and the lower level interactions of the target database.
    Changes to the database or storage system used and low level optimisations are decoupled from the high level API logic.
    """
    def __init__(self):
        pass

    def item_exists(self, item_name:str, attr_filters:dict):
        return True
        # filter_ = [self.storage[item_name][attr_name] == attr_value for attr_name, attr_value in attr_filters.items()]
        # return self.session.query(exists().where(filter_)).scalar()
    
    def get_items(self, *args, **kwargs):
        return [{'Name':'RecipeMany'}]

    def get_item(self, *args, **kwargs):   
        return {'Name':'RecipeMany'}

    def update_item(self, *args, **kwargs):
        return None
    
    def delete_item(self, *args, **kwargs):
        return {'Name':'RecipeSingle'}
    
    def add_item(self, *args, **kwargs):
        return None

    