%define name rbbr
%define version 0.6.0
%define release 9

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
Requires: ruby >= 1.8 ruby-gtk2 rubygem(gettext)
BuildRequires: ruby-devel rubygem(gettext)
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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{ruby_sitelibdir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%doc README README.ja AUTHORS ChangeLog 




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-7mdv2010.0
+ Revision: 433062
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-6mdv2009.0
+ Revision: 260089
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-5mdv2009.0
+ Revision: 247965
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.6.0-3mdv2008.1
+ Revision: 140744
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Sat Feb 10 2007 Pascal Terjan <pterjan@mandriva.org> 0.6.0-3mdv2007.0
+ Revision: 118808
- mkrel
- XDG menu
- Import rbbr

* Sat Jul 02 2005 Pascal Terjan <pterjan@mandriva.org> 0.6.0-2mdk
- fix lib64

* Mon Jun 21 2004 Pascal Terjan <pterjan@mandrake.org> 0.6.0-1mdk
- 0.6.0

* Mon Jun 14 2004 Pascal Terjan <pterjan@mandrake.org> 0.5.1-2mdk
- use real name...

