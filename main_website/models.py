# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class ChallVideos(models.Model):
    champion = models.ForeignKey('Champions', models.DO_NOTHING, db_column='CHAMPION_ID', blank=True, null=True)  # Field name made lowercase.
    chall_videos_id = models.AutoField(db_column='CHALL_VIDEOS_ID', primary_key=True)  # Field name made lowercase.
    chall_name = models.CharField(db_column='CHALL_NAME', max_length=30, blank=True, null=True, unique=True)  # Field name made lowercase.
    chall_link = models.URLField(db_column='CHALL_LINK', blank=True, null=True, unique=True)  # Field name made lowercase.

    class Meta:
        db_table = 'chall_videos'
    def __str__(self):
        return self.chall_name


class Champions(models.Model):
    champion_id = models.AutoField(db_column='CHAMPION_ID', primary_key=True)  # Field name made lowercase.
    champion_name = models.CharField(db_column='CHAMPION_NAME', max_length=25, unique=True)  # Field name made lowercase.
    champion_icon = models.ImageField(db_column='CHAMPION_ICON', upload_to='champion/icon/', max_length=100, blank=True, null=True, unique=False)  # Field name made lowercase.
    champion_story = models.TextField(db_column='CHAMPION_STORY', blank=True, null=True)  # Field name made lowercase.
    users_favourite = models.ManyToManyField(User, blank=True)
    class Meta:
        db_table = 'champions'

    def __str__(self):
        return self.champion_name


class ChampionsPresentations(models.Model):
    champion = models.ForeignKey(Champions, models.DO_NOTHING, db_column='CHAMPION_ID', blank=True, null=True)  # Field name made lowercase.
    presentation_name = models.CharField(db_column='PRESENTATION_NAME', max_length=60, null=True)
    presentation_link = models.URLField(db_column='PRESENTATION_LINK', blank=True, null=True, unique=True)  # Field name made lowercase.
    presentation_version = models.CharField(db_column='PRESENTATION_VERSION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    champions_presentations_id = models.AutoField(db_column='CHAMPIONS_PRESENTATIONS_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'champions_presentations'

    def __str__(self):
        return self.presentation_name

class ChampionsSkills(models.Model):
    champion = models.ForeignKey(Champions, models.DO_NOTHING, db_column='CHAMPION_ID', blank=True, null=True)  # Field name made lowercase.
    skills_id = models.AutoField(db_column='SKILLS_ID', primary_key=True)  # Field name made lowercase.
    skill_name = models.CharField(db_column='SKILL_NAME', max_length=40, blank=True, null=True, unique=True)  # Field name made lowercase.
    skill_cooldown = models.CharField(db_column='SKILL_COOLDOWN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    skill_cost = models.CharField(db_column='SKILL_COST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    skill_range = models.IntegerField(db_column='SKILL_RANGE', blank=True, null=True)  # Field name made lowercase.
    skill_description = models.TextField(db_column='SKILL_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    skill_icon = models.ImageField(db_column='SKILL_ICON', upload_to='skills/icon/', max_length=100, blank=True, null=True,unique=True)  # Field name made lowercase.

    class Meta:
        db_table = 'champions_skills'
    def __str__(self):
        return self.skill_name

class Items(models.Model):
    item_id = models.AutoField(db_column='ITEM_ID', primary_key=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=30, blank=True, null=True, unique=True)  # Field name made lowercase.
    item_cost = models.IntegerField(db_column='ITEM_COST', blank=True, null=True)  # Field name made lowercase.
    item_description = models.TextField(db_column='ITEM_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    item_icon = models.ImageField(db_column='ITEM_ICON', upload_to='items/icon/', max_length=100, blank=True, null=True,unique=True)  # Field name made lowercase.
    champions = models.ManyToManyField('main_website.Champions', blank=True)
    class Meta:
        db_table = 'items'
    def __str__(self):
        return self.item_name

class Runes(models.Model):
    runes_id = models.AutoField(db_column='RUNES_ID', primary_key=True)  # Field name made lowercase.
    runes_type = models.CharField(db_column='RUNES_TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rune_name = models.CharField(db_column='RUNE_NAME', max_length=30, blank=True, null=True, unique=True)  # Field name made lowercase.
    rune_description = models.TextField(db_column='RUNE_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    rune_icon = models.ImageField(db_column='RUNE_ICON', max_length=100,  upload_to='runes/icon/',  blank=True, null=True, unique=True)  # Field name made lowercase.
    champions = models.ManyToManyField('main_website.Champions', blank=True)
    class Meta:
        db_table = 'runes'
    def __str__(self):
        return self.rune_name

class UserExtended(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to='users/icon/', blank=True)
    biography = models.TextField(blank=True, null=True)
