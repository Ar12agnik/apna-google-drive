from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User,Group
from django.core.mail import send_mail
from sosta_gdrive import settings
@receiver(post_save,sender = User)
def add_to_group(sender,instance,created, **kwargs):
    if created:
        print("triggered")
        grp,created=Group.objects.get_or_create(name="users")
        instance.groups.add(grp)

@receiver(post_save,sender = User)
def notify_admins(sender,instance,created,**kwargs):
    if created:
        admin = User.objects.get(is_staff=True,email__isnull=False)
        Subject=f"Pending Aproval for manager"
        message=f"Hey {admin.first_name}!\n {instance.username} needs your approval To become a manager!\n Please do the needful! \n please note that you  can eather approve the request or reject it! "
        send_mail(Subject,message,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=[admin.email],fail_silently=False)