from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from .automata_logic import DFA, NFA, NFA_epsilon, RG
from .serializers import DFASerializer, NFASerializer, NFAEpsilonSerializer, RGSerializer

class RunDFA(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DFASerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            dfa = DFA(
                data['states'], data['alphabet'], data['transition_function'],
                data['start_state'], data['accept_states'], data['current_state']
            )
            result = dfa.run_with_input_list(request.data.get('input_list', []))
            return Response({"result": result})
        return Response(serializer.errors, status=400)

class ConvertNFAToDFA(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NFASerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            nfa = NFA(
                data['states'], data['alphabet'], data['transition_function'],
                data['start_state'], data['accept_states'], data['current_state']
            )
            dfa = nfa.convert_to_DFA()
            return Response(DFASerializer(dfa).data)
        return Response(serializer.errors, status=400)

class ConvertNFAEpsilonToDFA(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NFAEpsilonSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            nfa_epsilon = NFA_epsilon(
                data['states'], data['alphabet'], data['transition_function'],
                data['start_state'], data['accept_states'], data['current_state']
            )
            dfa = nfa_epsilon.convert_to_DFA()
            return Response(DFASerializer(dfa).data)
        return Response(serializer.errors, status=400)

class ConvertToRG(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DFASerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            dfa = DFA(
                data['states'], data['alphabet'], data['transition_function'],
                data['start_state'], data['accept_states'], data['current_state']
            )
            rg = dfa.convert_to_RG()
            return Response(RGSerializer(rg).data)
        return Response(serializer.errors, status=400)

