@echo off
cd ..
git add ./index.html
git commit -m "%date:~0,10%, %time%"
git push origin gh-pages
exit