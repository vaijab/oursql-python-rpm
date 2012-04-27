Summary: MySQL bindings for python
Name: oursql-python
Version: 0.9.3
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: https://launchpad.net/oursql

Source0: http://launchpad.net/oursql/trunk/%{version}/+download/oursql-%{version}.tar.bz2

BuildRoot: %{_tmppath}/oursql-%{version}-%{release}-root
BuildRequires: python-devel python-setuptools
BuildRequires: mysql-devel Cython
Requires: mysql-libs python

%description
Python interface to MySQL

oursql is a new set of MySQL bindings for python 2.4+, including python 3.x.
Here’s a short list of reasons why you should use oursql over MySQLdb:

- oursql has real parameterization, sending the SQL and data to MySQL
  completely separately.
- oursql allows text or binary data to be streamed into the database
  and streamed out of the database, instead of requiring everything
  to be buffered in the client.
- oursql can both insert rows lazily and fetch rows lazily.
- oursql has unicode support on by default.
- oursql supports python 2.4 through 2.7 without any deprecation warnings
  on 2.6+ (see PEP 218) and without completely failing on 2.7 (see PEP 328).
- oursql runs natively on python 3.x.
- oursql is licensed under the BSD license.

%prep
%setup -q -n oursql-%{version}

%build
#rm -f doc/*~
export libdirname=%{_lib}
CFLAGS="$RPM_OPT_FLAGS" python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

export libdirname=%{_lib}
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README CHANGELOG COPYING
%{_libdir}/python?.?/site-packages/oursql.so

%changelog

 * Releasing the GIL for a few more functions that query the remote mysql
   server, fixing launchpad bug #582124.

 * Fixing a memory leak caused by a half-finished code refactor.

 * Working around mysql sometimes returning invalid date data, fixing
   launchpad bug #672059.

