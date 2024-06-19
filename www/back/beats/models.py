from django.core.validators import MaxValueValidator, FileExtensionValidator
from django.db import models


class Mood(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    author = models.ForeignKey('users.Profile', related_name='playlists', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Beat(models.Model):
    GENRES = (
        ('jazz', 'Джаз'),
        ('rock', 'Рок'),
        ('metal', 'Метал'),
        ('pop', 'Поп'),
        ('rap', 'Реп'),
        ('blues', 'Блюз'),
        ('hip-hop', 'Хип-хоп'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    genre = models.CharField(choices=GENRES, max_length=25)
    mood = models.ForeignKey('beats.Mood', related_name='beats', on_delete=models.CASCADE)
    wav_price = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    trackout_price = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    author = models.ForeignKey('users.Profile', related_name='beats', on_delete=models.CASCADE)
    discounted = models.BooleanField(default=False)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    bpm = models.PositiveIntegerField()
    on_sale = models.BooleanField(default=True)
    tagged_file = models.FileField(upload_to='beats',  null=False, blank=False, validators=[FileExtensionValidator(['mp3'])])
    wav_file = models.FileField(upload_to='beats',  null=False, blank=False, validators=[FileExtensionValidator(['wav'])])
    trackout_file = models.FileField(upload_to='beats',  null=True, blank=True, validators=[FileExtensionValidator(['zip'])])
    playlist = models.ManyToManyField('beats.Playlist', related_name='beats', blank=True, null=True)

    def add_to_playlist(self, playlist):
        if self.author.user.username == playlist.author.user.username:
            self.playlist.add(playlist)
            self.save()
        else:
            raise Exception('Нельзя добавить чужой бит в свой плейлист.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__discount_percent = self.discount_percent

    def save(self, *args, **kwargs):
        if self.discount_percent > 0:
            self.discounted = True
        else:
            self.discounted = False
        super().save()

    def __str__(self):
        return self.name


class Like(models.Model):
    beat = models.ForeignKey('beats.Beat', related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey('users.Profile', related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.beat.name} - {self.user.user.username}"
