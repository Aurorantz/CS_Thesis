# automata/serializers.py
from rest_framework import serializers
from .automata_logic import DFA, NFA, NFA_epsilon, RG

class DFASerializer(serializers.Serializer):
    states = serializers.ListField()
    alphabet = serializers.ListField()
    transition_function = serializers.DictField()
    start_state = serializers.CharField()
    accept_states = serializers.ListField()
    current_state = serializers.CharField()

class NFASerializer(DFASerializer):
    pass  # Can extend the base DFA serializer if needed

class NFAEpsilonSerializer(DFASerializer):
    pass  # Can extend the base DFA serializer if needed

class RGSerializer(serializers.Serializer):
    variables = serializers.ListField()
    terminal_symbols = serializers.ListField()
    start_symbol = serializers.CharField()
    production_rules = serializers.DictField()
    Type = serializers.CharField()