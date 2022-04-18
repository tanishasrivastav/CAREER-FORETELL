from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Blog
from .models import Contact

# ML
import pandas as pd
from sklearn.preprocessing import LabelEncoder  
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split  

# Create your views here.

def home(request):
    if(request.method == 'POST'):

        name = request.POST['name']
        age = request.POST['age']

        school = request.POST['school']
        email = request.POST['email']

        ten = int(request.POST['marks10'])
        twelve = int(request.POST['marks12'])
        enterance = int(request.POST['marksent'])
        intrest = request.POST['intrest']

        inp = [ten, twelve, enterance, intrest]

        fs = FileSystemStorage()
        data = fs.open('final_dataset.csv')

        dataset=pd.read_csv(data)
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1].values

        label_encoder_x= LabelEncoder()  
        X[:, 3]= label_encoder_x.fit_transform(X[:, 3])  

        inp[3:4]= label_encoder_x.transform(inp[3:4])
        inp=[inp]

        X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.1, random_state=0)  

        reg = LogisticRegression(random_state = 0)
        reg.fit(X_train, y_train)

        output=reg.predict(inp)[0]

        return render(request, 'output.html', {"output":output, "name":name, "age":age, "ten":ten, "twelve":twelve, "entrance":enterance, "interest":intrest})
        
    return render(request, 'home.html')

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs':blogs})

def blog(request, slug):
    blog = Blog.objects.get(blogID=slug)
    return render(request, 'blog.html', {'blog':blog})

def about(request):
    if(request.method=='POST'):
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        subject = request.POST['subject']
        message = request.POST['message']
        
        Contact.objects.create(name=name, email=email, contact=contact, subject=subject, message=message)
        return render(request, 'about.html', {"message": "Message sent successfully."})

    return render(request, 'about.html')
