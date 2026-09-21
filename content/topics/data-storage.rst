Data storage systems
====================

**This is still incomplete and pushed halfway through editing.**

This page will explain the various data storage systems we have (or
maybe just support the user docs at :doc:`data/index`).


Background
----------

Typical people usually think of storage as part of a computer.  At our
scale, storage is often a different system from the computing system,
and it can be *difficult* for a typical user to keep track of this.
There are some pictures that try to visualize remote mounting vs
copying data in :doc:`triton/tut/remote-data`.

A place in the **filesystem** where a storage system is available is
called a **mount** point, and **mounting** is the process of making it
available (think of *mounting* a hard disk in a chassis and connecting
it).  One can run the ``mount`` command to list all active mounts, and
you will see many real ones and many virtual ones.  This can be used
to verify what server is connected to each particular mount.

One of the reasons for different types of storage systems is that each
is good for something else.  It's better to have one backed up system
and a larger, faster, non-backed up one, than trying to make one
system do everything.  Sometimes users get uncomfortable when they
have to manage this, but it's the price of being a serious computing
person.  Some of the main properties are speed (bulk transfer), speed
(latency for each operation), size, backed-upness/snapshots, and where
each system is mounted.

The last point about "where each system is mounted" is easy for those
experienced in things to think about, but is actually very hard to
remember off the top of your head (needing to be checked or looked up
every time).  The human brain just doesn't think this way.

Network capacity is a significant bottleneck for network storage
systems.  Triton has an internal Infiniband connection that provides
speeds on the orders of tens of GiB/second.  The ability to
simultaneously serve multiple requests is anoteh


Aalto storage systems
---------------------


Aalto storage system terminology
--------------------------------

We have too many different names that are too similar to each other.
As Aalto unifies we should work out consistency.  A proposal (by
rkdarst) for making things cleardiscussion is below (edit or make comments):


.. list-table::
   :header-rows: 1

   * - System
     - Canonical name
     - Other names
     - Deprecated names
     - Comments
   * - /m/dept/project/X
     - Department project
     - Project, {CS,NBE,...} project, Department teamwork
   * - /m/dept/archive/X
     - Department archive
     - Archive, {CS,NBE,...} archive, Department teamwork
   * - Triton /scratch/dept/project/
     - Triton project
     - Triton scratch
     - "scratch"
   * - Triton
       /scratch/work/username/
     - Triton personal
     - Triton work
     - "work"
   * - Triton homes
       /home/username/
     - Triton home
     - "home"
   * - Teamwork (Aalto managed)
     - Teamwork; Aalto teamwork; "Project"
     -
     -
   * - Aalto home directories
     - Aalto home
     -
     -
     -
   * - Aalto work
     - Aalto work drive
     - "work"
     -
     - The full name "Aalto work drive" makes the distinction from
       other works clear.
