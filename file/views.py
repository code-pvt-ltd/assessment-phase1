from django.shortcuts import render, redirect
from django.template import loader, Context
from django.contrib.auth.models import User,auth


from django.urls import reverse
import sys
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from file.models import PackageOne, Packaget, Packageth, Packagef, schoolatlincharges, teachernominatedforatl, aes, \
    student_login_detail, AI_Questions, table, venreg1, moc


# labregistration page
def Package1(request):
    if request.method == 'POST':
        sel = request.POST.get('sel')
        other = request.POST.get('other')
        scope = request.POST.get('scope')
        days = request.POST.get('days')
        who = request.POST.get('who')
        if sel is not None or sel != "" or other is not None or other != "" or scope is not None or scope != "" or days is not None or days != "" or who is not None or who != "":
            pc1 = PackageOne(Electroniclist=sel, otherofferingsPleasespecify=other, Scopeoftraining=scope,
                             Noofdaysoftraining=days, Whoattendedtraining=who)
            pc1.save()
            # print(other,scope,days,who)
            return HttpResponseRedirect("/Package1")
        return HttpResponse('invalid')
    return render(request, 'regi.html')


def Package2(request):
    if request.method == 'POST':
        cel = request.POST.get('cel')
        other = request.POST.get('other')
        scope = request.POST.get('scope')
        days = request.POST.get('days')
        who = request.POST.get('who')
        if cel is not None or cel != "" or other is not None or other != "" or scope is not None or scope != "" or days is not None or days != "" or who is not None or who != "":
            pc2 = Packaget(Printer=cel, OtherOfferingsPleasespecify=other, Scopeoftraining=scope,
                           Noofdaysoftraining=days, Whoattendedtraining=who)
            pc2.save()
            return HttpResponseRedirect('/Package2')
        return HttpResponse('invalid')
    return render(request, 'package2.html')


def Package3(request):
    if request.method == 'POST':
        selv = request.POST.get('selv')
        other = request.POST.get('other')
        scope = request.POST.get('scope')
        days = request.POST.get('days')
        who = request.POST.get('who')
        if selv is not None or selv != "" or other is not None or other != "" or scope is not None or scope != "" or days is not None or days != "" or who is not None or who != "":
            pc3 = Packageth(Field=selv, Otherofspecify=other, Scopeoftraining=scope, Noofdaysoftraining=days,
                            Whoattendedtraining=who)
            pc3.save()
            return HttpResponseRedirect('/Package3')
        return HttpResponse('invalid')
    return render(request, 'package3.html')


def Package4(request):
    if request.method == 'POST':
        self = request.POST.get('self')
        other = request.POST.get('other')
        scope = request.POST.get('scope')
        days = request.POST.get('days')
        who = request.POST.get('who')
        print(self, other, scope, days, who)
        if self is not None or self != "" or other is not None or other != "" or scope is not None or scope != "" or days is not None or days != "" or who is not None or who != "":
            pc4 = Packagef(Safety=self, OtherOfferingsPleasespecify=other, Scopeoftraining=scope,
                           Noofdaysoftraining=days, Whoattendedtraining=who)
            pc4.save()
            return HttpResponseRedirect('/Package4')

        return HttpResponse('invalid')
    return render(request, 'package4.html')


def userlogin(request):

    if request.method == "POST":
        ValMobilenumber = request.POST.get("Mobilenumber")
        # studentid = request.POST.get("studentid")
        # username = request.POST.get("username")
        Valpassword = request.POST.get("password")
        # username=getattr(object,'username')
        list = student_login_detail.objects.get(Mobilenumber=ValMobilenumber)

        username = list.username
        request.session['username'] = username
        print(username)
        # username = request.session['username']
        print(ValMobilenumber, Valpassword, username)
        try:

            if student_login_detail.objects.filter(Mobilenumber=ValMobilenumber).exists():
                db = student_login_detail.objects.get(Mobilenumber=ValMobilenumber)
                if db.Mobilenumber == ValMobilenumber:
                    if db.Mobilenumber == ValMobilenumber and db.password == Valpassword:
                        return HttpResponseRedirect("/userlogin", {"username": username})
                    return HttpResponse("Invalid Credentials")
            elif student_login_detail.objects.filter(email=ValMobilenumber).exists():
                db = student_login_detail.objects.get(email=ValMobilenumber)
                if db.email == ValMobilenumber and db.password == Valpassword:
                    return HttpResponseRedirect("/userlogin", {"username": username})
                return HttpResponse("Invalid Credentials")
        except Exception as e:
            print(e)
            return HttpResponse("No Value Found")
    return render(request, "index1.html")

