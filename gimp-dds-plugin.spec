Name:           gimp-dds-plugin
Version:        2.1.0
Release:        2%{?dist}
Summary:        A plugin for GIMP allows you to load/save in the DDS format
Summary(ru):    Плагин GIMP для работы с форматом DDS

License:        GPLv2+
URL:            http://code.google.com/p/gimp-dds/
Source0:        http://gimp-dds.googlecode.com/files/gimp-dds-%{version}.tar.bz2
# Correct FSF address
# http://code.google.com/p/gimp-dds/issues/detail?id=17
Patch0:         gimp-dds-plugin-license.patch


BuildRequires:  gimp-devel >= 2.4.0
BuildRequires:  pkgconfig

Requires:       gimp >= 2.4

%description
This is a plugin for GIMP. It allows you to load and save images in the
Direct Draw Surface (DDS) format.

%description -l ru
Плагин для GIMP, помогающий загружать и сохранять изображения
в формате Direct Draw Surface (DDS).


%prep
%setup -q -n gimp-dds-%{version}
%patch0 -p1 -b .license


%build
make %{?_smp_mflags}


%install
GIMP_PLUGINS_DIR=`gimptool-2.0 --gimpplugindir`
mkdir -p $RPM_BUILD_ROOT$GIMP_PLUGINS_DIR/plug-ins
install dds $RPM_BUILD_ROOT$GIMP_PLUGINS_DIR/plug-ins


%files
%{_libdir}/gimp/2.0/plug-ins/dds
%doc COPYING LICENSE README


%changelog
* Mon Jul 16 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 2.1.0-2
- added patch for fix FSF address in sources

* Fri Jul 13 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 2.1.0-1
- initial release
