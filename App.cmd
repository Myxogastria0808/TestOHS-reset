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
    git clone "https://github.com/Myxogastria0808/TestOHS-main.git/"
) else if %input_strong%==e (
        start https://myxogastria0808.github.io/CodeBox/
) else if %input_strong%==u (
    git add .
    git commit -m "%date:~0,10%, %time%"
    git push origin main
) else if %input_strong%==p (
    cd compression
    start image.sh
)  else if %input_strong%==m (
    cd margin
    python margin.py
    start image.sh
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
echo --------------------------------------------------------------------------------------------
echo 本当に、%input_recovery%を削除しますか？
echo.
echo 削除する場合は y を、削除しない場合は n を入力してください。
echo --------------------------------------------------------------------------------------------

color b0

set /P input_double-check="ここに入力してください:"
echo %input_double-check%

pause

if %input_double-check%==y (
    gh repo delete %input_double-check%
    echo --------------------------------------------------------------------------------------------
    echo %input_recovery%の削除は、正常に行われました。
    echo --------------------------------------------------------------------------------------------
    pause
) else if %input_double-check%==n (
    goto :R
) else (
    goto :double-check
)

exit