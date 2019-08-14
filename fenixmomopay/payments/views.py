import http.client, urllib.request, urllib.parse, urllib.error, base64
from payments.models import MomoRequest


def generate_token(key, authorization, body):
    headers = {
        # Request headers
        'Authorization': authorization,
        'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
        conn.request("POST", "/disbursement/token/?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

'''function to create payment request'''
def requesttopay(authorization, target_env, key, callback_url, ref_id, body):
    headers = {
        # Request headers
        'Authorization': authorization,
        'X-Callback-Url': callback_url,
        'X-Reference-Id': ref_id,
        'X-Target-Environment': target_env,
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
        conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


'''function to get status of the payments'''
def get_status(authorization, target_env, key, body, referenceid):
    headers = {
        # Request headers
        'Authorization': authorization,
        'X-Target-Environment': target_env,
        'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
        conn.request("GET", "/collection/v1_0/requesttopay/" + referenceid + "?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def account_balance(authorization, target_env, key, body):
    headers = {
        # Request headers
        'Authorization': authorization,
        'X-Target-Environment': target_env,
        'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
        conn.request("GET", "/disbursement/v1_0/account/balance?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def validate_account(authorization, target_env, key):
    headers = {
        # Request headers
        'Authorization': authorization,
        'X-Target-Environment': target_env,
        'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
        conn.request("GET",
                     "/disbursement/v1_0/accountholder/{accountHolderIdType}/{accountHolderId}/active?%s" % params,
                     "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def create_momo_request(request):
    if request.method == 'GET':
        '''takes assumption that form data is already json encoded'''
        momo_request = MomoRequest.objects.create(request.body)
        '''trigger a collection request here upon successful object creation'''
        if momo_request.pk is not None:
            requesttopay("kjdakjd", "windows", "jhdas2",  "https://fenixcollections.ug/pay/sucess/", 213123, request.body)
        else:
            print("Momo Request Object not created")
