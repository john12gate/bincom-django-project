# from django.db import models
#
# # Create your models here.
#
# class BincomModel(models.Model):
#
#         agentname = models.CharField(max_length=200)
#         announced_lga_results = models.IntegerField()
#         announced_pu_results = models.IntegerField()
#         announced_state_results = models.IntegerField()
#         announced_ward_results = models.IntegerField()
#         lga = models.CharField(max_length=200)
#         party = models.CharField(max_length=200)
#         polling_unit = models.CharField(max_length=200)
#         states = models.CharField(max_length=200)
#         ward = models.CharField(max_length=200)



from django.db import models

class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField()
    polling_unit_number = models.CharField(max_length=100)
    polling_unit_name = models.CharField(max_length=200)
    polling_unit_description = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    entered_by_user = models.CharField(max_length=100)
    date_entered = models.DateField()
    user_ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.polling_unit_name

    class Meta:
            db_table = 'polling_unit'  # Set the table name
