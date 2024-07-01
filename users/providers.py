from urllib.parse import urlencode
from social_core.backends.oauth import BaseOAuth2
from django.conf import settings

class FortyTwoOAuth2(BaseOAuth2):
	name = 'fortytwo'
	AUTHORIZATION_URL = 'https://api.intra.42.fr/oauth/authorize'
	ACCESS_TOKEN_URL = 'https://api.intra.42.fr/oauth/token'
	ACCESS_TOKEN_METHOD = 'POST'

	def get_user_details(self, response):
		return {
			'username': response.get('username'),
			'email': response.get('email'),
			'first_name': response.get('first_name'),
			'last_name': response.get('last_name'),
		}
	
	def user_data(self, access_token, *args, **kwargs):
		url = 'https://api.intra.42.fr/v2/me?' + urlencode({
			'access_token': access_token
		})
		return self.get_json(url)

