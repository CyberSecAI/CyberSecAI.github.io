https://www.youtube.com/watch?v=6Rg5M69bMgQ https://drive.google.com/file/d/1zkthSSmKX4aMSuGJoBTy_kV0LS4pkDTY/view




https://www.builder.io/blog/claude-code
https://www.youtube.com/watch?v=n7iT5r0Sl_Y

install gh app
https://youtu.be/n7iT5r0Sl_Y?t=171


[Mastering Claude Code in 30 minutes](https://www.youtube.com/watch?v=6eBSHbLKuN0)


https://github.com/hesreallyhim/awesome-claude-code


https://www.youtube.com/watch?v=T_IYHx-9VGU
CUSTOM COMMAND FILES

Note: all of these are saved in my home directory's (~) .claude folder:
~/.claude/commands/file.md

Iterative Design
https://sharetext.io/2b77be78

Project Settings
https://sharetext.io/279f5af9

Git Save
https://sharetext.io/3a540768
(forked from online resource)



# Git Commit : Well Formatted Commits

This command helps you create well-formatted commits with conventional commit messages and emoji.

## Usage

To create a commit, just type:
```
/commit
```

Or with options:
```
/commit --no-verify
```

## What This Command Does

1. Unless specified with `--no-verify`, ALWAYS runs pre-commit checks:
   - any possible linting to ensure code quality
   - any possible build to verify the build succeeds
   - any possible documentation generation to update documentation
2. Checks which files are staged with `git status`
3. Automatically adds all modified and new files with `git add`
4. Performs a `git diff` to understand what changes are being committed
5. Analyzes the diff to determine if multiple distinct logical changes are present
6. Creates a commit message using emoji conventional commit format

## Best Practices for Commits

- **Verify before committing**: Ensure code is linted, builds correctly, and documentation is updated. Make sure to run ALL of the pre-commit checks first.
- **Atomic commits**: Each commit should contain related changes that serve a single purpose
- **Split large changes**: If changes touch multiple concerns, split them into separate commits
- **Conventional commit format**: Use the format `<type>: <description>` where type is one of:
  - `feat`: A new feature
  - `fix`: A bug fix
  - `docs`: Documentation changes
  - `style`: Code style changes (formatting, etc)
  - `refactor`: Code changes that neither fix bugs nor add features
  - `perf`: Performance improvements
  - `test`: Adding or fixing tests
  - `chore`: Changes to the build process, tools, etc.
- **Present tense, imperative mood**: Write commit messages as commands (e.g., "add feature" not "added feature")
- **Concise first line**: Keep the first line under 72 characters
- **Emoji**: Each commit type is paired with an appropriate emoji:
  - ✨ `feat`: New feature
  - 🐛 `fix`: Bug fix
  - 📝 `docs`: Documentation
  - 💄 `style`: Formatting/style
  - ♻️ `refactor`: Code refactoring
  - ⚡️ `perf`: Performance improvements
  - ✅ `test`: Tests
  - 🔧 `chore`: Tooling, configuration
  - 🚀 `ci`: CI/CD improvements
  - 🗑️ `revert`: Reverting changes
  - 🧪 `test`: Add a failing test
  - 🚨 `fix`: Fix compiler/linter warnings
  - 🔒️ `fix`: Fix security issues
  - 👥 `chore`: Add or update contributors
  - 🚚 `refactor`: Move or rename resources
  - 🏗️ `refactor`: Make architectural changes
  - 🔀 `chore`: Merge branches
  - 📦️ `chore`: Add or update compiled files or packages
  - ➕ `chore`: Add a dependency
  - ➖ `chore`: Remove a dependency
  - 🌱 `chore`: Add or update seed files
  - 🧑‍💻 `chore`: Improve developer experience
  - 🧵 `feat`: Add or update code related to multithreading or concurrency
