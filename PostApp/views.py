from django.shortcuts import render
from django.http import HttpResponse

def user_detail(request, id):
   return HttpResponse(f"Информация о пользователе с ID = {id}")

def article_detail(request, id):
   return HttpResponse(f'Вы просматриваете статью с номером {id}')

def user_profile(request, username):
   return HttpResponse(f'Профиль пользователя: {username}')
# def feedback_view(request):
#    result = None
#    if request.method == "POST":
#        name = request.POST.get("name",)
#        message = request.POST.get("message",)
#        result = f"Спасибо, {name}! Мы получили твоё сообщение: {message}"
     

#    return render(request, "form.html", {"result": result})

def main_page(request):
   return render(request, "base.html")

articles = [
   {"id": 1, "title": "Django основы"},
   {"id": 2, "title": "Шаблоны в Django"},
   {"id": 3, "title": "ORM и базы данных"}
]

def article_detail(request, id):
   article = next((a for a in articles if a["id"] == id), None)
   if article:
       return HttpResponse(f"Статья: {article['title']}")
   else:
       return HttpResponse("Статья не найдена")
