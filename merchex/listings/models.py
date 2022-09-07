from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        ROCK = 'R', 'Rock'
        POP = 'P', 'Pop'
        COUNTRY = 'C', 'Country'
        JAZZ = 'J', 'Jazz'
        BLUES = 'B', 'Blues'
        METAL = 'M', 'Metal'
        OTHER = 'O', 'Other'
        HIP_HOP = 'H', 'Hip Hop'
        SYNTH_POP = 'S', 'Synth Pop'
        ALTERNATIVE_ROCK = 'A', 'Alternative Rock'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(default='H', choices=Genre.choices, max_length=5)
    biography =models.fields.CharField(default='', max_length=1000)
    year_formed = models.fields.IntegerField(
        default=2020,
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_website = models.fields.URLField(null=True, blank=True)

class Title(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Type(models.TextChoices):
        ALBUM = 'A', 'Album'
        SINGLE = 'S', 'Single'
        EP = 'E', 'EP'
        COMPILATION = 'C', 'Compilation'
        OTHER = 'O', 'Other'

    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(default='', max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        default=2020,
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    type = models.fields.CharField(choices= Type.choices ,max_length=100)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)