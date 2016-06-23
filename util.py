from __future__ import print_function
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
import boto3

class dynamo:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb', 
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name='us-east-1'
        )
        
        self.tables = {}
        self.tables['podcasts'] = self.dynamodb.Table('podsub.podcasts')
        self.tables['episodes'] = self.dynamodb.Table('podsub.episodes')
        self.tables['users'] = self.dynamodb.Table('podsub.users')
    
    def get_one(self, table, id):
        if table not in self.tables:
            raise KeyError('Table not found')
        
        ret = self.tables[table].get_item(Key=id)
        
        if 'Item' in ret:
            return ret['Item']
        return None

class responses:
    def encode(obj):
        return json.dumps(obj)
    
    def error_message(code, message):
        resp = {'code': code, 'message': message}
        return responses.encode(resp)