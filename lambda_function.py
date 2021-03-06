from __future__ import print_function
from podsub import PodSub
from util import responses

def lambda_handler(event, context):
    pod = PodSub()
    
    try:
        endpoint = event['context']['resource-path'].lower()
        method = event['context']['http-method'].lower()
    except KeyError:
        raise RuntimeError(responses.error_message(400, 'Bad Response'))
    
    if 'AuthToken' in event['params']['header']:
        user = pod.get_user_by_auth_token(event['params']['header']['AuthToken'])
    
    if endpoint == '/register' and method == 'post':
        return pod.register(event['body-json'])
    
    if endpoint == '/login' and method == 'post':
        return pod.login(event['body-json'])
    
    if endpoint == '/podcasts' and method == 'get':
        return pod.get_podcasts(user, **event['params']['querystring'])
    
    if endpoint == '/podcasts' and method == 'post':
        return pod.post_podcast(user, event['body-json'])
    
    if endpoint == '/podcasts/{id}' and method == 'get':
        return pod.get_podcast(user, event['params']['path']['id'])

    if endpoint == '/podcasts/{id}' and method == 'delete':
        return pod.delete_podcast(user, event['params']['path']['id'])
    
    if endpoint == '/episodes' and method == 'get':
        return pod.get_episodes(user, **event['params']['querystring'])
    
    if endpoint == '/episodes/{id}' and method == 'put':
        return pod.update_episode(user, event['params']['path']['id'], event['body-json'])

    if endpoint == '/episodes/{id}' and method == 'delete':
        return pod.delete_episode(user, event['params']['path']['id'])
    
    if endpoint == '/episodes/{id}' and method == 'get':
        return pod.get_episode(user, event['params']['path']['id'])
    
    raise RuntimeError(responses.error_message(400, 'Bad Request'))
