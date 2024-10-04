# Git Setup and Usage Guide

## 1. Setting up Git on Local Machine and Linking to Existing Repository

### A. Install Git
1. Download Git from [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Follow the installation instructions for your operating system

### B. Configure Git
Open a terminal or command prompt and run:
```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

### C. Create a Local Repository
1. Open a terminal or command prompt
2. Navigate to your project directory:
   ```
   cd path/to/your/project
   ```
3. Initialize a new Git repository:
   ```
   git init
   ```

### D. Link to Existing Remote Repository
1. Go to GitHub and copy the URL of your repository
2. In your terminal, add the remote repository:
   ```
   git remote add origin https://github.com/yourusername/your-repo-name.git
   ```

### E. Pull Existing Code (if any)
If the remote repository already has code:
```
git pull origin main
```

### F. Push Your Local Code to GitHub
1. Add your files to the staging area:
   ```
   git add .
   ```
2. Commit your changes:
   ```
   git commit -m "Initial commit"
   ```
3. Create and switch to the main branch (if not already on it):
   ```
   git checkout -b main
   ```
4. Push your code to GitHub:
   ```
   git push -u origin main
   ```

## 2. Steps to Push New Code

### A. Make Changes to Your Code
Edit your files as needed in your preferred text editor or IDE

### B. Check Status of Your Repository
```
git status
```
This will show you which files have been modified

### C. Stage Your Changes
To stage all changed files:
```
git add .
```
To stage specific files:
```
git add filename1 filename2
```

### D. Commit Your Changes
```
git commit -m "Brief description of your changes"
```

### E. Push Your Changes to GitHub
```
git push origin main
```

## Additional Tips

- Always pull before starting work:
  ```
  git pull origin main
  ```
- To create a new branch:
  ```
  git checkout -b new-branch-name
  ```
- To switch between branches:
  ```
  git checkout branch-name
  ```
- To merge branches:
  ```
  git checkout main
  git merge branch-name
  ```
- To see commit history:
  ```
  git log
  ```

Remember to replace `yourusername`, `your-repo-name`, and other placeholders with your actual information.

