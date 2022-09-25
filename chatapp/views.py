from django.shortcuts import render

def home(request):
    return render(request, 'chatapp/index.html')

def room(request, room_name):
    return render(request, 'chatapp/room.html', {
        'room_name' : room_name
    })

#api
from .models import Conversation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyUser as User
from .serializers import ConversationListSerializer, ConversationSerializer, MyUserSerializer
from django.db.models import Q 
from django.shortcuts import redirect, reverse


@api_view(['POST'])
def start_convo(request):
    data = request.data
    username = data.pop('username')
    try:
        participant = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'message': 'the user you trying to message does not exist'})
    
    conversation = Conversation.objects.filter(Q(initiator=request.user, receipient=participant) | Q(initiator=participant, receipient=request.user))
    
    if conversation.exists():
        return redirect(reverse('get_conversation', args=(conversation[0].id, )))
    else:
        conversation = Conversation.objects.create(initiator=request.user, receipient=participant)
        return Response(ConversationSerializer(instance=conversation).data)

@api_view(['GET'])
def get_conversation(request, convo_id):
    conversation = Conversation.objects.filter(id=convo_id)
    if not conversation.exists():
        return Response({'message': 'Conversation does not exist'})
    else:
        serializer = ConversationSerializer(instance=conversation[0])
        return Response(serializer.data)

@api_view(['GET'])
def conversations(request):
    conversation_list = Conversation.objects.filter(Q(initiator=request.user) | Q(receipient=request.user))
    serializer = ConversationListSerializer(instance=conversation_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_list(request):
    users = User.objects.all().order_by('username')
    serializer = MyUserSerializer(instance=users, many=True)
    return Response(serializer.data)