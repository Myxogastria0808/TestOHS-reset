chcp 65001
@echo off

cd ..
cd ..
xcopy post-processed-files ..\img\ /e /h /y

:IMG
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
cd post-processed-files
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
    echo ---------------------------------------------------------------------------------------------
    echo 圧縮が行われていないファイルを表示されたウェブアプリケーションで圧縮してください。
    echo.
    echo この画面は閉じてください。
    echo ---------------------------------------------------------------------------------------------
    pause
    exit
) else (
    goto :IMG
)

exit