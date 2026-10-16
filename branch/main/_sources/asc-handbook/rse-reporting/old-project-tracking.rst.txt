OLD: Project management: RSE perspective
========================================

**OLD material - will be deleted once it is moved to other locations.**


Summary
-------


Procedures by project size
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * * Size
     * Priority
     * How to select
     * When starting
     * When finishing
   * * Garage
     * Top
     * Try to help everyone: help, redirect, or give advice to do themselves.
     * Ask who you are, unit, background.  Ensure you help them at the
       level they need.  Shadow other help sessions to learn new things.
     * Record in `garage diary <https://version.aalto.fi/gitlab/AaltoScienceIT/garagediary>`__ (with unit)
   * * Small
     * Third
     * When garage project needs extra time and you {have time & want} to
       do it.
     * Discuss expectations with customer.  Usually meetings are in
       garage times; record in garage diary for each visit.
     * (none, already in diary)
   * * Medium
     * Lowest (filler)
     * When we have time, in proportion to :doc:`unit priorities
       <rse/procedures/units-info>`.

       Confirm in weekly meeting before accepting.
     * Initial triage in garage.  Arrange a detailed planning meeting.
       Usually at least two RSE staff, at one experienced in the topic
       attend.  Invite the customer's supervisor if needed.  Use the
       `template doc
       <https://docs.google.com/document/d/1XcxeNLRq0kOsFbDEmA7ArdbIrCVudMWHPFQsKRVcTIk>`__.
       Make an issue in rse-projects issue tracker if it seems like a
       good project, even if we can't do it.  Await a decision in weekly
       RSE meeting before promising anything.  In the meeting, the
       responsible RSE is decided and they contact the customer.
     * rse-projects issue tracker updated
       (:doc:`../ref/project-done`).
   * * Large
     * Second (try to do all we can to get outside funding)
     * If there is not enough time for all requests, in proportion to :doc:`unit priorities <rse/procedures/units-info>`.
     * Same ^
     * Same ^

Procedures for tracked projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * * Stage
     * What it means
     * How to get here
     * Info stored in
   * * S0 Lead
     * You've learned someone has a vague idea
     * Whoever knows them best talks and explains the ideas of RSE
       stuff.  Give basic expectations.  Ask them if they want to
       proceed.
     * - If vague: nowhere, tell them to contact us again when ready.

       - If a concrete lead: make a rse-projects issue with state
	 "Lead".  Include description, estimated time, unit label, and
	 ``/summary`` at least.
       - If they want to proceed: (a) set up the planning meeting
	 yourself or (b) add to weekly meeting agenda to find someone
	 who will do the pre-planning meeting.
   * * Planning meeting
     * Discussed enough to understand what it is
     * Planning meeting with at least two RSEs (doesn't have to be
       those who got the lead, but it's good if someone who might do
       it is there + someone who can mentor that person).  Use the `template doc
       <https://docs.google.com/document/d/1XcxeNLRq0kOsFbDEmA7ArdbIrCVudMWHPFQsKRVcTIk>`__
       or similar.
     * Template doc + `rse-projects
       <https://version.aalto.fi/gitlab/AaltoRSE/rse-projects/>`__
       issue created
   * * S1/S2 Accepted (Waiting / Queued)
     * We've decided we can do the project.
     * Decision in weekly meeting based on pre-planning meeting info.
       Ensure we have time, ensure we have funding.  Look for
       unmanaged risks.  Final check for who has time to actually do
       the project.  Checklist:

       * Project can be defined
       * A RSE has skills, interest, and *time*
       * Team as whole has time and skills to support

     * Person(s) doing it contact the customer.
   * * S3 In progress
     * It's being worked on.
     * (someone starts working on it)
     * Halli if needed.  Update rse-projects issue periodically.  Keep
       good communication with the customer, for example in the same
       planning doc.
   * * S5 Reporting
     * Project is basically done but we are waiting for stats to add
       to rse-projects before forgetting about it.
     * (finish project)
     * rse-projects issue label
   * * S6 Done
     * Done, don't have to think about it anymore
     * Discuss with customer: what do they need to know from here?
       Add to weekly meeting agenda to discuss lessons leaned.
     * rse-projects issue fully updated with label, summary, time
       spent/saved, and other stats.
   * * S7 Maintenance
     * Project is done but it still occupies our minds since we may be
       asked to do maintenance in the future.
       Add to weekly meeting agenda to discuss lessons leaned.
     * (finish project)
     * rse-projects issue label
   * * S8 Cancelled
     * It was a good project, but we decided not to do it
     * Either we decide we don't have time, or customer decides it is
       no longer needed.
     * rse-projects issue label.




Finance time tracking
---------------------

Halli serves as our source of truth about funded projects.  For
projects with their own funding (external or internal funding), you
should get instructions about how to record it.  All other projects
(funded by the department's/school's basic funding) is marked in Halli
to the standard RSE salaries project (ask for it).



.. _rse-project-admin-types-of-projects:

Notes on special types of projects
----------------------------------

Special projects
~~~~~~~~~~~~~~~~

Examples: EU-funded projects

Special projects are their own distinct entity and are not mixed with
other work of our team.  They receive dedicated days for their work,
and are not given attention on other days.  Because these get
exclusive days, the master data of these projects is in Halli, and
because Halli can be used for records later, they are not recorded in
Gitlab. (Note: "special" does not mean better, it's usually more
productive to be available for researchers whenever they need us).

Special projects get one Gitlab issue to track the overall contact,
but it isn't updated on a day-to-day basis.

Daily procedures: A Gitlab issue is created for every project, with
funding source ``Funding::Project``.  At the end of every day, record
the working time in Halli.  As much as possible, these project days
should not be mixed with other work, but internal team meetings,
etc. are allowed if necessary.  In Halli, record each day's worktime
(scaled to the standard 7.25h/day) in proportion to the time spent on
the special project (allocated to that project)/internal work
(allocated to RSE-salaries).


Normal funded projects
~~~~~~~~~~~~~~~~~~~~~~

For projects providing their own funding, Halli is also used to track
the time spent on them, but you can work on them whenever the
customers request.

Daily procedures: A Gitlab issue is created for every project, with
funding source ``Funding::Project``.  Halli is marked to the
respective project and at least is correct by-month.


Internal charging projects
~~~~~~~~~~~~~~~~~~~~~~~~~~

"Internal changing" projects are funded, but are paid as a lump-sum
internal invoice and Halli is not used.  These projects are not very
common.  Gitlab is used to track time spent on these projects.

Daily procedures: Like above for Gitlab.  Halli is marked to the
standard RSE-salaries project.  ``Funding::Project``


Basic funding projects
~~~~~~~~~~~~~~~~~~~~~~

These projects are paid by our basic funding, provided by our
sponsoring units.  This also includes all of our internal work,
meetings, development, and teaching.

Daily procedures: Same as above.  Gitlab funding marked as
``Funding::Unit``


Gitlab day-to-day procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `the rse-timetracking repository
<https://github.com/AaltoRSE/rse-timetracking>`__ for info on how to use
Gitlab.  But the actual data is in **rse-projects**, a separate
private repository.
