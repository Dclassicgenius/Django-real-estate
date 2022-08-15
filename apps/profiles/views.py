from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import ProfileNotFound, NotYourProfile
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer, UpdateProfileSerializer


class AgentListAPIView(generics.ListAPIView):
    queryset = Profile.objects.filter(is_agent=True)
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = ProfileSerializer

class TopAgentsListAPIView(generics.ListAPIView):
    queryset = Profile.objects.filter(top_agent=True)
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = ProfileSerializer

class GetProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    renderer_classes = [ProfileJSONRenderer,]

    def get(self, request):
      user = self.request.user
      user_profile = Profile.objects.get(user=user)
      serializer = ProfileSerializer(user_profile, context={'request': request})
      return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    renderer_classes = [ProfileJSONRenderer,]
    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound()

        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile()
        
        data = request.data
        serialiser = UpdateProfileSerializer(instance=request.user.profile, data=data, partial=True)
        serialiser.is_valid()
        serialiser.save()
        return Response(serialiser.data, status=status.HTTP_200_OK)
        