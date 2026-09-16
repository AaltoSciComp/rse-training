Project planner
===============

Summary
-------

The "project planner" may be better called a project mentor, or
architect, or something like that.  (If you have a better name, let me
know).  This role takes a new project request from a customer,
figures out what they actually need, and makes the plan for how to do
it.  If the task is very clear, one could go straight to doing it
(:doc:`project-work`), but many times we are the computing expert,
not the customers.  In these cases, we need to work with the customer
(domain expert) to figure out what is needed.

The "project planner" is distinct from :doc:`project-work` since you
may hand off the main work to someone else to actually do, possibly
serving as their :doc:`technical-mentor` during the project.  In
short, figuring out what to do is usually harder than doing it (at
least it's a different skill).  That's why we have multiple people
involved.


Main challenges/pitfalls
------------------------

* Customers may not know what they need (and maybe not even what to
  ask for).  If we do exactly what they ask, we may do the wrong
  thing.  We need to carefully work to find out what the goals are.
  This is research, and you are a part of a research team, not a
  contracted developer.
* The job requires having a broad knowledge of what tools are
  available and even going and learning more to plan the project.
* Defining what is our responsibility and what is the customer's
  responsibility.
* Planning enough to know what to do, while taking into account that
  in research the long-term plan may not be known.
* Even after you do know what to do, explaining it clearly and
  concisely enough that the customers and others can understand what
  is happening. (This often happens when needing to present the
  project to more customers than the original ones.)
* Determining if the customer-RSE relationship is enough, or if extra
  support such as project managers are needed.
* Customers may present overly broad project plans, perhaps even
  generated with AI and thus not realistic or representative of what
  the customer actually needs.
* It can sometimes be difficult to know if a project even should be
  accepted, or declined (and in that case, providing the next best
  options to the customers).
* All the risks that come with research and software development,
  combined.


Expectations / checklists
-------------------------

* Serve as the second contact to projects (first contact may be
  someone hearing the broad idea and suggesting a meeting) and
  organize a planning meeting with the right people.
* During the planning meeting, really figure out what the people need
  (which may require digging, and also helping to come up with what
  the right solution is).  Assume you are part of a research team, not
  a contracted developer.
* Use your experience and communication skills to develop a workable
  plan along with the customers.
* Write down the plan so that everyone is on the same page and
  expectations are known across all sides.  Clearly allocate the
  different types of work to RSEs or academics.
* Avoid the `XY problem <https://en.wikipedia.org/wiki/XY_problem>`__.
* Ensure that customers are aware of any risks and you have a plan if
  the risks come.
* Identify risks on our side due to lack of skills or domain knowledge
  and make sure that risk is mitigated (learning something, more
  active customer involvement, adding more checkpoints, or making
  sure the customer knows the risk exists.)
* Ensure that there is someone to manage the project, as much as
  needed, if the RSE can't do themselves.
* Have initial finance discussions (team supervisor needs to finalize
  it).
* Present the project in the weekly RSE meeting and your evaluation if
  we should take it or not.  During this meeting, also help the team
  come up with the right people to do the project.  You don't
  necessarily have to do every project yourself, even if you are
  involved in planning them.
* Have the courage to say "no" when that is the best answer, and
  decide when that is the case.  In these situations, make a plan with
  the next-best options for the customers to do what they need to do.
* If someone else new is working on the projects, mentor them with the
  material from :doc:`project-work`.
* If you aren't working directly with the project, stay engaged enough
  to keep the project on-track, either as a :doc:`technical-mentor`,
  domain mentor, or general mentor role.


External materials
------------------

* `Project starting template <https://docs.google.com/document/d/1XcxeNLRq0kOsFbDEmA7ArdbIrCVudMWHPFQsKRVcTIk>`__
* :doc:`/asc-handbook/rse-reporting/index`
* :doc:`/asc-handbook/rse-reporting/prioritization`
* :doc:`rse/project-lifecycle`
* :doc:`rse/for-group-leaders`
* :doc:`scicomp/zen-of-scicomp`
* ... and almost everything else on :doc:`rse/index`


Training program: materials
---------------------------


Exercises
---------

Future todo: making the first Gitlab issue?

.. exercise:: Planner-1: Roleplay a straightforward project (concept meeting)

   Goal: practice the first meeting with a potential customer and
   establish the basic principles of doing a project.  Walk them
   through what to expect in the RSE project process.

   You: roleplay answering the situation below.  Ask the basics and
   establish if the concept of RSE is appropriate for the project,
   what will happen, etc.  You don't have to pretend to be the one to
   do the project, but you are getting enough info to take it to a
   weekly meeting to find the right person to go to the next stage.

   Your partner: roleplay a customer requesting a fairly normal
   project.

   Example cases:

   * LUMI porting
   * Optimizing some HPC software
   * Developing a web visualization for some data
   * Adding documentation, testing, packaging, etc. to some existing
     project.
   * Creating a data analysis pipeline.
   * (you can think of your own things, too)


.. exercise:: Planner-2: Roleplay a planning meeting, continuing from above

   Goal: practice a structured way to plan out the project, so that
   everyone leaves with a clear idea of what will happen.  Practice
   with the template project planning doc or equivalent, and
   co-editing a doc to produce a plan.

   Like the exercise above (maybe combined with above), but fill out
   all template doc and make a plan for what should actually happen
   (the "planning meeting").  Go through, extracting information about
   what needs to be done, discuss who does what, and write it down.

   (For this exercise, you probably want to use an involved-enough
   project that both people understand enough and could possibly do)


.. exercise:: Planner-3: Roleplay responding to a project request we can most likely not fulfill

   Goal: practice directing the customer to other resources or
   otherwise finding their best way forward, even when we have to say
   "no".  (This would normally not happen in the concept meeting, but
   you would take it to the weekly meeting to present to others
   anyway.  You can pretend you did that already, or just pretend you
   already know we can't do it.)

   Like the exercise above, but you need to tell the customer that
   it's not within our capacity (either time or skills) right now.
   Give a special focus to making sure they have some other path
   forward.

   Your partner: there are different reasons we might not be able to
   fulfill the project:

   * It takes too long (years of time, better to hire someone
     themselves)
   * It is too specialized (ENG researcher needs specialized laboratory
     instrument programming, ASIC programming, or something).
   * They need CPU design


.. exercise:: Planner-4:: Roleplay digging to figure out the project

   Goal: customers don't always volunteer important information about
   the project easily.  Practice your skills at digging in, so you
   won't forget to do it later.

   You: roleplay talking with the customer to figure out their
   project, and discuss if you can or cant' do it.

   Your partner: present your own previous work as an RSE project.
   Don't be too specific (in fact act a bit shy and non-communicative)
   and force your partner to ask questions to dig deeper and
   happening.
