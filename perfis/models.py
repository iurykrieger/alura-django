from django.db import models


class Profile(models.Model):

    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=15, null=False)
    name_company = models.CharField(max_length=255, null=False)

    def invite(self, invited_profile):
        Invitation(inviter=self, invited=invited_profile).save()


class Invitation(models.Model):

    inviter = models.ForeignKey(Profile, related_name='invitations_sent')
    invited = models.ForeignKey(Profile, related_name='invitations_received')
