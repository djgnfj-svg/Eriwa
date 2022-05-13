from rest_framework import serializers

from api.models import MasteryModel, MostPickModel, ItemModel, TraitModel

class MasterySerializer(serializers.ModelSerializer):
	class Meta:
		model = MasteryModel
		exclude = ("id", "nickname", "mmr")

class MostpickSerializer(serializers.Serializer):
	most_one_charName = serializers.CharField(max_length=30, read_only=True)
	most_one_charimg = serializers.ImageField(read_only=True)

	most_two_charName = serializers.CharField(max_length=30, read_only=True)
	most_two_charimg = serializers.ImageField(read_only=True)

	most_three_charName = serializers.CharField(max_length=30, read_only=True)
	most_three_charimg = serializers.ImageField(read_only=True)

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemModel
		exclude = ("id","charName")

class TraitSerializer(serializers.ModelSerializer):
	#image 추가하기
	class Meta:
		model = TraitModel
		exclude = ("id",)