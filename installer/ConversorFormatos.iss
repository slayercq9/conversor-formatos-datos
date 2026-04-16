#define MyAppName "Conversor de Formatos Tabulares"
#define MyAppExeName "ConversorFormatos.exe"
#define MyAppPublisher "Fernando Corrales Quirós"
#ifndef MyAppVersion
  #define MyAppVersion "5.2.0"
#endif
#define MyAppURL "https://github.com/"
#define MySourceDir "..\\dist\\ConversorFormatos"

[Setup]
AppId={{8C249B2A-7032-4068-A67E-C351081E7BEE}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
DefaultDirName={autopf}\Conversor de Formatos Tabulares
DefaultGroupName=Conversor de Formatos Tabulares
DisableProgramGroupPage=yes
OutputDir=..\installer-output
OutputBaseFilename=ConversorFormatos-{#MyAppVersion}-setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
SetupIconFile=..\assets\icon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el escritorio"; GroupDescription: "Accesos directos opcionales:"

[Files]
Source: "{#MySourceDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\MANUAL_USUARIO.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\CHANGELOG.md"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\Conversor de Formatos Tabulares"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\Conversor de Formatos Tabulares"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Abrir Conversor de Formatos Tabulares"; Flags: nowait postinstall skipifsilent
