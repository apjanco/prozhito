# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Collections(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    text = models.TextField()
    tag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'collections'


class DiariesLanguages(models.Model):
    diary = models.IntegerField()
    language = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'diaries_languages'


class DiariesLatest(models.Model):
    person = models.IntegerField()
    diary = models.IntegerField()
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'diaries_latest'


class DiariesStatuses(models.Model):
    diary = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'diaries_statuses'


class Diary(models.Model):
    id = models.IntegerField(primary_key=True)
    person = models.IntegerField()
    status = models.CharField(max_length=14)
    notes = models.IntegerField()
    firstnote = models.DateField(db_column='firstNote')  # Field name made lowercase.
    lastnote = models.DateField(db_column='lastNote')  # Field name made lowercase.
    team = models.TextField()
    premier = models.IntegerField(blank=True, null=True)
    user = models.IntegerField()
    updateddate = models.IntegerField(db_column='updatedDate')  # Field name made lowercase.
    createddate = models.IntegerField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diary'


class DiaryComments(models.Model):
    id = models.IntegerField(primary_key=True)
    diary = models.IntegerField()
    text = models.TextField()
    user = models.IntegerField()
    createddate = models.IntegerField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diary_comments'


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    text = models.TextField()
    pictures = models.TextField()
    user = models.IntegerField()
    createddate = models.IntegerField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news'


class Notes(models.Model):
    id = models.IntegerField(primary_key=True)
    diary = models.IntegerField()
    text = models.TextField()
    date = models.DateField()
    datetop = models.DateField(db_column='dateTop')  # Field name made lowercase.
    notdated = models.IntegerField(db_column='notDated')  # Field name made lowercase.
    julian_calendar = models.IntegerField()
    pictures = models.IntegerField()
    user = models.IntegerField()
    createddate = models.IntegerField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notes'


class NotesComments(models.Model):
    id = models.IntegerField()
    number = models.BigIntegerField()
    note = models.IntegerField()
    text = models.TextField()
    user = models.IntegerField()
    createddate = models.IntegerField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notes_comments'


class NotesDatestr(models.Model):
    id = models.IntegerField()
    datestr = models.TextField(db_column='dateStr')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notes_dateStr'


class NotesPictures(models.Model):
    id = models.IntegerField()
    note = models.IntegerField()
    name = models.TextField()
    title = models.TextField()
    user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notes_pictures'


class NotesPreview(models.Model):
    id = models.IntegerField()
    diary = models.IntegerField()
    user = models.IntegerField()
    createddate = models.IntegerField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notes_preview'


class NotesPreviewReference(models.Model):
    preview = models.IntegerField()
    note = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notes_preview_reference'


class NotesQuotes(models.Model):
    id = models.IntegerField()
    text = models.TextField()
    diary = models.IntegerField()
    note = models.IntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'notes_quotes'


class Persons(models.Model):
    id = models.IntegerField()
    firstname = models.TextField(db_column='firstName')  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName')  # Field name made lowercase.
    thirdname = models.TextField(db_column='thirdName')  # Field name made lowercase.
    nickname = models.TextField()
    edition = models.TextField()
    birthday = models.TextField(db_column='birthDay')  # Field name made lowercase.
    deathday = models.TextField(db_column='deathDay')  # Field name made lowercase.
    birthday2 = models.DateField(db_column='birthDay2')  # Field name made lowercase.
    deathday2 = models.DateField(db_column='deathDay2')  # Field name made lowercase.
    agearound = models.IntegerField(db_column='ageAround')  # Field name made lowercase.
    info = models.TextField()
    additional_info = models.TextField()
    forvolunteers = models.TextField(db_column='forVolunteers')  # Field name made lowercase.
    wikilink = models.TextField(db_column='wikiLink')  # Field name made lowercase.
    avatar = models.IntegerField()
    countdiaries = models.IntegerField(db_column='countDiaries')  # Field name made lowercase.
    user = models.IntegerField()
    gender = models.IntegerField()
    updated = models.IntegerField()
    createddate = models.IntegerField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persons'


class PersonsPartners(models.Model):
    person = models.IntegerField()
    partner = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'persons_partners'


class PersonsPictures(models.Model):
    id = models.IntegerField()
    person = models.IntegerField()
    name = models.TextField()
    title = models.TextField()
    user = models.IntegerField()
    createddate = models.IntegerField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persons_pictures'


class PersonsStatus(models.Model):
    id = models.IntegerField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'persons_status'


class PersonsStatusReference(models.Model):
    status = models.IntegerField()
    persons = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'persons_status_reference'


class ProjectPartners(models.Model):
    id = models.IntegerField()
    name = models.TextField()
    logo = models.IntegerField()
    info = models.TextField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_partners'


class ProjectTeam(models.Model):
    id = models.IntegerField()
    name = models.TextField()
    logo = models.IntegerField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_team'


class Sessions(models.Model):
    session_id = models.CharField(max_length=24)
    last_active = models.PositiveIntegerField()
    contents = models.TextField()

    class Meta:
        managed = False
        db_table = 'sessions'


class SphinxCountersNotes(models.Model):
    maxts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sphinx_counters_notes'


class Statuses(models.Model):
    id = models.IntegerField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'statuses'


class Subscribe(models.Model):
    id = models.IntegerField()
    name = models.TextField()
    email = models.TextField()
    status = models.IntegerField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subscribe'


class Tags(models.Model):
    id = models.IntegerField()
    name = models.TextField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tags'


class TagsDiaries(models.Model):
    diary = models.IntegerField()
    tag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tags_diaries'


class TagsNotes(models.Model):
    note = models.IntegerField()
    tag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tags_notes'


class TagsPersons(models.Model):
    person = models.IntegerField()
    tag = models.IntegerField()
    group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tags_persons'


class TagsType(models.Model):
    id = models.IntegerField()
    name = models.TextField()
    clearname = models.TextField(db_column='clearName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tags_type'


class Users(models.Model):
    id = models.IntegerField()
    firstname = models.TextField(db_column='firstName')  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName')  # Field name made lowercase.
    password = models.TextField()
    email = models.TextField()
    admin = models.IntegerField()
    status = models.IntegerField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
