# project-site-src

This is a repo for source code of the project website.

## The source code

The site is written in Django, using django-distil to generate a static website.

Static websites have no database, in this we rely on markdown and bibtex files to store dynamic information, which will be included the next time the site is compiled.


### Adding new info to the site

In general, all text is sourced from markdown files and the naming of the files under `main/markdown/` should be obvious


#### News and info

News items are written in markdown. Files are stored in under `main/news-n-info/` and should be named in the following format `<YYYY-MM-DD>_<short-item-title>.md`, e.g. `2024-09-12_project-kickoff.md` no spaces or weirdo diacritics like å or ä in the filename - not following the naming convention will lead to unexpected results in the output of the website.

#### Your bio

...under `main/markdown/team-bios`


#### references to publications

References are stored in bibtex under `main/bibtex/`. We have a file for each of the team members and one for the project. This allows us to advertise our own publications that aren't necessarily a result of the project while also clearly listing project output on the relevant page.


 