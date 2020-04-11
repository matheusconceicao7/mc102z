tosse = input() == "True"
febre = input() == "True"
dificuldade_respirar = input() == "True"

print("Tosse:", tosse)
print("Febre:", febre)
print("Dificuldade para respirar:", dificuldade_respirar)
print("Provavelmente eh COVID-19:", tosse and febre and dificuldade_respirar)
