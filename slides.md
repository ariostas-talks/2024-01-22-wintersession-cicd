[comment]: # (This presentation was made with markdown-slides)
[comment]: # (Can be found here: https://gitlab.com/da_doomer/markdown-slides)
[comment]: # (Compile this presentation with the command below)
[comment]: # (mdslides slides.md)

[comment]: # (Set the theme:)
[comment]: # (THEME = white)
[comment]: # (CODE_THEME = github)

[comment]: # (controls: true)
[comment]: # (keyboard: true)
[comment]: # (markdown: { smartypants: true })
[comment]: # (hash: false)
[comment]: # (respondToHashChanges: false)

## Continuous Integration and Continuous Delivery (CI/CD) with GitHub Workflows

Andres Rios Tascon | Wintersession 2024 | Jan 22, 2024

[comment]: # (!!!)

## What is CI and CD

- Continuous Integration:<br>
  Frequent merging of changes into main branch

- Continuous Deployment:<br>
  Automatic release of new software versions

[comment]: # (!!!)

## What is CI for?

- Running tests (dynamic and static)
  - Check if new changes break any existing functionality
  - Check if code follows formatting guidelines


[comment]: # (||| data-auto-animate)

## What is CI for?

- Building documentation<br>
  - Run Doxygen/Sphinx/etc generate documentation in pdf or html form
  - Check if examples in the documentation work

[comment]: # (||| data-auto-animate)

## What is CI for?

- Build static websites
  - Build and publish a website to GitHub Pages/ReadTheDocs/etc

[comment]: # (||| data-auto-animate)

## What is CI for?

- Generating pull requests for updates and other maintenance
  - Update dependencies
  - Fix typos and coding style

[comment]: # (||| data-auto-animate)

## What is CI for?

- Whatever your project needs!

[comment]: # (!!! data-auto-animate)

## What are the benefits?

- Consistent, controlled environment between runs
- Runs every PR/commit/tag/whatever you choose
- Can't be skipped or forgotten, no contributor setup
- Can run lots of OS's, Python versions, compilers, etc

[comment]: # (!!!)

## Some major CI services

- **Travis CI**: Very popular for years, but not anymore.
- **Jenkins**: A self-host only OSS solution.
- **Appveyor**: The original Windows CI service.
- **Circle CI**: The first more “modern” design.
- **GitLab CI**: For years, this was one of the best services. Still very good.
- **Azure Pipelines**: Very modular design is easy to upgrade and maintain.
- **GitHub Actions (GHA)**: Extremely simple and popular. Actions are easy to write and share.

[comment]: # (!!!)

### Today we will be focusing on GitHub Actions

<br>

We first need to briefly discuss exit codes and YAML.

[comment]: # (!!!)

### Exit codes

- Every time you run a command in a shell there is an exit code that indicates if it ran successfully, or if there was an error.
- An exit code of `0` indicates that the command ran successfully, other numbers indicate an error.
- Sometimes different numbers correspond to different errors.

[comment]: # (||| data-auto-animate)

### Exit codes

```bash [1-3|4-7|8-12]
> mkdir test
> echo $0
0
> mkdir test
mkdir: test: File exists
> echo $0
1
> mkdir -z test
mkdir: illegal option -- z
usage: mkdir [-pv] [-m mode] directory_name ...
> echo $0
64
```

[comment]: # (||| data-auto-animate)

### Exit codes

- CI workflows will typically stop once they encounter a non-zero exit code.
- Sometimes you may need to run a command that might fail, but you want the workflow to proceed.
- Some scripts and binaries don't respect this standard and return non-zero exit codes even when successful.

[comment]: # (||| data-auto-animate)

### Exit codes

Error codes can be ignored using logical or (||)
```bash
> mkdir -z test || echo "ignore"
ignore
```

It is also useful to use logical and (&&) to run a command only if another one is successful.
```
> <command1> && <command2>
```

[comment]: # (!!! data-auto-animate)

