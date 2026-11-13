
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Note

def home_view(request):
    return render(request,'codehere/home.html')


def signup_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:

            return render(request, 'codehere/signup.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(username=username).exists():

            return render(request, 'codehere/signup.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'codehere/signup.html')


def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')


        user=authenticate(request,username=username,password=password)

        if user is not None:
         login(request,user)
         return redirect('dashboard')

        else:
         return render(request,'codehere/login.html',{
            'error':"invalid username or password"
         })

    return render(request,'codehere/login.html')



@login_required
def dashboard_view(request):

    notes = Note.objects.filter(user=request.user)

    return render(
        request,
        'codehere/dashboard.html',
        {'notes': notes}
    )



def logout_view(request):
   logout(request)
   return redirect('home')





@login_required
def create_note_view(request):

    if request.method == 'POST':

        title = request.POST.get('title')

        content = request.POST.get('content')

        Note.objects.create(
            user=request.user,
            title=title,
            content=content
        )

        return redirect('dashboard')

    return render(request, 'codehere/create_note.html')


@login_required
def update_note_view(request, note_id):

    note = get_object_or_404(
        Note,
        id=note_id,
        user=request.user
    )

    if request.method == 'POST':

        note.title = request.POST.get('title')

        note.content = request.POST.get('content')

        note.save()

        return redirect('dashboard')

    return render(
        request,
        'codehere/update_note.html',
        {'note': note}
    )



@login_required
def delete_note_view(request, note_id):

    note = get_object_or_404(
        Note,
        id=note_id,
        user=request.user
    )

    if request.method == 'POST':

        note.delete()

        return redirect('dashboard')

    return redirect('dashboard')
