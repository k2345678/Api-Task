from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class Home(ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    def post(self,request):
        start_point = int(request.data["start_point"])
        end_point = int(request.data["end_point"])
        string = request.data["string"]
        if start_point>end_point:
            return Response({"msg":"please check the End Point greater then Start Point"},status=status.HTTP_400_BAD_REQUEST)
        elif start_point<0 and end_point<0:
            return Response({"msg":"It should be greater then 0"},status=status.HTTP_400_BAD_REQUEST)
        elif len(string)<end_point:
            return Response({"msg":"It should be greater then end point"},status=status.HTTP_400_BAD_REQUEST)
        else:
            data = Data.objects.create(
                start_point = start_point,
                end_point = end_point,
                string = string,
                
            )
            serialize = DataSerializer(data)
            return Response({"msg":"Data Created Succesfully!","data":serialize.data},status=status.HTTP_200_OK)
        

        

            
    
    

    

