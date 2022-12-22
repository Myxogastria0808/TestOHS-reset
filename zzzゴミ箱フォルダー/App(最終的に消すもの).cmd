chcp 65001
@echo off

:P
set input_password =

echo --------------------------------------------------------------------------------------------
echo パスワードを入力してください。
echo --------------------------------------------------------------------------------------------

color b0

set /P input_password="ここに入力してください:"
echo %input_password%

pause

if %input_password%==hello (
    goto :A
) else (
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    echo パスワードが間違っています。
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    goto :P
)
rem =================================================================================================
:A
set input_strong =

echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo --------------------------------------------------------------------------------------------
echo ウェブサイトのファイル一式をダウンロードする場合は、d と入力してください。
echo.
echo ウェブサイトの編集を行う場合は、e と入力してください。
echo.
echo ウェブサイトの更新をする場合は、u と入力してください。
echo.
echo 画像の圧縮のみを行う場合は、compressionフォルダーに画像をいれて p と入力してください。
echo.
echo 余白の付与及び圧縮を行う場合は、marginフォルダーに画像を入れて m と入力してください。
echo.
echo ホームページの表示に不具合が発生した場合でサーバー側に問題が疑われる場合は、github と入力してください。
echo.
echo ウェブサイトのArchive作成を行う場合は、archiveと入力してください。
echo.
echo Archiveコマンドは、1年に一度だけ動作させてください。
echo.
echo Archiveの作成を間違えて行ってしまった場合は、r と入力して、削除作業を行ってください。
echo. 
echo このバッチファイルを終了する場合は、exit と入力してください。
echo.
echo (このバッチファイルを操作するときは、インターネットに接続していることを確認してください。)
echo --------------------------------------------------------------------------------------------

color b0

set /P input_strong="ここに入力してください:"
echo %input_strong%

pause

if %input_strong%==d (
    cd /
    cd %USERPROFILE%/Downloads/
    git clone "https://github.com/Myxogastria0808/TestOHS-main.git/"
) else if %input_strong%==e (
    start https://myxogastria0808.github.io/CodeBox/
) else if %input_strong%==u (
    git add .
    git commit -m "%date:~0,10%, %time%"
    git push origin gh-pages
) else if %input_strong%==p (
    cd img-system/system
    start image.sh
    echo ---------------------------------------------------------------------------------------------
    echo ターミナル画面が消えたら、エンターキーを押してください。
    echo ---------------------------------------------------------------------------------------------
    pause
    goto :img
)  else if %input_strong%==m (
    cd img-system/system
    python margin.py
    start image.sh
    echo ---------------------------------------------------------------------------------------------
    echo ターミナル画面が消えたら、エンターキーを押してください。
    echo ---------------------------------------------------------------------------------------------
    pause
    goto :img
) else if %input_strong%==github (
    start https://github.com/Myxogastria0808/
) else if %input_strong%==archive (
    start ./archive-edit-place/archive.cmd
) else  if %input_strong%==r (
    goto :R
) else if %input_strong%==exit (
    exit
) else (
    goto :A
)

exit

rem =================================================================================================
:img
set input_img =

echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo ---------------------------------------------------------------------------------------------
echo 全ての画像ファイルが圧縮されていることを確認してください。
echo.
echo 圧縮後のファイル一覧
cd ..
cd ./post-processed-files/
dir
echo.
echo 全ての画像ファイルが圧縮されている場合は、y を入力してください。
echo.
echo (y を入力すると終了します。)
echo.
echo 圧縮できていない画像ファイルがある場合は、n を入力してください。
echo.
echo ※1 n を入力すると画像圧縮を行うためのウェブアプリケーションが表示されます。
echo.
echo ※2 画像圧縮ができていない画像に関しては、表示されたウェブアプリケーションで画像圧縮を行ってください。
echo ---------------------------------------------------------------------------------------------

set /P input_img="ここに入力してください:"
echo %input_img%

pause

if %input_img%==y (
    exit
) else if %input_img%==n (
    start https://squoosh.app/
    exit
) else (
    goto :img
)

rem =================================================================================================
:R
set input_recovery =

echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo --------------------------------------------------------------------------------------------
echo 削除したいRepository名を入力してください。
echo.
echo 誤ってRepository削除コマンドを入力した場合は、b と入力してください。
echo.
echo (bと入力すると始めのメニューに戻ります。)
echo.
echo Repository名の一覧
gh repo list
echo --------------------------------------------------------------------------------------------

set /P input_recovery="ここに入力してください:"
echo %input_recovery%

pause

if %input_recovery%==main (
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    echo 削除することができないRepositoryです。
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    pause  
    goto :R
) else if %input_recovery%==archive (
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    echo 削除することができないRepositoryです。
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    pause
    goto :R
) else if %input_recovery%==reset (
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    echo 削除することができないRepositoryです。
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    pause
    goto :R
) else if %input_recovery%==b (
    goto :A
) else (
    goto :double-check
)


:double-check
set input_double-check =
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo --------------------------------------------------------------------------------------------
echo 本当に、%input_recovery%を削除しますか？
echo.
echo 削除する場合は y を、削除しない場合は n を、終了する場合は e を入力してください。
echo --------------------------------------------------------------------------------------------

color b0

set /P input_double-check="ここに入力してください:"
echo %input_double-check%

pause

if %input_double-check%==y (
    gh repo delete %input_recovery%
    goto :double-check-return
) else if %input_double-check%==n (
    goto :R
) else if %input_double-check%==e (
    exit
) else (
    goto :double-check
)

:double-check-return
set input_double-check-return =
echo --------------------------------------------------------------------------------------------
echo 実行結果は、✓ Deleted repository %input_recovery% となっていますか。
echo.
echo 上記のログと一致している場合は y を、一致していない場合は n を入力してください。
echo.
echo (y を入力すると終了し、n を入力すると削除確認のメニューに戻ります。)
echo --------------------------------------------------------------------------------------------

color b0

set /P input_double-check-return="ここに入力してください:"
echo %input_double-check-return%

pause

exit