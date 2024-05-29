black = formarter, can be set as default formater in vscode.
        pip install black + vsconfig or use vscode plugging and set the config in preferences

pylint = linter
    pip install pylint + vsconfig or use vscode plugging and set the config in preferences
    pylint OPTIONS --generate-rcfile > .pylintrc
    pylint --rcfile=.pylintrc
    pylint OPTIONS --disable=W
    # pylint: disable=missing-function-docstring

Flake8 - A popular linter combining Pyflakes, pycodestyle, and McCabe complexity analysis for quick quality assurance.
Flake8 + darglint plugging to validate docstream formats/inputs.
pip install flake8 + config via file configuration (optional) - no vscode plugging 
pip install darglint + config via flake8 file configuration (optional) - no vscode plugging

autoDocstream = https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
                vscode plugging.

Category	Linter
Linter	Pylint - A highly-configurable linter for comprehensive error checking and customizable coding guidelines enforcement.
General	Flake8 - A popular linter combining Pyflakes, pycodestyle, and McCabe complexity analysis for quick quality assurance.
Typing	MyPy - A user-friendly type checker focusing on static type checking and gradual typing support.
Typing	Pyright - A fast, lightweight type checker and linter by Microsoft, offering real-time development feedback.
Imports ordering	isort - A Python utility for sorting imports automatically, ensuring a clean and organized import section in your code.
Documentation	pydocstyle - Docstring style checker.
Security	Safety - checks Python dependencies for known security vulnerabilities and suggests the proper remediations for vulnerabilities detected.
Security	Bandit - a tool designed to find common security issues in Python code.
Code complexity	Xenon - a monitoring tool based on Radon. It monitors your code's complexity. Ideally, Xenon is run every time you commit code.
Code complexity	Radon - a tool that computes various metrics from the Python source code.