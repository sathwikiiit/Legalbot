from typing import Any
from django.shortcuts import render,HttpResponse
from .Validate import checkuser,Data
from .Doc import create_document,create_suit
# Create your views here.
from django.template.loader import render_to_string
from django.conf import settings
import os

session = Data()
def login(request):
    session.web_data['user']= 'Guest'
    return render(request,'Login.html',session.web_data)
def dashboard(request):
    content = request.POST
    if checkuser(content):
        session.web_data['user']= content.get('first')
        return render(request,'Dashboard.html',session.web_data)
    else:
        session.web_data['content']='INVALID USERNAME OR PASSWORD, PRESS BACK AND ENTER CORRECT CREDENTIALS'
        return render(request,'Error.html',session.web_data)
def confirm(request):
    context = request.POST.dict()
    del context['csrfmiddlewaretoken']
    session.hidden['docs']=[]
    for i,j in context.items():
        if j=='on':
            session.hidden['docs']+=[i]
    for i in session.hidden['docs']:
        del context[i]
    context['Dfs']=context['Dfs'].split('\r\n')
    context['Pfs']=context['Pfs'].split('\r\n')
    context['IANumber']='    ' if context['IANumber']=='' else  context['IANumber']
    context['OSNumber']='    'if context['OSNumber']=='' else context['OSNumber']
    for i,j in context.items():
        session.web_data[i]=j
        session.Document_data[i]=j
    context['Dfs']= ', '.join(session.Document_data['Dfs'])
    context['Pfs']= ', '.join(session.Document_data['Pfs'])
    session.web_data['dict']=context.items()
    return render(request,'ConfirmDetails.html',session.web_data)
def suit_form(request):
    return render(request,'Suit_Form.html',session.web_data)
def suit_type(request):
    return render(request,'SuitType.html',session.web_data)

def Document(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'new.docx')
    session.optimize_data()
    create_suit(render_to_string('suit.html',session.Document_data),file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
        
def Notice(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'new.docx')
    session.optimize_data()
    create_document(render_to_string('notice.html',session.Document_data),file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response