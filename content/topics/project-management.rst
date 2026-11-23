Project management
==================

This page gives some RSE-specific advice on project management.  It
doesn't replace learning about standard project management practices,
but is more targeted towards our usual projects.  As wil

**Being research does not mean that project management is easier.  It
means it's harder, since understanding the vision and defining the
scope must be woven together with understanding what is possible, each
feeding off the other one.** This is far harder than
`hardness(academic research) +hardness(normal projects)` and the
difficulty can sometimes increase unexpectedly.

.. seealso::

   * :doc:`project-process`: time-oriented project management guide.
   * :doc:`project-pitfalls`: what-goes-wrong oriented project
     management guide.
   * :doc:`/asc-handbook/rse-reporting/projects`: minimum mandatory
     reporting.

..
  What's a project?  A time-limited coordinated effort among different
  people?

  What's project management?  Keeping these people working efficiently
  together.


Why project management?
-----------------------

Think of any major enough human achievement :inote:`landing on the
moon is a classic one, but that's too chiché`.  I'm usually less
impressed with the technology of the achievement than the way so many
people were able to work together to get it done.  This is what
project management achieves.

If a project is completely clear and routine to everyone from the
start, collaboration can work without special management effort.  The
farther you are from that, the more special effort is needed - and the
more structured it will tend to need to be.  If it doesn't exist,
chaos will happen.

Almost anytime someone comes to us with (in their mind) a very
difficult project, it hasn't turned out to be that hard.  The actually
hard project seem easy but become hard because we aren't clear on what
to do, we can't communicate well, there is no long term plan, it
shifts over time, and so on.  This is what project management can help
with :inote:`[research] it's not making research any more predictable,
but lets us react to the unpredictability.`


..
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



Research vs real-life project management
----------------------------------------

TODO: any wisdom here?



Figuring out the scope
----------------------

Go slow in this phase.  Multiple sessions of building up understanding
is better than long emails with many questions.

There is a difference between the **statement of need** (what the
customer wants) and **scope of work** (what we will actually do).
Don't confuse them or ask the customer to decide the scope of work for
us (but also don't do it without their input).

You may need to iterate many "bad" ideas to get good ones.  This is
why you should propose (multiple) reasonable-ish courses of action for
discussion, and maybe it will improve from there.  For a well-known
field (for example civil engineering) the domain of "what can be done"
is relatively well known.  Not so for us.

And... how to figure out what to do?  Surely you didn't think this
short page can teach you that.  Finding out what to do is hard, there
are many buzzwords like "design thinking", "engineering thinking",
"radical creativity" :inote:`!!!` and more.  Realize it's a
combination of science and art meeting technology and business
:inote:`!!! (these are funny because they are Aalto University
slogans)`.



Planning
--------

TODO.

Perhaps covered by :doc:`project-process`.



Iteration
---------

We know about iteration from software development: agile, sprints,
scrum, and so on.  It's only natural to us, and this should still be
used.  But at the research level, iteration can also be **big phases
of research**, which is a research, not software development,
consideration.

.. admonition:: Example: data collection

   I was working on a data collection project, and the broad vision
   was to get mobile phone data from people in a hospital environment.
   The whole project was implemented as **phases**, where each phase
   provides some useful result, even without the other phases.

   * Investigate different Android apps and run them on my own phone.
     Give some useful figures to be included in presentations about
     the power of data.
   * Run it on several group member's phones as a test.
   * Run a student course and let the students use the tools.
     Students worked as researchers, understanding the data, with
     access only to their data, and their final report was about what
     the data told them.  This helped to guide future research.
   * Yet another student course.
   * Pilot with some people in a hospital.
   * Full study with some people in a hospital.

   The phases were not just useful for the technical development, but
   also helping the relevant ethics/legal staff to get used to our
   work before we got to more demanding things.  The project could not
   have been done skipping many of the middle steps, and overall it
   took years - yet each phase was designed to provide some benefit.
   This is kind of an extreme example, but it's representative of how
   to design things.  It requires engineering-application cooperation
   to figure this out.

Customers will often only have some end goal in mind, and often think
that requesting the end goal will work.  We need to tell them the
risks of going straight to the end goal, and then also help to come up
with the right phases that are *useful to them*.  This requires
knowing a lot about their work - maybe as far as shadowing them some.

This can also be simpler, for example "before we can plan turning your
software into a web server, we have to figure out your script.  We
will first do that before even planning out the web server part."

Creating the project phases is usually one of the hardest part of
planning.



The project brief
-----------------

When working on projects, we often need to describe the project to
others.  This can be summarizing the actions to the customer, or
summarizing the project to other internal people for their own
specific feedback (ethics, security, web dev, etc.) :inote:`For a
project to be successful, you need to be able to efficiently use the
knowledge of these experts, given their limited time.  Don't make them
dig to figure out what the story is`.  This quick summary is the
**project brief**.  By having one description (which is at a good
level of detail), we can more easily take advantage of all of our
skills.  (See also :doc:`communication`)

This is not the current status report.  This is somehow a summary of
the customer's needs, scope of work, expected challenges and what
happens for them.  It can be updated as the project develops, but
(again) isn't simply the current status.  Think of it this way: **If a
random RSE reads the project brief, are they able to tell if they have
any important information or skills they should offer to the
project?** :inote:`For example, "we have tried that before and it
wasn't a good idea", "I think this needs ethics review", etc.`



Present options to the customer
-------------------------------

It can be overwhelming to try to figure out the right path -
especially when there is no one perfect path.  It's hard to tell a
customer the whole range of possibilities and help them make a
meaningful decision (unless they are already very good at the topic).

To simplify, can you narrow things down into some representative
options, for example 3-4, and present these along with the trade-offs.
Then, you can use these to discuss the various trade-offs and they can
give meaningful guidance in what the right direction is.  Of course,
this may not immediately lead you to the plan, but can help you iterate
further.



The project manager
-------------------

TODO: many of our projects are too small to need a dedicated project
manager, but we need to take on this role anyway.  It should be made
clear who is currently waiting on who and who is in change of moving
things forward (my invented "prime mover" term).  There should also be
some outside person who can make sure things are going OK, even if
they are not heavily involved themselves.
