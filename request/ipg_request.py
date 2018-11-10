import hashlib, requests, json
import time as time_
import datetime


def get_buy_id():
    try:
        return int(round(time_.time() * 1000))
    except:
        return 123456789


def get_token(lang):
    try:
        terminal_number = "YOUR TERMINAL NUMBER"
        password = "YOUR PASSWORD"
        redirect_url = 'http://www.ecd-co.ir/solutions/ipg/demo/back'  # YOUR BACK ADDRESS

        buy_id = str(get_buy_id())

        amount = '1000'  # set your amount

        dt = datetime.datetime.now()
        date = dt.strftime('%Y-%m-%d')
        time = dt.strftime('%H:%M')

        hash_string = terminal_number + buy_id + amount + date + time + redirect_url + password
        check_sum = hashlib.sha1(hash_string.encode('utf-8')).hexdigest()
        params = {
            'TerminalNumber': terminal_number,
            'BuyID': buy_id,
            'Amount': amount,
            'date': date,
            'time': time,
            'RedirectURL': redirect_url,
            'Language': lang,
            'CheckSum': check_sum.upper(),
        }
        response = requests.post('https://ecd.shaparak.ir/ipg_ecd/PayRequest',
                                 data=json.dumps(params),
                                 headers={'Content-type': 'application/json; charset=utf-8',
                                          'Accept': 'text/json',
                                          'User-Agent': 'firefox'})

        if response.status_code == 200:
            body = response.json()
            if "Res" in body:
                return body.get("Res")

        return None

    except:
        return None


def submit_confirm(ipg_demo_back):
    try:
        params = {
            "Token": ipg_demo_back.token
        }
        requests.post('https://ecd.shaparak.ir/ipg_ecd/PayConfirmation',
                      data=json.dumps(params),
                      headers={'Content-type': 'application/json; charset=utf-8',
                               'Accept': 'text/json',
                               'User-Agent': 'firefox'})
        return None

    except:
        return None


def submit_reverse(ipg_demo_back):
    try:
        params = {
            "Token": ipg_demo_back.token
        }
        requests.post('https://ecd.shaparak.ir/ipg_ecd/PayReverse',
                      data=json.dumps(params),
                      headers={'Content-type': 'application/json; charset=utf-8',
                               'Accept': 'text/json',
                               'User-Agent': 'firefox'})
        return None

    except:
        return None
