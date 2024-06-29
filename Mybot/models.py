from django.db import models

# Create your models here.
class Loginform(models.Model):
    user_name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=8)
    NameScript = models.TextField(max_length=300)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Loginform'
        verbose_name_plural = 'Loginforms'

class Suit(models.Model):
    """Model definition for Suit."""
    court = models.CharField(max_length=200)
    city = models.CharField(max_length=60)
    IAnum = models.IntegerField()
    OSnum = models.IntegerField()
    Year = models.IntegerField()
    Plaintiffs = models.TextField()
    Defendants = models.TextField()
    pf1 = models.CharField(max_length=300)
    df1 = models.CharField(max_length=300)
    # TODO: Define fields here
    def name(self):
        return self.pfl() + ' vs ' +self.dfl()
    def pfl(self):
        n=len(self.Plaintiffs.split('\n'))
        suffix = ' and others' if n>1 else ' and another' if n==1 else ''
        return self.pf1 + suffix
    def dfl(self):
        n=len(self.Defendants.split('\n'))
        suffix = ' and others' if n>1 else ' and another' if n==1 else ''
        return self.pf1 + suffix
    class Meta:
        """Meta definition for Suit."""

        verbose_name = 'Suit'
        verbose_name_plural = 'Suits'

    def __str__(self):
        """Unicode representation of Suit."""
        pass
