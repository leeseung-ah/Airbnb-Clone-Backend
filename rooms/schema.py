import strawberry
import typing
from . import types
from . import queries
from common.permissions import OnlyLOggedIn


@strawberry.type
class Query:
    all_rooms: typing.List[types.RoomType] = strawberry.field(
        resolver=queries.get_all_rooms,
        permission_classes=[OnlyLOggedIn],
    )

    room: typing.Optional[types.RoomType] = strawberry.field(
        resolver=queries.get_room,
    )
