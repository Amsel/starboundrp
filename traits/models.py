from django.db import models


class Trait(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()

    # the number of slots it uses
    weight = models.IntegerField(default=1)
    bonus = models.BooleanField(default=False)

    # The trait requires other traits
    depends_on = models.ManyToManyField('Trait',
                                        related_name='trait_depends_on',
                                        blank=True, default=None)
    # The trait conflicts with other traits
    conflicts_with = models.ManyToManyField('Trait',
                                            related_name='trait_conflicts_with',
                                            blank=True, default=None)

    characters = models.ManyToManyField('character.Character', blank=True)

    def __str__(self):
        return self.name

    def is_bonus(self):
        return self.bonus

    def is_malus(self):
        return not self.bonus
