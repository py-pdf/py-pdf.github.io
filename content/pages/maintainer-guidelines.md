Title: Maintainer guidelines
Tags: guideline, maintainer

## Table of contents
<!-- To update this ToC based on the sections below : markdown-toc -i content/pages/maintainer-guidelines.md -->

<!-- toc -->

- [Volunteering](#volunteering)
- [Governance](#governance)
  * [The relationship of py-pdf to its projects](#the-relationship-of-py-pdf-to-its-projects)
  * [Conditions for projects to be added to py-pdf](#conditions-for-projects-to-be-added-to-py-pdf)
  * [Responsibility of project maintainers](#responsibility-of-project-maintainers)
  * [GitHub roles](#github-roles)
- [Releases](#releases)

<!-- tocstop -->

## Volunteering
All [@py-pdf](https://github.com/py-pdf) members are volunteers.
They dedicate some of their time to maintain open-source projects, answer questions and review Pull Requests.

[@py-pdf](https://github.com/py-pdf) members should never be required to operate within deadlines, or even respond within a given time frame.

If you are a user of a [@py-pdf](https://github.com/py-pdf) project and want something done,
whether it is a bugfix or a feature request, your best options for achieving what you want are:

* being polite and patient
* volunteer to contribute yourself

To all [@py-pdf](https://github.com/py-pdf) members, remember: [it's okay to hit pause](https://opensource.guide/best-practices/#its-okay-to-hit-pause), and take time away from volunteer open-source work.

<br>

## Governance
`py-pdf` governance model is descibed there:
<https://pypdf.readthedocs.io/en/latest/meta/project-governance.html>

<br>

## The relationship of py-pdf to its projects

`py-pdf` wants to ensure the Python-PDF ecosystem is prospering. We recognize that individual
maintainers did and still do an outstanding job, but we also see that personal lives sometimes
move away from software projects.

That means:

1. `py-pdf` offers the platform to exchange ideas and provide feedback
2. `py-pdf` administrators who are not project members do interfere, when (a) no activity by the maintainers is in the project for at least 6 months and at least 3 friendly "are you alive" questions over at least 6 weeks. (b) security issues are detected
3. `py-pdf` leaves the projects do their thing in all other cases.

<br>

## Conditions for projects to be added to py-pdf

We want projects which provide value to users and we need to be able to maintain them. We want to improve the Python / PDF ecosystem and not scatter it.

1. The project has to be a Python project and about PDF documents
2. If it's a software project, it has (1) a README with the projects purpose, installation instructions, and a usage example (2) it's either the main project or the fork that has more popularity measured in GitHub stars
3. It either has a different purpose than all other projects in `py-pdf` or is more popular than the existing projects for that purpose
4. It needs to be a FOSS license (e.g. BSD, MIT, Apache)

<br>

## Responsibility of project maintainers

1. **Software Reliability**: Please ensure that your project follows best practices in software development. Introduce a [deprecation process](https://pypdf.readthedocs.io/en/latest/dev/deprecations.html) and follow it.
2. **Kindness**: We are all here because it's fun to help others and create good software. But we are humans: people can have bad days and people might not speak English as a mother tongue. When in doubt, assume the best. Let people know how you perceived their interaction.
3. **Know your Limits**: It's ok to reduce the time you spend on your project or even step away from it. Stay healthy.
4. **Let your Project Grow**: Especially if you step away, let others take over. Make it explicit that you're looking for another person who would take over.
It's OK to [say no](https://opensource.guide/best-practices/#learning-to-say-no).

<!--
As recommended [by the opensource.guide](https://opensource.guide/leadership-and-governance/), a `GOVERNANCE.md` file in every repository could point to this page as reference.
-->

<br>

## GitHub roles
The base permission for [@py-pdf](https://github.com/py-pdf) members is set to **Write**,
meaning any [@py-pdf](https://github.com/py-pdf) member has read permissions,
can manage issues and pull requests, and also push to repositories.

We encourage [@py-pdf](https://github.com/py-pdf) members, and especially maintainers, to make their organization membership **public**
on <https://github.com/orgs/py-pdf/people>, in order to clarify who has ownership of the organization, and the associated rights to perform package releases:

![](../images/github-org-public-membership.png)

<br>

## Releases
Depending on the projects, the release process can be automated inside GitHub Actions pipelines, or stays manual.

<!-- TODO: use a dedicated Pypi user like Jazzband does? cf. https://jazzband.co/about/releases -->

<!-- TODO: add a section on Security & reporting vulnerabilities ? cf. https://jazzband.co/about/security -->

<script>
const ANCHOR_ID_CHAR_RANGE_TO_IGNORE = '[\x00-\x2F\x3A-\x40\x5B-\x60\x7B-\uFFFF]+';
function slugify(s) {
  var s = String(s)
  s = s.trim()
  s = s.toLowerCase()
  s = s.replace(new RegExp('^'+ANCHOR_ID_CHAR_RANGE_TO_IGNORE, 'g'), '')
  s = s.replace(new RegExp(ANCHOR_ID_CHAR_RANGE_TO_IGNORE, 'g'), '-')
  return encodeURIComponent(s);
}
document.querySelectorAll('h2').forEach(function (title) {
  // Add an HTML "id" based on the heading title slugified:
  title.id = slugify(title.textContent);
  // Add a clickable link on hover:
  var a = document.createElement('a');
  a.href = document.location + '#' + title.id;
  a['aria-hidden'] = true;
  a.style.float = 'left';
  a.style['padding-right'] = '4px';
  a.style['margin-left'] = '-20px';
  a.style['line-height'] = 1;
  title.appendChild(a);
  var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('aria-hidden', true);
  svg.setAttribute('height', 16);
  svg.setAttribute('width', 16);
  svg.setAttribute('viewBox', '0 0 16 16');
  svg.style.color = '#1b1f23';
  svg.style['vertical-align'] = 'middle';
  svg.style.visibility = 'hidden';
  a.appendChild(svg);
  var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  path.setAttributeNS(null, 'fill-rule', 'evenodd');
  path.setAttributeNS(null, 'd', 'M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z');
  svg.appendChild(path);
  title.onmouseover = function () { this.getElementsByTagName('svg')[0].style.visibility = 'visible'; };
  title.onmouseout = function () { this.getElementsByTagName('svg')[0].style.visibility = 'hidden'; };
});
</script>
