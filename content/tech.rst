Tech stuff
==========

This list is made for new people, who have been hired as RSEs at
Aalto.  This isn't a list of what someone has to know to apply, **and
not what people should know before starting**.  It only provides a
map, a RSE will incrementally learn things here (and probably things
not on the list - this list is what we already know).  In the future,
we expect this list to be copied and reused in other contexts.

Someone might take ~6 months to slowly learn things on this list as
they need them.  Not everything will be needed.

Linux and shell
---------------

* Shell scripting and the OS interface

  * Advanced Bash SCripting guide: https://tldp.org/LDP/abs/html/

* Containers

  * Docker: https://docs.docker.com/get-started/overview/ (though we don't Docker on the cluster, it's good to know anyway)
  * Dockerfile reference: https://docs.docker.com/engine/reference/builder/
  * Apptainer (formerly called "singularity"):

    * This is what is actually used on the cluster
    * https://apptainer.org/docs/user/latest/
    * Key things: make own container, convert docker to apptainer, how to run on cluster
    * singularity_wrapper and how it works with Lmod: https://scicomp.aalto.fi/triton/usage/singularity/ (load a singularity module and you can see where the script is)

* Lmod:

  * https://lmod.readthedocs.io/en/latest/
  * (hint: personal modulefiles: mkdir ~/modulefiles ; module use ~/modulefiles)
  * Mainly basic use + writing modulefiles

* Conda

  * especially resolving GPU code related issues

* 

Software development tools
--------------------------

* CodeRefinery lessons (https://coderefinery.org)
* git-intro: https://coderefinery.github.io/git-intro/
* and git-collaborative: https://coderefinery.github.io/git-collaborative/
* Reproducible Research: https://coderefinery.github.io/reproducible-research/
* Documentation: https://coderefinery.github.io/documentation/
* (Jupyter: https://coderefinery.github.io/jupyter/)
* Automated Testing https://coderefinery.github.io/testing/
* `Modular type-along
  <https://coderefinery.github.io/modular-type-along/>`__ or `Modular
  code developmenent presentation
  <http://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/modular-code-development/master/talk.md>`__
* Social coding: https://coderefinery.github.io/social-coding/

There are a few other interesting CodeRefinery lessons: https://coderefinery.org/lessons/


HPC
---

* Triton tutorials is what we expect our users to know, and reading through these is enough (it will be familiar): https://scicomp.aalto.fi/triton/#tutorials
* And in general, browse (but not read in detail) the rest of the Triton  https://scicomp.aalto.fi/triton/


Programming
-----------

Python
~~~~~~

* Python virtual environments and Conda environments: https://scicomp.aalto.fi/scicomp/python/ , https://scicomp.aalto.fi/triton/apps/python/
  * Be able to create a virtual environment
* Python module/package structure
* Python packaging
  * https://packaging.python.org/en/latest/tutorials/packaging-projects/
  * setup.py vs pyproject.toml (newer)
* Python command line interfaces (argparse), installing interfaces via packages, ...
* Other steps for a good project
  * Good project structure (module-name/module_name/)
  * Command line interface
  * Modular and maintainable code
  * Installable: setup.py vs pyproject.toml
  * Linter (if worth it)
  * Test coverage (if worth it)
  * Good documentation (README, code-level docs, sphinx + RTD/gh-pages)
  * Automated tests to the degree useful for the project.  At least minimal.
  * Github Actions
  * PyPI release
  * conda-forge release
  * GH-action for releasing to PyPI/conda-forge

Examples:
* 


Data processing
---------------
* webdataset
* Small file management in various ways
* Exercise: i/o benchmarking

Data management
---------------
* FAIR data
* Open Science
* Aalto Data Agents webinars


Web stuff
---------
* intro, debugging
* django?
