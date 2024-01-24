from constant import AUTH_SVC_API_URL
import requests
import json


class AuthSvcAPI:
    _AUTH_URL = AUTH_SVC_API_URL

    def get_role_default_permission(self, token=None, role="Super Admin"):
        try:
            URL = f"{self._AUTH_URL}permissions/default?role={role}"

            if token:
                headers = {"Authorization": f"Bearer {token}"}
                response = requests.get(URL, headers=headers, data={})
                if response.status_code == 200:
                    role_permission = json.loads(response.text)
                    if role_permission["status"]:
                        return role_permission["data"]
                    else:
                        raise Exception("Something went wrong!")
                else:
                    raise Exception("Something went wrong!")
            else:
                raise Exception("Please pass access token")
        except Exception as e:
            print(
                self.__class__.__name__,
                ": Exception when fetching role's default permission",
                str(e),
            )
            raise e

    def create_user(self, email, first_name, last_name, role, permission, token=None):
        try:
            URL = f"{self._AUTH_URL}users"
            payload = {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "role": role,
                "permission": permission,
            }
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.post(URL, headers=headers, data=json.dumps(payload))
            response_text = json.loads(response.text)
            if response.status_code == 201:
                return response_text
            else:
                msg = response_text["data"]["message"] or "Something went wrong!"
                raise Exception(msg)
        except Exception as e:
            print(
                self.__class__.__name__,
                ": Exception when creating user",
                str(e),
            )
            raise e
