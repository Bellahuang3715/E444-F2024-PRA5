import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("latency_results.csv")

average_latency = df.groupby('Test Case')['Latency (s)'].mean()
print(f"Average latency: {average_latency}")

# generate boxplot for latencies
plt.figure(figsize=(10, 4))
df.boxplot(column='Latency (s)', by='Test Case', showfliers=False, showmeans=True, meanline=True)

# set plot title and labels
plt.title("Latency Results Boxplot for Each Test Case")
plt.xlabel("Test Case")
plt.ylabel("Latency (seconds)")
plt.tight_layout()
plt.savefig('boxplot.png')
plt.show()
