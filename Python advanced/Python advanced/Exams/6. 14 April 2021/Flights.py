def flights(*args):
    flights_dict = {}
    count = 1
    for i in args:
        if count == 1:
            if i == 'Finish':
                return flights_dict
            if i not in flights_dict:
                flights_dict[i] = 0
            current_dest = i
            count = 0
        else:
            count = 1
            flights_dict[current_dest] += i
