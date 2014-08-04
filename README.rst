This is a template for a PyQt4 application

To get started::

    pip install cookiecutter
    cookiecutter ...

This will prompt you for some values, and create a new directory using the
repo_name you give it. Inside that directory, you can do

.. code:: python

    ./compile_ui.py    # Compile the UI
    python3 -m myapp   # Run the application

To modify the UI, use Qt Designer, saving files in ``package/ui/``, and rerun
``./compile_ui.py`` to recompile the files. You should keep the .ui files in
version control; it's up to you whether you keep the generated .py files in
there as well.