chcp 65001
@echo off

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
echo このバッチファイルを終了する場合は、e と入力してください。
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
    exit
) else (
    goto :A
)