from rest_framework.response import Response
from rest_framework import viewsets, status

from api.error_utils import error_msg
from api.DRF.User_serializers import UserStatsSerializer, UserStatsSerializerCreateSerializer, UserInfoSerializer, UserInfoCreateSerializer

from .Game_serializers import  UserGameRecordCreateSerializer, UserGameRecordSerializer
from ..models import ER_Stats_Model, ER_User_Info_Model, ER_Game_Record

class UserStatsViewSet(viewsets.ModelViewSet):
	queryset  = ER_Stats_Model.objects.all()
	serializer_class = UserStatsSerializer

	def create(self, request):
		serializer = UserStatsSerializerCreateSerializer(data=request.data)
		if serializer.is_valid():
			rtn = serializer.create(request, serializer.data)
			if rtn:
				return Response(UserStatsSerializer(rtn).data, status=status.HTTP_201_CREATED)
		else :
			return Response(error_msg(1), status=status.HTTP_400_BAD_REQUEST)
	#GET
	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = UserStatsSerializer(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	#detail
	def retrieve(self, request, pk=None):
		queryset = ER_User_Info_Model.objects.filter(nickname=pk).last()
		if queryset:
			serializer = UserInfoSerializer(queryset)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else :
			return Response(error_msg(5), status=status.HTTP_404_NOT_FOUND)

class UserInfoViewSet(viewsets.ModelViewSet):
	queryset = ER_User_Info_Model.objects.filter().order_by("-id")
	serializer_class = UserInfoSerializer

	#POST
	def create(self, request):
		#todo 만약 이미 유저가 존재한다면 업데이트를 진행
		serializer = UserInfoCreateSerializer(data=request.data)
		if serializer.is_valid():
			nickname = serializer.data.get("nickname")
			#리디렉트
			if ER_User_Info_Model.objects.filter(nickname=nickname):
				return(self.retrieve(request, nickname))

			rtn = serializer.create(request, serializer.data)
			if rtn:
				return Response(UserInfoSerializer(rtn).data, status=status.HTTP_201_CREATED)
		else :
			return Response(error_msg(1), status=status.HTTP_400_BAD_REQUEST)

	#GET
	def list(self, request, *args, **kwargs):
		msg = "의미없는 창 입니다"
		return Response({"msg" : msg}, status=status.HTTP_400_BAD_REQUEST)

	#detail
	def retrieve(self, request, pk=None):
		queryset = ER_User_Info_Model.objects.filter(nickname=pk).last()
		if queryset:
			serializer = UserInfoSerializer(queryset)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else :
			return Response(error_msg(5), status=status.HTTP_404_NOT_FOUND)

class UserGameViewSet(viewsets.ModelViewSet):
	queryset = ER_Game_Record.objects.filter().order_by("-id")
	serializer_class = UserGameRecordSerializer

	#? 이건 의미없을듯? 일단 보류하자
	def list(self, request, *args, **kwargs):
		msg = "의미없는 창 입니다"
		return Response({"msg" : msg}, status=status.HTTP_400_BAD_REQUEST)
	
	def retrieve(self,request, pk=None):
		queryset = ER_Game_Record.objects.filter(nickname=pk).order_by("-id")[:20]
		if queryset:
			temp = {}
			for i, data in enumerate(queryset):
				temp[i] = UserGameRecordSerializer(data).data 
			return Response(temp, status=status.HTTP_201_CREATED)
		else :
			return Response(error_msg(5), status=status.HTTP_404_NOT_FOUND)

	#POST
	def create(self, request):
		serializer = UserGameRecordCreateSerializer(data=request.data)
		if serializer.is_valid():
			rtn = serializer.create(request, serializer.data)
			if rtn:
				#여기서 rtn을반복문을 돌면서 UserInfoSerializer(rtn).data 이걸 json으로 만들자
				temp = {}
				for i, data in enumerate(rtn):
					temp[i] = UserGameRecordSerializer(data).data 
				return Response(temp, status=status.HTTP_201_CREATED)
		else :
			return Response(error_msg(1), status=status.HTTP_400_BAD_REQUEST)
