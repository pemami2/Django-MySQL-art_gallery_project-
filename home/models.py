from django.db import models

# Create your models here.
#class Record(models.Model):
#   title = models.CharField(max_length=200)
#    body = models.TextField()

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Artist(models.Model):
    artistid = models.IntegerField(db_column='ArtistID', primary_key=True)  # Field name made lowercase.
    artist = models.CharField(db_column='Artist', max_length=50)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='BirthPlace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    styleid = models.ForeignKey('Style', models.DO_NOTHING, db_column='StyleID')  # Field name made lowercase.
    def __str__(self):
        return self.artist
    class Meta:
        managed = False
        db_table = 'artist'


class Artshow(models.Model):
    artshowid = models.IntegerField(db_column='ArtShowID', primary_key=True)  # Field name made lowercase.
    artshow = models.CharField(db_column='ArtShow', max_length=50)  # Field name made lowercase.
    artistid = models.ForeignKey(Artist, models.DO_NOTHING, db_column='ArtistID')  # Field name made lowercase.
    artworkid = models.ForeignKey('Artwork', models.DO_NOTHING, db_column='ArtworkID')  # Field name made lowercase.
    dateandtime = models.DateTimeField(db_column='DateAndTime', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey('Location', models.DO_NOTHING, db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
    contactid = models.ForeignKey('Contact', models.DO_NOTHING, db_column='ContactID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.artshow
    class Meta:
        managed = False
        db_table = 'artshow'


class Artwork(models.Model):
    artworkid = models.IntegerField(db_column='ArtworkID', primary_key=True)  # Field name made lowercase.
    artistid = models.ForeignKey(Artist, models.DO_NOTHING, db_column='ArtistID')  # Field name made lowercase.
    artist = models.CharField(db_column='Artist', max_length=50)  # Field name made lowercase.
    artwork = models.CharField(db_column='Artwork', max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateofcreation = models.DateField(db_column='DateOfCreation', blank=True, null=True)  # Field name made lowercase.
    dateacquired = models.DateField(db_column='DateAcquired', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey('Location', models.DO_NOTHING, db_column='LocationID')  # Field name made lowercase.
    def __str__(self):
        return self.artwork
    class Meta:
        managed = False
        db_table = 'artwork'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contact(models.Model):
    contactid = models.IntegerField(db_column='ContactID', primary_key=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=50)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Phone', unique=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.contact
    class Meta:
        managed = False
        db_table = 'contact'


class Customer(models.Model):
    customerid = models.IntegerField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=50)  # Field name made lowercase.
    phone = models.IntegerField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    styleid = models.ForeignKey('Style', models.DO_NOTHING, db_column='StyleID', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.customer
    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Location(models.Model):
    location = models.CharField(db_column='Location', unique=True, max_length=50)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationID', primary_key=True)  # Field name made lowercase.
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.location
    class Meta:
        managed = False
        db_table = 'location'


class Style(models.Model):
    styleid = models.IntegerField(db_column='StyleID', primary_key=True)  # Field name made lowercase.
    style = models.CharField(db_column='Style', unique=True, max_length=50)  # Field name made lowercase.
    popularity = models.IntegerField(db_column='Popularity', blank=True, null=True)  # Field name made lowercase.
    consultant = models.CharField(db_column='Consultant', max_length=50, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.style
    class Meta:
        managed = False
        db_table = 'style'
    