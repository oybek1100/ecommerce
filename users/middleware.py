import time 


from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout

class InactiveUserLogoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user


        if user.is_authenticated and not user.is_active:
            last_seen = request.session.get('last_inactive_seen')
            now = int(time.time())

            if last_seen:
                elapsed = now - last_seen
                if elapsed > 3600:  
                    logout(request)
                    request.session.flush()
            else:
                request.session['last_inactive_seen'] = now