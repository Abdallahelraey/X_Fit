class TrainingParameters:
    def __init__(self, muscle_groups, reps, sets, tempo, intensity, rest, load, schedule, frequency, volume, split, duration, exercise_selection):
        self._muscle_groups = muscle_groups
        self._reps = reps
        self._sets = sets
        self._tempo = tempo
        self._intensity = intensity
        self._rest = rest
        self._load = load
        self._schedule = schedule
        self._frequency = frequency
        self._volume = volume
        self._split = split
        self._duration = duration
        self._exercise_selection = exercise_selection

    @property
    def muscle_groups(self):
        return self._muscle_groups

    @muscle_groups.setter
    def muscle_groups(self, muscle_groups):
        self._muscle_groups = muscle_groups

    @property
    def reps(self):
        return self._reps

    @reps.setter
    def reps(self, reps):
        self._reps = reps

    @property
    def sets(self):
        return self._sets

    @sets.setter
    def sets(self, sets):
        self._sets = sets

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, tempo):
        self._tempo = tempo

    @property
    def intensity(self):
        return self._intensity

    @intensity.setter
    def intensity(self, intensity):
        self._intensity = intensity

    @property
    def rest(self):
        return self._rest

    @rest.setter
    def rest(self, rest):
        self._rest = rest

    @property
    def load(self):
        return self._load

    @load.setter
    def load(self, load):
        self._load = load

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        self._schedule = schedule

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        self._frequency = frequency

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = self._reps * self._load * self._sets

    @property
    def split(self):
        return self._split

    @split.setter
    def split(self, split):
        self._split = split

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def exercise_selection(self):
        return self._exercise_selection

    @exercise_selection.setter
    def exercise_selection(self, exercise_selection):
        self._exercise_selection = exercise_selection


