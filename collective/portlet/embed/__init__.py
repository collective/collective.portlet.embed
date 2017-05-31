from Products.CMFCore.permissions import setDefaultRoles
from zope.i18nmessageid import MessageFactory
# See http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)

messageFactory = MessageFactory('collective.portlet.embed')

setDefaultRoles('collective.portlet.embed: Add embed portlet',
                ('Manager', 'Site Administrator', 'Owner',))
