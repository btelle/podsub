from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY
import boto3

class db:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb', 
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
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

def lambda_function(event, context):
    db = db()
    
    print(db.get_one('users', 1))
