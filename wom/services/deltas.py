# wom.py - An asynchronous wrapper for the Wise Old Man API.
# Copyright (c) 2023-present Jonxslays
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

import typing as t

from wom import enums
from wom import models
from wom import result
from wom import routes

from . import BaseService

__all__ = ("DeltaService",)

ValueT = t.TypeVar("ValueT")
ResultT = result.Result[ValueT, models.HttpErrorResponse]


class DeltaService(BaseService):
    """Handles endpoints related to deltas."""

    __slots__ = ()

    async def get_global_delta_leaderboards(
        self,
        metric: enums.Metric,
        period: enums.Period,
        *,
        player_type: models.PlayerType | None = None,
        player_build: models.PlayerBuild | None = None,
        country: models.Country | None = None,
    ) -> ResultT[list[models.DeltaLeaderboardEntry]]:
        params = self._generate_map(
            metric=metric.value,
            period=period.value,
            playerType=player_type.value if player_type else None,
            playerBuild=player_build.value if player_build else None,
            country=country.value if country else None,
        )

        route = routes.GLOBAL_DELTA_LEADERS.compile().with_params(params)
        data = await self._http.fetch(route, self._list)

        if isinstance(data, models.HttpErrorResponse):
            return result.Err(data)

        return result.Ok([self._serializer.deserialize_delta_leaderboard_entry(d) for d in data])