def indexpage(request):
    return render(request, "index.html" )

'''def userlogin(request):
    print("in the userlogin")
    return render(request, "userlogin.html" )'''

def schoolreg(request):
    print("in the schoolreg")
    return render(request, "schoolreg.html", )

    def schoolreg(request):
        return render(request, "index2.html")

    def schoolreg(request):
        return render(request, "index3.html")


def atl_login(request):
    return render(request, "schoolreg.html")


def vendorreg(request):
    return render(request, "vendor.html")


def mentorofchange(request):
    return render(request, "mentorofchange.html")


def school_details_atl_incharge(request):
    if request.method == "POST":
        school_name = request.POST.get("school_name")
        school_reg_id = request.POST.get("school_reg_id")
        country = request.POST.get("country")
        state = request.POST.get("state")
        district = request.POST.get("district")
        pincode = request.POST.get("pincode")
        phone = request.POST.get("phone")
        Email = request.POST.get("Email")
        affilation_body = request.POST.get("affilation_body")
        print(school_name, school_reg_id, country, state, district, pincode, phone, Email, affilation_body)
        try:

            ram = school_details_atl_incharge(school_name=school_name, school_reg_id=school_reg_id, country=country,
                                              state=state, district=district, pincode=pincode, phone=phone, Email=Email,
                                              affiliation_body=affilation_body)
            print(school_name, school_reg_id, country, state, district, pincode, phone, Email, affilation_body)
            ram.save()
            return HttpResponseRedirect("/school_details_atl_incharge/")
        except Exception as e:
            print(e)

            return HttpResponse("Error")
    return render(request, "index1.html")


def schoolatlinchargeweb(request):
    if request.method == "POST":
        valpersonname = request.POST.get("personname")
        valpersonID = request.POST.get("personID")
        valmobile = request.POST.get("mobile")
        valemail = request.POST.get("email")
        print(valpersonname, valpersonID, valmobile, valemail)
        try:
            print("Try Sction")
            val = schoolatlincharges(personname=valpersonname, personID=valpersonID, mobile=valmobile, email=valemail)
            val.save()
            return HttpResponseRedirect("/schoolatlinchargeweb/")
        except Exception as e:
            print(e)
            return HttpResponse("invaliduser")
    return render(request, "index2.html")


def AESWeb(request):
    if request.method == "POST":
        option1 = request.POST.get("option1")
        date1 = request.POST.get("date1")
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("email")
        option2 = request.POST.get("option2")
        date2 = request.POST.get("date2")
        option3 = request.POST.get("option3")
        date3 = request.POST.get("date3")
        print(option1, date1, name, number, email, option2, date2, option3, date3)
        try:
            val = aes(option1=option1, date1=date1, name=name, number=number, email=email, option2=option2, date2=date2,
                      option3=option3, date3=date3)
            val.save()
            return HttpResponseRedirect("/AESWeb/")
        except Exception as e:
            return HttpResponse("Invalid......")
    return render(request, "index3.html")


def TNFA(request):
    if request.method == "POST":
        vname = request.POST.get("name")
        vphone = request.POST.get("number")
        vemailid = request.POST.get("email")
        try:
            val = teachernominatedforatl(name=vname, phone=vphone, emailid=vemailid)
            val.save()
            return HttpResponseRedirect("/TNFA/")
        except Exception as e:
            return HttpResponse("invaliduserpass")
    return render(request, "index4.html")


