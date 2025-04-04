
import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n = 300
years = list(range(2003, 2024))

# Helper functions
def random_race():
    return np.random.choice(['Black', 'White', 'Latino', 'Other'], p=[0.55, 0.35, 0.05, 0.05])

def random_position():
    return np.random.choice(['QB', 'WR', 'RB', 'OL', 'DL', 'LB', 'DB', 'Special Teams', 'None'], 
                            p=[0.1, 0.14, 0.14, 0.18, 0.14, 0.1, 0.1, 0.05, 0.05])

def coaching_position():
    return np.random.choice(['Position Coach', 'Special Teams', 'Offensive Coordinator', 'Defensive Coordinator', 'Head Coach'], 
                            p=[0.4, 0.1, 0.2, 0.2, 0.1])

def policy_window(year):
    if year < 2011:
        return '2003–2010'
    elif year < 2021:
        return '2011–2020'
    else:
        return '2021–2023'

# Generate synthetic data
data = []
for i in range(1, n + 1):
    race = random_race()
    start_year = np.random.choice(years)
    tenure_years = np.random.randint(3, 20)
    end_year = min(start_year + tenure_years, 2023)
    years_experience = end_year - start_year
    position = random_position()
    player_to_coach = int(position != 'None')
    c_position = coaching_position()
    promoted_to_head = int(c_position == 'Head Coach')
    promotion_year = np.random.choice(range(start_year + 3, end_year + 1)) if promoted_to_head and years_experience >= 3 else None
    team_perf = round(np.random.normal(loc=0.55, scale=0.15), 2)
    team_perf = min(max(team_perf, 0), 1)
    rr_interview = np.random.choice([0, 1], p=[0.6, 0.4]) if race != 'White' else 0
    interview_year = promotion_year if rr_interview and promoted_to_head else None
    policy = policy_window(interview_year) if interview_year else None

    data.append({
        'coach_id': i,
        'race': race,
        'start_year': start_year,
        'player_to_coach_transition': player_to_coach,
        'position_played': position,
        'coaching_position': c_position,
        'years_experience': years_experience,
        'team_performance_rating': team_perf,
        'promoted_to_head': promoted_to_head,
        'promotion_year': promotion_year,
        'tenure_years': years_experience,
        'rooney_rule_interview': rr_interview,
        'interview_year': interview_year,
        'policy_window': policy
    })

# Create and save dataset
df = pd.DataFrame(data)
df.to_csv("cleaned_synthetic_nfl_coach_dataset.csv", index=False)
print("Synthetic NFL coaching dataset created and saved as 'cleaned_synthetic_nfl_coach_dataset.csv'")
