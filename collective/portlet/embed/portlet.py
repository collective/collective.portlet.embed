from zope import component
from zope import schema
from zope import interface
from zope.formlib import form

from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.portlet.static import static

from plone.app.portlets.portlets import base

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.portlet.embed import messageFactory as _

class IEmbedPortlet(static.IStaticPortlet):
    """A portlet which renders predefined static HTML.

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    text = schema.Text(
        title=_(u"HTML Code to embed"),
        description=_(u"The html snippet you want to use. It can be iframe, javascript, html"),
        required=True)


class Assignment(static.Assignment):
    interface.implements(IEmbedPortlet)
    header = _(u"title_portlet", default=u"Embed portlet")

    text = u""
    omit_border = False

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
        """Generate a CSS class from the portlet header
        """
        header = self.data.header
        normalizer = component.getUtility(IIDNormalizer)
        return "portlet-embed-%s" % normalizer.normalize(header)

class AddForm(base.AddForm):
    """add form"""
    form_fields = form.Fields(IEmbedPortlet)
    label = _(u"title_add_portlet",
              default=u"Add embed portlet")
    description = _(u"description_portlet",
                    default=u"A portlet which can display embed HTML code.")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    """Portlet edit form.
    """
    form_fields = form.Fields(IEmbedPortlet)
    label = _(u"title_edit_portlet",
              default=u"Edit embed portlet")
    description = _(u"description_portlet",
                    default=u"A portlet which can display embed HTML code.")
