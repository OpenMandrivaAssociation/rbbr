%define name rbbr
%define version 0.6.0
%define release %mkrel 3

Summary: RuBy BRowser
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://ruby-gnome2.sourceforge.jp/hiki.cgi?rbbr
Source0: %{name}-%{version}-withapi.tar.bz2
Source1: %{name}-16.png.bz2
Source2: %{name}-32.png.bz2
Source3: %{name}-48.png.bz2
License: GPL
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby >= 1.8 ruby-gtk2 ruby-gettext
BuildRequires: ruby-devel ruby-gettext
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
rm -rf %buildroot
ruby install.rb install --prefix=%buildroot
%find_lang %name --all-name 

#menu
install -m 755 -d %buildroot%{_menudir}
cat << EOF > %buildroot%{_menudir}/%{name}
?package(%name): needs="x11" \
        section="More Applications/Development/Tools" \
        title="RBBR" \
        longtitle="RuBy BRowser" \
        command="%{_bindir}/%{name}" \
        icon="%{name}.png" \
	xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=RBBR
Comment=RuBy BRowser
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;Development;X-MandrivaLinux-MoreApplications-Development-Tools;
EOF

# icon
install -m 755 -d %buildroot{%{_miconsdir},%{_liconsdir}}
bzcat %{SOURCE1} > %buildroot%_miconsdir/%{name}.png
bzcat %{SOURCE2} > %buildroot%_iconsdir/%{name}.png
bzcat %{SOURCE3} > %buildroot%_liconsdir/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{ruby_sitelibdir}/%{name}*
%{_datadir}/%{name}
%{_menudir}/%name
%{_datadir}/applications/*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%doc README README.ja AUTHORS ChangeLog 


