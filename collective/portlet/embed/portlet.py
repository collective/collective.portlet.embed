from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.portlet.embed import messageFactory as _
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.portlet.static import static
from z3c.form import field
from zope import component
from zope import interface
from zope import schema
try:
    from plone.app.portlets.browser import z3cformhelper as base
except ImportError:
    # Plone 5?
    from plone.app.portlets.portlets import base


class IEmbedPortlet(static.IStaticPortlet):
    """A portlet which renders predefined static HTML.

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    text = schema.Text(
        title=_(u"HTML Code to embed"),
        description=_(u"The html snippet you want to use. It can be iframe, "
                      u"javascript, html"),
        required=True)

    portlet_class = schema.TextLine(
        title=_(u"Portlet class"),
        required=False,
        description=_(u"CSS class to add to the portlet")
    )


class Assignment(static.Assignment):
    interface.implements(IEmbedPortlet)
    header = _(u"title_portlet", default=u"Embed portlet")

    text = u""
    omit_border = False
    portlet_class = ''

    def __init__(self, header=u"", text=u"", omit_border=False, footer=u"",
                 more_url='', portlet_class=''):
        self.header = header
        self.text = text
        self.omit_border = omit_border
        self.footer = footer
        self.more_url = more_url
        self.portlet_class = portlet_class


class Renderer(static.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('portlet.pt')

    def text(self):
        return self.data.text

    def css_class(self):
        """Generate a CSS class from the portlet header and class attributes
        """
        header = self.data.header
        normalizer = component.getUtility(IIDNormalizer)
        result_class = "portlet-embed-%s" % normalizer.normalize(header)
        if self.data.portlet_class:
            result_class += " %s" % self.data.portlet_class
        return result_class


class AddForm(base.AddForm):
    """add form"""
    schema = IEmbedPortlet
    fields = field.Fields(IEmbedPortlet)
    label = _(u"title_add_portlet",
              default=u"Add embed portlet")
    description = _(u"description_portlet",
                    default=u"A portlet which can display embed HTML code.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.
    """
    schema = IEmbedPortlet
    fields = field.Fields(IEmbedPortlet)
    label = _(u"title_edit_portlet",
              default=u"Edit embed portlet")
    description = _(u"description_portlet",
                    default=u"A portlet which can display embed HTML code.")
