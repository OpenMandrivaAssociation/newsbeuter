%define name	newsbeuter
%define version 2.0
%define release %mkrel 2

Summary:	RSS/Atom feed reader for text terminals
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	MIT
Group:		Networking/News
Url:		http://www.newsbeuter.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	stfl-devel
BuildRequires:	sqlite3-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncursesw-devel

%description
Newsbeuter is an open-source RSS/Atom feed reader for text
terminals. It runs on Linux, FreeBSD, Mac OS X and other Unix-like
operating systems. Newsbeuter's great configurability and vast number
of features make it a perfect choice for people that need a slick and
fast feed reader that can be completely controlled via keyboard.

A summary of some of its features:

* Subscribe to RSS 0.9x, 1.0, 2.0 and Atom feeds
* Download podcasts
* Freely configure your keyboard shortcuts
* Search through all downloaded articles
* Categorize and query your subscriptions with a flexible tag system
* Integrate any data source through a flexible filter and plugin
  system
* Automatically remove unwanted articles through a "killfile"
* Define "meta feeds" using a powerful query language
* Synchronize newsbeuter with your bloglines.com account
* Import and exporting your subscriptions with the widely used OPML
  format
* Freely define newsbeuter's look'n'feel through free color
  configurability and format strings

%prep
%setup -q

%build
%make

%install
%__rm -rf %{buildroot}
make DESTDIR=%{buildroot} prefix=/usr install

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES LICENSE README TODO doc/xhtml/*.html
%_bindir/*
%_datadir/locale/*
%_mandir/man1/*

