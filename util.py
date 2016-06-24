from __future__ import print_function
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
import boto3, json

class schemas:
    auth_token = {
        'token': 'test-token-asdf',
        'expires': 1466727955.949729,
        'user_id': '12038674e56-sduyds-23238g-dsygser6t83'
    }

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
        self.tables['auth_tokens'] = self.dynamodb.Table('podsub.auth_tokens')
    
    def get_one(self, table, id):
        if table not in self.tables:
            raise KeyError('Table not found')
        
        ret = self.tables[table].get_item(Key=id)
        
        if 'Item' in ret:
            return ret['Item']
        return None
    
    def insert(self, table, item):
        if table not in self.tables:
            raise KeyError('Table not found')
        
        ret = self.tables[table].put_item(Item=item)
        return True
    
    def get_user_by_email(self, email):
        res = self.tables['users'].query(
            IndexName='email_index', 
            KeyConditionExpression=boto3.dynamodb.conditions.Key('email').eq(email.lower()),
            Limit=1
        )
        
        if 'Items' in res and len(res['Items']) > 0:
            return res['Items'][0]
        return None

class responses:
    def encode(self, obj):
        return json.dumps(obj)
    
    def error_message(self, code, message):
        resp = {'code': code, 'message': message}
        return self.encode(resp)
