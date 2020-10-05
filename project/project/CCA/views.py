from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Questionaries,User_Marks,Field


def index(request):
    return render(request,'CCA/index.html')

def test(request,field_id):
    english = Questionaries.objects.filter(field_id=field_id)
    print("field_id",field_id)
    e_0=english[0]
    e_1=english[1]
    e_2=english[2]
    e_3=english[3]
    e_4=english[4]
    en_0 = Questionaries.objects.filter(questions=e_0)
    en_1 = Questionaries.objects.filter(questions=e_1)
    en_2 = Questionaries.objects.filter(questions=e_2)
    en_3 = Questionaries.objects.filter(questions=e_3)
    en_4 = Questionaries.objects.filter(questions=e_4)

    param = {'english': english,'en_0':en_0,'en_1':en_1,'en_2':en_2,'en_3':en_3,'en_4':en_4,'e_0':e_0,
    'field_id':field_id}
    return render(request,'CCA/test.html',param)



 

    
def english(request,field_id,template_name='CCA/computer.html'):
    q2=[]
    for i in range(1,6):
        q1=request.POST.get('op_'+str(i))
        q2.append(q1)
    print("q2",q2)
    user_ans = [i for i in q2 if i]
    print("user_ans",user_ans)
    english = Questionaries.objects.filter(field_id=field_id)
    print("eeeee",english)
   
    e_0=english[0]
    e_1=english[1]
    e_2=english[2]
    e_3=english[3]
    e_4=english[4]
    en_0 = Questionaries.objects.filter(questions=e_0)
    en_1 = Questionaries.objects.filter(questions=e_1)
    en_2 = Questionaries.objects.filter(questions=e_2)
    en_3 = Questionaries.objects.filter(questions=e_3)
    en_4 = Questionaries.objects.filter(questions=e_4)
    
    marks=[]
    crct_ans=[]
    for i in [e_0,e_1,e_2,e_3,e_4]:
        crct_ans.append(i.answer)
        marks.append(i.diff_id.marks)
    print("marks",marks)
    print("crct_ans",crct_ans)

    

    
    

    total=0
    for i in range(0,5):
        if user_ans[i]==crct_ans[i]:
            total=total+marks[i]
        else:
            total=total+0

    print("total",total)

    user = request.user
    userid = user.id
    print("user",user)
    #print("field",field_id)
    a_field=Field.objects.get(ID1=field_id)
    
    x=a_field.subject



    try:
        add= User_Marks.objects.get(users=userid)
        add.x=total
        add.save()
    except:
        add=User_Marks()
        add.users=user
        add.x=total
        add.save()
    print("add",add)
    
    param = {'english': english,'q2':q2,'total':total,'field_id':field_id}
    return render(request,template_name,param)






class UserFromView(View):
    form_class = UserForm #forms.py
    template_name = 'CCA/registration_form.html'

    #display blank form
    def get(self ,request):
        form = self.form_class(None) #none means by default it has no data
        return render(request,self.template_name,{'form':form})

    #process form data into database(add info into database)
    def post(self,request):
        #request.post , the information that they type in the forms
        form = self.form_class(request.POST)
        if form.is_valid():
            #create the objects for the form but doesnot save it to database
            user = form.save(commit=False)

            #clean normalized data (same format i/p)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #to change user password
            user.set_password(password)
            #save all in database
            user.save()
            
            
            #user is now registered for the website


            #authenticate and login the user and returns user objectsif credentials are correct
            user = authenticate(username=username,password=password)
            #user returns name either bucky etc

            if user is not None:
               if user.is_active:
                   login(request,user)
                    #after login return to homepage
                   return redirect('CCA:index')


        #if not login correctly then return to the blank form
        return render(request, self.template_name, {'form': form})

def result(request):
    return render(request,'CCA/result.html')


def home(request):
    return render(request,'CCA/home.html')
    
