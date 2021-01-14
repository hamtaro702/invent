from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    def __str__(self) :
       return self.name
    def __str__(self) :
       return self.desc

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class ActiveDirectory(models.Model):
    employeeid = models.IntegerField(primary_key=True)
    costcenter = models.CharField(max_length=45, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    division = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    employee_name_th = models.CharField(max_length=100, blank=True, null=True)
    employee_name_eng = models.CharField(max_length=100, blank=True, null=True)
    start_working_day = models.CharField(max_length=45, blank=True, null=True)
    group = models.CharField(max_length=45, blank=True, null=True)
    level = models.CharField(max_length=45, blank=True, null=True)
    accout = models.CharField(max_length=45, blank=True, null=True)
    use_ad = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    use_vpn = models.CharField(max_length=45, blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_directory'


class AdDepartment(models.Model):
    department_id = models.CharField(primary_key=True, max_length=25)
    department_name = models.CharField(max_length=75, blank=True, null=True)
    def __str__(self) :
       return self.department_id
    def __str__(self) :
       return self.department_name

    class Meta:
        managed = False
        db_table = 'ad_department'


class AssetBrand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asset_brand'


class AssetCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, blank=True, null=True)
    system = models.ForeignKey('AssetSystem', models.DO_NOTHING, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asset_category'


class AssetInformation(models.Model):
    def __int__(self) :
       return self.asset_id
    asset_id = models.AutoField(primary_key=True)
    system = models.ForeignKey('AssetSystem', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(AssetCategory, models.DO_NOTHING, blank=True, null=True)
    project = models.CharField(max_length=1000, blank=True, null=True)
    device_name = models.CharField(max_length=255, blank=True, null=True)
    host_name = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    brand = models.ForeignKey(AssetBrand, models.DO_NOTHING, blank=True, null=True)
    model = models.ForeignKey('AssetModel', models.DO_NOTHING, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    imei = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    sim = models.CharField(max_length=50, blank=True, null=True)
    mac_address_lan = models.CharField(max_length=100, blank=True, null=True)
    mac_address_wifi = models.CharField(max_length=100, blank=True, null=True)
    ip_wifi = models.CharField(max_length=100, blank=True, null=True)
    ip_lan = models.CharField(max_length=100, blank=True, null=True)
    asset = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    branch = models.ForeignKey('Branch', models.DO_NOTHING, blank=True, null=True)
    building = models.CharField(max_length=100, blank=True, null=True)
    floor = models.CharField(max_length=50, blank=True, null=True)
    status = models.ForeignKey('AssetStatus', models.DO_NOTHING, blank=True, null=True)
    po = models.CharField(max_length=50, blank=True, null=True)
    invoice = models.CharField(max_length=50, blank=True, null=True)
    date_stockin = models.DateField(blank=True, null=True)
    date_stockout = models.DateField(blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bookno = models.CharField(db_column='Bookno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    condition_no = models.CharField(max_length=50, blank=True, null=True)
    windows_edition = models.CharField(max_length=45, blank=True, null=True)
    win_product_key = models.CharField(max_length=45, blank=True, null=True)
    office_edition = models.CharField(max_length=45, blank=True, null=True)
    office_product_key = models.CharField(max_length=45, blank=True, null=True)
    line = models.CharField(max_length=45, blank=True, null=True)
    vpn = models.CharField(max_length=45, blank=True, null=True)
    cpu = models.CharField(max_length=50, blank=True, null=True)
    ram = models.CharField(max_length=50, blank=True, null=True)
    storage = models.CharField(max_length=50, blank=True, null=True)
    filepath = models.CharField(max_length=100, blank=True, null=True)
    costcenter = models.CharField(max_length=45, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'asset_information'


class AssetModel(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    brand = models.ForeignKey(AssetBrand, models.DO_NOTHING, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asset_model'


class AssetPost(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'asset_post'


class AssetStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asset_status'


class AssetSystem(models.Model):
    system_id = models.AutoField(primary_key=True)
    system_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asset_system'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branch'


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    def __str__(self) :
       return self.brand_name

    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brand'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, blank=True, null=True)
    system = models.ForeignKey('System', models.DO_NOTHING, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Condition(models.Model):
    condition_id = models.IntegerField(primary_key=True)
    condition_value = models.CharField(max_length=45, blank=True, null=True)
    condition_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condition'


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


class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=250, blank=True, null=True)
    document_file = models.CharField(max_length=250, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'document'


class InventoryInformation(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    system = models.ForeignKey('System', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    model = models.ForeignKey('Model', models.DO_NOTHING, blank=True, null=True)
    part_number = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    mac_address = models.CharField(max_length=50, blank=True, null=True)
    asset = models.CharField(max_length=50, blank=True, null=True)
    host_name = models.CharField(max_length=50, blank=True, null=True)
    ip_management = models.CharField(max_length=50, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    floor = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey('Status', models.DO_NOTHING, blank=True, null=True)
    po = models.CharField(max_length=50, blank=True, null=True)
    invoice = models.CharField(max_length=50, blank=True, null=True)
    po_number = models.CharField(max_length=50, blank=True, null=True)
    date_stockin = models.DateField(blank=True, null=True)
    date_stockout = models.DateField(blank=True, null=True)
    user_stockout = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_information'


class Model(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model'


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'status'


class System(models.Model):
    system_id = models.AutoField(primary_key=True)
    system_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'system'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=25, blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    adminind = models.IntegerField(db_column='adminInd')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=25, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'

class TheViewAsset(models.Model):
    asset_id = models.IntegerField(primary_key = True)
    project = models.CharField(max_length=1000, blank=True, null=True)
    device_name = models.CharField(max_length=255, blank=True, null=True)
    host_name = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    imei = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    sim = models.CharField(max_length=50, blank=True, null=True)
    mac_address_lan = models.CharField(max_length=100, blank=True, null=True)
    mac_address_wifi = models.CharField(max_length=100, blank=True, null=True)
    ip_wifi = models.CharField(max_length=100, blank=True, null=True)
    ip_lan = models.CharField(max_length=100, blank=True, null=True)
    asset = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    building = models.CharField(max_length=100, blank=True, null=True)
    floor = models.CharField(max_length=50, blank=True, null=True)
    po = models.CharField(max_length=50, blank=True, null=True)
    invoice = models.CharField(max_length=50, blank=True, null=True)
    date_stockin = models.DateField(blank=True, null=True)
    date_stockout = models.DateField(blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bookno = models.CharField(max_length=100, blank=True, null=True)
    condition_no = models.CharField(max_length=50, blank=True, null=True)
    windows_edition = models.CharField(max_length=45, blank=True, null=True)
    win_product_key = models.CharField(max_length=45, blank=True, null=True)
    office_edition = models.CharField(max_length=45, blank=True, null=True)
    office_product_key = models.CharField(max_length=45, blank=True, null=True)
    line = models.CharField(max_length=45, blank=True, null=True)
    vpn = models.CharField(max_length=45, blank=True, null=True)
    cpu = models.CharField(max_length=50, blank=True, null=True)
    ram = models.CharField(max_length=50, blank=True, null=True)
    storage = models.CharField(max_length=50, blank=True, null=True)
    filepath = models.CharField(max_length=100, blank=True, null=True)
    costcenter = models.CharField(max_length=45, blank=True, null=True)
    branch_name = models.CharField(max_length=50, blank=True, null=True)
    brand_name = models.CharField(verbose_name="brand_name", max_length=50, blank=True, null=True)
    category_name = models.CharField(max_length=50, blank=True, null=True)
    model_name = models.CharField(max_length=50, blank=True, null=True)
    status_name = models.CharField(max_length=50, blank=True, null=True)
    system_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'the_view_asset'
