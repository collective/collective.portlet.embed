#!/bin/sh
PRODUCTNAME='collective.portlet.embed'
I18NDOMAIN=$PRODUCTNAME

# Synchronise the .pot with the templates.
i18ndude rebuild-pot --pot locales/${PRODUCTNAME}.pot --create ${I18NDOMAIN} .
i18ndude merge --pot locales/${I18NDOMAIN}.pot --merge locales/${I18NDOMAIN}-manual.pot

# Synchronise the resulting .pot with the .po files
i18ndude sync --pot locales/${PRODUCTNAME}.pot locales/*/LC_MESSAGES/${PRODUCTNAME}.po