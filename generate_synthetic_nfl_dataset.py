
import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Parameters
n_samples = 300
races = ['Black', 'White', 'Latino', 'Other']
positions = ['QB', 'RB', 'WR', 'OL', 'DL', 'LB', 'DB', 'Special Teams', 'None']
coaching_positions = ['Assistant Coach', 'Position Coach', 'Coordinator']

# Race distribution based on realistic NFL player demographics
race_distribution = {
    'Black': 0.55,
    'White': 0.35,
    'Latino': 0.07,
    'Other': 0.03
}

# Target number of head coach promotions by race (realistic to actual NFL trends)
promotion_targets = {
    'White': 32,   # ~80%
    'Black': 6,    # ~15%
    'Latino': 1,   # ~2.5%
    'Other': 1     # ~2.5%
}

# Generate base dataset
data = []
for i in range(n_samples):
    race = np.random.choice(races, p=[race_distribution[r] for r in races])
    position_played = np.random.choice(positions)
    coaching_position = np.random.choice(coaching_positions)
    years_experience = np.random.randint(1, 21)
    team_performance_rating = round(np.random.uniform(0.3, 0.9), 2)
    rooney_rule_interview = int(race != 'White' and np.random.rand() < 0.5)

    data.append({
        'coach_id': i + 1,
        'race': race,
        'position_played': position_played,
        'coaching_position': coaching_position,
        'years_experience': years_experience,
        'team_performance_rating': team_performance_rating,
        'rooney_rule_interview': rooney_rule_interview,
        'promoted_to_head': 0,
        'promotion_year': np.nan,
        'tenure_years': np.random.randint(1, 6)
    })

df = pd.DataFrame(data)

# Assign head coach promotions based on race-based targets
for race, num_promote in promotion_targets.items():
    eligible = df[df['race'] == race].sample(n=num_promote, random_state=42)
    df.loc[eligible.index, 'promoted_to_head'] = 1
    df.loc[eligible.index, 'coaching_position'] = 'Head Coach'
    df.loc[eligible.index, 'promotion_year'] = np.random.randint(2003, 2024, size=num_promote)
    df.loc[eligible.index, 'tenure_years'] = np.random.randint(3, 11, size=num_promote)

# Save dataset
df.to_csv('realistic_nfl_promotions_dataset.csv', index=False)
print("Synthetic NFL dataset generated and saved as 'realistic_nfl_promotions_dataset.csv'")
