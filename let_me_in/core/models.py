from django.db.models import Model, ForeignKey, CharField, FloatField


NESTED_PROFIT_PERCENTAGE = 25


class User(Model):
    """
    A custom user so that we can add permissions easily
    """
    referrer = ForeignKey(
        'self', null=True, blank=True, related_name="referees")
    name = CharField(max_length=255, null=True, blank=True)
    email = CharField(max_length=255, unique=True)
    score = FloatField(default=0.0)

    def referee_count(self, percent=100):
        referees = list(self.referees.all())
        count = len(referees) * percent / 100
        for referee in referees:
            count += referee.referee_count(
                percent * NESTED_PROFIT_PERCENTAGE / 100)
        return count

    def update_score(self):
        self.score = self.referee_count()
        self.save()

    def __str__(self):
        return "%d - %s - %s - %f" % (
            self.id, self.name, self.email, self.score)

    def __repr__(self):
        return "<User: %s>" % self.__str__()
