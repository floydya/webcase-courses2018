def sun_angle(time):
    minut = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
    if minut > 359 and minut < 1081:
        return (minut - 360)*180/720
    return  'I don\'t see the sun!'
