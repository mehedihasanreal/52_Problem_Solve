t = int(input())
for _ in range(t):
    total_runs, current_runs, balls_left = map(int, input().split())
    played_balls = 300 - balls_left
    current_run_rate = (current_runs / played_balls) * 6
    required_run_rate = (((total_runs + 1) - current_runs) / balls_left) * 6
    print(f"{current_run_rate:.2f} {required_run_rate:.2f}")
