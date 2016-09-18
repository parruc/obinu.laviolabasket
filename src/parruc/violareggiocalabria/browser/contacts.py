# -*- coding: utf-8 -*-
from parruc.violareggiocalabria import _
from parruc.violareggiocalabria.utils import send_mail
from plone.app.users.schema import checkEmailAddress
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from z3c.form import field
from z3c.form import form
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


recipients_voc = SimpleVocabulary(
    [SimpleTerm(value=u'info@violareggiocalabria.it',
                token=u'i',
                title=u'Contact'),
     SimpleTerm(value=u'marketing@violareggiocalabria.it',
                token=u'm',
                title=u'Marketing'), ])


class IContactForm(Interface):
    """ Form field definitions for Zoho contact forms """

    recipient = schema.Choice(
        title=_(u"Destinatario"),
        vocabulary=recipients_voc,
        required=True,)

    name = schema.TextLine(
        title=_(u"Nome"),
        # description=_(u"Il tuo nome e cognome"),
        required=True,)

    email = schema.TextLine(
        title=_(u"Email"),
        # description=_(u"Indirizzo email che useremo per contattattarti"),
        required=True,
        constraint=checkEmailAddress,)

    phone = schema.TextLine(
        title=_(u"Telefono"),
        # description=_(u"Il tuo numero di telefono o di cellulare"),
        default=u"",
        required=False,)

    text = schema.Text(
        title=_(u"Messaggio"),
        # description=_(u"Scrivi qui il testo del tuo messaggio"),
        required=True,)


class ContactForm(form.Form):
    fields = field.Fields(IContactForm)
    template = ViewPageTemplateFile("templates/contacts.pt")
    ignoreContext = True
    recipients_voc = recipients_voc

    def updateWidgets(self):
        super(ContactForm, self).updateWidgets()
        # self.widgets['recipient'].mode = interfaces.HIDDEN_MODE

    @button.buttonAndHandler(u'Invia il messaggio')
    def handleApply(self, action):
        data, errors = self.extractData()
        messages = IStatusMessage(self.request)
        if errors:
            return False
        try:
            source = "admin@violareggiocalabria.it"
            recipients = [recipients_voc.getTerm(data["recipient"]).value, ]
            subject = "[Sito Viola] Nuova mail da %(name)s" % data

            # Custom message with a name filled in
            message = u"""Hai ricevuto una mail di contatto dal sito violareggiocalabria.it:

            Dati del richiedente:
            Nome: %(name)s
            Email: %(email)s
            Telefono: %(phone)s
            Testo:

            %(text)s

            """ % (data)
            send_mail(source, recipients, subject, message)
            messages.add(u"""La tua email è stata inviata con successo.
                         Ti risponderemo prima possibile.""",
                         type=u"info")
        except:
            messages.add(u"""C'è stato un problema nell'invio della posta.
                         Riprova o contattaci telefonicamente.""",
                         type=u"error")
            return False


ContactFormView = ContactForm  # layout.wrap_form(ContactForm, index=index)
