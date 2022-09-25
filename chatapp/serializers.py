from .models import MyUser, Conversation, Message
from rest_framework import serializers

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('conversation_id', )

class ConversationListSerializer(serializers.ModelSerializer):
    initiator =  MyUserSerializer()
    receipient = MyUserSerializer()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['initiator', 'receipient', 'last_message']

    def get_last_message(self, instance):
        message = instance.message_set.first()
        return MessageSerializer(instance=message)

class ConversationSerializer(serializers.ModelSerializer):
    initiator =  MyUserSerializer()
    receipient = MyUserSerializer()
    message_set = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['initiator', 'receipient', 'message_set']
        