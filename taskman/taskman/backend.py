from django.contrib.auth.models import User , check_password
from django.contrib.auth.backends import ModelBackend

class EmailAuth(ModelBackend):
	
	def authenticate(self,email=None, password=None):
		try:
			user_obj = User.objects.get(email=email)
			valid_passkey = user_obj.check_password(password)
			
			if valid_passkey:
				return user_obj
		except User.DoesNotExist:
			return None

