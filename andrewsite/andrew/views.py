"""Views"""
#from django.shortcuts import render ppylint: disable=unused-import
from django.views import generic

class IndexView(generic.ListView): #pylint:  disable=too-many-ancestors
    """Index view"""
    template_name = 'andrew/index.html'
    queryset = None


class DetailView(generic.DetailView): #pylint:  disable=too-many-ancestors
    """Detail view"""
    template_name = 'andrew/detail.html'
    queryset = None
