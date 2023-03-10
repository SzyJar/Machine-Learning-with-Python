def player(prev_play, opponent_history=[], my_history=['']):
  guess = "S"
  predict = None
  
  if len(opponent_history) > 500:
    del opponent_history[0]
    del my_history[0]

  if len(opponent_history) > 2:
    guess = opponent_history[-2]  

  # Opponent moves history
  opponent_history.append(prev_play)

  # level of insight
  level = 12
  # Predict opponent's next move
  match = 0
  for pattern_len in range(level, 1, -1):
    for i in range(len(opponent_history) - 1, 0, -1):
      match = 0
      for j in range(pattern_len):
        if i - j > 0 and opponent_history[-1] == opponent_history[i]:
          if opponent_history[-1 - j] == opponent_history[i - j]:
            if my_history[-1 - j] == my_history[i - j]:
              match += 1
      if match >= pattern_len and i + 2 <= len(opponent_history):
        predict = opponent_history[i + 1]
        break
    if match >= pattern_len and i + 2 <= len(opponent_history):
      break

  # Act according to prediction
  if predict == "R":
    guess = "P"
  elif predict == "P":
    guess = "S"
  elif predict == "S":
    guess = "R"

  # My moves history
  my_history.append(guess)
  
  return guess


def player_rps(prev_play, my_history=['']):
  if my_history[-1] == "R":
    my_history.append("P")
    return "P"
  if my_history[-1] == "P":
    my_history.append("S")
    return "S"
  my_history.append("R")
  return "R"