from django.urls import path
from .views import *

urlpatterns = [
    path('run_dfa/', RunDFA.as_view(), name='run_dfa'),
    path('run_nfa/', RunNFA.as_view(), name='run_nfa'),
    path('convert_dfa_to_rg/', ConvertDFAToRG.as_view(), name='convert_dfa_to_rg'),
    path('convert_nfa_to_dfa/', ConvertNFAToDFA.as_view(), name='convert_nfa_to_dfa'),
    path('convert_nfa_epsilon_to_dfa/', ConvertNFAEpsilonToDFA.as_view(), name='convert_nfa_epsilon_to_dfa'),
    path('convert_to_rg/', ConvertToRG.as_view(), name='convert_to_rg'),
    path('convert_nfae_to_rg/', ConvertNFAEpsilonToRG.as_view(), name='convert_nfae_to_rg'),
]
