# Systers Git & GitHub Workshop

Welcome to Systers! 💜 This guide is a reference for our Git and GitHub workshop. You don't need to memorize every command—focus on understanding the workflow and knowing where to look when you need help.

## 1. Git vs. GitHub vs. GitHub Desktop

- **Git:** Tracks changes to files and manages version history.
- **GitHub:** Hosts repositories online and supports collaboration.
- **GitHub Desktop:** A graphical interface for common Git operations.
- **Fork:** Your own copy of someone else's GitHub repository.
- **Clone:** A local copy of a repository on your computer.
- **Commit:** A saved snapshot of changes.
- **Branch:** A separate line of development.
- **Push:** Send local commits to a remote repository.
- **Pull request (PR):** Propose changes for review and merging.
- **Upstream:** The original repository you forked.

## 2. Set up SSH for terminal Git

We'll use SSH for terminal exercises on school machines.

**Test your connection:**

```bash
ssh -T git@github.com
```

If authentication succeeds, GitHub will greet you by username.

If it fails, you may need to configure an SSH key. Follow GitHub's [SSH setup guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

Never share your private key. On shared school machines, follow your school's policies for SSH keys.

**Note:** HTTPS cloning is still supported, but GitHub account passwords no longer work for Git authentication. GitHub Desktop uses its own sign-in workflow.

## 3. Contribute using the terminal

### Step 1: Fork and clone

1. Open the original Systers repository on GitHub.
2. Click **Fork** and create a copy under your account.
3. On your fork, click **Code → SSH** and copy the URL.

```bash
git clone git@github.com:YOUR-USERNAME/systers-community.git
cd systers-community
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Create a branch and make a change

```bash
git switch -c add-my-idea
```

Edit `community/PROJECT_IDEAS.md` and add a project idea or learning goal.

### Step 3: Review, commit, and push

```bash
git status
git diff
git add community/PROJECT_IDEAS.md
git commit -m "Add my project idea"
git push -u origin add-my-idea
```

- `status` shows changed files and your current branch.
- `diff` shows what changed.
- `add` stages changes for a commit.
- `commit` saves changes to your local history.
- `push` uploads your branch to your fork.

### Step 4: Open a pull request

On GitHub, create a pull request from your fork's `add-my-idea` branch to the original Systers repository's `main` branch.

Review your changes, write a short description, and submit the PR. A maintainer can review and merge it.

## 4. Use GitHub Desktop

You can perform the same workflow graphically:

1. Fork the original repository on GitHub.
2. In GitHub Desktop, sign in and select **File → Clone repository**. Clone your fork.
3. Create a branch using the branch menu.
4. Edit a file and save it.
5. Review changes in the **Changes** tab.
6. Enter a commit message and click **Commit**.
7. Click **Publish branch** or **Push origin**.
8. Create a pull request targeting the original Systers repository.

GitHub Desktop and the terminal use the same underlying Git concepts.

## 5. Version control and recovery

Git keeps a history of your changes, so you can inspect earlier versions and recover from mistakes.

### View history and changes

```bash
git status
git diff
git log --oneline
git show COMMIT-ID
```

These commands show your current state, changes, commit history, and details about a particular commit.

### Undo uncommitted changes to a file

```bash
git restore FILE
```

This discards uncommitted changes to that file and restores it to the latest commit. **Check your changes first—they may be lost.**

### Restore an older version of a file

```bash
git restore --source=COMMIT-ID -- FILE
```

This restores the file's contents from a selected commit into your working directory. Review the result, then commit it if you want to keep the recovery.

### Undo a commit safely

```bash
git revert COMMIT-ID
```

This creates a new commit that reverses an earlier commit. It is generally safer for changes that have already been shared.

**Caution:** Avoid `git reset --hard` until you understand it. It can discard uncommitted work and move your branch backward.

## 6. Keep your fork up to date

To retrieve changes from the original repository, add it as a remote:

```bash
git remote add upstream git@github.com:ORGANIZATION/systers-community.git
git fetch upstream
```

Replace the example URL with the original Systers repository's SSH URL.

To merge its `main` branch into your local `main` branch:

```bash
git switch main
git merge upstream/main
git push origin main
```

Review your changes before pushing. If Git reports a merge conflict, pause and ask for help.

## Quick command reference

| Command | Purpose |
|---|---|
| `git clone URL` | Clone a repository |
| `git switch -c NAME` | Create a branch |
| `git status` | Check your working tree |
| `git diff` | Inspect changes |
| `git add FILE` | Stage changes |
| `git commit -m "MESSAGE"` | Save a commit |
| `git push` | Upload commits |
| `git pull` | Fetch and integrate changes |
| `git log --oneline` | View history |
| `git restore FILE` | Discard uncommitted file edits |
| `git revert COMMIT-ID` | Undo a commit with a new commit |

Remember: small contributions count, mistakes are part of learning, and you can always ask for help. 💜
