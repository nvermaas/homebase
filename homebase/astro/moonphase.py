class MoonPhase(object):
    def __init__(self, **kwargs):
        for field in ('phase', 'date', 'time'):
            setattr(self, field, kwargs.get(field, None))

moonphases = {
    1: MoonPhase(id=1, phase='New Moon', date='2018-01-01', time='12:00:00'),
    2: MoonPhase(id=2, phase='First Quarter', date='2018-02-01', time='12:00:00'),
    3: MoonPhase(id=3, phase='Full Moon', date='2018-03-01', time='12:00:00'),
    4: MoonPhase(id=4, phase='Last Quarter', date='2018-04-01', time='12:00:00'),
}