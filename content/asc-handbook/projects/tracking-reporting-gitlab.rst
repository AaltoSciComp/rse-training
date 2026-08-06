Gitlab: project tracking and reporting
======================================

For anything big enough to be a "project", it should be in Gitlab with
basic information (labels describing customer and tasks), and then
approximate monthly time via the monthly time planning spreadsheet.

Halli is the official time record, but Halli projects do not necessarily
line up with practical projects (projects can pull from various
funding sources and Halli is not precise enough for a report).



When is something a "project" and not support?
----------------------------------------------

This is a good question and there is no fixed answer.

* Project: requires more than several days on our part.

* Project: has value in appearing separately on our reports by name
  (and you are willing to record the time spent each month in the
  ``rse-timetracking`` spreadsheet.

* Should be a project: major courses we teach.



Basic principles
----------------

* We have an internal repository ``rse-projects`` in the Aalto Gitlab.
  This contains the metadata of all the projects.

* Create a new issue that describes the project (see a section below).
  For the most part, create a new issue with the template, fill in the
  fields, and apply all relevant labels.

* **Everything that is big enough to be a "project" should have a
  Gitlab issue.** This provides a tracking number ``RSE#NNN`` which is
  the permanent identifier and is automatically parsed for reports.

* There is a Google Drive spreadsheet ``rse-timetracking`` which
  records the time *by month*.  We do not need to track our time by
  day.  Monthly tracking is enough.

  * For each thing that is big enough to be a project, make sure that
    the rough monthly time is set correctly.



Gitlab summary
--------------

There is an issue template (``Default``) that has a basic template to
fill out.  Fill it out well enough to give someone an idea what is
happening.  Be structured and add all relevant labels.

This contains:

* Name
* Summary
* Contacts and supervisor
* Unit
* Funding
* Labels to indicate what it covers...

You can read details of using Gitlab at
https://github.com/AaltoRSE/rse-timetracking (but that is too
detailed and I wouldn't recommend reading it).



``rse-timetracking`` spreadsheet
--------------------------------

This is the person x month spreadsheet rkdarst is using for long-term
planning.  Each month's cell should be accurate for what you did at
the end of each month.  Each project should be tagged with ``#NNN``
and a script will extract this to get the time distribution.

The spreadsheet does not have to have anything classified as "support"
in it.  That fits in spare unallocated time.  A person should not
usually go above 80% full (to have time for these other things).



Reporting by step
-----------------

* **Idea phase:** (there is no project yet, you are just talking to
  people).  You don't need to do any reporting, but if this is a
  concrete idea (for example a grant has been submitted), you can make
  tracking issue with the state ``S:0-Lead`` so we can track our
  upcoming work.

* **Kick-off** (possibly with supervisor): Make the full issue and
  update it.  Give a report to the RSE weekly meeting and ask for any
  other feedback and a "go/no-go" decision.

* **Technical planning**: There is usually not that much to update,
  but one should make sure time estimates, etc. are approximately
  correct.

* **Working on it**: Keep the ``rse-timetracking`` spreadsheet up to
  date month-by-month.

* **Done**: Move the issue to state "done", update the summary and, if
  possible, ask how much time we saved the customer and report it with
  ``/timesaved``.  If it's mostly done but you are waiting for info
  from the customer, you can move it to start "reporting"

* **Maintenance**: Use this state if the main work is done, but it
  remains under our maintenance (we may be called to fix stuff for it
  later).  It is important we can say how much of this work we do.
  Don't forget to update maintenance time to the ``rse-timetracking``
  spreadsheet.



Example report outputs
----------------------

*This section shows what kind of reports we can make with the data, so
you can see the purposes of the reports - if you can see the output,
that may help with motivation to produce the data.  See*
:doc:`rse/reports/2025`.


.. figure:: https://github.com/AaltoSciComp/scicomp-docs/blob/master/rse/reports/2025-projects-schools.png?raw=true

   Showing the projects per school.  This shows funders where our time
   goes.  (Note it does not consider time spent per project).

See the full report for more.
