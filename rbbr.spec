Summary: RuBy BRowser
Name:    rbbr
Version: 0.6.0
Release: 11
URL: http://ruby-gnome2.sourceforge.jp/hiki.cgi?rbbr
Source0: %{name}-%{version}-withapi.tar.bz2
Source1: %{name}-16.png.bz2
Source2: %{name}-32.png.bz2
Source3: %{name}-48.png.bz2
Source100: %{name}.rpmlintrc
License: GPL
Group: Development/Other
Requires: ruby >= 1.8
Requires: rubygem(gtk2)
Requires: rubygem(gettext)
BuildRequires: ruby-devel
BuildRequires: rubygem(gettext)
BuildArch: noarch
Obsoletes: ruby-rbbr
Provides: ruby-rbbr

%description
rbbr is a ruby application to browse modules/classes hierarchy and their
constants and methods.

%prep
%setup -q -n %{name}-%{version}-withapi

%build
ruby install.rb config
ruby install.rb setup

%install
ruby install.rb install --prefix=%{buildroot}
%find_lang %{name} --all-name 

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=RBBR
Comment=RuBy BRowser
Comment[ru]=Броузер классов и модулей Ruby
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;Development;X-MandrivaLinux-MoreApplications-Development-Tools;
EOF

# icon
install -m 755 -d %{buildroot}{%{_miconsdir},%{_liconsdir}}
bzcat %{SOURCE1} > %{buildroot}%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > %{buildroot}%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > %{buildroot}%{_liconsdir}/%{name}.png

%files -f %name.lang
%{_bindir}/*
%{ruby_sitelibdir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%doc README README.ja AUTHORS ChangeLog 
