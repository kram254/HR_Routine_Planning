import pandas as pd
import matplotlib.pyplot as plt
from itertools import chain, repeat
from pulp import *

def ncycles(iterable, n):
    # sequence elements n times
    return chain.from_iterable(repeat(tuple(iterable), n))

def visualize_staff_demand(df_staff):
    plt.figure(figsize=(10, 6))
    ax = df_staff.plot.bar(x='Days', y='Staff Demand', color='brown', legend=False)
    plt.title('Daily Workers - Resources Demand')
    plt.xlabel('Days of the week')
    plt.ylabel('Number of Workers')
    plt.show()

def optimize_staff_scheduling(n_staff, hours):
    # Create circular list of days
    n_days = [i for i in range(7)]
    n_days_c = list(ncycles(n_days, 3))

    # Working days
    list_in = [[n_days_c[j] for j in range(i, i + 5)] for i in n_days_c]

    # Days off
    list_excl = [[n_days_c[j] for j in range(i + 1, i + 3)] for i in n_days_c]

    # Build and solve the optimization model
    model = LpProblem("Minimize the number of staff ", LpMinimize)
    x = LpVariable.dicts('shift_', n_days, lowBound=0, cat='Integer')

    model += lpSum([x[i] for i in n_days])

    for d, l_excl, staff in zip(n_days, list_excl, n_staff):
        model += lpSum([x[i] for i in n_days if i not in l_excl]) >= staff

    model.solve()

    print("Status:", LpStatus[model.status])

    daily_workers = {}
    for v in model.variables():
        daily_workers[int(v.name[-1])] = int(v.varValue)

    scheduled_dict = {}
    for day in daily_workers.keys():
        scheduled_dict[day] = [daily_workers[day] if i in list_in[day] else 0 for i in n_days]

    return scheduled_dict, model

def print_schedule_image(df_sch):
    fig, ax = plt.subplots(figsize=(10, 6)) 
    ax.axis('tight')
    ax.axis('off')
    the_table = plt.table(cellText=df_sch.values,
                          colLabels=df_sch.columns,
                          rowLabels=df_sch.index,
                          colColours=["grey"]*7,
                          cellColours=[['lightgreen' if val > 0 else 'salmon' for val in row] for row in df_sch.values],
                          loc='center')
    plt.title('Optimized Staff Schedule', y=-0.1)
    fig.tight_layout()
    plt.savefig('schedule.png')
    plt.show()

def main():
    n_staff = [31, 45, 40, 40, 48, 30, 25]
    hours = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    df_staff = pd.DataFrame({'Days': hours, 'Staff Demand': n_staff})

    visualize_staff_demand(df_staff)

    scheduled_dict, model = optimize_staff_scheduling(n_staff, hours)

    df_sch = pd.DataFrame(scheduled_dict).T
    df_sch.columns = hours
    df_sch.index = [f'Shift: {day}' for day in hours]
    
    print_schedule_image(df_sch)

    print("Total number of Staff =", pulp.value(model.objective))

    print("Optimized Staff Schedule:")
    print(df_sch)
    print("Total Staff Schedule per Day:")
    print(df_sch.sum(axis=0))

    df_supp = df_staff.copy().set_index('Days')
    df_supp['Staff Supply'] = df_sch.sum(axis=0)
    df_supp['Extra_Resources'] = df_supp['Staff Supply'] - df_supp['Staff Demand']
    df_supp.to_csv('workers.csv')

    ax = df_supp.plot.bar(y=['Staff Demand', 'Staff Supply'], figsize=(10, 6), fill=True, color=['grey', 'brown'])
    df_supp.plot(y=['Extra_Resources'], color=['green'], secondary_y=True, ax=ax, linewidth=3)
    plt.title(' workers demand and supply')
    plt.xlabel('Day of the week')
    plt.ylabel('Number of Workers')
    plt.show()

if __name__ == "__main__":
    main()
