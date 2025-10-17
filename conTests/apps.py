from django.apps import AppConfig

class ContestConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'conTests'

        def ready(self):
            import threading
            import time
            from django.utils import timezone

            def check_contests():
                from .models import Contest  
                from django.db.utils import OperationalError
                from django.core.exceptions import ImproperlyConfigured

                while True:
                    try:
                        now = timezone.now()
                        ended_contests = Contest.objects.filter(end_time__lte=now)
                        for contest in ended_contests:
                            for participant in contest.contestparticipant_set.all():
                                participant.update_scores()
                            contest.update_ratings()
                    except (OperationalError, ImproperlyConfigured):
                        pass

                    time.sleep(60)

            threading.Thread(target=check_contests, daemon=True).start()
