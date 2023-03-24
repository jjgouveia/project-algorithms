def study_schedule(permanence_period, target_time):
    n = 0
    period = range(len(permanence_period))
    try:
        for i in period:
            entry, exit = permanence_period[i]
            if entry <= target_time <= exit:
                n += 1
        return n
    except TypeError:
        None
