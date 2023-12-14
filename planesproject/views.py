from .models import PlaneModel
from django.http import JsonResponse


def indexPageView(request):
    planes = PlaneModel.objects.all()

    # Serialize the queryset to a list of dictionaries
    serialized_planes = list(planes.values())

    response = JsonResponse({'planes': serialized_planes})

    return response

  