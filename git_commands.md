* git init creates a new repository
* git status : files that have been modified, files that will and will not be committed, files that git will ignore
* git add : takes a file or folder as parameter, flag -A will add all files to the next commit that have been modified
* git commit : -m 'message'
* git help [whatever] : gives the parameters needed, use stack overflow instead if makes no sense
* git pull : pulls the shit from github
* git push : pushes the shit to github
* git clone : clones the repo to local
* git log : which commits have been made
* git diff : how does the current file differ from the last commit
* git checkout filename : overwrites the changes after last commit
* git remote add origin https://github.com/tirri/thesis.git : github will tell to do this

  505  git
  508  git init
  509  touch .gitignore
  510  vi .gitignore 
  511  git status
  513  git status
  514  git add -A
  515  git status
  516  git commit -m 'Initial commit'
  517  git status
  518  git log
  521  cd .git
  525  git status
  526  git diff parse_messages_from_json.py 
  527  git checkout parse_messages_from_json.py 
  528  git status
  529  git remote add origin https://github.com/tirri/thesis.git
  530  git push -u origin master
  531  touch git_commands.md
  537  git remote
  538  git status
  539  git add git_commands.md 
  540  git status
  541  git push 
  542  git status
  543  git commit -m 'Helpful git commands in this file'
  544  git status
  545  git log
  546  git log -oneline
  547  git help log
  548  git log --oneline
  549  git status
  550  git push
  551  git status
  552  git status
  554  git add README.md 
  555  git commit -m 'updated readme'
  556  git status
  557  git push
  558  git pull
  559  git pull
  562  git status
  563  git commit 
  564  git add
  565  git add .
  566  git status
  567  git commit -m 'fixed merge issues'
  568  git push
  570  history | grep git
