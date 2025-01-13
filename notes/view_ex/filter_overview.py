from ..forms import OverviewFilter
from ..models import Note
from django.db.models import Q

def filter_overview(request):
    form = OverviewFilter(request.POST)
    if form.is_valid():
        author = form.cleaned_data.get("author")
        category = form.cleaned_data.get("category")
        search = form.cleaned_data.get("search")
        time_period = form.cleaned_data.get("time_period")
    
    queryset = Note.objects.all()


    if author:
        queryset = queryset.filter(author__username=author)
    if category:
        queryset = queryset.filter(category__name=category)
    if search:
        search_terms = search.split()
        search_queries = Q()
        for term in search_terms:
            search_queries |= Q(note__icontains=term) | Q(title__icontains=term)
        queryset = queryset.filter(search_queries)

    limit = 30


    return queryset[:limit]