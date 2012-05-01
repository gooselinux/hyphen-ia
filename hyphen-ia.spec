Name: hyphen-ia
Summary: Interlingua hyphenation rules
%define upstreamid 20050628
Version: 0.%{upstreamid}
Release: 2.1%{?dist}
Source: http://www.ctan.org/get/language/hyphenation/iahyphen.tex
Group: Applications/Text
URL: http://www.ctan.org/tex-archive/help/Catalogue/entries/iahyphen.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LPPL
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Patch0: hyphen-ia-cleantex.patch

%description
Interlingua hyphenation rules.

%prep
%setup -T -q -c -n hyphen-ia
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl iahyphen.tex hyph_ia.dic ISO8859-1
echo "Created with substring.pl by substrings.pl iahyphen.tex hyph_ia.dic ISO8859-1" > README
echo "---" >> README
head -n 25 iahyphen.tex >> README

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_ia.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20050628-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050628-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 28 2009 Caolan McNamara <caolanm@redhat.com> - 0.20050628-1
- bump to next day for consistency

* Tue Mar 17 2009 Caolan McNamara <caolanm@redhat.com> - 0.20050627-1
- initial version
