from . import generic

__all__ = [
    "IndexView",
]


class IndexView(generic.TemplateView):
    """
    View rendering the site's index page.
    """

    template_name = "anion/index.html"
