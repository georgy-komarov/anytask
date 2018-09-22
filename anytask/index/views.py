from django.shortcuts import render_to_response
from django.template import RequestContext

from schools.models import School


def index(request):
    schools = School.objects.all().order_by('name')

    # current_year = get_current_year()
    # courses = Course.objects.filter(is_active=True).order_by('name')
    # archive_courses = Course.objects.exclude(is_active=True).order_by('year', 'name')

    context = {
        'schools': schools,
    }

    return render_to_response('index.html', context, context_instance=RequestContext(request))
