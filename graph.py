import pandas as pd
import matplotlib.pyplot as plt

def header():
    # Read the CSV file with DSA and Aptitude counters
    df = pd.read_csv("dsa_responses.csv", header=None, names=['datetime', 'dsa_counter', 'aptitude_counter'])

    # Convert 'datetime' column to datetime type
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Extract date from datetime
    df['date'] = df['datetime'].dt.date

    # Group by date and sum the counters
    df_dsa = df.groupby('date', as_index=False)['dsa_counter'].sum()
    df_aptitude = df.groupby('date', as_index=False)['aptitude_counter'].sum()

    # Create a full date range
    full_date_range = pd.date_range(start=df['date'].min(), end=df['date'].max())

    # Reindex to include all dates in the range
    df_dsa.set_index('date', inplace=True)
    df_dsa = df_dsa.reindex(full_date_range, fill_value=0).rename_axis('date').reset_index()

    df_aptitude.set_index('date', inplace=True)
    df_aptitude = df_aptitude.reindex(full_date_range, fill_value=0).rename_axis('date').reset_index()

    # Merge both dataframes
    df_combined = pd.merge(df_dsa, df_aptitude, on='date')
    df_combined.rename(columns={'dsa_counter': 'DSA Counter', 'aptitude_counter': 'Aptitude Counter'}, inplace=True)

    op = 'processed_data.csv'
    df_combined.to_csv(op, index=False)

    print(f"Processed data saved to {op}")

    return df_combined

def graph(df):
    plt.figure(figsize=(12, 6))
    
    # Plot DSA Counter
    plt.plot(df['date'], df['DSA Counter'], label='DSA Counter', color='blue')
    
    # Plot Aptitude Counter
    plt.plot(df['date'], df['Aptitude Counter'], label='Aptitude Counter', color='green')
    
    plt.xlabel('Date')
    plt.ylabel('Number of Problems Solved')
    plt.title("Problems Solved Tracker")
    plt.legend()
    plt.grid(True)

    plt.show()
