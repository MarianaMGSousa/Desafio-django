from django.shortcuts import render,redirect
from .models import Livro
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    livros = Livro.objects.all() #pega tudo o que foi cadastrado no nosso model
    return render(request, 'home.html', {'livro': livros}) #nessas {} que envia para o template

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username') #usar sempre as mesmas variáveis do arquivo html
        email = request.POST.get('email')
        senha = request.POST.get('senha')
                    
        user = User.objects.filter(username=username).first() #estamos verificando se já existe um username igual ao digitado para evitar duplicidade
        
        if user:
            return HttpResponse('Já existe esse usuário')
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return redirect('/biblioteca_virtual/')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
            
        user = authenticate(username=username,password=senha)
        if(user):
            login_django(request, user)
            return redirect('/biblioteca_virtual/') 
        else:
            return HttpResponse('Usuário ou senha inválidos')
        
def logout_login(request): 
    logout(request)
    return redirect('login') 
 
 
def cadastro_livros(request):
    if request.method == "GET":
        return render(request, 'cadastro_livros.html')
    else:
        titulo = request.POST.get('titulo') #usar sempre as mesmas variáveis do arquivo html
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        data_cadastro = request.POST.get('data_cadastro')
                    
        livro = Livro.objects.filter(titulo=titulo).first() #estamos verificando se já existe um titulo igual ao digitado para evitar duplicidade
        
        if livro:
            return HttpResponse('Já existe este livro cadastrado')
        livro = Livro.objects.create(titulo=titulo, autor=autor, editora=editora, data_cadastro=data_cadastro)
        livro.save()
        return redirect('/biblioteca_virtual/')
 
        
def plataforma(request):
    if request.user.is_authenticated:
        return HttpResponse('Plataforma') #Só vai puder acessar quem estiver logado
    return HttpResponse('Você precisa estar logado')

 
