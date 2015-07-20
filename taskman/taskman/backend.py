from django.contrib.auth.models import User , check_password
from django.contrib.auth.backends import ModelBackend

class EmailAuth(ModelBackend):
	"""
	Custom Backend to support authentication via Email and Password
	"""
	def authenticate(self,email=None, password=None):
		try:
			user_obj = User.objects.get(email=email)
			valid_passkey = user_obj.check_password(password)
			
			if not valid_passkey:
				user_obj.error="Username/Password missmatch"
				return user_obj
			else:
				user_obj.error = None
				return user_obj
		except User.DoesNotExist:
			return None

