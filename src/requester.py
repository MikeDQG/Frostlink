from requests import Session
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
        self.session.get("https://192.168.3.50/PIC6/")

    def login(self):
        url = 'https://192.168.3.50/PIC6/api/auth/login'
        send_object = {
            "password": "0011",
            "username": "user"
        }
        response = self.session.post(url, json=send_object)
        data = response.json()
        print(data)
        print(response.status_code)
        
        return str(data[0]['token']) # str(data['data'])
        print(token)
        
        headers = {
            'Content-Type': 'application/json'
        }

    def logout(self):
        url = 'https://192.168.3.50/PIC6/api/auth/logout'
        payload = { "token": self.token }
        response = self.session.post(url, json=payload)
        print(response.status_code)
        print(response.json())

    def get_temps(self):
        url = 'https://192.168.3.50/PIC6/api/menu/getmenutable'
        payload = {
                    "token": self.token,
                    "path": "TEMP",
                    "type": "service_data",
                    "POC_table": "0"
                }
        response = self.session.post(url, json=payload)
        print(response.json())

    def navigate(self):
        url = 'https://192.168.3.50/PIC6/api/user_navigation_history/savenavigationhistory'
        payload = {"fromPage":"Home - CARRIER 30XW","toPage":"Main Menu","userAccessLevel":"NONE","timestamp":1702820981960,"currentMobileOS":"unknown","token":self.token}
        response = self.session.post(url, json=payload)
        print(response.status_code)
    

    def navigate2(self):
        url = 'https://192.168.3.50/PIC6/api/user_navigation_history/savenavigationhistory'
        payload = {"fromPage":"Main Menu","toPage":"Menu_Target_Status_Table","userAccessLevel":"NONE","timestamp":1702820983861,"currentMobileOS":"unknown","token":self.token}
        response = self.session.post(url, json=payload)
        print(response.status_code)

    def monitoring(self):
        url = 'https://192.168.3.50/PIC6/api/monitor_tasks/getmonitoringtaskupdates'
        payload = {"token": self.token}
        response = self.session.post(url, json=payload)
        print(response.status_code)
    

        