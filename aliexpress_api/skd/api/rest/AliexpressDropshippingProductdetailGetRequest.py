from ..base import RestApi


class AliexpressDropshippingProductdetailGetRequest(RestApi):

    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        RestApi.__init__(self, domain, port)
        self.app_signature = None
        self.ship_to_country = None
        self.product_id = None
        self.target_currency = None
        self.target_language = None

    def getapiname(self):
        return "aliexpress.ds.product.get"
