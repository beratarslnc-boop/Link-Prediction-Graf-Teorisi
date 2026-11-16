from math import log
import random

# Veri setini okuma
f = open("facebook_combined.txt", "r")
l = f.readlines()
f.close()

all_edges = []
for line in l:
  s = line.split()
  if len(s) > 2:
    all_edges.append((int(s[0]), int(s[1])))

random.seed(42)
top_k = int(len(all_edges) * 0.2)
test_edges = random.sample(all_edges, top_k)

test_set = set()
for u, v in test_edges:
  test_set.add((u, v))
  test_set.add((v, u))

adj = {}
for u, v in all_edges:
  if u not in adj:
    adj[u] = []
  if v not in adj:
    adj[v] = []
  if (u, v) not in test_set:
    adj[u].append(v)
    adj[v].append(u)

nodes = list(adj.keys())


def adamic_adar(g, u, v):
  score = 0
  for w in g[u]:
    if w in g[v] and len(g[w]) > 1:
      score += 1 / log(len(g[w]))
  return score


scores = []
count = 0
print("Hesaplaniyor, lutfen bekleyin...")

while count < 10000:
  u, v = random.choice(nodes), random.choice(nodes)
  if u != v and v not in adj[u] and (u, v) not in test_set:
    s = adamic_adar(adj, u, v)
    if s > 0:
      scores.append((u, v, s))
    count += 1

for u, v in test_edges:
  scores.append((u, v, adamic_adar(adj, u, v)))

scores.sort(key=lambda x: x[2], reverse=True)

correct = sum(
    1 for i in range(top_k) if (scores[i][0], scores[i][1]) in test_set
)
print("Test Kenar Sayisi:", top_k)
print("Dogru Tahmin:", correct)
print("Doğruluk: %" + str(round((correct / top_k) * 100, 2)))