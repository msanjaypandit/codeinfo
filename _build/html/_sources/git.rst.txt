.. _git:

GIT
============

Basics
----------

Use any git provider such as **Github/Gitlab/Bitbucket/Amazon Codecommit** and create a blank repository. You will receive two url, one url is **httpurl** and second will be **sshurl**. httpurl need username and password or token, while sshurl need private and publickey to connect. As this is blank repository, we need to put our code files into it.

``ssh-keygen -t rsa  -C "emailid"``
 * To generate SSH key for bitbucket

*Open your codefiles folder using git bash/terminal. Now connect your code with the repository using below comments, it will work in both cases,either your code is blank or not blank on your machine*

Connect with GIT repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``git init`` 
  * Use this code to initiate git in a Directory. 
 
``git remote add origin <httpurl/sshurl>`` 
  * Use this code to link your directory to git url. 
  

*if you receive repo details from your client and it is blank*

``git clone user@gitpath.git``
 * git clone allow you to get all files of git in a directory having name gitpath

``git clone user@gitpath.git  directory-name``
 * git clone allow you to get all files of git in a directory with the name 'directory-name'

Configure your GIT on your machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``git config --global user.name "[name]"``
  * Sets the name you want atached to your commit transactions

``git config --global user.email "[email address]"``
  * Sets the email you want atached to your commit transactions

``git config``
 * Use it to view git config settings.

When you complete your code
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``git diff``
  * Shows file differences not yet staged

``git status``
 * Current status of your repository. 
 * Git offers suggestions on what to do, offering commands on how to stage or commit those files.

``git add``
 * The git add command appends a change in the working directory to the staging area. 
 * A change can be either a removal or an addition of a file or directory. This a preparatory step toward committing your changes.
 * The actual actions are already “done,” but this command officially nominates those changes to be committed.
 * You can add the —all option. Entering git add —all stages all changes in the working directory and subdirectories, including removals of directories.

.. Tip::

   git add filename1 filename2

``git diff --staged``
  * Shows file differences between staging and the last file version

``git reset [filename]``
  * Unstages the file, but preserve its contents

``git commit``
 * The git commit command records changes you make to the local repository.
 * You can also use git commit to delete files, though it’s a somewhat roundabout way of doing so.
 * Git is essentially a tree of commits, where a commit is a change (an addition, deletion, or update).
 * Doing git commit will commit the changes that you have staged with git add. The commit is made on your local repository.
 * It must be pushed to remotes (repositories not on your computer) to be shared.

.. Tip::

  git commit -m "Your message"

``git push`` or ``git push origin master``
 * Run the git push command to push your changes to the repository. There are a variety of ways you can tweak this, as you can combine the push command with exceptions.
 * On its own, git push makes changes to the repository and all of its associations.
 * The git push `<remote> <branch>` command will push the changes on `<branch>` from your local repository to `<remote>`, which is usually the repository on a server  
   where you collaborate with your colleagues.
 * By default, the first remote is called "origin." If you’ve made changes in your new-feature branch, you’d do git push origin new-feature to send the changes (commits) of new-feature to the place where you collaborate with your colleaguesn.

.. Tip::

 git push origin master

 git push origin <branch-name>

Branches
----------

Branch Basics
^^^^^^^^^^^^^

``git branch``
  * Lists all local branches in the current repository

.. Tip::

 Your default branch can be 'main' or 'master' depends on GIT service provider

``git branch <branch-Name>``
  * Create a new branch 'branch-Name'

``git checkout -b <branch-Name>``
 * Create a new branch called “branch-Name” and move to it.
 * Got an idea for a new feature? Enter git checkout -b new-feature to create a new branch called “new-feature” and open it. 
 * The new branch allows you to work in parallel with your colleagues, keeping your code separate from theirs during the time you’re working on that branch.
 * When you’re ready to share your work, you can push your branch to a remote repo or merge it back into the main branch (usually master/main).

``git branch -d <branch-Name>``
  * Deletes the specified branch “branch-Name”

:ref:`when-you-complete-your-code`

Work with specific branch and dafault branch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``git checkout master``
 * git checkout allows you to move between branches and potentially restore tree files.
 * The command git checkout master switches you to the master branch, which is always the best place to start before making changes to your repo.

``git checkout <branch-Name>``
  * To move in BranchName

``git pull origin master``
 * Get the latest updates on the master branch, 
 * A git pull is actually a combination of git fetch, which grabs all the latest  information, and git merge, which merges the two histories together. 
 * Always run git pull origin master before starting work on a repository.


