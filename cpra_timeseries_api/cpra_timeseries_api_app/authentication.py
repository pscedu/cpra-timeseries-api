from rest_framework import authentication


class URLTokenAuthentication(authentication.TokenAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")

        if auth_header is None:
            # Check for the url param
            params = request.query_params
            token = params.get('token', None)
        else:
            return super(request)

        return self.authenticate_credentials(token)
