Project processes
=================

This page describes in general what to consider when working on
projects.  It is probably not that specific to Aalto RSE, and probably
needs adjustment to any individual project.  Still, it is useful to
have one place with good practices and a description of all the way
that things can go wrong.

.. seealso::

  * For the minimum mandatory reporting work, see
    :doc:`/asc-handbook/rse-reporting/projects`.
  * For the user-focused view, see :doc:`rse/project-lifecycle`
  * For an old version of this page that should be copied here, see
    :doc:`project-process-old`.

Terminology:

Project
   Anything large enough to need tracking and structure.  Has an issue
   in RSE project tracker. Rule of thumb for the size is anything that requires
   more than a couple of hours of work.

Garage support
   Any small things we do that don't require extensive
   tracking on our side.  Something where we mainly answer requests
   and is pushed forward by the customer coming to talk to us.  May or
   may not actually come through garage.

Project (informal)
   Confusingly, can sometimes mean both "project" and "garage
   support".



Why project management?
-----------------------

If a project is completely clear to everyone from the start,
collaboration without special management effort can work.  The farther
things come from "routine", the more is needed - and the more
structured it will tend to need to be.  If it doesn't exist, beware of
chaos.

* Make sure that we and our customers have the same goals.
* Define clear goals, objectives, deliverables, and deadlines.
* Keep track of things long-term.
* Record where our time goes, so that we can get good reports for our
  funders, so that we will continue to be well-funded in the future.
* Avoid projects which we may not be successful at due to {undefined
  goals, impossible goals, or generally not knowing what is going on}.
* Prevent over-committing ourselves.
* Show that our output work roughly corresponds to input funding (by
  unit, and goals of those units).
* Provide sound financial tracking for projects that need it.


Summary
-------

.. admonition:: Summary

   * There is a funnel from everyone we talk to, to those who actively
     talk about a project, to those doing a project.  Help people down
     that funnel by the actions on this page.
   * Research is *not* like typical consulting projects in that the
     outcome (or even achievable) is not as likely to be well-known
     in advance.
   * Our customers tend to have less experience doing projects and
     working with us, so we need to take more care to manage them and
     help them through their work


Outreach
--------

.. admonition:: Summary

   * Tell customers about what we do and help them understand how we
     can help.  Check :doc:`/asc-handbook/ref/outreach-material` for
     ideas.
   * You can give basic ideas, brainstorm, and think of ideas even
     before there is a "project".  Remember it may be difficult for
     them to understand what we can do.
   * Invite them to talk with us for more, but also...
   * Take their contact info and follow up with them if appropriate
     :inote:`for example after a few weeks so they can think about it
     some - maybe even asking someone else who has different knowledge
     to do come with you or do it`.

We are often out talking to researchers to tell them about what we do.
This is just the first introduction, so there is not yet a concrete
project or anything to do, but if someone may have something, one
should try to work on developing the idea.

You should:

* Talk and bounce initial ideas off of them.

(depending on the circumstances,) Make a note of their contact info,
and either you or someone else follow up.  In the follow up you could:

* Ask how things are going
* Ask if they would like to meet to talk further (could be as simple
  as lunch or chatting in the coffee room)

Unless we are fully booked, try not to leave good potential customer
with only a "come to garage" - yes, leave them with that, but also do
some follow-up.



..
  The idea/concept meeting is the initial discussion where the project idea
  is discussed. First point of contact is not necessarily the
  project manager, but rather anyone who can provide initial guidance and context
  on what we do and how we operate.

  Having this initial discussion in garage is recommended. However the main purpose here
  is to gather initial information on the project, understand the context, and present
  what RSEs can offer.

  The main goals of this meeting are to:

  * Understand the problem or opportunity.
  * Learn more about the customer, and their research.
  * Getting contact information to follow-up on the project.

  These points could be noted in RSE project tracker as a draft for future reference.

  This first point of contact helps establish the initial understanding of a potential project
  and sets the stage for further planning and discussions. Discussing the main point in
  RSE weekly meeting is a great way to keep the team informed.



Kick-off meeting (scope)
------------------------

.. admonition:: Summary

   * Get all information needed to make the plan.
   * Make sure everyone is on the same page (even those not taking
     part in detailed planning or expectation)
   * **Figure out the initial desired scope**, even if it will be
     adjusted later.
   * In the common case where the long-term plan can not be know, plan
     for iterations.

The kick-off meeting is the first real project step (though, it's not
guaranteed to become a project from here).  This is the time to
determine the overall viability of a project or not by understanding
what is needed.  Make sure the customer's supervisor is on board, if
relevant :inote:`Not relevant for small, "phd-projects".  More
relevant when it is large, purpose is less clear, many people are
involved, or it requires funding`. In all but the simplest cases, it
is recommended to have the team leader or a senior RSE involved in
this meeting as well.

