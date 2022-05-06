import email
from secrets import choice
from urllib.request import proxy_bypass
import django
from django.shortcuts import render, redirect

from .models import *
from django.core.mail import send_mail
from random import randint
from django.views.decorators.csrf import csrf_exempt
from Member.models import *
from Watchman.models import *

 
# Create your views here.

def home(request):
    return render(request,"Chairman\index.html")

def login(request):
    if "email" in request.session:
        uid = User.objects.get(email= request.session ['email'])
        nall=Notice.objects.all().order_by('created_at').reverse()
        
        if uid.role=='Chairman':
            cid = Chairman.objects.get(user_id = uid)
            mcount=Member.objects.all().count()
            ncount=Notice.objects.all().count()
            ccount=Complain.objects.all().count()
           
            
            return render(request,"Chairman/index.html", {'uid':uid,'cid':cid, 'mcount':mcount , 'ncount':ncount, 'ccount':ccount, 'nall':nall})

        elif uid.role=="Member" or "member":
            mid=Member.objects.get(user_id=uid)
        
            return render(request,"Member/m_index.html", {'uid':uid,'mid':mid})
   
    if request.POST:
        pemail=request.POST['email']
        ppassword=request.POST['password']

    
    #here User is modelname, email is the fieldname and pemail is python variable which contains html input
    #(variable=modelname.objects.get(fieldame,python_variable))
    try:
        uid = User.objects.get(email= pemail)  

        if uid.password== ppassword: 

            if uid.role=="Chairman":
                cid = Chairman.objects.get(user_id = uid)
                request.session['email']=uid.email
                send_mail(" Digital Society","WELCOME TO THE DIGITAL SOCIETY","testerhariom50@gmail.com",[uid.email])
                return render(request,"Chairman\index.html", {'uid':uid, 'cid':cid})

            elif uid.role=="Member" or "member":

                mid=Member.objects.get(user_id=uid)

                if uid.first_time_login==False:
                    email=uid.email
                    otp=randint(1111,9999)
                    uid.otp=otp
                    uid.save()
                    msg= "you otp is "+str(otp)
                    send_mail("Forgot-password",msg,"testerhariom50@gmail.com",[email])
                    return render(request,"Member\m_resetpassword.html",{'email':email})

                else:
                    request.session['email']=uid.email
                    return render (request, "Member/m_index.html",{'uid':uid,'mid':mid})
            else:

                pass
        else:

            e_msg="Invalid password"
            return render(request,"Chairman\login.html",{'e_msg':e_msg})
    except:

        #e_msg= "Email doesn't exist"  
        return render(request,"Chairman\login.html")
                   

    else:
        return render(request, "Chairman\login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        s_msg="Successfully Logged out"
        return render(request,"Chairman\login.html",{'s_msg':s_msg})
        
    else:
        return render(request,"Chairman\login.html")

def c_profile(request):

    if "email" in request.session:
        uid = User.objects.get(email= request.session ['email'] )

        if request.POST:
            currentpassword=request.POST['currentpassword']
            newpassword=request.POST['newpassword']

            if uid.password==currentpassword:
                uid.password=newpassword
                uid.save()    #update
                u_msg="Password updated Successfully"
                return redirect ('c-profile')
                

        else:
            if uid.role=='Chairman':
                cid = Chairman.objects.get(user_id = uid)
                return render(request,"Chairman/c_profile.html",{'uid':uid, 'cid':cid})
    else:
        redirect('login')    




   
def c_dashboard(request):
    return redirect('login')



def forgot_password(request):

    if request.POST:
        email=request.POST['email']
        otp=randint(1111,9999)
        uid=User.objects.filter(email= email).first()
        try:
            if uid:
                uid.otp=otp #store
                uid.save()  #update
                msg= "you otp is "+str(otp)
                send_mail("Forgot-password",msg,"testerhariom50@gmail.com",[email])
                return render(request,"Chairman/resetpassword.html",{'email': email})

        except:
            e_msg="email does not exists"
            return render(request,"Chairman/forgotpassword.html",{'e_sgm':e_msg})
              
    else:

        return render(request,"Chairman/forgotpassword.html")
    
def reset_password(request):
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        newpassword=request.POST['newpassword']
        confirmpassword=request.POST['confirmpassword']

        uid = User.objects.get(email= email) 
        if newpassword==confirmpassword:
            if str(uid.otp)==otp:
                uid.password= newpassword
                uid.is_verified=True
                uid.first_time_login=True
                uid.save()
                return redirect('login')
            else:
                e_msg=" Invalid Otp"
                return render(request,"Chairman/resetpassword.html", {'e_msg':e_msg, 'email': email})
        else:
            e_msg=" Both Password didn't match ! "
            return render(request,"Chairman/resetpassword.html",{'e_msg':e_msg, 'email': email})
    else:
        return render(request,"Chairman/forgotpassword.html")


# def update(request):
#     uid=User.objects.get(email=request.session['email'])
#     cid=Chairman.objects.get(user_id=uid)
#     mid = Member.objects.all()
#     return render(request,"Chairman/all_members.html",{"mid":mid,"cid":cid,"uid":uid})      


@ csrf_exempt
def add_member(request): 
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        l1=['odoo3ro','393ndewd','9402dmedj','32ed2mwd']

        if request.POST:
            email=request.POST['email']
            password=email[:4]+ choice(l1)
            house_no=request.POST['house_no']
            role="member"


            uid=User.objects.create(email=email,password=password, role=role)
            hid=House.objects.get(house_no=house_no)
            print("-------------------->",uid)
            print("hid------------------->",hid)
            hid.status="Active"
            hid.save()
            mid=Member.objects.create(
                    user_id=uid,
                    house_no=hid,

                    firstname=request.POST['firstname'],
                    lastname=request.POST['lastname'],
                    contact=request.POST['contact'],
                    occupation=request.POST['occupation'],
                    birthdate=request.POST['birthdate'],
                    job_address=request.POST['job_address'],
                    no_of_members=request.POST['no_of_members'],
                    marital_status=request.POST['marital_status'],
                    native=request.POST['native'],
                    nationality=request.POST['nationality'],
                    gender=request.POST['gender'],
                    vehicle_type=request.POST['vehicle_type'],
                    no_of_vehicles=request.POST['no_of_vehicles'],
                    id_proof=request.FILES['id_proof'],
                    )
                    
            if mid:
                msg="Your generated Password is "+password
                send_mail("Welcome the the Digital Socity", msg, "testerhariom50@gmail.com",[email])
                m_all= Member.objects.all()
                return render(request,"Chairman/all_members.html",{"m_all":m_all,"cid":cid,"uid":uid})


        else:
            house_all=House.objects.filter(status="pending")
            return render(request,"Chairman/member.html",{'uid':uid, 'cid':cid,'house_all':house_all})
    else:
        return redirect('login')

def all_member(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        mid = Member.objects.all()

        
        if uid.role=='Chairman' or "chairman":
            
           return render(request,"Chairman/all_members.html",{"mid":mid,"uid":uid,"cid":cid}) 

        elif uid.role=="Member" or "member":
            
            return render(request,"Member/m_all_members.html",{"mid":mid,"uid":uid, "cid":cid})  
     
def add_notice(request):
    if request.POST:
        nid=Notice.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            pic=request.FILES['pic'],
            video=request.FILES['videofile'],
            
        )
        return redirect('view-notice')
  
    else:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)

        return render(request,"Chairman/add_notice.html",{'uid':uid,'cid':cid })

