from __future__ import print_function
from util import responses, dynamo
from decimal import Decimal
import uuid, bcrypt, time

class PodSub:
    def __init__(self):
        self.db = dynamo()
        self.responses = responses()
        
    def register(self, body):
        exists = self.db.get_user_by_email(body['email'])
        if exists:
            return self.responses.error_message(400, 'User already exists')
        else:
            user = {
                'id': str(uuid.uuid4()), 
                'email': body['email'], 
                'passhash': bcrypt.hashpw(body['password'], bcrypt.gensalt())
            }
            self.db.insert('users', user)
            
            auth_token = {
                'token': uuid.uuid4().hex, 
                'expires': Decimal(time.time()+60*60*6), 
                'user_id': user['id']
            }
            self.db.insert('auth_tokens', auth_token)
            
            return self.responses.encode({'token': auth_token['token'], 'message': 'Registered successfully'})
    
    def login(self, body):
        user = self.db.get_user_by_email(body['email'])
        if user:
            if bcrypt.checkpw(body['password'], user['passhash']):
                auth_token = {
                    'token': uuid.uuid4().hex, 
                    'expires': Decimal(time.time()+60*60*6), 
                    'user_id': user['id']
                }
                self.db.insert('auth_tokens', auth_token)
                return self.responses.encode({'token': auth_token['token'], 'message': 'Logged in successfully'})
            else:
                return self.responses.error_message(403, 'Authentication Error: Permission Denied')
        else:
            return self.responses.error_message(403, 'Authentication Error: Permission Denied')