One main goal of this meeting is to figure out the scope, as in, what
is desired to be included or not.  The customers usually has some
vision of their needs, not necessarily the way of getting there or
what exactly should be included.  So, one needs to work with them to
figure out some initial ideas and what the scope *could* be.

The main goals are to:

* Get all the information you need early (no surprises later)
* Introduce the project team and stakeholders.
* Understand the project objectives, scope, and deliverables.
* Discuss roles, responsibilities, and expectations.
* Establish communication channels and reporting mechanisms.
* Confirm the project timeline and key milestones.

This meeting ensures that everyone is aligned and ready to begin the project work.



Technical planning
------------------

.. admonition:: Summary

   * Take the time to go from the needs and general plan identified
     above to a specific, implantable plan.
   * This may require more help than just the RSEs in the previous
     meeting.
   * This stage can be iterative and customers should be a part of it
     as much as needed.
   * Ensure an OK from everyone before going on.

The technical planning phase involves detailed planning of the technical aspects
of the project.  This may, or may not, be at the same time as the
kick-off (or it may start there and carry on later).

The main goals are to:

* Define the technical requirements and specifications.
* Identify potential risks and mitigation strategies.
* Plan the technical tasks and allocate resources.
* Establish development and testing procedures.

Without a good plan, work can become disorganized. Taking the time to plan thoroughly
is crucial for the success of the project. Consulting with team members and
stakeholders is important to ensure that all perspectives are considered.
Taking the time to discuss the plan with the customer and team leader helps
ensure that the plan is realistic and aligned with expectations.

This phase ensures that the project has a clear technical roadmap and
that potential issues are addressed early. Listing the technical tasks and
technologies and their dependencies helps in tracking progress and managing
resources effectively.

Each project will have two RSEs assigned to it, responsible for different aspects
of the technical work. The work distribution is not necessarily equal and should
be based on expertise and project needs.


Communication and work during the project
-----------------------------------------

.. admonition:: Summary

   * Being research, the end goal was uncertain at the start and
     likely is changing over time.
   * You must keep the customers will-informed and part of the loop.
   * If customers ever disappear, ask advice rather than continue
     working on the wrong thing.

Effective communication and collaboration are crucial throughout the project.
Using customer's preferred communication channel is highly recommended; as the primary
stakeholders should be kept happy and informed through regular updates.
Regular meetings are also recommended, and using status reports and collaborative
tools are essential to achieve these goals.

To make sure you get help when needed, and identify issues in early stages, it is important
to discuss the project with your team and team leader too.

The main goals are to:

* Keep all stakeholders informed of progress and changes.
* Facilitate collaboration among team members.
* Address issues and risks promptly.
* Ensure that project documentation is up-to-date.

Regular meetings, status reports, and collaborative tools help maintain alignment
and transparency during the project.


Wrap-up
-------

.. admonition:: Summary

   * Being research, projects have a way of going on forever.  Try to
     have some end of your active phase (may need to be planned in
     advance).
   * Take the time to get some reflect and get statistics.
   * It doesn't mean you stop all communication.

The wrap-up phase occurs at the end of the project.

The main goals are to:

* Review project outcomes and deliverables.
* Assess project performance against objectives.
* Document lessons learned and best practices.
* Report time and resource usage, and ask about /timesaved for the project.

This phase ensures that the project is formally closed and that valuable insights
are captured for future projects.


Maintenance and support
-----------------------

.. admonition:: Summary

   * Research goes on and projects blend in to each other.  You do not
     have to completely stop support at the end.
   * If ongoing maintenance is likely, discuss it from the start.
   * Avoid doing a project where the customers are not able to manage
     anything without you (unless that's the explicit goal) :inote:`In
     other words, don't create something so complex that only you or
     an expert RSE can understand it.  Make it suitable to the users.`

The maintenance and support phase occurs after the project has been completed and delivered.

The main goals are to:

* Address any issues or bugs that arise post-deployment.
* Provide ongoing support to users and stakeholders.
* Implement updates and improvements as needed.
* Ensure the continued performance and reliability of the project.

This phase ensures that the project remains functional and valuable over time,
and that any emerging needs are addressed.


Dropped projects
----------------

Sometimes, projects may be discontinued or paused before completion.
As we are working with researchers, their focus may shift to another project
or area of research, leading to the discontinuation or pausing of the current project.
If the project is discontinued or paused, it is important to properly document
the reasons and any work completed:

* Document any work completed and lessons learned.
* Reallocate resources to other projects as needed.
* Communicate the decision to all stakeholders and team leader

This phase ensures that even discontinued projects are properly closed and
that valuable insights are captured for future initiatives.
