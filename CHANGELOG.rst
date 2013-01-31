Changelog
=========

0.0.11 (2013-01-31)
-------------------
#. Remove error thrown by middleware when there is no user agent and use alternative to prevent spambot likes. This is a django-secretballot bug.

0.0.10 (2012-10-08)
------------------
#. Added ``object_liked`` signal that is sent on like.

0.0.9 (2012-09-28)
------------------
#. Added ability to specify a template to be rendered for ``likes`` inclusion tag.

0.0.8 (2012-08-20)
------------------
#. Updated ``likes_enabled_test`` and ``can_vote_test`` signals to send through sender, thereby allowing listeners to listen to specific senders.

0.0.7 (2012-08-20)
------------------
#. Revert to vote_total on inclusion tag.

0.0.6 (2012-07-24)
------------------
#. Allow for downvotes.

0.0.5 (2011-09-15)
------------------
#. Corrected manifest to include missing static resources.

0.0.4 (2011-09-14)
------------------
#. Documentation, number of fixes.

0.0.3
-----
#. Handle multiple likes buttons on the same page
#. Remove dependency on jmbo
#. Unit tests

0.0.2
-----
#. Prevent local cache on like redirect.

0.0.1
-----
#. Initial release.

