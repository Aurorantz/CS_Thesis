# CS_Thesis
Data form 
 {
  "states": ["S", "A", "B"],
  "alphabet": ["a", "b", "Epsilon"],
  "start_state": "S",
  "accept_states": ["A"],
  "transition_function": {
    "S,Epsilon": ["A", "B"],
    "A,a": ["A"],
    "A,b": ["B"],
    "B,a": ["B"],
    "B,b": ["A"]
  },
  "current_state": "S"
}