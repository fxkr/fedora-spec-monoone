%global fontname monoone
%global fontconf 60-%{fontname}.conf

%global commit 2af22693d64d95adecd81a15f2ec1a5683d34937
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           %{fontname}-fonts
Version:        20131001
Release:        1%{?dist}
Summary:        a monospaced font for programming and code review

Group:          User Interface/X
License:        OFL
URL:            https://github.com/madmalik/monoOne/
Source0:        https://github.com/madmalik/monoOne/archive/%{commit}.tar.gz
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description


%prep
%setup -c -q


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p monoOne-2af22693d64d95adecd81a15f2ec1a5683d34937/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf} *.otf

%doc


%changelog

