Summary:	RSS/Atom feed reader for text terminals
Name:		newsbeuter
Version:	2.5
Release:	2
License:	MIT
Group:		Networking/News
Url:		http://www.newsbeuter.org
Source0:	%{name}-%{version}.tar.gz
Patch0:		newsbeuter-2.5-gcc4.7.patch
BuildRequires:	gettext-devel
BuildRequires:	stfl-devel
BuildRequires:	pkgconfig(json)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(sqlite3)

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
%patch0 -p1

%build
CXXFLAGS=-fpermissive %make prefix=%{_prefix}

%install
%makeinstall_std prefix=%{_prefix}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS CHANGES LICENSE README TODO doc/xhtml/*.html
%{_bindir}/*
%{_mandir}/man1/*

