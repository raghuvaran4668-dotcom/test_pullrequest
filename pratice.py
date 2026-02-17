# List of members
members = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace"]

# List of tasks
tasks = ["Code Review", "Bug Fixing", "Testing", "Documentation", "Deployment"]

def assign_tasks(week_number):
    # Rotate members based on week number
    rotated_members = members[week_number % len(members):] + members[:week_number % len(members)]
    
    # Assign first 5 members to 5 tasks
    assignments = {}
    
    for i in range(len(tasks)):
        assignments[rotated_members[i]] = tasks[i]
    
    return assignments

# Example: Show assignments for 4 weeks
for week in range(4):
    print(f"\nWeek {week + 1} Assignments:")
    weekly_tasks = assign_tasks(week)
    
    for member, task in weekly_tasks.items():
        print(f"{member} → {task}")

