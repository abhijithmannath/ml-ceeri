from .models import RawSession, RaspDataSet
from .serializers import RawSessionSerializer, RaspDataSerializer
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.mixins import UpdateModelMixin

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


# Main Patient Session View
class RawSessionView(UpdateModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, 
	generics.GenericAPIView):
    queryset = RawSession.objects.all()
    serializer_class = RawSessionSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, 
    							BasicAuthentication) #Authentication

    # GET End Point to Retrieve List of all Patient Sessions
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    #POST End Point to UPDATE/CREATE SESSION    
    def post(self, request, *args, **kwargs):
    	if self.get_object():
    		return self.update(request, *args, **kwargs)
    	else:
    		return self.create(request, *args, **kwargs)
    		

    def get_object(self):
    	"""
		Gets invidual Session objects
    	"""
    	args = self.request.data
    	_obj = RawSession.objects.filter(patient_id=args['patient_id'], 
    			session_name=args['session_name']).first()
    	return _obj


class PiDataView(mixins.ListModelMixin, mixins.CreateModelMixin, 
	generics.GenericAPIView):
    queryset = RaspDataSet.objects.all()
    serializer_class = RaspDataSerializer
    authentication_classes = (BasicAuthentication)


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		for x in request.data['data']:
			RaspDataSet.objects.create(**x)
		return Response(1)

    		

