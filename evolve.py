import os
import json
import datetime
import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def get_spiral_coords(n):
    # Ulam spiral coordinate calculation
    # (0,0) is 1
    # Right: (1,0) is 2
    # Up: (1,1) is 3
    # Left: (0,1) is 4
    # Left: (-1,1) is 5
    if n == 1: return 0, 0
    
    # Layer number (shell)
    k = math.ceil((math.sqrt(n) - 1) / 2)
    t = 2 * k + 1 # side length
    m = t * t # max value in this shell
    
    # Positions relative to max value m
    if n >= m - (t - 1): return k - (m - n), -k # Bottom
    m -= t - 1
    if n >= m - (t - 1): return -k, -k + (m - n) # Left
    m -= t - 1
    if n >= m - (t - 1): return -k + (m - n), k # Top
    return k, k - (m - n + t - 1) # Right

def evolve(count=50):
    base_dir = os.path.dirname(__file__)
    state_path = os.path.join(base_dir, 'state.json')
    grid_dir = os.path.join(base_dir, 'grid')
    log_path = os.path.join(base_dir, 'spiral-log.md')

    with open(state_path, 'r') as f:
        state = json.load(f)

    start_n = state["n"]
    primes_found = []
    
    for i in range(count):
        n = start_n + i + 1
        if is_prime(n):
            x, y = get_spiral_coords(n)
            primes_found.append((n, x, y))
            cell_file = os.path.join(grid_dir, f"prime_{n}_{x}_{y}.txt")
            with open(cell_file, 'w') as f:
                f.write(f"prime {n}")

    state["n"] += count
    state["last_updated"] = datetime.date.today().isoformat()
    
    with open(state_path, 'w') as f:
        json.dump(state, f, indent=4)

    # ASCII Snapshot (sparse)
    # We need to know ALL primes found so far to draw the spiral
    # But for a log entry, let's just draw the neighborhood of the latest primes
    all_primes = []
    for filename in os.listdir(grid_dir):
        if filename.startswith('prime_'):
            parts = filename.replace('prime_', '').replace('.txt', '').split('_')
            all_primes.append((int(parts[1]), int(parts[2])))

    if all_primes:
        min_x = min(p[0] for p in all_primes) - 1
        max_x = max(p[0] for p in all_primes) + 1
        min_y = min(p[1] for p in all_primes) - 1
        max_y = max(p[1] for p in all_primes) + 1
    else:
        min_x, max_x, min_y, max_y = -5, 5, -5, 5

    # Center the snapshot around (0,0) if it's small
    rows = []
    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) == (0,0):
                row += '1' # Origin
            elif any(p[0] == x and p[1] == y for p in all_primes):
                row += '█'
            else:
                row += ' '
        rows.append(row)
    
    ascii_snapshot = "\n".join(rows)
    date_str = datetime.date.today().isoformat()
    
    with open(log_path, 'a') as f:
        f.write(f"| {state['n']} | {date_str} |\n```\n{ascii_snapshot}\n``` |\n")

    # Generate human summary
    primes_today = len(primes_found)
    summary = f"The prime search has reached N={state['n']}. "
    summary += f"Today, {primes_today} new primes (celestial bodies) were discovered and added to the constellation map. "
    summary += "The diagonal clusters characteristic of the Ulam Spiral are becoming more visible in the project's grid."

    with open(os.path.join(base_dir, 'summary.txt'), 'w') as f:
        f.write(summary)

    # Update README with latest status
    readme_path = os.path.join(base_dir, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as f:
            content = f.read()
        
        start_marker = "<!-- LATEST_STATUS_START -->"
        end_marker = "<!-- LATEST_STATUS_END -->"
        
        if start_marker in content and end_marker in content:
            parts = content.split(start_marker)
            prefix = parts[0] + start_marker
            suffix = end_marker + parts[1].split(end_marker)[1]
            new_content = f"{prefix}\n> {summary}\n{suffix}"
            
            with open(readme_path, 'w') as f:
                f.write(new_content)

if __name__ == "__main__":
    evolve()
