from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from channels.db import database_syn_to_async


user=get_user_model()

class CustomAuthMiddleware(BaseMiddleware):
    async def __call__(self, receive,scope,send):
        user=await self.get_user(scope)
        scope['user']=user
        return await super().__call__(scope, receive,send)
    @database_syn_to_async
    def get_user(self,scope):
        query_string=str(scope["query_string"].decode('utf-8')).split("=")
        ["token","kjnasjfhgahjsgf"]
        token=query_string[1]
        if token:
            try:
                access_token=AccessToken(token)
                user=User.objects.get(id=access_token['user_id'])
                return user
            except User.DoesnotExists:
                pass
            
        return AnonymousUser()
        