Project processes
=================

This page describes how projects work in general - what you should
consider when doing it.  For the minimum mandator reporting work, see :doc:`/asc-handbook/projects/tracking-reporting-gitlab`.


Why project management?
-----------------------

Our project management is designed to:

* Record where our time goes, so that we can get good reports for our
  funders, so that we will continue to be well-funded in the future.
* Show that our output work roughly corresponds to input funding (by
  unit, and goals of those units).
* Avoid projects which we may not be successful at due to {undefined
  goals, impossible goals, or generally not knowing what is going on}.
* Prevent over-committing ourselves.
* Provide sound financial tracking for projects that need it.


Prioritization
--------------

See the summary at the top (G/S/M/L projects)   In short,

* **Garage** projects get top priority since they connect us together
  and serve to share skills.
* Then we would do projects preferred by funders (projects with their
  own funding, those from units providing funding).
* Then fill with other things.



Typical project flow
--------------------

This is what should happen for anything bigger than a "small"
project.

Project lead
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is project ideas, which are not yet ready to plan or begin.

* Anyone may hear of a potential project at any time.  You can tell
  them about the RSE service, what will happen next, and see if they
  are interested.
* You shouldn't commit to anything.
* If it is only a broad idea, not concrete at all.

  * Tell them about RSE services and how it might be useful.
  * Tell them how to contact us once it's ready.

* If there is an actual project idea, but it's not ready to be planned
  yet.

  * (you can ask someone else to do this if you aren't the right
    person)
  * Ask them enough to understand if it's appropriate for us, what
    skills it needs, etc.
  * Set expectations with the customer.
  * Create an ``rse-projects`` issue with the description.  Include
    description/skills needed, and set at least the unit label, state
    ``S::0-lead``, and estimated time.
  * Tell them they need to contact us when they are ready.
  * This serves as a insight for future needs, but we don't actively
    work yet.

* If there is an actual project idea and it's ready to be planned.

  * Add it to the RSE weekly meeting agenda.
  * Begin the planning phase, or find someone else to do that.
  * If you need to find project planners and can't via chat/garage,
    add it to a RSE weekly meeting agenda.

* Cases where a ``rse-projects`` issue should be made:

  * You are very sure it will become a project (may as well get the
    project number to start tracking).
  * It's a serious request for a lot of resources.  It's useful to
    know what may be requested.
  * It's RSE services being written into a grant application.  It's
    good to know all of these cases for our reports.  RSE leader
    should usually be contacted for grant application stuff.


Project planning
~~~~~~~~~~~~~~~~

This meetings gets enough details so that we can make a decision to
begin.  It may happen right away (lead comes up in garage) or after
some delay (need to find the people to do the meetings).

* `Pre-planning meeting template doc
  <https://docs.google.com/document/d/1XcxeNLRq0kOsFbDEmA7ArdbIrCVudMWHPFQsKRVcTIk>`__
* The point is to get enough information (for the next step) to know
  if we should take on the project.
* Two RSEs (one of which should be experienced in projects) meet with
  the customers.  This is a good chance for an experienced person to
  mentor someone learning the topic.

  * The supervisor of the customers should be invited if it is
    relevant (it's funded, it needs their direction, etc.)

* Nothing is promised at this time, and planning doesn't have to go
  into technical details.  But it should be deep enough to know if
  there's a technical reason we can't take it on.
* Fill out the project template together with the customers (or
  whatever your system is).  Make a copy in some shared space, give
  everyone edit access, and start filling out.  *Write stuff down.*
* The purpose of this meeting is to set expectations

  * What is the actual need and desired outcome
  * What we actually can do and may have time to do
  * How hard the project will be
  * How much time it might take us
  * What the risks are (including risks that we just can't do what is
    needed, or it's not as useful as one would hope)
  * What each party needs to do
  * Who will manege it long-term
  * Funding

* At this point, there should be an issue made in
  rse-projects.

  * The readme in the `rse-timetracking repository
    <https://github.com/AaltoRSE/rse-timetracking>`__ describes how
    the rse-projects repository works
  * `rse-projects itself is private in Aalto GitLab
    <https://version.aalto.fi/gitlab/AaltoRSE/rse-projects/>`__.


Decision to begin
~~~~~~~~~~~~~~~~~

The project plan as above is brought to the RSE meeting for a go/no-go
decision.

* The project is presented at the meeting to decide if we can or can't
  do it.

  * Project has been defined
  * A RSE has skills, interest, and *time*
  * Team as whole has time and skills to support
  * What is the goal?
  * How do you plan on approaching it?
  * What help do you need?
  * What risks have you discussed?

* This isn't because RSEs need to ask permission, but to make sure we
  think of everything and provide a reasonable change to say "no"
  without it being someone's personal decision.

  * Key point: we don't want to over-commit
  * Others may have experience in the topic and have valuable advice
  * Others may know of other risks

* We will consider things such as:

  * Who has time to do the implementation (it doesn't have to be the
    same person who attended the planning meeting, but it's good if we
    look ahead and likely candidates attend the planning meeting).
  * Does the team overall have time?
  * Are there any risks which weren't discussed in the planning
    meeting?  How to handle them with the customer?
  * Do we think we can actually do it?
  * Funding (RSE leader may give advice on this)


Working on the project
~~~~~~~~~~~~~~~~~~~~~~

* This is mostly independent work.
* RSEs are expected to ask for help if it is needed.  Add an agenda
  item in the RSE weekly meeting if you can't get help in garage or
  you need a wider audience.
* If the project has funding, record time spent in Halli.
* Update the time estimate in rse-projects, if the expected time
  changes.
* TODO: add more here


Ending the project
~~~~~~~~~~~~~~~~~~

* Update the issue tracker.
* See the :doc:`/asc-handbook/ref/project-done` checklist.
* TODO: add more here
