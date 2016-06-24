from __future__ import print_function
from util import dynamo

def auth_handler(event, context):
    token = event['authorizationToken']
    db = dynamo()
    
    token_item = db.get_one('auth_tokens', token)
    
    if token_item:
        if token_item['expires'] > time.time():
            return generatePolicy(token['user_id'], 'Allow', event['methodArn'])
        else:
            return generatePolicy(token['user_id'], 'Deny', event['methodArn'])
        
    else:
        return "Unauthorized"

def generatePolicy(principalId, effect, resource):
    authResponse = {}
    authResponse['principalId'] = principalId
    if effect and resource:
        policyDocument = {}
        policyDocument['Version'] = '2012-10-17'
        policyDocument['Statement'] = []
        
        statementOne = {}
        statementOne['Action'] = 'execute-api:Invoke'
        statementOne['Effect'] = effect
        statementOne['Resource'] = resource
        policyDocument['Statement'].append(statementOne)
        
        authResponse['policyDocument'] = policyDocument
    return authResponse
