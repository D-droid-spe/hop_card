from django.shortcuts import render,redirect,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Malade, Doctor
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def About(requeste):
    return render(requeste,'about.html')
def Home(requeste):
    return render(requeste,'home.html')
def contact(requeste):
    return render(requeste,'contact.html')
def index(request):
    if not request.user.is_stafe:
        return redirect('login')
    return render(request,'index.html')
def Login(request):
    error= ""
    if request.method=="POST":
        u= request.POST['uname']
        p=request.POST['pwd']
        user= authenticate(username=u,password=p)
        try:
           if user.is_staff:
              login(request,user)
              error = "no"
           else:
               error = "yes"
        except:
            error = "yes"
    d={'error': error}
    return render(request,"login.html",d)
def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')
                          
def patient_illness_info(request):
    if request.method == 'GET':
        numero_identite = request.GET.get('numero_identite')
        malade = Malade.objects.filter(numero_identite=numero_identite).first()
        if malade:
            return render(request, 'doctoredetail.html', {'patient_illness': malade})
        else:
            error_message = "Malade with the given identification number does not exist."
            return render(request, 'doctoredetail.html', {'error_message': error_message})
    return render(request, 'doctoredetail.html')

def add_doctor_info(request):
    if request.method == 'POST':
        # Récupérez les données du formulaire
        malade_id = request.POST.get('numero_identite')
        remarks = request.POST.get('remarks')

        # Créez ou récupérez le Malade approprié en fonction de l'ID du médecin
        malade = Malade.objects.get( numero_identite= malade_id)

        # Enregistrez les remarques dans le champ description du modèle Malade
        malade.effets_maladie = remarks
        malade.save()

        # Redirigez l'utilisateur vers une page de confirmation ou une autre page appropriée
        return redirect('doctors_form')
    else:
        # Si la méthode de la requête n'est pas POST, affichez simplement le formulaire
        return render(request, 'doctors_form.html')


    

