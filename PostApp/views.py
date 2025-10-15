from django.shortcuts import render

# Create your views here.

def feedback_view(request):
   result = None
   if request.method == "POST":
       name = request.POST.get("name",)
       message = request.POST.get("message",)
       result = f"Спасибо, {name}! Мы получили твоё сообщение: {message}"
     

   return render(request, "form.html", {"result": result})