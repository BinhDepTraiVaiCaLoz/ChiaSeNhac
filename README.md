#Tạo git
cd /path/to/your/project
git init
git remote add origin https://github.com/<your-username>/<repository-name>.git

#push code
git add .
git commit -m "Comment"
git branch -M main
git push -u origin main

#pull code
git pull