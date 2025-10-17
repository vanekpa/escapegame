# Uploading This Project to GitHub

Follow these steps to publish the current project to a new GitHub repository.

1. **Create a repository on GitHub**
   - Visit https://github.com/new while logged in.
   - Provide a repository name (for example, `escape-game-chunker`).
   - Choose whether the repository should be public or private, then click **Create repository**.  Leave the "Initialize this repository" options unchecked.

2. **Connect the local project to the remote repository**
   - Ensure you are in the project root inside your terminal:
     ```bash
     cd /workspace/escapegame
     ```
   - Add the new GitHub repository as a remote named `origin` (replace the URL with your own repository URL):
     ```bash
     git remote add origin git@github.com:<username>/<repository>.git
     ```
     If you prefer HTTPS:
     ```bash
     git remote add origin https://github.com/<username>/<repository>.git
     ```
   - Confirm that the remote is configured:
     ```bash
     git remote -v
     ```
     The command should list the GitHub URL for both `fetch` and `push`.  If it does not, repeat the `git remote add` command or
     update the remote URL with `git remote set-url origin <url>`.

3. **Push the existing history to GitHub**
   - Push the current `work` branch to GitHub:
     ```bash
     git push -u origin work
     ```
   - After the first push you can run `git push` without extra arguments to update the same branch.

4. **Create a pull request (optional)**
   - If you plan to merge `work` into another branch (for example, `main`), open the new repository on GitHub, click **Compare & pull request**, review the changes, and submit the PR.

## Troubleshooting
- If Git reports that `origin` already exists, update its URL instead:
  ```bash
  git remote set-url origin git@github.com:<username>/<repository>.git
  ```
- Authenticate using an SSH key or a GitHub personal access token depending on which remote URL you use.
- If `git push` responds with `fatal: No configured push destination.`, it means no remote has been added yet.  Add the remote
  using step 2 and re-run the push command, or provide the remote name explicitly: `git push origin work`.

## Example push attempt from this environment
To verify the current setup, we ran `git push` directly in the container.  The command failed with the following output:

```
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using
    git remote add <name> <url>
and then push using the remote name
    git push <name>
```

This confirms that the repository still lacks a configured remote.  After you add your GitHub repository as `origin`, the same
command will succeed.

