from django.db import models


class school_details_atl_incharge(models.Model):
    school_name = models.CharField(max_length=200, blank=True)
    school_reg_id = models.IntegerField(primary_key=True)
    # Address = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    pincode = models.IntegerField()
    phone = models.CharField(max_length=10, blank=True)
    Email = models.EmailField(default="")
    affiliation_body = models.CharField(max_length=100)
    def __str__(self):
        return str(self.school_name)
# Create your models here.
class ATLEstablishmentStatus(models.Model):
    Radio1=models.CharField(max_length=50)
    WhichDate=models.DateField()
    Name=models.CharField(max_length=70)
    ContactNumber=models.IntegerField(unique=True)
    EmailID=models.EmailField(max_length=300)
    Radio2=models.CharField(max_length=50)
    WhichDate1=models.DateField()
    Radio3=models.CharField(max_length=50)
    WhichDate2=models.DateField()
    Date=models.DateField()
    def __str__(self):
        return str(self.WhichDate)



class PackageOne(models.Model):
    Electroniclist=models.CharField(max_length=40)
    otherofferingsPleasespecify=models.CharField(max_length=200)
    Scopeoftraining=models.CharField(max_length=400)
    Noofdaysoftraining=models.IntegerField(unique=True)
    Whoattendedtraining=models.CharField(max_length=80)
    def __str__(self):
        return str(self.Whoattendedtraining)


class Packaget(models.Model):
    Printer=models.CharField(max_length=50)
    OtherOfferingsPleasespecify=models.CharField(max_length=80)
    Scopeoftraining=models.CharField(max_length=70)
    Noofdaysoftraining=models.IntegerField(unique=True)
    Whoattendedtraining=models.CharField(max_length=80)

    def __str__(self):
        return str(self.Scopeoftraining)


class Packageth(models.Model):
    Field = models.CharField(max_length=50)
    Otherofspecify = models.CharField(max_length=80)
    Scopeoftraining=models.CharField(max_length=70)
    Noofdaysoftraining=models.IntegerField(unique=True)
    Whoattendedtraining=models.CharField(max_length=80)
    def __str__(self):
        return str(self.Noofdaysoftraining)


class Packagef(models.Model):
    Safety= models.CharField(max_length=50)
    OtherOfferingsPleasespecify=models.CharField(max_length=80)
    Scopeoftraining=models.CharField(max_length=70)
    Noofdaysoftraining=models.IntegerField(unique=True)
    Whoattendedtraining=models.CharField(max_length=80)

    def __str__(self):
        return str(self.Whoattendedtraining)
        
"""class SchoolInfo(models.Model):
    NameOfSchool = models.CharField(max_length=200, blank = False, null = False)
    RegistrationSchoolId = models.IntegerField(default="",primary_key=True)
    #Address = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100,  blank=True)
    state = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    Pincode = models.IntegerField()
    Phone = models.CharField(max_length=10, blank=True)
    Email = models.EmailField(default="")
    AffiliationBody = models.CharField(max_length=100)
    def __str__(self):
        return str(self.RegistrationSchoolId)"""
        
class schoolatlincharges(models.Model):
    personname = models.CharField(max_length=200)
    personID = models.IntegerField(primary_key=True)
    mobile = models.IntegerField()
    email = models.CharField(max_length=100)
    def __str__(self):
        return str(self.personname)

class aes(models.Model):
    option1 = models.CharField(max_length=20)
    date1 = models.CharField(max_length=100)
    name = models.CharField(max_length=100,primary_key=True)
    number = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    option2=models.CharField(max_length=10)
    date2 = models.CharField(max_length=100)
    option3=models.CharField(max_length=10)
    date3 = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)  

class teachernominatedforatl(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    phone = models.IntegerField()
    emailid = models.EmailField(max_length=254)
    
    def __str__(self):
        return (self.name)
        
class student_login_detail(models.Model):

    Mobilenumber = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=230)
    username=models.CharField(max_length=100)


    def __str__(self):
        return str(self.Mobilenumber)

        
class Atl_login_detail(models.Model):
    Mobilenumber = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=230)
    def __str__(self):
        return str(self.Mobilenumber)
        
class Questions(models.Model):
    order = models.IntegerField(default=0)
    question = models.CharField(max_length=200, null=False)
    option1 = models.CharField(max_length=60, null=False)
    option2 = models.CharField(max_length=60, null=False)
    option3 = models.CharField(max_length=60, null=False)
    option4 = models.CharField(max_length=60, null=False)

class AI_Questions(models.Model):
    order = models.IntegerField(default=0)
    question = models.CharField(max_length=200, null=False)
    option1 = models.CharField(max_length=60, null=False)
    option2 = models.CharField(max_length=60, null=False)
    option3 = models.CharField(max_length=60, null=False)
    option4 = models.CharField(max_length=60, null=False)
    answer = models.CharField(max_length=100, null=True)
 

class Answer(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=True)

class Tracker(models.Model):

    correct_answers = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    not_attempted = models.BooleanField(default=True)

class Response(models.Model):
    tracker = models.ForeignKey(Tracker,on_delete=models.CASCADE)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE,null=True,blank=True)

class venreg1(models.Model):
    GEM = models.CharField(max_length=100)
    GEMordernumber = models.IntegerField()
    PurchaseOrderNo = models.IntegerField()
    Enrollmentforwhichpackage = models.CharField(max_length=100)
    CompanyName = models.CharField(max_length=100)
    CompanyIncorporationID = models.IntegerField()
    Address = models.CharField(max_length=500)
    ContactNumber = models.IntegerField()
    EmailID = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    ContactNumber1 = models.IntegerField()
    EmailID1 = models.CharField(max_length=100)
    Doyouwanttoaddmoreteacheardetails = models.CharField(max_length=100)
    def __str__(self):
        return str(self.CompanyName)
        
        
class moc(models.Model):
    NameofMentor = models.CharField(max_length=100)
    MentorID = models.IntegerField()
    WhoAppointed = models.CharField(max_length=100)
    Whichdatehegotappointed = models.CharField(max_length=100)
    EducationBackground = models.CharField(max_length=100)
    ProfessionalBackground = models.CharField(max_length=100)
    ContactDetails = models.IntegerField()
    Address = models.CharField(max_length=500)
    Whichcompanycurrentlysheheisworking = models.CharField(max_length=500)
    Whichprofilesheheisworking = models.CharField(max_length=500)
    Howmanydaysdoesshehevisitsschools = models.CharField(max_length=300)
    Specializationandskills = models.CharField(max_length=500)
    def __str__(self):
        return str(self.NameofMentor)

class table(models.Model):
    school_name = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=True)
    student_name = models.CharField(max_length=20, null=True)
    roll_number = models.IntegerField() 
    class_section = models.CharField(max_length=20, null=True)
    grade = models.CharField(max_length=10, null=True)
    date = models.CharField(max_length=10, null=True)
        



class Profile(models.Model):
    GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)








