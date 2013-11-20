from plone.app.testing import (
    PloneWithPackageLayer,
    IntegrationTesting,
    FunctionalTesting,
)
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.testing import z2
import collective.portlet.embed


FIXTURE = PloneWithPackageLayer(
    zcml_filename="configure.zcml",
    zcml_package=collective.portlet.embed,
    additional_z2_products=[],
    gs_profile_id='collective.portlet.embed:default',
    name="collective.portlet.embed:FIXTURE"
)

INTEGRATION = IntegrationTesting(
    bases=(FIXTURE,),
    name="collective.portlet.embed:Integration"
)

FUNCTIONAL = FunctionalTesting(
    bases=(FIXTURE,),
    name="collective.portlet.embed:Functional"
)

ROBOT = FunctionalTesting(
    bases=(AUTOLOGIN_LIBRARY_FIXTURE, FIXTURE, z2.ZSERVER),
    name="collective.portlet.embed:Robot"
)
