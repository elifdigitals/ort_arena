from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Contest, ContestExercise, ContestParticipant, ParticipantAnswer, Duel
from .serializers import (
      ContestSerializer,
      ContestExerciseSerializer,
      ContestParticipantSerializer,
      ParticipantAnswerSerializer,
      DuelSerializer
)



User = get_user_model()


      
class ContestViewSet(viewsets.ModelViewSet):
      queryset = Contest.objects.all()
      serializer_class = ContestSerializer


class ContestExerciseViewSet(viewsets.ModelViewSet):
      queryset = ContestExercise.objects.all()
      serializer_class = ContestExerciseSerializer


class ContestParticipantViewSet(viewsets.ModelViewSet):
      queryset = ContestParticipant.objects.all()
      serializer_class = ContestParticipantSerializer


class ParticipantAnswerViewSet(viewsets.ModelViewSet):
      queryset = ParticipantAnswer.objects.all()
      serializer_class = ParticipantAnswerSerializer



class CreateDuelView(generics.CreateAPIView):
      permission_classes = [IsAuthenticated]
      serializer_class = DuelSerializer

      def post(self, request):
            opponent_id = request.data.get('opponent_id')
            opponent = User.objects.filter(id=opponent_id).first()
            if not opponent:
                  return Response({'error': 'Opponent not found'}, status=404)
            if opponent == request.user:
                  return Response({'error': 'You cannot duel yourself'}, status=400)

            duel = Duel.objects.create(challenger=request.user, opponent=opponent)
            return Response(DuelSerializer(duel).data, status=201)


class AcceptDuelView(generics.UpdateAPIView):
      permission_classes = [IsAuthenticated]
      serializer_class = DuelSerializer
      queryset = Duel.objects.all()

      def patch(self, request, pk):
            duel = self.get_object()
            if duel.opponent != request.user:
                  return Response({'error': 'You cannot accept this duel'}, status=403)
            duel.accept()
            return Response(DuelSerializer(duel).data)


class RejectDuelView(generics.UpdateAPIView):
      permission_classes = [IsAuthenticated]
      serializer_class = DuelSerializer
      queryset = Duel.objects.all()

      def patch(self, request, pk):
            duel = self.get_object()
            if duel.opponent != request.user:
                  return Response({'error': 'You cannot reject this duel'}, status=403)
            duel.reject()
            return Response(DuelSerializer(duel).data)


class FinishDuelView(generics.UpdateAPIView):
      permission_classes = [IsAuthenticated]
      serializer_class = DuelSerializer
      queryset = Duel.objects.all()

      def patch(self, request, pk):
            duel = self.get_object()
            if duel.challenger != request.user and duel.opponent != request.user:
                  return Response({'error': 'Not your duel'}, status=403)
            duel.finish()
            return Response(DuelSerializer(duel).data)
