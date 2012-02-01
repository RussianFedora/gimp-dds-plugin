Name:           gimp-dds-plugin
Version:        2.0.9
Release:        1%{?dist}.R
Summary:        A plugin for GIMP allows you to load/save in the DDS format
Summary(ru):    Плагин GIMP для работы с форматом DDS

License:        GPLv2+
URL:            http://code.google.com/p/gimp-dds/
Source0:        http://gimp-dds.googlecode.com/files/gimp-dds-%{version}.tar.bz2
Source100:      README.RFRemix

BuildRequires:  gimp-devel >= 2.4.0
BuildRequires:  pkgconfig

Requires:       gimp >= 2.4

%description
This is a plugin for GIMP version 2.6.x. It allows you to
load and save images in the Direct Draw Surface (DDS) format.

%description -l ru
Плагин для GIMP, помогающий загружать и сохранять изображения
в формате Direct Draw Surface (DDS).


%prep
%setup -q -n gimp-dds-%{version}


%build
sed -i 's|gimpui-2.0)|gimpui-2.0) -lm|' Makefile.linux
make %{?_smp_mflags}
cp %{SOURCE100} .


%install
rm -rf $RPM_BUILD_ROOT
GIMP_PLUGINS_DIR=`gimptool-2.0 --gimpplugindir`
mkdir -p $RPM_BUILD_ROOT$GIMP_PLUGINS_DIR/plug-ins
install dds $RPM_BUILD_ROOT$GIMP_PLUGINS_DIR/plug-ins


%files
%defattr(-,root,root,-)
%{_libdir}/gimp/2.0/plug-ins/dds
%doc COPYING LICENSE README README.RFRemix


%changelog
* Mon Jan 30 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 2.0.9-1.R
- initial release
