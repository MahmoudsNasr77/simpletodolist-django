from django.shortcuts import render,redirect
from .models import list
from django.urls import reverse
from .forms import post
import datetime
def todo_list(request):
    list_view=list.objects.all()
    current_datetime = datetime.datetime.now() 
    if request.method=='POST':
        form=post(request.POST)
        if form.is_valid():
          form.save()
          return redirect(request.META['HTTP_REFERER'])
    else:
      form=post()
    context={'list_view':list_view,'form':form,'current_datetime':current_datetime}
    return render(request,'list.html',context)
def delete(request, id):
  member = list.objects.get(id=id)
  member.delete()
  return redirect(request.META['HTTP_REFERER'])


'''
def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
         userform=EditUserForm(request.POST,request.FILES,instance=request.user)
         profileform=EditProfileForm(request.POST,request.FILES,instance=profile)
         if userform.is_valid and profileform :
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            userform.save()
            return redirect(reverse('accounts:profile'))
            
    else:
         userform=EditUserForm(instance=request.user)
         profileform=EditProfileForm(instance=profile)
    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})
'''
