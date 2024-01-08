from django.shortcuts import render
from .models import *

def main(request):
    members = list(Member.objects.all().values())
    return render(request, "all-members.html", {"members": members})

def member(request, name):
    member_list = Member.objects.filter(is_main=True)
    member = Member.objects.get(name = name)
    return render(request, "biography.html", {"member": member, "member_list": member_list})