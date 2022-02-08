import requests
import datetime

class FedexTracker:
    def __init__(self):
        self.session = requests.session()
        self.init_url_format = 'https://www.fedex.com/fedextrack/?tracknumbers={}'
        self.tracking_url = 'https://api.fedex.com/track/v2/shipments'

    def login(self, tracking_number):
        ### get client_id
        response = self.session.get('https://www.fedex.com/fedextrack/properties/WTRKProperties.json')
        self.client_id = response.json()['api']['client_id']

    def get_tracking(self, tracking_number):
        self.login(tracking_number)

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Authorization': 'Bearer {}'.format(self.client_id),
            'Content-Type': 'application/json',
            'Origin': 'https://www.fedex.com',
        }

        data = {
            'appDeviceType':'WTRK',
            'appType':'WTRK',
            'supportCurrentLocation':True,
            'trackingInfo': [
                {
                    'trackNumberInfo': {
                        'trackingCarrier':'',
                        'trackingNumber':tracking_number,
                        'trackingQualifier':''
                    }
                }
            ],
            'uniqueKey':''
        }

        response = self.session.post(self.tracking_url, json=data, headers=headers)

        if response.status_code != 200:
            print("request failed, error code : ",response.status_code)
            return

        res_json = response.json()
        package = res_json['output']['packages'][0]
        tracking_info = {
            'estDeliveryDateTime': package['estDeliveryDt'],
            'status': package['statusWithDetails'],
            'lastScanStatus': package['lastScanStatus'],
            'lastScanDateTime': package['lastScanDateTime'],
        }

        return tracking_info
