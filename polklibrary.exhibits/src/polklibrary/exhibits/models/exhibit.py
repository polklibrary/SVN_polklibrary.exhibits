from polklibrary.type.templater import MessageFactory as _
from plone import api
from plone.app.textfield import RichText
from plone.app.textfield.widget import RichTextWidget
from plone.autoform import directives as form
from plone.supermodel import model
from zope import schema
from zope.interface import directlyProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary


class IExhibit(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )

    description = schema.Text(
            title=u"Description",
            required=False,
        )
            
    js = schema.Text(
            title=u"Exhibit Javascript Plugin",
            description=u"You must include the &lt;script&gt; elements",
            required=False,
        )
         
    css = schema.Text(
            title=u"Exhibit CSS Plugin",
            description=u"You must include the &lt;style&gt; elements",
            required=False,
        )
        
    body = RichText(
            title=u"Exhibit Home Page",
            default_mime_type='text/structured',
            default=u"",
            required=False,
        )
          