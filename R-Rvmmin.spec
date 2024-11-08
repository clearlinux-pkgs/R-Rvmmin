#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Rvmmin
Version  : 2018.4.17.1
Release  : 45
URL      : https://cran.r-project.org/src/contrib/Rvmmin_2018-4.17.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Rvmmin_2018-4.17.1.tar.gz
Summary  : Variable Metric Nonlinear Function Minimization
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-optextras
BuildRequires : R-optextras
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n Rvmmin
cd %{_builddir}/Rvmmin

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641116549

%install
export SOURCE_DATE_EPOCH=1641116549
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rvmmin
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rvmmin
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rvmmin
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Rvmmin || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Rvmmin/DESCRIPTION
/usr/lib64/R/library/Rvmmin/INDEX
/usr/lib64/R/library/Rvmmin/Meta/Rd.rds
/usr/lib64/R/library/Rvmmin/Meta/demo.rds
/usr/lib64/R/library/Rvmmin/Meta/features.rds
/usr/lib64/R/library/Rvmmin/Meta/hsearch.rds
/usr/lib64/R/library/Rvmmin/Meta/links.rds
/usr/lib64/R/library/Rvmmin/Meta/nsInfo.rds
/usr/lib64/R/library/Rvmmin/Meta/package.rds
/usr/lib64/R/library/Rvmmin/Meta/vignette.rds
/usr/lib64/R/library/Rvmmin/NAMESPACE
/usr/lib64/R/library/Rvmmin/NEWS
/usr/lib64/R/library/Rvmmin/R/Rvmmin
/usr/lib64/R/library/Rvmmin/R/Rvmmin.rdb
/usr/lib64/R/library/Rvmmin/R/Rvmmin.rdx
/usr/lib64/R/library/Rvmmin/demo/broydt_test.R
/usr/lib64/R/library/Rvmmin/demo/cyq_test.R
/usr/lib64/R/library/Rvmmin/demo/genrose_test.R
/usr/lib64/R/library/Rvmmin/doc/Rvmmin.R
/usr/lib64/R/library/Rvmmin/doc/Rvmmin.Rmd
/usr/lib64/R/library/Rvmmin/doc/Rvmmin.html
/usr/lib64/R/library/Rvmmin/doc/index.html
/usr/lib64/R/library/Rvmmin/help/AnIndex
/usr/lib64/R/library/Rvmmin/help/Rvmmin.rdb
/usr/lib64/R/library/Rvmmin/help/Rvmmin.rdx
/usr/lib64/R/library/Rvmmin/help/aliases.rds
/usr/lib64/R/library/Rvmmin/help/paths.rds
/usr/lib64/R/library/Rvmmin/html/00Index.html
/usr/lib64/R/library/Rvmmin/html/R.css
/usr/lib64/R/library/Rvmmin/tests/BTbad.R
/usr/lib64/R/library/Rvmmin/tests/groseRvmmin.R
