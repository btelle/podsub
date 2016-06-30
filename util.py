from __future__ import print_function
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
import boto3, json

class schemas:
    auth_token = {
        'token': 'test-token-asdf',
        'expires': 1466727955.949729,
        'user_id': '12038674e56-sduyds-23238g-dsygser6t83'
    }
    
    user = {
        'id': '12038674e56-sduyds-23238g-dsygser6t83',
        'email': 'user@server.com',
        'passhash': '$2a$12$3UIdq0eXvo2LIP3Ae89T4.M4beFQLdXnsW/N91b6EZbBXSyESfeoq',
        'podcasts': [
            '762238678c98-87675ef334-2334adfe-2333434'
        ],
        'episodes': [
            'a06f86dd-ea2a-4616-91ee-a09fedd32cbd': {
                'status': 'in_progress',
                'progress': 1233
            }
        ]
    }
    
    podcast = {
        'id': '762238678c98-87675ef334-2334adfe-2333434',
        'title': 'Podcast Title',
        'description': 'Description of Podcast',
        'url': 'https://stitcher.com/shows/asdf.rss',
        'image': 'https://cdn.stitcher.com/asdf.jpg',
        'explicit': False
    }
    
    episode = {
        'id': 'a06f86dd-ea2a-4616-91ee-a09fedd32cbd',
        'guid': 'asdfsieehuods',
        'url': 'https://cdn.stitcher.com/asdf.mp3',
        'release_date': '2016-06-27T23:48:05-700',
        'duration': 2640
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
        resp = {'message': message, 'code': code}
        return resp
