#Para conseguir mandar pushes no celular
import httplib
import urllib

##### SITE: https://pushover.net


#Funcoes para controle dos pushes
class PushoverSender:
	def __init__(self, user_key, api_key):
		self.user_key = user_key
		self.api_key = api_key

	def send_notification(self,text):
		conn = httplib.HTTPSConnection("api.pushover.net:443")
		post_data = {'user':self.user_key, 'token':self.api_key,'message':text}
		conn.request("POST","/1/messages.json",urllib.urlencode(post_data),{"Content-type":"application/x-www-form-urlencoded"})

pushover_sender = PushoverSender('u2a6tbkannveuw484savn9zx9x9fiu','a77ivooyg7194qqf8nqmwyy5dky52t')

pushover_sender.send_notification('Este eh um teste de push')

