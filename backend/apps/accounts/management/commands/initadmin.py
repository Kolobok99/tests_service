from django.core.management import BaseCommand

from apps.accounts.models import UserModel


class Command(BaseCommand):
    help = 'Создает админа (root:root)'
    def handle(self, *args, **options):
        """Создает админа, если в БД нет ни одного user(is_superuser=True)"""

        if not UserModel.objects.filter(is_superuser=True):
            UserModel.objects.create_superuser(
                email='root@mail.com',
                password='root',
            )
        # try:
        #     UserModel.objects.create_user(
        #         email='driver@mail.com',
        #         password='12345',
        #         is_active=True
        #     )
        # except:
        #     pass
        self.stdout.write(self.style.SUCCESS("Админ создан!"))