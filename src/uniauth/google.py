from .unify import Handler, null

# Using OAuth 2.0 for Web Server Applications


class Google(Handler):
    id = "google"

    @classmethod
    def auth(
        cls,
        client_id=null,
        redirect_uri=null,
        scope=null,
        access_type=null,
        state=null,
        include_granted_scopes=null,
        login_hint=null,
        prompt=null,
        response_type=null,
    ):
        return cls.redirect(
            "https://accounts.google.com/o/oauth2/v2/auth",
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
            access_type=access_type,
            state=state,
            include_granted_scopes=include_granted_scopes,
            login_hint=login_hint,
            prompt=prompt,
            response_type=response_type,
        )
