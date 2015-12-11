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

default_js = """
$(document).ready(function(){

    // Add javascript here
    
});
"""

default_css = """
/* To suppress elements blocks, uncomment them below ======================== */
/* #header { display: none ; } */
/* #breadcrumbs { display: none ; } */
/* #content { display: none ; } */


/* Default Styles Below ===================================================== */

body {
    font-family: "Roboto","Helvetica Neue",Helvetica,Arial,sans-serif;
    font-size: 16px;
}

a {
    color: #6CAED8;
}

#header {
    background-color: black;
    background-position: middle left;
    padding: 40px;
}

#banner {
    height: 15px;
}

#title {
    color: white;
    font-size: 32px;
    font-weight: bold;
}

#breadcrumbs {
    background-color: #999999;
    padding: 5px 15px 8px;
}
#breadcrumbs a {
    color: white;
    vertical-align: bottom;
}
#breadcrumbs span {
    color: #bbbbbb;
    vertical-align: bottom;
}

"""



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
            default_mime_type='text/plain',
            output_mime_type='text/plain',
            required=False,
            default=unicode(default_js),
        )
         
    css = schema.Text(
            title=u"Exhibit CSS Plugin",
            description=u"You must include the &lt;style&gt; elements",
            default_mime_type='text/plain',
            output_mime_type='text/plain',
            required=False,
            default=unicode(default_css),
        )
        
    body = RichText(
            title=u"Exhibit Home Page",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )
          