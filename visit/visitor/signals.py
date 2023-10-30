from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from visit.visitor.models import RestaurantReservation,Visitor


# @receiver(post_save, sender=RestaurantReservation)
# def send_email_on_model_creation(sender, instance, created, **kwargs):
#     if created:
#         visitor_info = Visitor.objects.get(pk=instance.visitor_id)
#         email_content = (f'Име: {visitor_info.first_name}\n'
#                          f'Фамилия: {visitor_info.last_name}\n'
#                          f'Компания: {visitor_info.company_name}')
#         recipient_email = 'Mariyan.Karastoyanov@witte-automotive.bg'
#         subjects = 'Инфорнация за посетителя'
#         send_mail(
#             subject=subjects,
#             message=email_content,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[recipient_email],
#         )



