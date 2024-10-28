from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render  # , redirect
from django.views.generic import (DetailView, ListView)

from .constants import POSTS_ON_PAGE
from .models import Tour


class TourListView(ListView):
    model = Tour
    paginate_by = POSTS_ON_PAGE
    template_name = 'tours/index.html'

    def get_queryset(self):
        self.request.session['username'] = self.request.user.username or None
        queryset = Tour.published_objects.published().order_by('price')
        search_query = self.request.GET.get('q')
        self.request.session['search_query'] = search_query or None
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))
        return queryset


class TourDetailView(DetailView):
    model = Tour
    template_name = 'tours/tour_detail.html'


def profile_detail(request, username):
    profile = get_object_or_404(
        User, username=username
    )
    if request.user == profile:
        tours = profile.favorites.all()
    else:
        raise Http404
    page_obj = Paginator(tours, POSTS_ON_PAGE).get_page(
        request.GET.get('page')
    )
    context = {
        'profile': profile,
        'page_obj': page_obj
    }
    return render(request, 'tours/profile.html', context)
