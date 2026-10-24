@echo off
title Clauze AI Enterprise - Pre-Publication Firewall
color 0E
cls
echo ==============================================================================
echo    CLAUZE ENTERPRISE AI - AUTONOMOUS BRAND GOVERNANCE FIREWALL
echo    Hackathon Grand Prize Edition (1,000-Competitor Contender)
echo ==============================================================================
echo.
echo  Starting Clauze Enterprise AI Executable...
echo.

if exist "Clauze_Enterprise_AI.exe" (
    start Clauze_Enterprise_AI.exe
    echo  [OK] Clauze_Enterprise_AI.exe launched successfully!
    exit /b 0
)

echo  [NOTICE] Launching browser directly to index.html...
start index.html
exit /b 0
