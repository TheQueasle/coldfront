from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.conf import settings
import ldap

class Command(BaseCommand):
    help = 'Add a specific user from LDAP'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=str)

    def handle(self, *args, **options):
        l = ldap.initialize(settings.AUTH_LDAP_SERVER_URI)
        username = settings.AUTH_LDAP_BIND_DN
        password  = settings.AUTH_LDAP_BIND_PASSWORD
        l.simple_bind_s(username, password)

        total = 0
        total_created = 0

        for user_id in options['user_id']:
            print("Looking up {}".format(user_id))
            results = l.search_s(settings.AUTH_LDAP_USER_SEARCH_BASE, ldap.SCOPE_SUBTREE, "(uid={})".format(user_id))
            for e, r in results:
                username = r['uid'][0].decode('utf-8')
                first_name = r['givenName'][0].decode('utf-8')
                last_name = r['sn'][0].decode('utf-8')
                try:
                    email = r['mail'][0].decode('utf-8')
                except Exception:
                    email = 'COULD_NOT_LOCATE'
                user, created = User.objects.get_or_create(username=username, email=email, first_name=first_name, last_name=last_name)
                total += 1
                if created:
                    user.set_unusable_password()
                    user.save()
                    total_created += 1
                    print("Added {}".format(user_id))
                else:
                    print("{} already exists".format(user_id))

        print("Found {}/{} users, added {}".format(total, len(options['user_id']), total_created))
