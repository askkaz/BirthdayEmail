import datetime, pytz, requests
def getDrchronoAuth(code):
    response = requests.post('https://drchrono.com/o/token/', data={
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://testingbirthdayapp.com:8000/birthdayEmails/signup',
        'client_id': 'zWgcsmzbQdkPZOf1YJBP63Ou0Ln0V7AqAF8kHWTq',
        'client_secret': 'A7t5QaRRqjl66Yo4wOJ7xeKe4RZTPv6zFFJYGEAhq30Jo6iLYyglQiJ809oCFL09LKJhmnuHrT7jqfZm1xNGVguUt2UKt047QdMumJopsc2Xe0cWUUvTNcU44DW5Y81n',
    })

    response.raise_for_status()
    data = response.json()
    result = {
        'access_token': data['access_token'],
        'refresh_token': data['refresh_token'],
        'expires_timestamp': datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in']),
    }
    return result