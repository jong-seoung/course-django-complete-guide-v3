import datetime
import json
from urllib.request import urlopen
from django.conf import settings

from django.db.models import QuerySet, Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView, 
    ListView, 
    YearArchiveView,
    MonthArchiveView, 
    DayArchiveView, 
    TodayArchiveView, 
    WeekArchiveView,
    ArchiveIndexView
    )

from hottrack.models import Song


def index(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("query", "").strip()

    song_qs: QuerySet[Song] = Song.objects.all()

    # melon_chart_url = "https://raw.githubusercontent.com/pyhub-kr/dump-data/main/melon/melon-20230910.json"
    # json_string = urlopen(melon_chart_url).read().decode("utf-8")
    # # 외부 필드명을 그대로 쓰기보다, 내부적으로 사용하는 필드명으로 변경하고, 필요한 메서드를 추가합니다.
    # song_list = [Song.from_dict(song_dict) for song_dict in json.loads(json_string)]

    if query:
        song_qs = song_qs.filter(
            Q(name__icontains=query)
            | Q(artist_name__icontains=query)
            | Q(album_name__icontains=query)
        )
        # song_list = [
        #     song
        #     for song in song_list
        #     if query in song.name
        #     or query in song.artist_name
        #     or query in song.album_name
        # ]

    return render(
        request=request,
        template_name="hottrack/index.html",
        context={
            "song_list": song_qs,
            "query": query,
        },
    )

class SongDetailView(DetailView):
    model = Song

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        melon_uid = self.kwargs.get("melon_uid")
        if melon_uid:
            return get_object_or_404(queryset, melon_uid=melon_uid)

        return super().get_object(queryset)


song_detail = SongDetailView.as_view()

class SongYearArchiveView(YearArchiveView):
    model = Song
    date_field = "release_date"  # 조회할 날짜 필드
    make_object_list = True

class SongMonthArchiveView(MonthArchiveView):
    model = Song
    # paginate_by = None
    date_field = "release_date"
    # 날짜 포맷 : "%m" (숫자, ex: "01", "1" 등), "%b" (디폴트, 월 이름의 약어, ex: "Jan", "Feb" 등)
    month_format = "%m"

class SongDayArchiveView(DayArchiveView):
    model = Song
    date_field = "release_date"
    month_format = "%m"


class SongTodayArchiveView(TodayArchiveView):
    model = Song
    date_field = "release_date"

    if settings.DEBUG:

        def get_dated_items(self):
            """지정 날짜의 데이터를 조회"""
            fake_today = self.request.GET.get("fake-today", "")
            try:
                year, month, day = map(int, fake_today.split("-", 3))
                return self._get_dated_items(datetime.date(year, month, day))
            except ValueError:
                # fake_today 파라미터가 없거나 날짜 형식이 잘못되었을 경우
                return super().get_dated_items()

class SongWeekArchiveView(WeekArchiveView):
    model = Song
    date_field = "release_date"
    # date_list_period = "week"
    # 템플릿 필터 date의 "W" 포맷은 ISO 8601에 따라 한 주의 시작을 월요일로 간주합니다.
    #  - 템플릿 단에서 한 주의 시작을 일요일로 할려면 커스텀 템플릿 태그 구현이 필요합니다.
    week_format = "%W"  # "%U" (디폴트, 한 주의 시작을 일요일), %W (한 주의 시작을 월요일)

class SongArchiveIndexView(ArchiveIndexView):
    model = Song
    # queryset = Song.objects.all()
    date_field = "release_date"  # 기준 날짜 필드
    paginate_by = 10  # 페이지 당 출력할 객체 수

    # date_list_period = "year"  # 단위 : year (디폴트), month, day, week
    def get_date_list_period(self):
        # URL Captured Value에 date_list_period가 없으면, date_list_period 속성을 활용합니다.
        return self.kwargs.get("date_list_period", self.date_list_period)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["date_list_period"] = self.get_date_list_period()
        return context_data