from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from django.utils import timezone
from birthdayEmails.models import DrchronoEmail

class Command(BaseCommand):
    help = 'Sends any emails that are overdue to be sent'
    def add_arguments(self, parser):
        parser.add_argument('--force',
            action='store_true',
            dest='force',
            default=False,
            help='Send all pending emails, regardless of whether the date has passed.')

    def handle(self, *args, **options):
        emails = DrchronoEmail.objects.filter(sent_date = None)
        if not options['force']:
            emails = emails.filter(send_date__lt=timezone.now())
        for email in emails:
            send_mail(email.subject.strip('\n'), email.body, 'drchronobirthday@gmail.com',
            ['adamkaz@gmail.com'], fail_silently=False)
            email.sent_date=timezone.now()
            email.save()
        num_emails = len(emails)
        self.stdout.write('%s emails sent' % num_emails)