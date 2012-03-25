from zope.publisher.browser import BrowserView


class datepickerconfig(BrowserView):

    calendar_type = 'gregorian'

    def __call__(self):
        language = getattr(self.request, 'LANGUAGE', 'en')
        calendar = self.request.locale.dates.calendars[self.calendar_type]

        template = """
jQuery.tools.dateinput.localize("%(language)s", {
    months: "%(monthnames)s",
    shortMonths: "%(shortmonths)s",
    days: "%(days)s",
    shortDays: "%(shortdays)s"
});

jQuery.tools.dateinput.conf.lang = "%(language)s";
jQuery.tools.dateinput.conf.format = "mm/dd/yyyy";
        """
        return template % (dict(language=language,
                                monthnames=','.join(calendar.getMonthNames()),
                                shortmonths=','.join(calendar.getMonthAbbreviations()),
                                days=','.join(calendar.getDayNames()),
                                shortdays=','.join(calendar.getDayAbbreviations()),
                                format=format
                                ))

class WidgetTraverse(BrowserView):

    @property
    def macros(self):
        return self.index.macros
