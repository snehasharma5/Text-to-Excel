from django.shortcuts import render, redirect
from .models import FileData
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.core import serializers


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('file_view', {'username':username})
        else:
            messages.error(request, 'Wrong USER or PASSWORD')
    else:
        return render(request, 'excel/home.html')
    return render(request, 'excel/home.html')


def file_view(request, username):
    show_data = FileData.objects.all()[0:5]

    if request.method == "POST":
        get_id = request.POST.get("del")
        object_data = FileData.objects.filter(id=get_id)

        if object_data is None:
            return render(request, 'excel/file_view.html', {"show_data": show_data})
        else:
            object_data.delete()
            return render(request, 'excel/file_view.html', {"show_data": show_data})
    if request.is_ajax():
        html = render_to_string(
            template_name='excel/file_view.html',
            context={"show_data": show_data}
        )
        data_dict = {"html_form_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'excel/file_view.html', {"show_data": show_data})


def update(request):
    if request.method == "POST":
        val = FileData.objects.get()
        val.first_name = request.POST['fname']
        val.save()
        message = 'update Successful'
    return HttpResponse(message)


def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out..')
    return redirect('login')


def likePost(request):
    show_data = FileData.objects.all()[0:5]
    # print(list(show_data))
    data1=[]
    for d in show_data:
        data = {}
        data["email_id"] = d.email_id
        data["first_name"] = d.first_name
        data["last_name"] = d.last_name
        data["gender"] = d.gender
        data["address"] = d.address
        data["city"] = d.city
        data["state"] = d.state
        data["ZIP"] = d.ZIP
        data["mobile"]=d.mobile
        data["date_of_birth"]=d.date_of_birth
        data["pk"]=d.pk
        
        data1.append(data)
    # data = serializers.serialize('json', show_data)
    return JsonResponse(data1, safe=False)


def search_item(request):
    q=request.GET.get('q')
    object_data = FileData.objects.filter(state__icontains=q)[0:5]
    data1=[]
    for d in object_data:
        data={}
        data["email_id"] = d.email_id
        data["first_name"] = d.first_name
        data["last_name"] = d.last_name
        data["gender"] = d.gender
        data["address"] = d.address
        data["city"] = d.city
        data["state"] = d.state
        data["ZIP"] = d.ZIP
        data["mobile"]=d.mobile
        data["date_of_birth"]=d.date_of_birth
        data["pk"]=d.pk
        
        data1.append(data)
    return JsonResponse(data1, safe=False)
