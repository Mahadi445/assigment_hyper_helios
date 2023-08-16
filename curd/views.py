from django.shortcuts import redirect, render, get_object_or_404
from curd.forms import UserInfoForm
from curd.models import user_info

# Create your views here.



def user_information(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')  # Redirect to the same page after successful submission
    else:
        form = UserInfoForm()
    
    return render(request, 'curd/user_information.html', {'form': form})



def contact_list_view(request):
    phn_list = user_info.objects.all() #fetch all data in database
    context = {
        'phn_list': phn_list
    }
    return render(request, 'curd/phonelist.html', context)



def update_contact_view(request, pk):
    phone = get_object_or_404(user_info, pk=pk)
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = UserInfoForm(instance=phone)
    
    return render(request, 'curd/update_phone.html', {'form': form})



def delete_contact_view(request, pk):
    phone = get_object_or_404(user_info, pk=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('contact_list')
    
    return render(request, 'curd/delete_phone.html', {'phone': phone})