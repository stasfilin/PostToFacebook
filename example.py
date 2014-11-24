import webbrowser
import requests # pip install requests

class Facebook:
    def __init__(self):
        self.client_id = "XXXXXXXXXXXXX"
        self.client_secret = "XXXXXXXXXXXXXXXXXXXXX"
        self.redirect_url = 'http://localhost:8080'
        try:
            webbrowser.open('https://www.facebook.com/dialog/oauth?client_id='+self.client_id+'&redirect_uri='+self.redirect_url+'&scope=offline_access,public_profile,publish_actions,user_activities,user_about_me')
            code = raw_input("Type code: ")
            self.code = self.check_code(code)
            r = requests.session()
            b = r.post('https://graph.facebook.com/oauth/access_token?client_id='+self.client_id+'&redirect_uri=http://localhost:8080/?code='+self.code+'&client_secret='+self.client_secret+'&code='+self.code)
            access_token = b.text.split('&')
            self.access_token = access_token[0].split('=')[1]
        except:
            print 'Error'

    def check_code(self, code):
        code = code.replace(self.redirect_url,'')
        code = code.replace('/?code=', '')
        code = code.replace('#_=_', '')
        return code
    def post(self, to="me", source={}):
        url = 'https://graph.facebook.com/v2.2/'+to+'/feed?access_token='+self.access_token
        for i in source:
            url+="&"+i+"="+"+".join(str(source[i]).split(' '))
        r = requests.session()
        b = r.post(url)
        

f = Facebook()
par = {'message': "True",
      'picture': "http://cs625727.vk.me/v625727914/7a5b/X68oTIAYvU4.jpg"
}

f.post(to="me", source=par)