### YAML

YAML (YAML Ain’t Markup Language, originally Yet Another Markup Language) is a human-readable data serialization language.

- Easy to read and use
- Very commonly used in CI configuration files.
- File extension is .yml or .yaml

[comment]: # (||| data-auto-animate)

### YAML

Defining scalar values:

```yaml
number-value: 42
boolean-value: true # can also be on or yes
string-value: "Hello world"
another-string: String without quotes
```

[comment]: # (||| data-auto-animate)

### YAML

Defining lists:

```yaml
colors:
  - red
  - green
  - blue

more_colors: [black, white]
```

[comment]: # (||| data-auto-animate)

### YAML

Defining dictionaries:

```yaml
person:
  name: John Smith
  age: 33
  job: accountant
```

[comment]: # (||| data-auto-animate)

### YAML

Defining multi-line strings:

```yaml
some-text: >
  Multiple
  lines
  of
  text
same-text: "Multiple lines of text\n"
```

[comment]: # (||| data-auto-animate)

### YAML

Defining multi-line strings:

```yaml
some-text: |
  Multiple
  lines
  of
  text
same-text: "Multiple\nlines\nof\ntext\n"
```

[comment]: # (!!! data-auto-animate)

### Setting up GitHub workflows

- Each workflow is configured by a yaml file placed in `.github/workflows`
- Can be set to trigger by a wide variety of events
- Can run your own commands or use actions written by you or third-parties

[comment]: # (||| data-auto-animate)

### Setting up GitHub workflows

This is the basic structure of a workflow file.

```yaml
on: <event or list of events>

jobs:
  job_1:
    name: <name of job>
    runs-on: <type of machine>
    steps:
      - run: <command1>
      - name: <name of step>
        run: <command 2>

  job_2:
    name: <name of job>
    runs-on: <type of machine>
    steps:
      - uses: <some third-party action>
```

[comment]: # (!!! data-auto-animate)

### CI Live Demo

Go to the following link:

https://github.com/ariostas/wintersession2024-cicd

[comment]: # (!!! data-auto-animate)

### Exercise 1

Modify something in the workflow. Can be anything you want! Here are some ideas:
- Modify the Python code so that the tests fail.
- Add a new step that runs some Python code.
- Add a step that produces an output and print it from another step.
- Add a new job that fails.

[comment]: # (!!! data-auto-animate)

### CD Live Demo

[comment]: # (!!! data-auto-animate)

### Exercise 2

Create a new workflow that generates these slides and publishes them to GitHub pages. Things you need:

- `actions/checkout`
- `actions/setup-python`
- `markdown-slides` from https://gitlab.com/da_doomer/markdown-slides
- `actions/upload-pages-artifact`
- `actions/deploy-pages`
- Repo > Settings > Pages > Source > GitHub Actions

[comment]: # (||| data-auto-animate)

### Exercise 2

Start by checking out the repo.

```yaml
- name: Check out repo
  uses: actions/checkout@v4
```

[comment]: # (||| data-auto-animate)

### Exercise 2

Then set up Python.

```yaml
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: "3.11"
```

[comment]: # (||| data-auto-animate)

### Exercise 2

Install `markdown-slides`.

```yaml
- name: Install markdown slides
  run: pip install git+https://gitlab.com/da_doomer/markdown-slides.git
```

[comment]: # (||| data-auto-animate)

### Exercise 2

Generate the slides.

```yaml
- name: Generate slides
  run: mdslides slides.md --output_dir slides
```

[comment]: # (||| data-auto-animate)

### Exercise 2

Upload pages artifact

```yaml
- name: Upload pages artifact
  uses: actions/upload-pages-artifact@v3
  with:
    path: ./slides
```

[comment]: # (||| data-auto-animate)

### Exercise 2

Deploy to GitHub Pages

```yaml
deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v3
```

[comment]: # (!!! data-auto-animate)

There's many more things to learn, but with this basic knowledge there is lots of things you can do!
