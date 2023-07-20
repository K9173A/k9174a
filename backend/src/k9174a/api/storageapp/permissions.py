from typing import List

from rest_framework.permissions import BasePermission


class IsRole(BasePermission):

    def __init__(self, allowed_roles: List[str]) -> None:
        self.allowed_roles = allowed_roles

    def has_permission(self, request, view) -> bool:
        return (
            self.allowed_roles == ['*'] or
            request.user.role and request.user.role.name in self.allowed_roles
        )
