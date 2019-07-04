workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
    """Title case passed in day argument (monday or MONDAY -> Monday)
       and check if it is in the given workout_schedule dict.

       If it is there retrieve the workout, if not raise a KeyError.

       Return the chill or go_train variable depending the retrieved
       workout value ('Rest' or workout bla)

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    try:
        action = workout_schedule[day.title()]
        if action == rest:
            action = chill
        else:
            action = go_train.format(action)
    except KeyError:
        raise KeyError('Workout does not exist.')

    return action


if __name__ == '__main__':
    print(get_workout_motd("Monday"))
    print(get_workout_motd("asdf"))
