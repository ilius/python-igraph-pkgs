Name: python3-igraph
Version: VRRSION
Release: 1
Summary: High performance graph data structures and algorithms (Python 3)

Group: 
License: GPLv2
URL: 

Requires: /usr/bin/python3.6 foo bar

BuildArch: x86_64

%description
This module extends Python with a Graph class which is capable of
handling arbitrary directed and undirected graphs with thousands of
nodes and millions of edges. Since the module makes use of the open
source igraph library written in almost 100% pure C, it is blazing
fast and outperforms most other pure Python-based graph packages
around.

%files
%defattr(-,root,root,-)
%{_prefix}/include/python3.6m/python-igraph/igraphmodule_api.h
%{_prefix}/lib64/python3.6/site-packages/igraph/*
%{_prefix}/lib64/python3.6/site-packages/python_igraph-0.7.1.post6-py3.6.egg-info/*
%{_prefix}/share/doc/packages/python3-igraph/COPYING

