Project reporting
=================

For anything big enough to be a "project", it should be in Gitlab with
basic information (labels describing customer and tasks), and then
approximate monthly time via the monthly time planning spreadsheet.

Halli is the official time record, but Halli projects do not necessarily
line up with practical projects (projects can pull from various
funding sources and Halli is not precise enough for a report).

.. admonition:: summary

   * If it passes the "project" threshold, make an issue in Gitlab.

   * At key stages (at least before committing), give a quick report
     in a RSE meeting so that others may be able to speak up if they
     know something you need to know.

   * Each month, make sure the rse-timetracking spreadsheet reflects
     what you actually did - more or less.  Every "project" should be
     here with a ``#NNN`` tag.

   * Keep the rse-timetracking spreadsheet up to date with committed
     time in the future..


When is something a "project" and not support?
----------------------------------------------

This is a good question and there is no fixed answer.

* Things generally indicating a "project"

  * Every major course.

  * Requires a 3 days or more on our part.

* Things generally indicating **not** a project

  * No value in listing it separately in reports to management (it
    looks trivial and dilutes the other good work we do)



``rse-projects`` Gitlab repository
----------------------------------

We have an internal repository ``rse-projects`` in the Aalto Gitlab.
This contains the metadata of all the projects.  **Everything that is
big enough to be a "project" should have a Gitlab issue.** This
provides a tracking number ``RSE#NNN`` which is the permanent
identifier and is automatically parsed for reports.


Create a new issue and use the issue template (``Default``).  Fill it
out well enough to give someone an idea what is happening.  Be
structured and add all relevant issue labels.


(You can read out-of-date details and semantics of the labels and
fields at https://github.com/AaltoRSE/rse-timetracking, but should
probably not read it until it is improved.)



``rse-timetracking`` spreadsheet
--------------------------------

This is the person × month spreadsheet used for long-term time
allocation.  The spreadsheet does not have to have anything classified
as "garage" or "support" in it.  That fits in spare unallocated time.
A person should not usually go above 80% full (to have time for these
other things).

What do the numbers mean?  Fraction of your actual time, so that (for
example) it is the percent value you would give for the Person-Months
in an EU or Halli report.

**For past months**, values should match up reasably closely with your
actual time distribution.  Every "project" worked on should be
included with a tag ``#NNN`` :inote:`This is motivation to not make
too many "projects" when not needed`.  Update the spreadsheet each
month when you make your Halli report :inote:`if you don't do Halli,
use the Halli reminders to remind you to do this`.

**For future months**, this should indicate your general expected
level of busyness, for time-planning purposes.  For example, you may
not know what project you will be working on, but know that 50% of
your time is booked for Institute X's support.  Record a "50" there.

Not everything in the spreadsheet has to be a project.  Things such as
"vacation", "RSE conference", "misc small AI consultations", etc. can
all be recorded.



Reporting by step
-----------------

* **Pre-discussion:** (there is no project yet, you are just talking
  to people about a future idea).  You don't need to do any reporting,
  but if this is a concrete idea (for example a grant has been
  submitted), you can make tracking issue with the state ``S:0-Lead``
  so we can track our upcoming work.

* **Idea meeting** (possibly with supervisor): Make the full Gitlab
  issue.  Give a report to the RSE weekly meeting and ask for any
  other feedback and a "go/no-go" decision.

* **Technical planning**: There is usually not that much to update,
  but one should make sure time estimates, etc. are approximately
  correct.  Give a report of the plan to the RSE weekly meeting and
  ask for any other feedback and a "go/no-go" decision.

* **Working on it**: Keep the ``rse-timetracking`` spreadsheet up to
  date month-by-month.  Important updates and news can go to the
  Gitlab issue, and use chat as needed.

* **Done**: Move the issue to state "done", update the summary and, if
  possible, ask how much time we saved the customer and report it with
  ``/timesaved``.  If it's mostly done but you are waiting for info
  from the customer, you can move it to start "reporting".

* **Maintenance**: Use this state if the main work is done, but it
  remains under our maintenance (we may be called to fix stuff for it
  later).  It is important we can say how much of this work we do.
  Don't forget to update maintenance time to the ``rse-timetracking``
  spreadsheet.



Example reports to management
-----------------------------

*This section shows what kind of reports we can make with the data, so
you can see the purposes of the reports - if you can see the output,
that may help with motivation to produce the data.  See*
:doc:`rse/reports/2025`.


.. figure:: https://github.com/AaltoSciComp/scicomp-docs/blob/master/rse/reports/2025-projects-schools.png?raw=true

   Showing the projects per school.  This shows funders where our time
   goes.  (Note it does not consider time spent per project).

See the full report for more figures.

TODO: add a report that extracts times from the spreadsheet and
metadata from Gitlab and makes a actual time report per-year.

Below is an example from the automatically-generated text report that
is sometimes requested.  It has the issue title, various metadata from
labels and ``/``-commands, and the ``/summary`` summary.

    Adding functionality to [some-software] (#nnn / ELEC)

    * Feb 202x
    * Contacts: user.name@example.com
    * Time saved / spent: 2w / 2w5d1h
    * Size: 2-M

    Researcher needed to access some information in [some software]
    that was not included in the Python API. We extended the API to
    provide the information and submitted a pull request to the
    original repository.
