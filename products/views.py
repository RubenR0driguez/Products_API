from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import productserializer
from .models import product

@api_view(['GET'])
def products_list(request):
    
    product = product.objects.all()

    serializer=productserializer(product, many=True)


    return Response(serializer.data)