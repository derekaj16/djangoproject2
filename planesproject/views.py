from .models import PlaneModel
from django.http import JsonResponse
from django.shortcuts import render


def indexPageView(request):
    planes = PlaneModel.objects.all()

    # Serialize the queryset to a list of dictionaries
    serialized_planes = list(planes.values())
    response = JsonResponse({'planes': serialized_planes})

    context = {
        'planes': planes
    }

    return render(request, 'planes_website/index.html', context)

  