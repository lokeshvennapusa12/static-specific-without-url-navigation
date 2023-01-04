from django.shortcuts import render

def staticfile(request):
    return render(request,'staticfile.html')
    
