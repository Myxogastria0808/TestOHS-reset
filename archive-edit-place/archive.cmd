chcp 65001
@echo off

color b0

git clone  https://github.com/Myxogastria0808/TestOHS-reset.git
cd TestOHS-reset
rmdir /s /q each-club-activity
mkdir each-club-activity
cd ..
cd ..
xcopy each-club-activity archive-edit-place\TestOHS-reset\each-club-activity\ /e /h /y
cd archive-edit-place
cd TestOHS-reset
git add .
git commit -m "%date:~0,4%"
git push origin gh-pages
rmdir /s /q .git
cd ..
rmdir /s /q TestOHS-reset


gh repo create %date:~0,4% --public
git clone https://github.com/Myxogastria0808/%date:~0,4%.git
cd %date:~0,4%
mkdocs new ./
mkdocs gh-deploy
git checkout gh-pages
del /q .nojekyll
del /q *.html
del /q sitemap.xml
del /q sitemap.xml.gz
del /q mkdocs.yml
rmdir /s /q css
rmdir /s /q fonts
rmdir /s /q img
rmdir /s /q js
rmdir /s /q search
rmdir /s /q docs
rmdir /s /q site
git add .
git commit -m "Initialize repository. The repository name is %date:~0,4%."
git push -u origin gh-pages
git clone --mirror https://github.com/Myxogastria0808/TestOHS-main.git mirror_erea
cd mirror_erea
git remote set-url --push origin https://github.com/Myxogastria0808/%date:~0,4%.git
git remote update
git push --mirror
cd ..
rmdir /s /q .git
rmdir /s /q mirror_erea
git clone https://github.com/Myxogastria0808/TestOHS-main.git
cd TestOHS-main
rmdir /s /q archive-edit-place
rmdir /s /q announcement
rmdir /s /q audio
rmdir /s /q business
rmdir /s /q cafeteria
rmdir /s /q calender
rmdir /s /q club-activity
rmdir /s /q communication
rmdir /s /q compression
rmdir /s /q css
rmdir /s /q daily-life-image-folder
rmdir /s /q general
rmdir /s /q hometown-tax-donation-program
rmdir /s /q img
rmdir /s /q img-system
rmdir /s /q introduction
rmdir /s /q js
rmdir /s /q library
rmdir /s /q margin
rmdir /s /q path
rmdir /s /q PDF
rmdir /s /q science
rmdir /s /q system
del /q index.html
rem 本番は、/s /q App.exe
del /q App.cmd
del /q README

git add .
git commit -m "%date:~0,4%"
git push origin gh-pages
rmdir /s /q .git
cd ..
rmdir /s /q TestOHS-main
git clone --mirror https://github.com/Myxogastria0808/TestOHS-reset.git mirror_erea
cd mirror_erea
git remote set-url --push origin https://github.com/Myxogastria0808/TestOHS-main.git
git remote update
git push --mirror
cd ..
cd ..
rmdir /s /q %date:~0,4%
git clone https://github.com/Myxogastria0808/TestOHS-archive.git
start https://myxogastria0808.github.io/CodeBox/





:A
set input_archive =

echo ==================================================================
echo ステップ１　以下のURLをコピーして所定の位置に貼り付けてください。
echo.
echo https://github.com/Myxogastria0808/%date:~0,4%.git
echo.
echo (参考) 西暦: %date:~0,4%
echo.
echo ステップ２　編集が終了したら、 u と入力してください。
echo.
echo (u と入力すると、蜻蛉の軌跡の更新が行われます。)
echo ===================================================================
color b0

set /P input_archive="ここに入力してください:"
echo %input_archive%

pause

if %input_archive%==u (
    cd TestOHS-archive
    git add .
    git commit -m "%date:~0,4%"
    git push origin gh-pages
) else (
    echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    echo 入力が間違っています。
    echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    goto :A
)



exit