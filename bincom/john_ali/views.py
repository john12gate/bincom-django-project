# from django.shortcuts import render
#
# # Create your views here.
#
# from .models import BincomModel
#
# def display_result(request):
#     blog_posts = BlogPost.objects.all()
#     return render(request, 'result/display_result.html', {'display_result': display_result})



# from django.shortcuts import render
# from .models import BincomModel
# # from . import views
# #from john_ali import views
# from john_ali.views import display_result
#
# def display_result(request):
#     bincom_models = BincomModel.objects.all()
#     return render(request, 'result/display_result.html', {'bincom_models': bincom_models})



#
# from django.shortcuts import render
# from .models import BincomModel
#
# def display_result(request):
#     bincom_models = BincomModel.objects.all()
#     return render(request, 'display_result.html', {'bincom_models': bincom_models})





# from django.shortcuts import render
# from .models import PollingUnit
#
# def display_result(request):
#     bincom_models = PollingUnit.objects.all()
#     return render(request, 'display_polling_unit.html', {'bincom_models': bincom_models})




# from django.shortcuts import render, get_object_or_404
# from .models import PollingUnit
#
# def display_polling_unit(request, polling_unit_id):
#     polling_unit = get_object_or_404(PollingUnit, polling_unit_id=polling_unit_id)
#     return render(request, 'display_polling_unit.html', {'polling_unit': polling_unit})
#
# def display_result(request):
#     bincom_models = PollingUnit.objects.all()
#     return render(request, 'display_result.html', {'bincom_models': bincom_models})



#     from django.shortcuts import render
#     from .models import PollingUnit
#
#     def polling_unit_list(request):
#         polling_units = PollingUnit.objects.all()  # Retrieve all polling units
#
#         context = {
#             'polling_units': polling_units
#         }
#
#         return render(request, 'polling_unit_list.html', context)



# from django.shortcuts import render, get_object_or_404
# from .models import PollingUnit
#
# def polling_unit_list(request):
#     polling_units = PollingUnit.objects.all()  # Retrieve all polling units
#
#     context = {
#         'polling_units': polling_units
#     }
#
#     return render(request, 'polling_unit_list.html', context)
#
#
# def polling_unit_detail(request, polling_unit_id):
#     polling_unit = get_object_or_404(PollingUnit, id=polling_unit_id)  # Retrieve the specific polling unit
#
#     context = {
#         'polling_unit': polling_unit
#     }
#
#     return render(request, 'polling_unit_detail.html', context)
#



# from django.shortcuts import render, get_object_or_404
# from .models import PollingUnit
#
# def polling_unit_detail(request, uniqueid):
#     polling_unit = get_object_or_404(PollingUnit, uniqueid=uniqueid)  # Retrieve the specific polling unit
#
#     context = {
#         'polling_unit': polling_unit
#     }
#
#     return render(request, 'polling_unit_detail.html', context)
#
#
# def polling_unit_list(request):
# #     polling_units = PollingUnit.objects.all()  # Retrieve all polling units
#
#     polling_units = get_object_or_404(PollingUnit, uniqueid=uniqueid)  # Retrieve the specific polling unit
#
#     context = {
#         'polling_units': polling_units
#     }
#
#     return render(request, 'polling_unit_list.html', context)
#
#
#
#





from django.shortcuts import render, get_object_or_404
from .models import PollingUnit

def polling_unit_list(request):
    polling_units = PollingUnit.objects.all()

    context = {
        'polling_units': polling_units
    }

    return render(request, 'polling_unit_list.html', context)


def polling_unit_detail(request, uniqueid):
    polling_unit = get_object_or_404(PollingUnit, uniqueid=uniqueid)

    context = {
        'polling_unit': polling_unit
    }

    return render(request, 'polling_unit_detail.html', context)


# def local_government_results(request):
#     local_governments = PollingUnit.objects.values('lga_id').distinct()
#
#     context = {
#         'local_governments': local_governments
#     }
#
#     return render(request, 'local_government_results.html', context)


def local_government_results(request):
    local_governments = PollingUnit.objects.values('lga_id').distinct()

    selected_lga = request.GET.get('lga_id')
    total_results = None

    if selected_lga:
        total_results = PollingUnit.objects.filter(lga_id=selected_lga).aggregate(
            total_field1=Sum('field1'),
            total_field2=Sum('field2'),
            # Add more fields for aggregation
        )

    context = {
        'local_governments': local_governments,
        'selected_lga': selected_lga,
        'total_results': total_results,
    }

    return render(request, 'local_government_results.html', context)



def save_polling_unit(request):
    if request.method == 'POST':
        # Retrieve the form data from the POST request
        polling_unit_id = request.POST.get('polling_unit_id')
        ward_id = request.POST.get('ward_id')
        lga_id = request.POST.get('lga_id')
        uniquewardid = request.POST.get('uniquewardid')
        polling_unit_number = request.POST.get('polling_unit_number')
        polling_unit_name = request.POST.get('polling_unit_name')
        polling_unit_description = request.POST.get('polling_unit_description')
        lat = request.POST.get('lat')
        long = request.POST.get('long')
        entered_by_user = request.POST.get('entered_by_user')
        date_entered = request.POST.get('date_entered')
        user_ip_address = request.POST.get('user_ip_address')

        # Create a new PollingUnit instance and save it to the database
        polling_unit = PollingUnit(
            polling_unit_id=polling_unit_id,
            ward_id=ward_id,
            lga_id=lga_id,
            uniquewardid=uniquewardid,
            polling_unit_number=polling_unit_number,
            polling_unit_name=polling_unit_name,
            polling_unit_description=polling_unit_description,
            lat=lat,
            long=long,
            entered_by_user=entered_by_user,
            date_entered=date_entered,
            user_ip_address=user_ip_address
        )
        polling_unit.save()

        # Redirect to a success page or display a success message
        return render(request, 'success.html')

    # If the request method is GET, render the form
    return render(request, 'form.html')
