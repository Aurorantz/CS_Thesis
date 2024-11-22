from django.urls import path
from .views import RunDFA, ConvertNFAToDFA, ConvertNFAEpsilonToDFA, ConvertToRG

urlpatterns = [
    path('run_dfa/', RunDFA.as_view(), name='run_dfa'),
    path('convert_nfa_to_dfa/', ConvertNFAToDFA.as_view(), name='convert_nfa_to_dfa'),
    path('convert_nfa_epsilon_to_dfa/', ConvertNFAEpsilonToDFA.as_view(), name='convert_nfa_epsilon_to_dfa'),
    path('convert_to_rg/', ConvertToRG.as_view(), name='convert_to_rg'),
]
