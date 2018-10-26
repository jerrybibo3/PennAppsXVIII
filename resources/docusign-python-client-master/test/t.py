from __future__ import absolute_import, print_function
from pprint import pprint
import unittest
import webbrowser
import json
import time

import docusign_esign as docusign
from docusign_esign import AuthenticationApi, TemplatesApi, EnvelopesApi
from docusign_esign.rest import ApiException
from ast import literal_eval

user_name = "anubhav@suri.org"
integrator_key = "1c7b9e81-3622-40ea-be67-bf016e49bafa"
base_url = "https://demo.docusign.net/restapi"
oauth_base_url = "account-d.docusign.com" # use account.docusign.com for Live/Production
redirect_uri = "https://www.docusign.com/api"
private_key_filename = "keys/docusign_private_key.txt"
user_id = "a8519415-24c0-4180-9feb-3b241e8865a0"
template_id = "6ca4414e-28e0-4203-9df9-8303b3e89877"

api_client = docusign.ApiClient(base_url)

# IMPORTANT NOTE:
# the first time you ask for a JWT access token, you should grant access by making the following call
# get DocuSign OAuth authorization url:
oauth_login_url = api_client.get_jwt_uri(integrator_key, redirect_uri, oauth_base_url)

# open DocuSign OAuth authorization url in the browser, login and grant access
# webbrowser.open_new_tab(oauth_login_url)
print(oauth_login_url)

# END OF NOTE

def send(inp=''):
    # configure the ApiClient to asynchronously get an access token and store it
    api_client.configure_jwt_authorization_flow(private_key_filename, oauth_base_url, integrator_key, user_id, 3600)

    docusign.configuration.api_client = api_client

    template_role_name = 'signer1'

    # create an envelope to be signed
    envelope_definition = docusign.EnvelopeDefinition()
    envelope_definition.email_subject = inp + 'Save yourself.'
    envelope_definition.email_blurb = 'ti ngis tnod'

    # assign template information including ID and role(s)
    envelope_definition.template_id = template_id

    # create a template role with a valid template_id and role_name and assign signer info
    t_role = docusign.TemplateRole()
    t_role.role_name = template_role_name
    t_role.name ='Bad Hacker'
    t_role.email = user_name

    # create a list of template roles and add our newly created role
    # assign template role(s) to the envelope
    envelope_definition.template_roles = [t_role]

    # send the envelope by setting |status| to "sent". To save as a draft set to "created"
    envelope_definition.status = 'sent'

    auth_api = AuthenticationApi()
    envelopes_api = EnvelopesApi()

    try:
        login_info = auth_api.login(api_password='true', include_account_id_guid='true')
        assert login_info is not None
        assert len(login_info.login_accounts) > 0
        login_accounts = login_info.login_accounts
        assert login_accounts[0].account_id is not None

        base_url, _ = login_accounts[0].base_url.split('/v2')
        api_client.host = base_url
        docusign.configuration.api_client = api_client

        envelope_summary = envelopes_api.create_envelope(login_accounts[0].account_id, envelope_definition=envelope_definition)
        assert envelope_summary is not None
        assert envelope_summary.envelope_id is not None
        assert envelope_summary.status == 'sent'

        print("EnvelopeSummary: ", end="")
        print(str(envelope_summary))
        eID = literal_eval(str(envelope_summary))['envelope_id']
        
    except ApiException as e:
        print("\nException when calling DocuSign API: %s" % e)
        assert e is None # make the test case fail in case of an API exception

    return login_accounts[0].account_id, eID

def status(aID, eID):
    envelopes_api = EnvelopesApi()
    stat = literal_eval(str(envelopes_api.get_envelope(aID, eID)))['status']
    return stat

aID, eID = send('4836 - ')
print(status(aID, eID))
for x in range (30, 0, -1):
    print(x)
    time.sleep(.95)
print(status(aID, eID))
