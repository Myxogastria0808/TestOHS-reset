@echo off
cd TestOHS-reset
rem 本番は、TestOHS-main
rmdir /s /q .git
cd ..
rmdir /s /q TestOHS-reset
rem 本番は、TestOHS-main
cd check
cd TestOHS-reset
rem 本番は、TestOHS-main
rmdir /s /q .git
cd ..
rmdir /s /q TestOHS-reset
exit