from django.shortcuts import render


def goods(request):
    return render(request, "html/goods.html")


def contacts(request):
    return render(request, "html/contacts.html")
