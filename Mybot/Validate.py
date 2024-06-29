from .models import Loginform
def checkuser(content):
    usr=content.get('first')
    if len(Loginform.objects.filter(user_name = usr))>0:
        for i in Loginform.objects.filter(user_name=usr):
            if i.pwd == content.get('password'):
                return True
            return False

class Data():
    def __init__(self) -> None:
        self.Document_data = {}
        self.web_data={}
        self.hidden ={}
        self.optimized= False
    def optimize_data(self):
        if not self.optimized:
            if 'Defendant1' in self.Document_data.keys():
                self.Document_data['Defendant1']+='' if len(self.Document_data['Dfs'])==1 else ' and another' if len(self.Document_data['Dfs'])==2 else ' and others'
                self.Document_data['tag2']='Defendant' if len(self.Document_data['Dfs'])==1 else 'Defendants'
                self.Document_data['tag4']='Respondent' if len(self.Document_data['Dfs'])==1 else 'Respondents'
            if 'Plaintiff1' in self.Document_data.keys():
                self.Document_data['Plaintiff1']+='' if len(self.Document_data['Pfs'])==1 else ' and another' if len(self.Document_data['Pfs'])==2 else ' and others'   
                self.Document_data['tag1']='Plaintiff' if len(self.Document_data['Dfs'])==1 else 'Plaintiffs'
                self.Document_data['tag3']='Plaintiff' if len(self.Document_data['Dfs'])==1 else 'Plaintiffs'