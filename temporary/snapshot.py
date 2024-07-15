import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def parse_snapshot_file(file_path):
    epochs = []
    mean_losses = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_epoch = None
        
        for line in lines:
            if 'epoch:' in line:
                current_epoch = int(line.split(':')[1].strip())
            elif 'mean_loss:' in line:
                mean_loss = float(line.split(':')[1].strip())
                if current_epoch is not None and mean_loss > 0:
                    epochs.append(current_epoch)
                    mean_losses.append(mean_loss)
                    current_epoch = None  # Reset after adding to list
                    
    return epochs, mean_losses

snapshot_file = 'snapshot.txt'
epochs, mean_losses = parse_snapshot_file(snapshot_file)

data = {'Epoch': epochs, 'Mean Loss': mean_losses}
df = pd.DataFrame(data)

window_size = 5
df['Moving Average'] = df['Mean Loss'].rolling(window=window_size).mean()
df['Moving Std Dev'] = df['Mean Loss'].rolling(window=window_size).std()

threshold = 0.2 
stable_epoch = df[df['Moving Std Dev'] < threshold]['Epoch'].min()

print(f"Optimal number of epochs: {stable_epoch}")

plt.figure(figsize=(10, 6))
plt.plot(df['Epoch'], df['Mean Loss'], label='Mean Loss')
plt.axvline(stable_epoch, color='r', linestyle='--', label=f'Stable at Epoch {stable_epoch}')
plt.xlabel('Epoch')
plt.ylabel('Mean Loss')
plt.title('Epochs vs Mean Loss')
plt.legend()
plt.grid(True)
plt.show()
