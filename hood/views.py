from django.shortcuts import render,redirect
from .models import Post,Profile,Neighborhood,Business,Join
from django.http import HttpResponse
from django.contrib import messages
from .forms import NewPostForm,UserForm,CreateHoodForm,ProfileForm,BusinessForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    hoods = Neighborhood.objects.all()
    businesses = Business.objects.all()
    posts = Post.objects.all()
    return render(request,'index.html',{"businesses":businesses,"posts":posts})

@login_required(login_url='/accounts/login/')
def profile(request,user_id=None):
    if user_id == None:
        user_id=request.user.id
    current_user = User.objects.get(id = user_id)
    user = current_user
    images = Post.objects.filter(user=current_user)
    profile = Profile.objects.all()
    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login')
def updateprofile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
			form = ProfileForm()
	return render(request, 'updateprofile.html',{"form":form })


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form":form})


@login_required(login_url='/accounts/login/')
def createHood(request):
    if request.method == 'POST':
        form = CreateHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = request.user
            hood.save()

        return redirect('index')
    else:
        form = CreateHoodForm()
        return render(request, 'new_hood.html', {"form": form})

def search(request):

    if 'business' in request.GET and request.GET['business']:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_business_name(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message, "businesses":searched_businesses})

    else:
        message = "You Haven't searched for any item"
        return render(request,'search.html',{"message":message })

@login_required(login_url = '/accounts/login')
def all_hoods(request):

    if request.user.is_authenticated:
        if Join.objects.filter(user_id=request.user).exists():
            hood = Neighborhood.objects.get(pk=request.user.join.hood_id.id)
            businesses = Business.objects.filter(hood=request.user.join.hood_id.id)
            posts = Post.objects.filter(hood=request.user.join.hood_id.id)
            print(posts)
            return render(request, "hood.html", locals())
        else:
            neighbourhoods = Neighborhood.objects.all()
            return render(request, 'hood.html', locals())
    else:
        neighbourhoods = Neighborhood.objects.all()

        return render(request, 'hood.html', locals())

def create_business(request):
    current_user = request.user
    print(Profile.objects.all())
    owner = Profile.objects.get(user = current_user)
    # this_hood = Neighborhood.objects.all()
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            new_biz=form.save(commit=False)
            new_biz.user = current_user
            # new_biz.hood =this_hood
            new_biz.save()
            return redirect('home')
    else:
        form = BusinessForm()
    return render(request,"businessform.html",locals())

@login_required(login_url='/accounts/login/')
def join(request, hoodId):
    neighbourhood = Neighborhood.objects.get(pk=hoodId)
    if Join.objects.filter(user_id=request.user).exists():

        Join.objects.filter(user_id=request.user).update(hood_id=neighbourhood)
    else:

        Join(user_id=request.user, hood_id=neighbourhood).save()

    messages.success(request, 'Success! You have succesfully joined this Neighborhood ')
    return redirect('hoods')
