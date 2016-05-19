# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s obinu.laviolabasket -t test_sponsor.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src obinu.laviolabasket.testing.OBINU_LAVIOLABASKET_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_sponsor.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Sponsor
  Given a logged-in site administrator
    and an add sponsor form
   When I type 'My Sponsor' into the title field
    and I submit the form
   Then a sponsor with the title 'My Sponsor' has been created

Scenario: As a site administrator I can view a Sponsor
  Given a logged-in site administrator
    and a sponsor 'My Sponsor'
   When I go to the sponsor view
   Then I can see the sponsor title 'My Sponsor'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add sponsor form
  Go To  ${PLONE_URL}/++add++Sponsor

a sponsor 'My Sponsor'
  Create content  type=Sponsor  id=my-sponsor  title=My Sponsor


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the sponsor view
  Go To  ${PLONE_URL}/my-sponsor
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a sponsor with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the sponsor title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