def question(request):
    ques1 = AI_Questions.objects.get(id=1)
    ques2 = AI_Questions.objects.get(id=2)
    ques3 = AI_Questions.objects.get(id=3)
    ques4 = AI_Questions.objects.get(id=4)
    ques5 = AI_Questions.objects.get(id=5)
    context = {
        'obj1': ques1,
        'obj2': ques2,
        'obj3': ques3,
        'obj4': ques4,
        'obj5': ques5,
    }
    return render(request, 'quiz.html', {'context': context})


def data(request):
    record = table.objects.get(id=2)
    content = {
        'object': record
    }
    return render(request, 'Dashboard.html', {'content': content})


def venregweb(request):
    if request.method == "POST":
        GEM = request.POST.get("order")
        GEMordernumber = request.POST.get("gemorderno")
        PurchaseOrderNo = request.POST.get("oredrno")
        Enrollmentforwhichpackage = request.POST.get("package")
        CompanyName = request.POST.get("comname")
        CompanyIncorporationID = request.POST.get("incorporationID")
        Address = request.POST.get("address")
        ContactNumber = request.POST.get("contact")
        EmailID = request.POST.get("email")
        Name = request.POST.get("name")
        ContactNumber1 = request.POST.get("contactno")
        EmailID1 = request.POST.get("email1")
        Doyouwanttoaddmoreteacheardetails = request.POST.get("more")
        print(GEM,GEMordernumber,PurchaseOrderNo,Enrollmentforwhichpackage,CompanyName,CompanyIncorporationID,Address,ContactNumber,EmailID,Name,ContactNumber1,EmailID1,Doyouwanttoaddmoreteacheardetails)
        try:
            val = venreg1(GEM=GEM, GEMordernumber=GEMordernumber, PurchaseOrderNo=PurchaseOrderNo,
                          Enrollmentforwhichpackage=Enrollmentforwhichpackage, CompanyName=CompanyName,
                          CompanyIncorporationID=CompanyIncorporationID, Address=Address, ContactNumber=ContactNumber,
                          EmailID=EmailID, Name=Name, ContactNumber1=ContactNumber1, EmailID1=EmailID1,
                          Doyouwanttoaddmoreteacheardetails=Doyouwanttoaddmoreteacheardetails)
            val.save()

            return HttpResponseRedirect("/schoolreg/")
        except Exception as e:
            return HttpResponse("Invalidreg")
    return render(request, "vendor.html")


def mentorofchangeweb(request):
    if request.method == "POST":
        NameofMentor = request.POST.get("name")
        MentorID = request.POST.get("mentorid")
        WhoAppointed = request.POST.get("who")
        Whichdatehegotappointed = request.POST.get("which")
        EducationBackground = request.POST.get("educational")
        ProfessionalBackground = request.POST.get("professional")
        ContactDetails = request.POST.get("contact")
        Address = request.POST.get("address")
        Whichcompanycurrentlysheheisworking = request.POST.get("company")
        Whichprofilesheheisworking = request.POST.get("profile")
        Howmanydaysdoesshehevisitsschools = request.POST.get("days")
        Specializationandskills = request.POST.get("skills")
        print(NameofMentor, MentorID, WhoAppointed, Whichdatehegotappointed)
        val = moc(NameofMentor=NameofMentor, MentorID=MentorID, WhoAppointed=WhoAppointed,
                  Whichdatehegotappointed=Whichdatehegotappointed, EducationBackground=EducationBackground,
                  ProfessionalBackground=ProfessionalBackground, ContactDetails=ContactDetails, Address=Address,
                  Whichcompanycurrentlysheheisworking=Whichcompanycurrentlysheheisworking,
                  Whichprofilesheheisworking=Whichprofilesheheisworking,
                  Howmanydaysdoesshehevisitsschools=Howmanydaysdoesshehevisitsschools,
                  Specializationandskills=Specializationandskills)
        val.save()
    return render(request, "mentorofchange.html")
