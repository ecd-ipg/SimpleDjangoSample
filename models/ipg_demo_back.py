

class IpgDemoBack:

    def __init__(self):
        self.state = '0'
        self.amount = '1000'
        self.error_code = ''
        self.error_description = ''
        self.reference_number = ''
        self.tracking_number = ''
        self.buy_id = ''
        self.token = ''

    def set_by_post(self, post):
        try:
            self.state = post.get('State')
            self.amount = post.get('Amount')
            self.error_code = post.get('ErrorCode')
            self.error_description = post.get('ErrorDescription')
            self.reference_number = post.get('ReferenceNumber')
            self.tracking_number = post.get('TrackingNumber')
            self.buy_id = post.get('BuyID')
            self.token = post.get('Token')
        except:
            pass