``git merge <branch-Name2>``
  * Combines the specified branch’s history into the current branch

   
``git merge --abort``
 * It will abort merging issue.

Other common working
--------------------

Refactor filenames
^^^^^^^^^^^^^^^^^^

``git rm <file-name>``
 * Deletes the file from the working directory and stages the deletion

``git rm --cached [file]``
 * Removes the file from version control but preserves the file locally

``git mv [file-original] [file-renamed]``
 * Changes the file name and prepares it for commit

Save fragments
^^^^^^^^^^^^^^
``git stash``
 * Temporarily stores all modified tracked files

``git stash list``
 * Lists all stashed changesets

``git stash pop``
 * Restores the most recently stashed files

``git stash drop``
 * Discards the most recently stashed changeset

Review History
^^^^^^^^^^^^^^

``git log``
 * Lists version history for the current branch

``git log --follow [file]``
 * Lists version history for a file, including renames

``git diff [first-branch]...[second-branch]``
 * Shows content differences between two branches

``git show [commit]``
 * Outputs metadata and content changes of the specified commit

REDO COMMITS
^^^^^^^^^^^^
*Erase mistakes and craf replacement history*

``git reset [commit]``
 * Undoes all commits afer [commit], preserving changes locally

``git reset --hard [commit]``
 * Discards all history and changes back to the specified commit

``git reset --hard origin/master``
 * It Keep you local changes and replace it your files with the files uploaded at master branch.

``git reset --hard [branchName]``
 * It Keep you local changes and replace it your files with the files uploaded at branchName branch.

Other Commands
--------------

.. code-block:: bash

   git checkout HEAD^
   git checkout -f master

``git reset --hard HEAD~1``
 * To remove last commit changes completely

.. code-block:: rst

   git checkout BRANCH-NAME -- filename
   git checkout origin/BRANCH-NAME -- filename

* To pull specific file from specific branch

``git diff develop(FIRST-BRANCH) feature/matches-and-filter(SECOND-BRANCH)  --ajax_mymatch.php(FILE-NAME)``
 * To check the difference between made in the file of two different branch

Gitignore file
--------------

Have a look gitignore.io website to generate gitignore file for your framework.

+----------------+-------------------------------------------------------------------------------+
|gitignore entry | Ignores every…                                                                |
+================+===============================================================================+
|target/         | …folder (due to the trailing /) recursively                                   |
+----------------+-------------------------------------------------------------------------------+
|target          | …file or folder named target recursively                                      |
+----------------+-------------------------------------------------------------------------------+
|/target         | …file or folder named target in the top-most directory (due to the leading /) |
+----------------+-------------------------------------------------------------------------------+
|/target/        | …folder named target in the top-most directory (leading and trailing /)       |
+----------------+-------------------------------------------------------------------------------+
| `*.class`      | …every file or folder ending with .class recursively                          |
+----------------+-------------------------------------------------------------------------------+


+-----------------+----------------------------------------------------------------------------------------+
|gitignore entry  | Ignores every…                                                                         |
+=================+========================================================================================+
|#comment         | …nothing, this is a comment (first character is a #)                                   |
+-----------------+----------------------------------------------------------------------------------------+
| \#comment       | …every file or folder with name #comment (\ for escaping)                              |
+-----------------+----------------------------------------------------------------------------------------+
|target/logs/     | …every folder named logs which is a subdirectory of a folder named target              |
+-----------------+----------------------------------------------------------------------------------------+
|`target/*/logs/` | …every folder named logs two levels under a folder named target (`*` doesn’t include /)|
+-----------------+----------------------------------------------------------------------------------------+
|`target/**/logs/`| …every folder named logs somewhere under a folder named target ( `** includes` /)      | 
+-----------------+----------------------------------------------------------------------------------------+
| `*.py[co]`      | …file or folder ending in .pyc or .pyo. However, it doesn’t match .py!                 |
+-----------------+----------------------------------------------------------------------------------------+
|!README.md |     | Doesn’t ignore any README.md file even if it matches an exclude pattern, e.g. `*.md.`  | 
|                 | NOTE This does not work if the file is located within an ignored folder.               |
+-----------------+----------------------------------------------------------------------------------------+

`Link text <http://local.devadoptds.com/member.html?utm_source=newsletter&utm_medium=email&utm_campaign=aprilv2&utm_content=check_matches>`_