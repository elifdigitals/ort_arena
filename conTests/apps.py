from django.apps import AppConfig
import threading
import time
from django.utils import timezone
from django.db.utils import OperationalError, ProgrammingError
from django.core.exceptions import ImproperlyConfigured


class ContestConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'conTests'

        def ready(self):
            import sys

            if any(cmd in sys.argv for cmd in ['makemigrations', 'migrate', 'shell', 'collectstatic', 'createsuperuser']):
                return

            from .models import Contest

            def check_contests():
                while True:
                    try:
                        now = timezone.now()
                        ended_contests = Contest.objects.filter(end_time__lte=now, is_finished=False)
                        for contest in ended_contests:
                            contest.finish_contest()
                    except (OperationalError, ProgrammingError, ImproperlyConfigured):
                        pass  
                    time.sleep(60)

            threading.Thread(target=check_contests, daemon=True).start()
