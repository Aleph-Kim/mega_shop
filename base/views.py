from django.shortcuts import render


def basePage(request):
    return render(request, 'base.html')