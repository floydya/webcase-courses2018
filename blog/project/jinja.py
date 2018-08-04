from jinja2.environment import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.contrib.humanize.templatetags import humanize


class JinjaEnvironment(Environment):
    """
    Инициализация среды Jinja, определение кастомных фильтров, фун-ий
    """
    def __init__(self, **kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.globals['static'] = staticfiles_storage.url
        self.globals['url'] = reverse
        self.filters['naturaltime'] = humanize.naturaltime
        self.filters['naturalday'] = humanize.naturalday
