%define		_class		Text
%define		_subclass	Wiki_Mediawiki
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.2.0
Release:	6
Summary:	Mediawiki parser for Text_Wiki
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Text_Wiki/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Parses Mediawiki mark-up to tokenize the text for Text_Wiki renderings.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-4mdv2012.0
+ Revision: 742294
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3
+ Revision: 679598
- mass rebuild

* Wed Oct 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-2mdv2011.0
+ Revision: 587006
- proper summary and description

* Wed Oct 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2011.0
+ Revision: 586978
- import php-pear-Text_Wiki_Mediawiki

