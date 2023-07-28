from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
# from .models import Profile, UserForm , ProfileForm

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# from django.shortcuts import redirect, render
# from .forms import SignupForm, UserForm, ProfileForm
# from django.contrib.auth import authenticate, login
# from django.contrib.auth import login as auth_login

# from .forms import SignUpForm

# from .models import Profile
# from django.contrib.auth.forms import UserCreationForm
# from .models import Profile, UserForm , ProfileForm

# from django.urls import reverse
# Create your views here.


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('/')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})

# def signup(request):
#     # 1. check if the request method is post (there is data & you want to save it)
#     if request.method=="POST":
#         form = SignupForm(request.POST)
        
#         # 2. check if the data is valid the save it 
#         if form.is_valid():
#             form.save()
            
#             # 3. to update the session i need to get the username & the password data
#             username = form.cleaned_data['username']  # will give me the username
#             password = form.cleaned_data['password1'] # will give me the password 1 or 2 are the same so it doesn't matter which one i chose
            
#             # 4. make sure that the data i took exist
#             user = authenticate(username=username,password=password) #TRUE/FALSE
            
#             # 5. if its correct then i need to login
#             login(request,user)
            
#             # 6. redirect the user to there profile
#             return redirect('/')
    
#     # 7. check if the user didn't put any data yet the render the form
#     else:
#         form = SignupForm()
        
#     # 8. render the html page
#     return render(request,'registration/signup.html',{'form':form})


# '''
# 1. It retrieves the Profile object for the current user by calling the get method on the Profile model's objects attribute and passing it the user field of the request object.
# 2. It renders the profile.html template and passes the Profile object as the profile variable to the template.
# '''


def profile(request):
    profile = Profile.objects.get(user=request.user) #OOP
    return render(request,'accounts/profile.html',{'profile': profile})


# PUT & PATCH
def profile_edit(request):
    # get from the database
    profile = Profile.objects.get(user=request.user)

    # Save the form
    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES,instance=profile ) # request.files to be able to update the image
        
        # check on validation for the 2 forms
        #        T                      T
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False) # i didn't save because i need first to send it to the user 
            myprofile.user = request.user # send data to the user then save
            myprofile.save() 
            
            # redirect to the accounts/profile
            return redirect(reverse('accounts:profile'))
    
    # Show the forms userform & profileform
    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'myaccount.html'
    success_url = reverse_lazy('myaccount')

    def get_object(self):
        return self.request.user