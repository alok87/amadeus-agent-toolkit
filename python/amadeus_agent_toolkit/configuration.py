from typing import Literal, Optional
from typing_extensions import TypedDict

# Object defined
Object = Literal[
    "searchFlights",
    "searchHotels",
    "getHotels",
]

# Permission type defined
class Permission(TypedDict, total=False):
    create: Optional[bool]
    update: Optional[bool]
    read: Optional[bool]

# BalancePermission type defined
class BalancePermission(TypedDict, total=False):
    read: Optional[bool]

# Actions defined
class Actions(TypedDict, total=False):
    payment_links: Optional[Permission]

# Context defined
class Context(TypedDict, total=False):
    account: Optional[str]

# Configuration defined
class Configuration(TypedDict, total=False):
    actions: Optional[Actions]
    context: Optional[Context]


def is_tool_allowed(tool, configuration):
    for resource, permissions in tool.get("actions").items():
        if resource not in configuration.get("actions", {}):
            return False
        for permission in permissions:
            if (
                not configuration["actions"]
                .get(resource, {})
                .get(permission, False)
            ):
                return False
    return True
