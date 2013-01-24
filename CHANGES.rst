Changelog
=========

1.0.7 (2013-01-24)
------------------

- Bugfix: Handle vocabularies with integers as values,
  see http://dev.plone.org/ticket/13421 [frapell]


1.0.6 (2012-10-11)
------------------

- Fixed link path reference of querywidget.js for the qunit tests
  [ichimdav]

- Improved multiselection widget readability by sorting its returned values 
  [ichimdav]

- Fixed overly long selection lists by displaying scrollbars for multiselection 
  widgets
  [ichimdav]

- Fixed conditional initialization of querywidget,
  see http://dev.plone.org/ticket/12529 [kroman0]


1.0.5 (2012-09-08)
------------------

- fixed http://dev.plone.org/ticket/13144 raw get returns persistent 
  querystring on .get(context, raw=True)
  [jensens]


1.0.4 (2012-08-14)
------------------

- Added initially missing RelativePathWidget widget macro
  [petschki]

- call the "@@querybuilder_html_results" view on collection context
  [petschki]

1.0.3 (2012-06-29)
------------------

- Get date field values from the widget instead of the field, as the field isn't
  yet updated at this point in the event call.
  [esteele]

- Properly handle finding/removing multiselection widgets, which are nested in
  dls.
  See http://dev.plone.org/ticket/12964
  [esteele]


1.0.2 (2012-04-15)
------------------

- Accept an optional 'brains' parameter for the field's get method which
  says to return normal catalog results instead of an IContentListing.
  [davisagli]

- Show currently-selected sort index.
  [esteele]

- Move querywidget widgets into browser views so we're not redefining the
  same template code in 3 places.
  [esteele]

- Add a relative date widget.
  [esteele]

- Fix errors in widget's dict access in edit template.
  [esteele]

- Render the "Remove line" via a view instead of creating it in javascript,
  so that we can localize it.
  Refs http://dev.plone.org/ticket/12377
  [esteele]


1.0.1 (2011-08-25)
------------------

- I18n fixes.
  [vincentfretin]


1.0 - 2011-07-19
----------------

- Initial release.

- Add MANIFEST.in.
  [WouterVH]
