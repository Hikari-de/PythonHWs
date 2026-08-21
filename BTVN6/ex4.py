import numpy as np

matches = np.column_stack((
    np.random.randint(5, 31, 5),
    np.random.randint(1, 20, 5),
    np.random.randint(0, 11, 5),
    np.random.randint(100, 401, 5)
))

print("Match statistics (Kills - Deaths - Assists - Combat Score):")
print(matches)

recent_kda = matches[-3:, :3]

print("---")
print("K-D-A of the last 3 matches:")
print(recent_kda)

kd_ratio = np.round(matches[:, 0] / matches[:, 1], 2)

print("---")
print("K/D ratio for each match:", kd_ratio)

max_kills = matches[:, 0].max()
total_assists = matches[:, 2].sum()
min_combat_score = matches[:, 3].min()

print("---")
print("Record Kills:", max_kills)
print("Total Assists:", total_assists)
print("Lowest Combat Score:", min_combat_score)

transposed_data = matches.T

print("---")
print("Data prepared for charting (Transposed):")
print(transposed_data)