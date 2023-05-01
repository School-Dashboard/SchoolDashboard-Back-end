# Git Flow
1. `git clone`
2. `git pull`
3. `git checkout -b new_branch_name`                  -> creates new branch and switches to it
4. `git add .`
5. `git commit -m "description of the changes"`     -> commits the changes
6. `git push origin your_branch_name`               -> push the local branch to the remte repo
7. `git checkout main`                              -> switch to main branch
8. `git merge new_branch_name`                      -> merge new_branch with main branch 
9. `git push`                                       -> push changes to remote repo on main branch 
10. `git branch -d new_branch_name`                  -> deletes the branch locally
11. `git push origin --delete new_branch_name`

# Install Docker
1. `sudo apt-get update`
2. `sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release software-properties-common`
3. `sudo mkdir -p /etc/apt/keyrings`
4. `curl curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg`
5. <code>echo \ <br>
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \ <br>
\$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list </code>
6. `sudo apt-get update`
7. `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin`
8. `sudo nano /etc/group` -> *search for docker and and add your username at the end of the line with docker (after the colon)*
9. Log out and log back in.<br>
	&nbsp;&nbsp;&nbsp;&nbsp;*If you get <span style="color:red">*"ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock."*</span> run:*
	    &nbsp;&nbsp;&nbsp;&nbsp;`sudo systemctl start docker`
10. `docker info` -> *if docker info appears without errors, instalation is ok*
11. `nano ~/.docker/config.json` -> *delete the line with 'credsStore'*


# Buld Docker Image
1. `cd path/to/folder/containing/docker file`
2. `docker build .`

# Run docker container
1. `cd path/to/folder/containing/docker-compose file`
2. `docker-compose up`<br>
   &nbsp;&nbsp;&nbsp;&nbsp;*to stop the curently running container press `CTRL+C` and run `docker-compose down`*
