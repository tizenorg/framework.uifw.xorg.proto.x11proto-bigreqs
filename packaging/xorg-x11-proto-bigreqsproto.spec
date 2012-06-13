
Name:       xorg-x11-proto-bigreqsproto
Summary:    X.Org X11 Protocol bigreqsproto
Version:    1.1.1
Release:    1
Group:      Graphics/X Window System
License:    MIT
URL:        http://www.x.org
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-bigreqsproto.manifest 
Provides:   bigreqsproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .

%reconfigure --disable-static \
    --libdir=%{_datadir}

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}




%files
%manifest xorg-x11-proto-bigreqsproto.manifest
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/bigreqstr.h
%{_includedir}/X11/extensions/bigreqsproto.h
%{_datadir}/pkgconfig/bigreqsproto.pc

/usr/share/doc/bigreqsproto/*


