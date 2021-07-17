from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from Utilizer.models import Contact
from django.contrib import messages
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'index.html')

# def about(request):
#     return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')
def analyze(request):
    # get's the text
    djtext=request.POST.get('text', 'deafult')

    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newline=request.POST.get('newline', 'off')
    extraspaceremover=request.POST.get('extraspaceremove', 'off')
    char_count_w=request.POST.get('charcounter_w', 'off')
    char_count=request.POST.get('charcounter', 'off')
    lower=request.POST.get('fullower', 'off')
    number=request.POST.get('removenum', 'off')
    # check if check box is on

    if removepunc=="on":
        # analyse this text
        punctuations='''!@#$%^&*()_-+={[]}'":;*/<>,.?~`|€\\`~₹'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext=analyzed # updating the djtext

    if number=="on":
        # analyse this text
        numbersall='''1234567890'''
        analyzed= ""
        for char in djtext:
            if char not in numbersall:
                analyzed=analyzed + char
        params={'purpose':'Numbers Remover','analyzed_text':analyzed}
        djtext=analyzed # updating the djtext
    # check if check box is on
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed + str(char).upper()

        params={'purpose':'Change to UPPER CASE','analyzed_text':analyzed}
        djtext=analyzed

    if lower=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed + str(char).lower()
        params={'purpose':'Change to lower case','analyzed_text':analyzed}
        djtext=analyzed
    
    if newline=='on':
        analyzed=""
        for char in  djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed + str(char)
        params={'purpose':'Remove new lines','analyzed_text':analyzed}
        djtext=analyzed

    if extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed + str(char)
        params={'purpose':'Remove new lines','analyzed_text':analyzed}
        djtext=analyzed

    if char_count=="on":
        analyzed=""
        for char in  djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed + str(char)
        djtext=analyzed
        
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index]==" "):
                analyzed=analyzed+str(char)
        djtext=analyzed

        i=0
        for char in djtext:
            i+=1
        analyzed=str(i)
        params={'purpose':'Only Character counter','analyzed_text':analyzed}
        djtext=analyzed
    
        
    if removepunc !="on" and number!="on" and fullcaps != "on" and char_count!="on" and extraspaceremover != "on" and newline != "on" and lower != "on":
        return HttpResponse("Error! please select any operator and try again")   
    
    return render(request,'analyze.html',params)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has Been Sent!')
    return render(request, 'contact.html')



