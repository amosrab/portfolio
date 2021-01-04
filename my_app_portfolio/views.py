from django.shortcuts import render
# ajouter
from .models import Images
from django.core.mail import EmailMessage  # django email


# Create your views here.

def home(request):
   """" context = {} # ajouter
    image = Images.objects.all() # ajouter
    context["something"] = "Envoyer quelque chose dans le backend." # ajouter
    return render(request, "index.html", context) # ajouter "context"
    """
   context = {}  # ajouter
   images = Images.objects.all()
   context["images"] = images

   # contact form

   if request.method == "post":
      name = request.POST.get("name")
      email = request.POST.get("email")
      subject = request.POST.get("subject")
      message = request.POST.get("message")

      #print(name+ "\n"+ email+ "\n"+ subject+"\n"+ message)

      email_message = EmailMessage(
         subject = name + " : "+subject,
         body = message,
         to = ['amosrab12@gmail.com'],
         header = {"Reply-To": email}
         )
      email_message.send()

   return render(request, "index.html", context)  #ajouter retourner aussi context
