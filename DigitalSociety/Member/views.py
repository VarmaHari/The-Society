import email
from django.shortcuts import render, redirect
from Member.models import *
from Chairman.models import *


#Create your views here.


def m_profile(request):

    if "email" in request.session:
        uid = User.objects.get(email= request.session ['email'] )
        mid=Member.objects.get(user_id=uid)

        if uid.role=='Member' or 'member':
           
            return render(request,"Member/m_profile.html",{'uid':uid, 'mid':mid})
    else:
        redirect('login')

def m_all_members(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Member" or "member":
            mid=Member.objects.filter(user_id=uid)
            m_all=Member.objects.exclude(user_id=uid)
            return render(request,"Member/m_all_members.html",{'uid':uid,'mid':mid,'m_all':m_all})

        else:
            return render(request,"Chairman/index.html")

def m_view_notice(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Member.objects.get(user_id=uid)
        nall=Notice.objects.all().order_by('created_at').reverse()
        return render(request,"Member/m_noticeview.html",{'uid':uid,'mid':mid,'nall':nall})

def m_view_notice_details(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Member.objects.get(user_id=uid)
        nid=Notice.objects.get(id=pk) 

        nall=NoticeView.objects.filter(member_id=mid,notice_id=nid)

        if nall:
            print("Already notice read")
        else:
            print("Read 1st time")
            nvid=NoticeView.objects.create(member_id=mid,notice_id=nid)



        return render(request,"Member/m_noticeview_details.html",{'uid':uid,'mid':mid,'nid':nid})


def add_complain(request):
    if request.POST:
        nid=Complain.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            pic=request.FILES['pic'],
            #video=request.FILES['videofile'],
            
        )
        return redirect('view-complain')
  
    else:
        uid=User.objects.get(email=request.session['email'])
        #cid=Chairman.objects.get(user_id=uid)
        mid=Member.objects.all()

        return render(request,"Member/add_complain.html",{'uid':uid,'mid':mid})

def m_view_complain(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        #cid=Chairman.objects.get(user_id=uid)
        call=Complain.objects.all().order_by('created_at').reverse()
        mid=Member.objects.all()


        return render(request,"Member/mcomplainview.html",{'uid':uid,'mid':mid,'call':call})


def m_add_event(request):
    if request.POST:
        eid=Event.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            pic=request.FILES['pic'],
            video=request.FILES['videofile'],
            
        )
        return redirect('m-view-event')
  
    else:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        mid=Member.objects.all()

        return render(request,"Member/m_add_event.html",{'uid':uid,'cid':cid,'mid':mid })

def m_view_event(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        mid=Member.objects.all()
        eall=Event.objects.all().order_by('created_at').reverse()
        return render(request,"Member/m_eventview.html",{'uid':uid,'cid':cid,'eall':eall,'mid':mid})
