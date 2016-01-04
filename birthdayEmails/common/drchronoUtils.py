import datetime, pytz, requests, os
from operator import itemgetter

#Birthday Email Keys
BIRTHDAY_CLIENT_SECRET = os.environ['BIRTHDAY_CLIENT_SECRET']
BIRTHDAY_CLIENT_ID = os.environ['BIRTHDAY_CLIENT_ID']

#Redirect URL
REDIRECT_URL = "http%3A//testingbirthdayapp.com%3A8000/signup"

def getDrchronoAuth(code):
    response = requests.post('https://drchrono.com/o/token/', data={
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://testingbirthdayapp.com:8000/signup',
        'client_id': BIRTHDAY_CLIENT_ID,
        'client_secret': BIRTHDAY_CLIENT_SECRET,
    })
    if response.status_code == requests.codes.ok:
        data = response.json()
        result = {
            'access_token': data['access_token'],
            'refresh_token': data['refresh_token'],
            'expires_timestamp': datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in']),
        }
    else:
        result = None
    return result

def getDrchronoLinkURL():
    return "https://drchrono.com/o/authorize/?redirect_uri="+REDIRECT_URL+"&response_type=code&client_id="+BIRTHDAY_CLIENT_ID

def getDrchronoPatientDetails(access_token):
    headers = {
        'Authorization': 'Bearer %s' % access_token,
    }
    patients = []
    patients_url = 'https://drchrono.com/api/patients'
    while patients_url:
        data = requests.get(patients_url, headers=headers).json()
        patients.extend(data['results'])
        patients_url = data['next'] # A JSON null on the last page
    return sorted(patients, key=itemgetter('last_name')) 

def refreshDrchronoAccessToken(refresh_token):
    response = requests.post('https://drchrono.com/o/token/', data={
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
        'client_id': BIRTHDAY_CLIENT_ID,
        'client_secret': BIRTHDAY_CLIENT_SECRET,
        })
    if response.status_code == requests.codes.ok:
        data = response.json()
        result = {
            'access_token': data['access_token'],
            'refresh_token': data['refresh_token'],
            'expires_timestamp': datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in']),
        }
    else:
        result = None
    return result
