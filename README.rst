Django mobile app store switcher
============

Django app to dedect if we have to redirect the client to Apple's App Store, to the Google Play Store or an other landing page.
This is build for exactly one app [1]_, that is available in the App Store and/or Google Play Store. 


Installation
------------

To get the latest stable release from PyPi


To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/arteria/django-mobileapps-store.git#egg=mobileapps_store-master


Add ``mobileapps_store`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'mobileapps_store',
    )

Add the ``mobileapps_store`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^mobileappsstore/', include('mobileapps_store.urls')),
    )

 


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate mobileapps_store



Requirements
------------

* httpagentparser

Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-mobileapps-store
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

.. [1] The app with the highest primary key/ID wins. 
