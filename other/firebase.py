import pyrebase
from firebase import firebase

# pyrebase ===========================
# certificate
local_certificate = certifi.where()
print('certifi: ' + local_certificate)
current_path = os.path.dirname(os.path.abspath(os.getcwd()))
os.environ['REQUESTS_CA_BUNDLE'] = local_certificate
self.config = {
    "apiKey": "AIzaSyCDjRq7efp30nTT0H3yFnRTw8Ik5B6tMoI",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://databaseName.firebaseio.com",
    "storageBucket": "projectId.appspot.com"
}
self.firebase = pyrebase.initialize_app(self.config)
self.auth = self.firebase.auth()

def login(self):
  email = self.ui.login_input.text()
  password = self.ui.password_input.text()
  try:
      self.auth.sign_in_with_email_and_password(email, password)
  except Exception as ex:
      error_response = str(ex).split('"message": "')[1].split('"')[0]
      self.ui.label_error.setStyleSheet('color: red')
      self.ui.label_error.setText(error_response)


# firebase =========================== 
firebase = firebase.FirebaseApplication('https://inrems-a8a50.firebaseio.com/')
data = {
    'Name': 'Evgeny Ravlyuk',
    'Email': 'vivexpro@gmail.com',
}

result = firebase.patch('/inrems-a8a50/users-x/', data)
result = firebase.post('/inrems-a8a50/users/', data)
result = firebase.get('/inrems-a8a50/users/', '')
result = firebase.put('/inrems-a8a50/users/-M0dhVbRpTgMG1rLjSUg', 'Name', 'Zheka')
result = firebase.delete('/inrems-a8a50/users/', '-M0dhVbRpTgMG1rLjSUg')
print(result)
