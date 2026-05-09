P_Rain = [0.7, 0.3]
P_Accident = [0.8, 0.2]

P_Traffic = {
    (0, 0): [0.9, 0.1],
    (0, 1): [0.6, 0.4],
    (1, 0): [0.5, 0.5],
    (1, 1): [0.1, 0.9]
}

def check_model():
    if sum(P_Rain) != 1:
        return False
    if sum(P_Accident) != 1:
        return False
    for key in P_Traffic:
        if sum(P_Traffic[key]) != 1:
            return False
    return True

print("Model Validity:", check_model())

print("\nBayesian Network Tools:")
tools = ["pgmpy", "BayesiaLab", "GeNIe", "Netica", "Hugin"]

for t in tools:
    print(t)

def inference_traffic_given_rain(rain_value):
    result = [0, 0]
    for accident in [0, 1]:
        p_acc = P_Accident[accident]
        p_t = P_Traffic[(rain_value, accident)]
        result[0] += p_t[0] * p_acc
        result[1] += p_t[1] * p_acc
    return result

res = inference_traffic_given_rain(1)

print("\nInference Result:")
print("P(Traffic=0 | Rain=1):", res[0])
print("P(Traffic=1 | Rain=1):", res[1])