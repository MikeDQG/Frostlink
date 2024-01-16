from requests import Response, Session
import urllib3
from urllib3.util.ssl_ import create_urllib3_context
from urllib3 import PoolManager, disable_warnings
from requests.adapters import HTTPAdapter
disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Requester():
    def __init__(self):
        self.session = self.get_unverified_session()
        self.get_cookie()
        self.token = self.login()


    def get_unverified_session(self) -> Session:

        class AddedCipherAdapter(HTTPAdapter):
            def init_poolmanager(self, connections, maxsize, block=False):
                ctx = create_urllib3_context(ciphers=":HIGH:!DH:!aNULL")
                self.poolmanager = PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_context=ctx
                )

        s = Session()
        s.verify = False
        s.mount("https://192.168.3.50", AddedCipherAdapter())
        return s
    

    def get_cookie(self):
        self.session.get('https://192.168.3.50/PIC6/')
    
    def _any_request(self, url, payload) -> Response:
        response = self.session.post(url, json=payload)
        if response.status_code != 200:
            self.logout()
            self.token = self.login()
        response = self.session.post(url, json=payload)
        if response.status_code != 200:
            raise Exception("Connection failed")
        return response

    def login(self):
        url = 'https://192.168.3.50/PIC6/api/auth/login'
        payload = {
            "password": "0011",
            "username": "user"
        }
        response = self.session.post(url, json=payload)
        data = response.json()
        print(data)
        print(response.status_code)
        
        return str(data[0]['token']) # str(data['data'])
      

    def logout(self):
        url = 'https://192.168.3.50/PIC6/api/auth/logout'
        payload = { "token": self.token }
        response = self.session.post(url, json=payload)
        print(response.status_code)
        print(response.json())

    def monitoring(self):
        url = 'https://192.168.3.50/PIC6/api/monitor_tasks/getmonitoringtaskupdates'
        payload = {"token": self.token}
        response = self._any_request(url=url, payload=payload)
        print(response.status_code)
        return response.json()
        
    
    def get_point_value(self):
        url = 'https://192.168.3.50/PIC6/api/point_value/getpointvalue'
        payload = {
            "pathlist":[
                {"widgetType":"PointValue","path":"db/Ui_Syn_Msg_Bottom/description"},
                {"widgetType":"PointValue","path":"db/Ui_Alias_CAP_T/present-value"},
                {"widgetType":"PointValue","path":"db/Ui_Alias_COND_EWT/present-value"},
                {"widgetType":"PointValue","path":"db/Ui_Alias_EWT/present-value"},
                {"widgetType":"PointValue","path":"db/Ui_Alias_LWT/present-value"},
                {"widgetType":"PointValue","path":"db/Ui_Alias_COND_LWT/present-value"},
                {"widgetType":"PointValue","path":"db/Ui_Alias_CTRL_PNT/present-value"},
                {"widgetType":"PointValue","path":"db/Ui_Alias_OAT/present-value"},
                {"widgetType":"PointValue","path":"db/Ui_Alias_unit_typ/present-value"},
                {"widgetType":"PointValue","path":"db/CTRLID_DEV_LOCATION/active-text"},
                {"widgetType":"PointValue","path":"db/Ui_Alias_FLOW_SW/present-value"},
                {"widgetType":"PointValue","path":"db/Ui_runtest_ip/active-text"},
                {"widgetType":"PointValue","path":"db/Ui_runtest_mask/active-text"},
                {"widgetType":"PointValue","path":"db/Ui_runtest_eth/active-text"}],
            "token": self.token
        }
        # handle response, print it out in a custom format
        response = self._any_request(url=url, payload=payload)
        print(response.status_code)
        return response.json()
        

    def confirm_alarms(self):
        #print("token: ", self.token)
        url = 'https://192.168.3.50/PIC6/api/tabular_data/savetabulardatainfo'
        payload = {"datasource":"ALARMRST","type":"service_data","data":[{"path":"ccn/ALARMRST/0","value":"1"}],"token":self.token}
        response = self._any_request(url=url, payload=payload)
        print(response.status_code)
        return response.json()
        
    
    def get_alarms(self):
        url = 'https://192.168.3.50/PIC6/api/tabular_data/gettabulardatainfo'
        payload = {
            "token":self.token,
            "path":"ALARMRST",
            "type":"service_data",
            "POC_table":"0"}
        response = self._any_request(url=url, payload=payload)
        print(response.status_code)
        return response.json()