def view_notice(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        nall=Notice.objects.all().order_by('created_at').reverse()
        return render(request,"Chairman/noticeview.html",{'uid':uid,'cid':cid,'nall':nall})
   

def watchman(request): 
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        wid=Watchman.objects.all()
        return render(request,"Chairman/watchman.html",{'uid':uid,'cid':cid,'wid':wid})

  
def approved(request,pk):
     if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
       
        user_id=User.objects.get(id=pk)
        user_id.is_verified=True
        user_id.save()
        return redirect('watchman')

def rejected(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
       
        user_id=User.objects.get(id=pk)
        user_id.is_verified=False
        user_id.save()
        return redirect('watchman')



def del_notice(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        nid=Notice.objects.get(id=pk)
        nid.delete()
        # nall=Notice.objects.all().order_by('created_at').reverse()
        # return render(request,"Chairman/noticeview.html",{'uid':uid,'cid':cid,'nall':nall,'nid':nid})


        return redirect('view-notice')

    else:
        return redirect('login')

def m_noticeview_details(request,pk):
      if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)

        nid=Notice.objects.get(id=pk)
        nvid=NoticeView.objects.filter(notice_id=nid)
        nall=NoticeView.objects.all().order_by('created_at').reverse()

        return render(request, 'Chairman/m-noticeview-details.html', {'uid':uid,'cid':cid,'nid':nid,'nvid':nvid,'nall':nall})


def view_complain(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        call=Complain.objects.all().order_by('created_at').reverse()
        # mid=Member.objects.get(user_id=uid)


    return render(request,"Chairman/complainview.html",{'uid':uid,'cid':cid,'call':call})
      
      
def add_event(request):
    if request.POST:
        eid=Event.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            pic=request.FILES['pic'],
            video=request.FILES['videofile'],
            
        )
        return redirect('view-event')
  
    else:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)

        return render(request,"Chairman/add_event.html",{'uid':uid,'cid':cid })

def view_event(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(user_id=uid)
        eall=Event.objects.all().order_by('created_at').reverse()
        return render(request,"Chairman/eventview.html",{'uid':uid,'cid':cid,'eall':eall})

   

