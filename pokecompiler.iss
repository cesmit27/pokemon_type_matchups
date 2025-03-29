[Setup]
AppName=Pokémon Type Matchups
AppVersion=1.0
DefaultDirName={pf}\PokemonTypeMatchups
DefaultGroupName=PokemonTypeMatchups
OutputBaseFilename=PokemonTypeMatchupsInstaller
Compression=lzma
SolidCompression=yes
UninstallDisplayName=Pokemon Type Matchups Uninstaller


[Files]
Source: "C:\Users\Colin\Downloads\test\build\exe.win-amd64-3.13\*"; DestDir: "{app}"; Flags: recursesubdirs

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"
Name: "startmenuicon"; Description: "Create a Start Menu icon"; GroupDescription: "Additional icons:"

[Icons]
Name: "{group}\Pokemon Type Matchups"; Filename: "{app}\poketest.exe"; Comment: "Launch Pokémon Type Matchups"; Tasks: startmenuicon
Name: "{commondesktop}\Pokemon Type Matchups"; Filename: "{app}\poketest.exe"; Comment: "Launch Pokémon Type Matchups"; Tasks: desktopicon

[Run]
Filename: "{app}\poketest.exe"; Description: "Launch Pokémon Type Matchups"; Flags: nowait postinstall
