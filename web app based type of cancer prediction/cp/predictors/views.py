from django.shortcuts import render
from django.http import HttpResponse
from . form import fm
import pickle




knn = pickle.load(open('./savedModel/knn.sav','rb'))

# Create your views here.


def cp(request):

    if request.method == 'POST':
        f = fm(request.POST)  

        Age = int(request.POST['Age'])
        Gender = int(request.POST['Gender'])
        Genetic_Risk = int(request.POST['Genetic_Risk'])
        Smoking = int(request.POST['Smoking'])
        Chest_Pain = int(request.POST['Chest_Pain'])
   
        Coughing_of_Blood = int(request.POST['Coughing_of_Blood'])
        Dry_Cough = int(request.POST['Dry_Cough'])
        
        y_pred = knn.predict([[Age,Gender,Genetic_Risk,Smoking,Chest_Pain,Coughing_of_Blood,Dry_Cough]])

        if y_pred == 0:
            y_pred = 'LOW'
        elif y_pred == 1:
            y_pred = 'MEDIUM'
        else:
            y_pred = 'HIGH'
        return render(request, 'cp.html',{'fm':fm,'result':y_pred})
    else:
        f = fm()
        

    return render(request, 'cp.html',{'fm':fm})
    