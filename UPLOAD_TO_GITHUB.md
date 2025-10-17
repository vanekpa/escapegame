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

