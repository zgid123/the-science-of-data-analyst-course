---
id: S412
url: https://web.engr.oregonstate.edu/~tgd/publications/dietterich-approximate-statistical-tests-nc1998.pdf
requested: https://web.engr.oregonstate.edu/~tgd/publications/dietterich-approximate-statistical-tests-nc1998.pdf
fetched: 2026-11-06T23:13+07:00
tool: fetch.py (curl + pypdf; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: partial
task: T06
part: 4
raw: raw.pdf (265 KB)
conversion: pypdf of https://web.engr.oregonstate.edu/~tgd/publications/dietterich-approximate-statistical-tests-nc1998.pdf (partial, 10682 words)
---
<!-- page 1 -->
Appro ximate Statistical T ests for Comparing
Sup ervised Classi/cation Learning Algorithms
Thomas G/. Dietteric h
tgd/@cs/.orst/.edu
Departmen t of Computer Science
Oregon State Univ ersit y
Corv allis/, OR /9/7/3/3/1
Decem be r /3/0/, /1/9/9/7
Abstract
This pap er reviews /v e appro ximate statistical tests for determining whether one learning al/-
gorithm out/-p erforms another on a particular learning task/. These tests are compared exp eri/-
men tally to determine their probabilit y of incorrectly detecting a di/erence when no di/erence
exists /(t yp e I error/)/. Tw o widely/-used statistical tests are sho wn to ha v e high probabilit y of
T yp e I error in certain situations and should nev er b e used/. These tests are /(a/) a test for the
di/erence of t w o prop ortions and /(b/) a paired/-di/erences t test based on taking sev eral random
train//test splits/. A third test/, a paired/-di/erences t test based on /1/0/-fold cross/-v alidation/, ex/-
hibits somewhat elev ated probabilit yo f T yp e I error/. A fourth test/, McNemar/'s test/, is sho wn
to ha v e lo w T yp e I error/. The /fth test is a new test/, /5x/2cv/, based on /5 iterations of /2/-fold
cross/-v alidation/. Exp erimen ts sho w that this test also has acceptable T yp e I error/. The pap er
also measures the po w er /(abilit y to detect algorithm di/erences when they do exist/) of these
tests/. The cross/-v alidated t test is the most po w erful/. The /5x/2cv test is sho wn to b e sligh tly
more po w erful than McNemar/'s test/. The c hoice of the b est test is determined b y the com/-
putational cost of running the learning algorithm/. F or algorithms that can be executed only
once/, McNemar/'s test is the only test with acceptable T yp e I error/. F or algorithms that can
b e executed ten times/, the /5x/2cv test is recommended/, b ecause it is sligh tly more p o w erful and
b ecause it directly measures v ariation due to the c hoice of training set/.
/1

<!-- page 2 -->
/1 In tro duction
In the researc h/, dev elopmen t/, and application of mac hine learning algorithms for classi/cation
tasks/, man y questions arise for whic h statistical metho ds are needed/. The purp ose of this pap er is
to in v estigate one of these questions/, demonstrate that existing statistical metho ds are inadequate
for this question/, and prop ose a new statistical test that sho ws acceptable p erformance in initial
exp erimen ts/.
T o understand the question raised in this pap er/, it is helpful to consider a taxonom y of the
di/eren t kinds of statistical questions that arise in mac hine learning/. Figure /1 giv es a taxonom yo f
nine statistical questions/.
Let us b egin at the ro ot of the tree/. The /rst issue w em ust consider is whether w e are studying
only a single application domain or whether w e are studying m ultiple domains/. In most applied
researc h/, there is a single domain of in terest/, and our goal is to /nd the b est classi/er or the b est
learning algorithm to apply in that domain/. Ho w ev er/, a fundamen tal goal of researc h in mac hine
learning is to /nd learning algorithms that w ork w ell o v er a wide range of application domains/. W e
will return to this issue b elo w/;; for the momen t/, let us consider the single/-domain case/.
Within a single domain/, there are t w o di/eren t sets of questions dep ending on whether w ea r e
analyzing classi/ers or algorithms/. A classi/er is a function that/, giv en an input example/, assigns
that example to one of K classes/. A learning algorithm is a function that/, giv en a set of examples
and their classes/, constructs a classi/er/. In a particular application setting/, our primary goal is
usually to /nd the b est classi/er and estimate its accuracy on future examples/. F or example/,
supp ose w e are w orking for a medical instrumen tation compan y and w e wish to man ufacture and
sell an instrumen t for classifying blo o d cells/. A t the time w e are designing the instrumen t/, w e could
gather a large collection of blo o d cells and ha v e ah uman exp ert classify eac h cell/. W e could then
apply a learning algorithm to pro duce a classi/er from this set of classi/ed cells/. The classi/er
w ould be implemen ted in the instrumen t and sold/. W e w an t our instrumen t to con tain the most
accurate classi/er w e can /nd/.
There are some applications/, ho w ev er/, where w em ust select the b est learning algorithm rather
than /nding the b est classi/er/. F or example/, supp ose w e w an t to sell an electronic mail system
that learns to recognize and /lter junk mail/. Whenev er the user receiv es an email message that
they consider junk mail/, they will /
ag that message/. P erio dically /, a learning algorithm included
in the program will analyze the accum ulated examples of junk and non/-junk email and up date its
/ltering rules/. Our job is to determine whic h learning algorithm to include in the program/.
The next lev el of the taxonom y distinguishes be t w een t w o fundamen tal tasks/: estimating ac/-
curacy and c ho osing b et w een classi/ers /(or algorithms/)/. When w e mark et our blo o d cell diagnosis
system/, w e w ould lik e to mak e a claim ab out its accuracy /. Ho w can w e measure this accuracy/?
And of course/, when w e design the system/, w ew an t to c ho ose the b est classi/er from some set of
a v ailable classi/ers/.
The lo w est lev el of the taxonom y concerns the amoun t of data a v ailable/. If w e ha v e a large
amoun t of data/, then w e can set some of it aside to serv e as a test set for ev aluating classi/ers/.
Muc h simpler statistical metho ds can be applied in this case/. Ho w ev er/, in most situations/, the
amoun t of data is limited and w e need to use all of it as input to our learning algorithms/. This
means that w em ust use some form of resampling /(i/.e/./, cross/-v alidation or the b o otstrap/) to p erform
the statistical analysis/.
No w that w e ha v e review ed the general structure of the taxonom y /, let/'s consider the nine
statistical questions/. W e assume that all data po i n ts /(examples/) are dra wn indep enden tly from a
/xed probabilit y distribution de/ned b y the particular application problem/.
Question /1/: Supp ose w e are giv en a large sample of data and a classi/er C /. The classi/er C ma y
/2

<!-- page 3 -->
small
sample
large
sample
small
sample
large
sample
small
sample
large
sample
small
sample
large
sample
predict choose
analyze algorithms
single domain multiple domains
9
predict choose
analyze classifiers
classifier
accuracy
between
classifiers
algorithm
accuracy
between
algorithms
12345678
Figure /1/: A taxonom y of statistical questions in mac hine learning/. The b o xed no de /(Question /8/)
is the sub ject of this pap er/.
ha v e be e n constructed using part of the data/, but there is enough data remaining for a separate
test set/. Hence/, w e can measure the accuracy of C on the test set and construct a binomial
con/dence in terv al /(Snedecor /& Co c hran/, /1/9/8/9/;; Efron /& Tibshirani/, /1/9/9/3/;; Koha vi/, /1/9/9/5/)/. Note
that in Question /1/, the classi/er could ha v e be e n pro duced b y an y metho d /(e/.g/./, in terviewing an
exp ert/)/;; it need not ha v e b een pro duced b y a learning algorithm/.
Question /2/: Giv en a small data set/, S /,s u p p o s e w e apply learning algorithm A to S to construct
classi/er C
A
/;; ho w accurately will C
A
classify new examples/? Because w e ha v e no separate test
set/, there is no direct w a y to answ er this question/. A frequen tly/-applied strategy is to con v ert
this question in to Question /6/: Can w e predict the accuracy of algorithm A when it is trained on
randomly/-selected data sets of /(appro ximately/) the same size as S /? If so/, then w e can predict the
accuracy of C
A
whic hw as obtained from training on S /.
Question /3/: Giv en t w o classi/ers C
A
and C
B
and enough data for a separate test set/, determine
whic h classi/er will be more accurate on new test examples/. This question can be answ ered b y
measuring the accuracy of eac h classi/er on the separate test set and applying McNemar/'s test/,
whic h will b e describ ed b elo w/.
Question /4/: Giv en t w o classi/ers C
A
and C
B
pro duced b y feeding a small data set S to t w o
learning algorithms A and B /, whic h classi/er will b e more accurate in classifying new examples/?
Again/, b ecause w e ha v e no separate set of test data/, w e cannot answ er this question directly /.
Again/, some researc hers ha v et a k en the approac ho f c o n v erting this problem in to a question ab out
learning algorithms /(Question /8/)/. If w e can determine whic h algorithm usually pro duces more
accurate classi/ers /(when trained on data sets of appro ximately the same size/)/, then w e can select
/3

<!-- page 4 -->
the classi/er /( C
A
or C
B
/) created b y that algorithm/.
Question /5/: Giv en a learning algorithm A and a large data set S /, what is the accuracy of the
classi/ers pro duced b y A when trained on new training sets of a sp eci/ed size m /? This question
has not receiv ed m uc h atten tion in the literature/. One approac h/, adv o cated b y the DEL VE pro ject
/(Hin ton/, Neal/, Tibshirani/, /& DEL VE team mem b ers/, /1/9/9/5/;; Rasm ussen/, /1/9/9/6/)/, is to sub divide S
in to a test set and sev eral disjoin t training sets of size m /. Then A is trained on eac h of the training
sets and the resulting classi/ers are tested on the test set/. The a v erage p erformance on the test set
estimates the accuracy of new runs/.
Question /6/: Giv en a learning algorithm A and a small data set S /,w h a t i s t h e accuracy of the
classi/ers pro duced b y A when A is trained on new training sets of the same size as S /? Koha vi
/(/1/9/9/5/) sho ws that strati/ed /1/0/-fold cross/-v alidation pro duces fairly go o d estimates in this case/.
Note that in an y resampling approac h/, w e cannot train A on training sets of exactly the same size
as S /. Instead/, w e train on data sets that ha v e sligh tly few er examples /(e/.g/./, /9/0/% of the size of S in
/1/0/-fold cross/-v alidation/) and rely on the assumption that the p erformance of learning algorithms
c hanges smo othly with c hanges in the size of the training data/. This assumption can be c hec k ed
exp erimen tally /(b y p erforming additional cross/-v alidation studies/) with ev en smaller training sets/,
but it cannot b e c hec k ed directly for training sets of the size of S /. Results on the shap e of learning
curv es sho w that in some cases this smo othness assumption will be violated /(Haussler/, Kearns/,
Seung/, /& Tish b y /, /1/9/9/4/)/. Nonetheless/, it is observ ed to hold exp erimen tally in most applications/.
Question /7/: Giv en t w o learning algorithms A and B and a large data set S /, whic h algorithm
will pro duce more accurate classi/ers when trained on data sets of a sp eci/ed size m /? This question
has not receiv ed m uc h atten tion/, although the DEL VE team has studied this question for regression
problems/. They divide S in to sev eral disjoin t training sets and a single test set/. Eac h algorithm is
trained on eac h training set/, and all resulting classi/ers are tested on the test set/. An analysis of
v ariance can then b e p erformed that includes terms for the c hoice of learning algorithm/, the c hoice
of the training set/, and eac h individual test example/. The Quasi/- F test /(Lindman/, /1/9/9/2/) is applied
to determine whether the e/ect due to the c hoice of learning algorithms is signi/can tly non/-zero/.
Question /8/: Giv en t w o learning algorithms A and B and a small data set S /,w h i c h algorithm will
pro duce more accurate classi/ers when trained on data sets of the same size as S /? The purp ose of
this pap er is to describ e and compare sev eral statistical tests for answ ering this question/. Because
S is small/, it will b e necessary to use holdout and resampling metho ds/. As men tioned in Question
/6 ab o v e/, this means that w e cannot answ er this question exactly without making the assumption
that the p erformance of the t w o learning algorithms c hanges smo othly with c hanges in the size of
the training set/. Sp eci/cally /,w e will need to assume that the relativ e di/erence in p erformance of
the t w o algorithms c hanges slo wly with c hanges in the size of the training set/.
Question /9/: Giv en t w o learning algorithms A and B and data sets from sev eral domains/, whic h
algorithm will pro duce more accurate classi/ers when trained on examples from new domains/? This
is p erhaps the most fundamen tal and di/cult question in mac hine learning/. Some researc hers ha v e
applied a simple sign test /(or the Wilco xon signed/-ranks test/) to try to answ er this question/, based
on single runs or cross/-v alidation/-based estimates/, but these tests do not tak e in to accoun t the
uncertain t y of the individual comparisons/. E/ectiv ely /,w ew an tt oc o m bine the results from sev eral
answ ers to Question /8/, where eac h answ er has an asso ciated uncertain t y /. This is an imp ortan t
question for future researc h/.
Questions /7/, /8/, and /9 are the most imp ortan t for exp erimen tal researc h on learning algorithms/.
When someone dev elops a new learning algorithm /(or a mo di/cation to an existing algorithm/)/,
answ ers to these questions can determine whether the new algorithm is b etter than existing algo/-
rithms/. Unfortunately /,m a n y data sets used in exp erimen tal researc h are to o small to allo w p osing
Question /7/. Hence/, this pap er fo cuses on dev elop ed go o d statistical tests for Question /8/. W e de/ne
/4

<!-- page 5 -->
and compare /v e statistical tests for this question/.
Before pro ceeding with the deriv ation of these statistical tests/, it is w orth noting that eac h of
the questions po s e d ab o v e can be extended be y ond classi/cation algorithms and misclassi/cation
rates/. F or example/, in man y decision/-making settings/, it is imp ortan tt o estimate the conditional
probabilit y that a new example b elongs to eac h of the K classes/. One measure of the accuracy of
probabilit y estimates is the log loss/, and Questions /1/, /2/, /5/, and /6 can all b e rephrased in terms of
determining the exp ected log loss of a classi/er or an algorithm/. Similarly /, Questions /3/, /4/, /7/, and
/8 can be rephrased in terms of determining whic h classi/er or algorithm has the smaller log loss/.
W ea r e u n a w are of an y statistical researc h sp eci/cally addressing these questions in the case of log
loss/, ho w ev er/.
In man y neural net w ork applications/, the task is to predict a con tin uous resp onse v ariable/.
In these problems/, the squared error is usually the natural loss function/, and Questions /1/, /2/, /5/,
and /6 can be rephrased in terms of determining the exp ected mean squared error of a predictor
or of an algorithm/. Similarly /, Questions /3/, /4/, /7/, and /8 can be rephrased in terms of determining
whic h predictor or algorithm has the smaller mean squared error/. Question /1 can b e addressed b y
constructing a con/dence in terv al based on the normal or t distribution /(dep ending on the size of
the test set/)/. Question /3 can be addressed b y constructing a con/dence in terv al for the exp ected
di/erence/. As men tioned ab o v e/, The DEL VE pro ject has dev elop ed analysis of v ariance tec hniques
for Questions /5 and /7/. Appropriate statistical tests for the small sample questions /(/2/, /4/, /6/, and /8/)
are still not w ell established/.
The statistical tests for regression metho ds ma y suggest w a ys of designing statistical tests for
the log loss case/. This is an imp ortan t area for future researc h/.
T o design and ev aluate statistical tests/, the /rst step is to iden tify the sources of v ariation that
m u s tb ec o n trolled b ye a c h test/. F or the case w e are considering/, there are four imp ortan t sources
of v ariation/.
First/, there is the random v ariation in the selection of the test data that is used to ev aluate
the learning algorithms/. On an y particular randomly/-dra wn test data set/, one classi/er ma y out/-
p erform another ev en though on the whole p opulation the t w o classi/ers w ould p erform iden tically /.
This is a particularly pressing problem for small test data sets/.
The second source of random v ariation results from the selection of the training data/. On an y
particular randomly/-dra wn training set/, one algorithm ma y out/-p erform another ev en though/, on
the a v erage/, the t w o algorithms ha v e the same accuracy /. Ev en small c hanges to the training set
/(suc h as adding or deleting a few data p oin ts/) ma y cause large c hanges in the classi/er pro duced
b y a learning algorithm/. Breiman /(/1/9/9/4/, /1/9/9/6/) has called this be h a vior /\instabilit y/"/, and he has
sho wn that this is a serious problem for the decision tree algorithms/, suc h as CAR T /(Breiman/,
F riedman/, Olshen/, /& Stone/, /1/9/8/4/)/.
A third source of v ariance can be in ternal randomness in the learning algorithm/. Consider/,
for example/, the widely/-used bac kpropagation algorithm for training feed/-forw ard neural net w orks/.
This algorithm is usually initialized with a set of random w eigh ts whic h it then impro v es/. The
resulting learned net w ork dep ends critically on the random starting state /(Kolen /& P ollac k/, /1/9/9/1/)/.
In this case/, ev en if the training data are not c hanged/, the algorithm is lik ely to pro duce a di/eren t
h yp othesis if it is executed again from a di/eren t random starting state/.
The last source of random v ariation that m ust b e handled b y statistical tests is random classi//-
cation error/. If a /xed fraction / of the test data p oin ts are randomly mislab eled/, then no learning
algorithm can ac hiev e an error rate of less than / /.
A go o d statistical test should not be fo oled b y these sources of v ariation/. The test should
conclude that the t w o algorithms are di/eren t if and only if their p ercen tage of correct classi/cations
w ould b e di/eren t/, on the a v erage/, when trained on a training set o fag i v en /xed size and tested
/5

<!-- page 6 -->
on all data p oin ts in the p opulation/.
T o accomplish this/, a statistical testing pro cedure m ust accoun t for these sources of v ariation/.
T o accoun t for test/-data v ariation and the p ossibilit y of random classi/cation error/, the statistical
pro cedure m ust consider the size of the test set and the consequences of c hanges in the test set/.
T o accoun t for training/-data v ariation and in ternal randomness/, the statistical pro cedure m ust
execute the learning algorithm m ultiple times and measure the v ariation in accuracy of the resulting
classi/ers/.
This pap er b egins b y describing /v e statistical tests b earing on Question /8/: McNemar/'s test/,
a test for the di/erence of t w o prop ortions/, the resampled t test/, the cross/-v alidated t test/, and a
new test called the /5x/2cv test/. The pap er then describ es a sim ulation study that seeks to measure
the probabilit y that eac h test will incorrectly detect a di/erence when no di/erence exists /(T yp e
I error/)/. The results of the sim ulation study sho w that only McNemar/'s test/, the cross/-v alidated
t test/, and the /5x/2cv test ha v e acceptable T yp e I error/. The T yp e I error of the resampled t test
is v ery bad and the test is v ery exp ensiv e computationally /, so w e do not consider it further/. The
T yp e I error of the di/erence/-of/-prop ortions test is unacceptable in some cases/, but it is v ery c heap
to ev aluate/, so w e retained it for further study /.
The sim ulation study is somewhat idealized and do es not address all asp ects of training/-data
v ariation/. T o obtain a more realistic ev aluation of the four remaining tests/, w e conducted a set of
exp erimen ts using real learning algorithms on realistic data sets/. W e measured bo t h the T yp e I
error and the po w er of the tests/. The results sho w that the cross/-v alidated t test has consisten tly
elev ated T yp e I error/. The di/erence/-of/-prop ortions test has acceptable t yp e I error/, but lo wp o w er/.
Both of the remaining t w o tests ha v e go o d T yp e I error and reasonable po w er/. The /5x/2cv test is
sligh tly more p o w erful than McNemar/'s test/, but also ten times more exp ensiv e to p erform/. Hence/,
the pap er concludes that the /5x/2cv test is the test of c hoice for inexp ensiv e learning algorithms/,
but that McNemar/'s test is b etter for more exp ensiv e algorithms/. Lisp co de implemen ting bo t h
tests is a v ailable from the author/.
/2 F ormal Preliminaries
W e will assume that there exists a set X of p ossible data p oin t s /,c a l l e dt h e p opulation /. There also
exists some tar get function /, f that classi/es eac h x /2 X in to one of K classes/. Without loss of
generalit y /, w e will assume that K /=/2 /, although none of the results in this pap er dep end on this
assumption/, since our only concern will b e whether an example is classi/ed correctly or incorrectly /.
In an application setting/, a sample S is dra wn randomly from X according to a /xed probabilit y
distribution D /. A collection of tr aining examples is constructed b y lab eling eac h x /2 S according
to f /( x /)/. Eac h training example therefore has the form h x/;; f /( x /) i /. In some applications/, there ma y
b e a source of classi/cation noise that randomly sets the lab el to an incorrect v alue/.
A learning algorithm A tak es as input a set of training examples R and outputs a classi/er
/^
f /.
The true error rate of that classi/er is the probabilit y that
/^
f will misclassify an example dra wn
randomly from X according to D /. In practice/, this error rate is estimated b y taking our a v ailable
sample S and sub dividing it in to a training set R and a test set T /. The error rate of
/^
f on T
pro vides an estimate of the true error rate of
/^
f on the p opulation/, X /.
The n ull h yp othesis to b e tested is that for a randomly dra wn training set R of /xed size/, the
t w o learning algorithms will ha v e the same error rate on a test example randomly/-dra wn from X /,
where all random dra ws are made according to distribution D /. Let
/^
f
A
b e the classi/er output b y
algorithm A trained on training set R /, and let
/^
f
B
b e the classi/er output b y algorithm B trained
/6

<!-- page 7 -->
on R /. Then the n ull h yp othesis can b e written as
Pr
R/;;x
/[
/^
f
A
/( x /)/= f /( x /)/] /= Pr
R/;;x
/[
/^
f
B
/( x /)/= f /( x /)/] /;;
where the notation Pr
R/;;x
indicates the probabilit yt a k en with resp ect to the random dra ws of the
training set R and the test example x /.
/3 Fiv e Statistical T ests
W en o w describ e the statistical tests that are the main sub ject of this pap er/. W e b egin with simple
holdout tests and then consider tests based on resampling from the a v ailable data/.
/3/./1 McNemar/'s test
T o apply McNemar/'s test /(Ev eritt/, /1/9/7/7/)/, w e divide our a v ailable sample of data S /,i n to a training
set R and a test set T /. W e train b oth algorithms A and B on the training set yielding classi/ers
/^
f
A
and
/^
f
B
/. W e then test these classi/ers on the test set/. F or eac h example x /2 T /,w e record ho w
it w as classi/ed and construct the follo wing con tingency table/:
n um b er of examples
 n um b er of examples
misclassi/ed b yb o t h
/^
f
A
and
/^
f
B
misclassi/ed b y
/^
f
A
but not b y
/^
f
B
n um b er of examples
 n um b er of examples
misclassi/ed b y
/^
f
B
but not b y
/^
f
A
misclassi/ed b yn e i t h e r
/^
f
A
nor
/^
f
B
/.
W e will use the notation
n
/0/0
n
/0/1
n
/1/0
n
/1/1
where n /= n
/0/0
/+ n
/0/1
/+ n
/1/0
/+ n
/1/1
is the total n um b er of examples in the test set T /.
Under the n ull h yp othesis/, the t w o algorithms should ha v e the same error rate/, whic h means that
n
/0/1
/= n
/1/0
/. McNemar/'s test is based on a /
/2
test for go o dness/-of/-/t that compares the distribution
of coun ts exp ected under the n ull h yp othesis to the observ ed coun ts/. The exp ected coun ts under
the n ull h yp othesis are
n
/0/0
/( n
/0/1
/+ n
/1/0
/) /= /2
/( n
/0/1
/+ n
/1/0
/) /= /2
 n
/1/1
The follo wing statistic is distributed /(appro ximately/) as /
/2
with /1 degree of freedom/;; it incor/-
p orates a /\con tin uit y correction/" term /(of /; /1 in the n umerator/) to accoun t for the fact that the
statistic is discrete while the /
/2
distribution is con tin uous/:
/( j n
/0/1
/; n
/1/0
j/; /1/)
/2
n
/0/1
/+ n
/1/0
/:
If the n ull h yp othesis is correct/, then the probabilit y that this quan tit y is greater than /
/2
/1 /;; /0 /: /9/5
/=
/3 /: /8/4/1/4/5/9 is less than /0/./0/5/. So w em a y reject the n ull h yp othesis in fa v or of the h yp othesis that the
t w o algorithms ha v e di/eren t p erformance when trained on the particular training set R /.
Note ho w ev er/, that this test has t w o shortcomings with regard to Question /8/. First/, it do es
not directly measure v ariabilit y due to the c hoice of the training set or the in ternal randomness of
/7

<!-- page 8 -->
the learning algorithm/. A single training set R is c hosen/, and the algorithms are only compared
using that training set/. Hence/, McNemar/'s test should only b e applied if w e be l i e v e these sources
of v ariabilit y are small/. Second/, it do es not directly compare the p erformance of the algorithms on
training sets of size j S j /, but only on sets of size j R j /, whic hm ust b e substan tially smaller than j S j
to ensure a su/cien tly large test set/. Hence/, w em ust assume that the relativ e di/erence observ ed
on training sets of size j R j will still hold for training sets of size j S j /.
/3/./2 A test for the di/erence of t w o prop ortions
A second simple statistical test is based on measuring the di/erence be t w een the error rate of
algorithm A and the error rate of algorithm B /(Snedecor /& Co c hran/, /1/9/8/9/)/. Sp eci/cally /, let
p
A
/=/( n
/0/0
/+ n
/0/1
/) /=n b e the prop ortion of test examples incorrectly classi/ed b y algorithm A and let
p
B
/=/( n
/0/0
/+ n
/1/0
/) /=n b e the prop ortion of test examples incorrectly classi/ed b y algorithm B /. The
assumption underlying this statistical test is that when algorithm A classi/es an example x from
t h et e s ts e t T /, the probabilit y of misclassi/cation is p
A
/. Hence/, the n um b er of misclassi/cations of
n test examples is a binomial random v ariable with mean np
A
and v ariance p
A
/(/1 /; p
A
/) n /.
The binomial distribution can be w ell/-appro ximated b y a normal distribution for reasonable
v alues of n /. F urthermore/, the di/erence be t w een t w o indep endent normally distributed random
v ariables is itself normally distributed/. Hence/, the quan tit y p
A
/; p
B
can be view ed as normally
distributed if w e assume that the measured error rates p
A
and p
B
are indep enden t/. Under the n ull
h yp othesis/, this will ha v e a mean of zero and a standard error of
se /=
s
/2 p /(/1 /; p /)
n
where p /=/( p
A
/+ p
B
/) /= /2i s t h e a v erage of the t w o error probabilities/.
F rom this analysis/, w e obtain the statistic
z /=
p
A
/; p
B
p
/2 p /(/1 /; p /) /=n
whic h has /(appro ximately/) a standard normal distribution/. W e can reject the n ull h yp othesis if
j z j />Z
/0 /: /9/7/5
/=/1 /: /9/6 /(for a /2/-sided test with probabilit yo f incorrectly rejecting the n ull h yp othesis
of /0/./0/5/)/.
This test has b een used b ym a n y researc hers including the author /(Dietteric h/, Hild/, /& Bakiri/,
/1/9/9/5/)/. Ho w ev er/, there are sev eral problems with this test/. First/, b ecause p
A
and p
B
are eac h
measured on the same test set T /, they are not indep enden t/. Second/, the test shares the dra wbac ks of
McNemar/'s test/: it do es not measure v ariation due to the c hoice of training set or in ternal v ariation
of the learning algorithm and it do es not directly measure the p erformance of the algorithms on
training sets of size j S j /, but rather on the smaller training set of size j R j /.
The lac k of indep endence of p
A
and p
B
can b e corrected b yc hanging the estimate of the standard
error to b e
se
/0
/=
r
n
/0/1
/+ n
/1/0
n
/2
/:
This estimate fo cuses on the probabilit y of disagreemen t of the t w o algorithms /(Snedecor /&
Co c hran/, /1/9/8/9/)/. The resulting z statistic can b e written as
z
/0
/=
j n
/0/1
/; n
/1/0
j/; /1
p
n
/0/1
/+ n
/1/0
/;;
/8

<!-- page 9 -->
whic hw e can recognize as the square ro ot of the /
/2
statistic in McNemar/'s test/.
In this pap er/, w e ha v e exp erimen tally analyzed the uncorrected z statistic/, since this statistic
is in curren t use and w ew an ted to determine ho w badly the /(incorrect/) indep endence assumption
a/ects the accuracy of the test/.
F or small sample sizes/, there are exact v ersions of bo t h McNemar/'s test and the test for the
di/erence of t w o prop ortions that a v oid the /
/2
and normal appro ximations/.
/3/./3 The resampled paired t test
The next statistical test w e consider is curren tly the most p opular in the mac hine learning literature/.
A series of /(usually/) /3/0 trials is conducted/. In eac h trial/, the a v ailable sample S is randomly divided
in to a training set R of a sp eci/ed size /(e/.g/./, t ypically t w o thirds of the data/) and a test set T /.
Learning algorithms A and B are b oth trained on R and the resulting classi/ers are tested on T /.
Let p
/( i /)
A
/(resp ectiv ely /, p
/( i /)
B
/) be the observ ed prop ortion of test examples misclassi/ed b y algorithm
A /(resp ectiv ely B /) during trial i /. If w e assume that the /3/0 di/erences p
/( i /)
/= p
/( i /)
A
/; p
/( i /)
B
w ere dra wn
indep enden tly from a normal distribution/, then w e can apply Studen t/'s t test/, b y computing the
statistic
t /=
p /
p
n
r
P
n
i /=/1
/( p
/( i /)
/;
 p /)
/2
n /; /1
/;;
where
 p /=
/1
n
P
n
i /=/1
p
/( i /)
/. Under the n ull h yp othesis/, this statistic has a t distribution with n /; /1
degrees of freedom/. F or /3/0 trials/, the n ull h yp othesis can b e rejected if j t j />t
/2/9 /;; /0 /: /9/7/5
/=/2 /: /0/4/5/2/3/.
There are man y p oten tial dra wbac ks of this approac h/. First/, as observ ed ab o v e/, the individual
di/erences p
/( i /)
will not ha v e a normal distribution/, b ecause p
/( i /)
A
and p
/( i /)
B
are not indep enden t/.
Second/, the p
/( i /)
/'s are not indep enden t/, b ecause the test sets in the trials o v erlap /(and the training
sets in the trials o v erlap as w ell/)/. W e will see be l o w that these violations of the assumptions
underlying the t test cause sev ere problems that mak e this test unsafe to use/.
/3/./4 The k /-fold cross/-v alidated paired t test
This test is iden tical to the previous one except that instead of constructing eac h pair of training
and test sets b y randomly dividing S /, w e instead randomly divide S in to k disjoin t sets of equal
size/, T
/1
/,/. /. /. /, T
k
/. W e then conduct k trials/. In eac h trial/, the test set is T
i
/, and the training set is
the union of all of the other T
j
/;;j /6/= i /. The same t statistic is computed/.
The adv an tage of this approac hi s t h a te a c h test set is indep enden t of the others/. Ho w ev er/, this
test still su/ers from the problem that the training sets o v erlap/. In a /1/0/-fold cross/-v alidation/, eac h
pair of training sets shares /8/0/% of the examples/. This o v erlap ma y prev en t this statistical test from
obtaining a go o d estimate of the amoun t of v ariation that w ould be observ ed if eac h training set
w ere completely indep enden t of previous training sets/.
T o illustrate this po i n t/, consider the nearest neigh bo r algorithm/. Supp ose our training set
con tains t w o clusters of p oin ts/: a large cluster b elonging to one class and a small cluster b elonging
to the other class/. If w e p erform a /2/-fold cross/-v alidation/, w e m ust sub divide this training data
in to t w o disjoin t sets/. If all of the p oin ts in the smaller cluster go in to one of those t w o sets/, then
b oth runs of the nearest neigh b or algorithm will ha v e elev ated error rates/, b ecause when the small
cluster is in the test set/, ev ery po i n t in it will be misclassi/ed/. When the small cluster is in the
training set/, some of its p oin ts ma y /(incorrectly/) b e treated as nearest neigh b ors of test set p oin ts/,
whic h also increases the error rate/. Con v ersely /, if the small cluster is ev enly divided b et w een the
t w o sets/, then the error rates will impro v e/, b ecause for eac h test p oin t there will b e a corresp onding
/9

<!-- page 10 -->
nearb y training p oin tt h a t will pro vide the correct classi/cation/. Either w a y /, w e can see that the
p erformance of the t w o folds of the cross/-v alidation will b e correlated rather than indep enden t/.
W ev eri/ed this exp erimen tally for /1/0/-fold cross/-v alidation on the Letter Recognition task /(/3/0/0
total training examples/) in an exp erimen t where the n ull h yp othesis w as true /(describ ed be l o w/)/.
W e measured the correlation co e/cien t be t w een the di/erences in error rates on t w o folds within
a cross/-v alidation/, p
/( i /)
and p
/( j /)
/. The observ ed v alue w as /0/./0/3/7/7/8/, whic h according to a t test is
signi/can tly di/eren t from /0 with p/< /1/0
/; /1/0
/. On the other hand/, if the error rates p
/( i /)
and p
/( j /)
are
dra wn from indep enden t /1/0/-fold cross/-v alidations /(i/.e/./, on indep enden td a t a sets/)/, the correlation
co e/cien ti s /; /0 /: /0/0/0/1/4 /;; whic h according to a t test is not signi/can tly di/eren t from zero/.
/3/./5 The /5x/2cv paired t test
In some initial exp erimen ts with the k /-fold cross/-v alidated paired t test/, w e attempted to determine
wh yt h e t statistic w as to o large in some cases/. The n umerator of the t statistic estimates the mean
di/erence in the p erformance of the t w o algorithms /(o v er the k folds/)/, while the denominator
estimates the v ariance of these di/erences/. With syn thetic data/, w e constructed k non/-o v erlapping
training sets and measured the mean and v ariance on those training sets/. W e found that while the
v ariance w as sligh tly underestimated when the training sets o v erlapp ed/, the means w ere o ccasionally
v ery p o orly estimated/, and this w as the cause of the large t v alues/. The problem can b e traced to
the correlations b et w een the di/eren t folds as describ ed ab o v e/.
W e found that if w e replaced the n umerator of the t statistic with the observ ed di/erence from
a single fold of the k /-fold cross/-v alidation/, the statistic b ecame w ell/-b eha v ed/. This led us to the
/5x/2cv paired t test/.
In this test/, w e p erform /5 replications of /2/-fold cross/-v alidation/. In eac h replication/, the a v ailable
data are randomly partitioned in to t w o equal/-sized sets S
/1
and S
/2
/. Eac h learning algorithm /( A
or B /) is trained on eac h set and tested on the other set/. This pro duces four error estimates/: p
/(/1/)
A
and p
/(/1/)
B
/(trained on S
/1
and tested on S
/2
/) and p
/(/2/)
A
and p
/(/2/)
B
/(trained on S
/2
and tested on S
/1
/)/.
Subtracting corresp onding error estimates giv es us t w o estimated di/erences p
/(/1/)
/= p
/(/1/)
A
/; p
/(/1/)
B
and
p
/(/2/)
/= p
/(/2/)
A
/; p
/(/2/)
B
/. F rom these t w o di/erences/, the estimated v ariance is s
/2
/=/( p
/(/1/)
/;
 p /)
/2
/+/( p
/(/2/)
/;
 p /)
/2
/,
where
 p /=/( p
/(/1/)
/+ p
/(/2/)
/) /= /2/. Let s
/2
i
be the v ariance computed from the i /-th replication/, and let p
/(/1/)
/1
b e the p
/(/1/)
from the v ery /rst of the /v e replications/. Then de/ne the follo wing statistic
/~
t /=
p
/(/1/)
/1
q
/1
/5
P
/5
i /=/1
s
/2
i
/;;
whic hw e will call the /5x/2cv
/~
t statistic/. W e claim that under the n ull h yp othesis/,
/~
t has appro ximately
a t distribution with /5 degrees of freedom/. The argumen tg o e sa sf o l l o ws/.
Let A b e a standard normal random v ariable and B be a /
/2
random v ariable with n /; /1 degrees
of freedom/. Then b y de/nition/, the quan tit y
A
p
B/= /( n /; /1/)
/(/1/)
has a t distribution with n /; /1 degrees of freedom if A and B are indep enden t/.
The usual t statistic is deriv ed b y starting with a set of random v ariables X
/1
/;;/:/:/: X
n
ha ving
a normal distribution with mean / and v ariance /
/2
/. Let
 X /=
/1
n
P
i
X
i
be the sample mean and
S
/2
/=
P
i
/( X
i
/;
 X /)
/2
b e the sum of squared deviations from the mean/. Then de/ne
A /=
p
n /(
 X /; / /) /=/
B /= S
/2
/=/
/2
/:
/1/0

<!-- page 11 -->
W ell/-kno wn results from probabilit y theory state that A has a standard normal distribution and
B has a /
/2
distribution with n /; /1 degrees of freedom/. A more remark able result from probabilit y
theory is that A and B are also indep enden t/, pro vided the original X
i
/'s w ere dra wn from a normal
distribution/. Hence/, w e can plug them in to Equation /(/1/) as follo ws/:
t /=
A
p
B/= /( n /; /1/)
/=
p
n /(
 X /; / /) /=/
p
S
/2
/= /( /
/2
/ /( n /; /1/)/)
/=
p
n /(
 X /; / /)
p
S
/2
/= /( n /; /1/)
/:
This giv es the usual de/nition of the t statistic when / /=/0 /.
W e can construct
/~
t b y analogy as follo ws/. Under the n ull h yp othesis/, the n umerator of
/~
t /,
p
/(/1/)
/1
/, is the di/erence of t w o iden tically distributed prop ortions/, so w e can safely treat it as an
appro ximately normal random v ariable with zero mean and unkno wn standard deviation / if the
underlying test set con tained at least /3/0 p oin ts/. Hence/, let A /= p
/(/1/)
/1
/=/ /.
Also under the n ull h yp othesis/, s
/2
i
/=/
/2
has a /
/2
distribution with /1 degree of freedom if w e mak e
the additional assumption that p
/(/1/)
i
and p
/(/2/)
i
are indep enden t/. This assumption is false/, as w eh a v e
seen ab o v e/, b ecause these t w o di/erences/-of/-prop ortions are measured on the opp osite folds of a /2/-
fold cross/-v alidation/. Still/, the assumption of indep endence is probably more appropriate for /2/-fold
cross/-v alidation than for /1/0/-fold cross/-v alidation/, b ecause in the /2/-fold case/, the training sets are
completely non/-o v erlapping /(and/, as alw a ys in cross/-v alidation/, the test sets are non/-o v erlapping/)/.
/(W ec hose /2/-fold cross/-v alidation b ecause it giv es large test sets and disjoin t training sets/. The
large test set is needed/, b ecause w e are only using one paired di/erence p
/(/1/)
/1
in
/~
t /. The disjoin t
training sets help mak e p
/(/1/)
i
and p
/(/2/)
i
more indep enden t/. A dra wbac k/, of course/, is that the learning
algorithms are trained on training sets half of the size of the training sets for whic h/, under Question
/8/, w e seek their relativ e p erformance/./)
W e could set B /= s
/2
/1
/=/
/2
/, but when w e tested this exp erimen tally /,w e found that the resulting
estimate of the v ariance w as v ery noisy /, and often zero/. In similar situations/, others ha v e found that
com bining the results of m ultiple cross/-v alidations can help stabilize an estimate/, so w e p erform
/v e /2/-fold cross/-v alidations and de/ne
B /=
/ 
/5
X
i /=/1
s
/2
i
/!
/
/
/2
/:
If w e assume that the s
/2
i
from eac h /2/-fold cross/-v alidation are indep enden to f e a c h other/, then
B is the sum of /5 indep enden t random v ariables eac h ha ving a /
/2
distribution with /1 degree of
freedom/. By the summation prop ert y of the /
/2
distribution/, this means B has a /
/2
distribution
with /5 degrees of freedom/. This last indep endence assumption is also false/, be c a u s e eac h /2/-fold
cross/-v alidation is computed from the same training data/. Ho w ev er/, exp erimen tal tests sho w ed that
this is the least problematic of the v arious indep endence assumptions underlying the /5x/2cv test/.
Finally /,t o use Equation /(/1/)/, w e m ust mak e the assumption that the v ariance estimates s
i
are
indep enden t of p
/(/1/)
/1
/. This m ust be assumed /(rather than pro v ed as in the usual t distribution
deriv ation/)/, b ecause w e are using only one of the observ ed di/erences of prop ortions rather than
the mean of all of the observ ed di/erences/. As discussed ab o v e/, the mean di/erence tends to
o v erestimate the true di/erence/, b ecause of the lac k of indep endence b et w een the di/eren t folds of
the cross/-v alidation/.
/1/1

<!-- page 12 -->
  
   
 

Predicted t value (based on quantile)
Observed t value
- 6 - 4 - 2 0246
-4 -2 0 2 4
Figure /2/: QQ plot comparing the distribution of /1/,/0/0/0 v alues of
/~
t to the v alues they should ha v e
under a t distribution with /5 degrees of freedom/. All po i n ts w ould fall on the line y /= x if the
distributions matc hed/.
With all of these assumptions/, w e can plug in to Equation /(/1/) to obtain
/~
t /.
Let us summarize the assumptions and appro ximations in v olv ed in this deriv ation/. First/, w e
emplo y the normal appro ximation to the binomial distribution/. Second/, w e assume pairwise inde/-
p endence of p
/(/1/)
i
and p
/(/2/)
i
for all i /. Third/, w e assume indep endence be t w een the s
i
/'s/. Finally /, w e
assume indep endence b et w een the n umerator and denominator of the
/~
t statistic/.
One w a yt oe v aluate the /5x/2cv statistic exp erimen tally is to mak ea q u a n tile/-quan tile plot /(QQ
plot/)/, as sho wn in Figure /2/. The QQ plot sho ws /1/,/0/0/0 computed v alues of the /5x/2cv statistic for a
case where the n ull h yp othesis is kno wn to apply /(the EXP/6 task as describ ed b elo w/)/. T o generate
a QQ plot/, the /1/,/0/0/0 v alues are sorted and assigned quan tiles /(i/.e/./, their rank in the sorted list
divided b y /1/,/0/0/0/)/. Then the in v erse cum ulativ e t distribution /(with /5 degrees of freedom/) is used
to compute for eac h quan tile/, the v alue that a t /-distributed random v ariable w ould ha v e tak en if it
had had that rank/. This v alue b ecomes the x co ordinate/, and the original v alue
/~
t b ecomes the y
co ordinate/. In other w ords/, for eac h observ ed p oin t/, based on its ordinal p osition within the /1/,/0/0/0
p oin ts/, w e can compute what v alue it should ha v e had if the /1/,/0/0/0 po i n ts had be e n truly dra wn
from a t distribution/. If the /1/,/0/0/0 p oin ts ha v ea t distribution with /5 degrees of freedom/, then they
/1/2

<!-- page 13 -->
should lie on the line y /= x /. The /gure sho ws a fairly go o d /t to the line/. Ho w ev er/, at the tails of
the distribution/,
/~
t is somewhat more conserv ativ e than it should b e/.
Our c hoice of /v e replications of cross/-v alidation is not arbitrary /. Exploratory studies sho w ed
that using few er or more than /v e replications increased the risk of T yp e I error/. A p ossible
explanation for this is that there are t w o comp eting problems/. With few er replications/, the noise in
the measuremen to ft h e s
i
/'s b ecomes troublesome/. With more replications/, the lac k of indep endence
among the s
i
/'s b ecomes troublesome/. Whether /v e is the b est v alue for the n um b er of replications
is an op en question/.
This completes our description of the /v e statistical tests of the n ull h yp othesis that t w o learning
algorithms ha v e the same error rate on a giv en p opulation /(based on a sample of that p opulation/)/.
/4 Sim ulation Exp erimen t Design
W e no w turn to an exp erimen tal ev aluation of these /v e metho ds/. The purp ose of the sim ulation
w as to measure the probabilit yo f T yp e I error of the algorithms/. AT yp e I error o ccurs when the
n ull h yp othesis is true /(i/.e/./, there is no di/erence be t w een the t w o learning algorithms/) and the
learning algorithm rejects the n ull h yp othesis/.
T o measure the probabilit yo f T yp e I error/, w e constructed some sim ulated learning problems/.
T o understand these problems/, it is useful to think abstractly ab out the be h a vior of learning
algorithms/.
/4/./1 Sim ulating the be h a vior of learning algorithms
Consider a p opulation of N data po i n ts and supp ose that the training set size is /xed/. Then for
ag i v en learning algorithm A /, de/ne /
A
/( x /)t o b e the probabilit yt h a t the classi/er pro duced b y A
when trained on a randomly/-dra wn training set /(of the /xed size/) will misclassify x /. If /
A
/( x /)/= /0 /,
then x is alw a ys correctly classi/ed b y classi/ers pro duced b y A /. If /
A
/( x /) /= /1/, then x is alw a ys
misclassi/ed/.
Figure /3 sho ws the measured v alues of / /( x /) for a p opulation of /7/,/6/7/0 po i n ts with resp ect to
the C/4/./5 decision tree algorithm /(Quinlan/, /1/9/9/3/) trained on randomly/-dra wn training sets of /1/0/0
examples/. The po i n ts w ere sorted b y their / v alues/. Giv en these / v alues/, w e could sim ulate the
b eha vior of C/4/./5 on a randomly dra wn test set of p oin ts b y taking eac h p oin t x and misclassifying
it with probabilit y / /( x /)/. This w ould not exactly repro duce the b eha vior of C/4/./5/, b ecause it assumes
that the misclassi/cation errors made b y C/4/./5 are indep enden tf o r eac h test example/, whereas in
fact the classi/cations of data p oin ts that are close together will tend to be highly correlated/.
Ho w ev er/, this sim ulated C/4/./5 pro cedure w ould ha v e the same a v erage error rate as the real C/4/./5
algorithm/, and it will exhibit a similar degree of v ariation from one random trial to the next/.
W ec a n s i m ulate learning algorithms with v arious prop erties b y de/ning a p opulation of p oin ts
X and assigning a v alue / /( x /)t o e a c h p oin t/. If w ew an t a learning algorithm to ha v eh i g h v ariance/,
w e can assign v alues of / near /0/./5/, whic hi s t h e v alue giving the maxim um v ariance for a binomial
random v ariable/. If w ew an tt w o learning algorithms to ha v e the same error rate on the p opulation/,
w e can ensure that the a v erage v alue of / o v er the p opulation X is the same for b oth algorithms/.
In our studies/, w ew an ted to construct sim ulated learning problems that w ould pro vide a /\w orst/-
case/" for our statistical tests/. T o accomplish this/, w e sough t to maximize the t w o main sources of
random v ariation/: v ariation resulting from the c hoice of test data sets and v ariation resulting from
the c hoice of training sets/. W e ignored the issue of classi/cation noise/. Because it a/ects training
and test data equally /, it can b e incorp orated in to the o v erall error rate/. W e also ignored in ternal
/1/3

<!-- page 14 -->
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0 1000 2000 3000 4000 5000 6000 7000 8000
epsilon(x) for C4.5
Data Point x
Figure /3/: Measured v alues of /
C /4 /: /5
/( x /) for a p opulation of /7/6/7/0 data p oin ts/.
randomness in the learning algorithms/, since this will manifest itself in the same w a y as training
set v ariance/|b y causing the same learning algorithm to pro duce di/eren t classi/ers/.
F or tests of T yp e I error/, w e designed t w os e t s o f / v alues/: /
A
/( x /) for algorithm A and /
B
/( x /) for
algorithm B/. W e established a target error rate / and c hose only t w o distinct v alues to use for /
A
/( x /)
and /
B
/( x /)/:
/1
/2
/ and
/3
/2
/ /. W e generated a p opulation of po i n ts/. F or the /rst half of the p opulation/,
w e assigned /
A
/( x /)/=
/1
/2
/ and /
B
/( x /)/=
/3
/2
/ /. F or the remaining half of the p opulation/, w e rev ersed this
and assigned /
A
/( x /)/=
/3
/2
/ and /
B
/( x /)/=
/1
/2
/ /. Figure /4 sho ws this con/guration of / v alues/. The size
of the p opulation is irrelev an t/, b ecause w e are sampling with replacemen t and there are only t w o
kinds of po i n ts/. The imp ortan t thing is that the p opulation is ev enly divided b et w een these t w o
kinds of training p oin ts/.
The e/ect of this is that eac h algorithm has an o v erall error rate of / /,a n d eac h algorithm has
the same total v ariance/. Ho w ev er/, for an y giv en test example/, the algorithms ha v e v ery di/eren t
error rates/. This mak es the e/ect of the random c hoice of test data sets v ery apparen t/. Indeed/,
unless the test data set is exactly equally divided be t w een the /rst half of the p opulation and
the second half of the p opulation/, there will b e an apparen ta d v an tage for one algorithm o v er the
other/. Our statistical tests will need to a v oid be i n g fo oled b y this apparen t di/erence in error
rates/. Exp erimen tal measuremen ts con/rmed that these c hoices of /
A
/( x /) and /
B
/( x /) did the be s t
job of sim ultaneously maximizing within/-algorithm v ariance and b et w een/-algorithm v ariation while
ac hieving the desired o v erall error rate of / /. In most of our exp erimen ts/, w e used a v alue of / /=/0 /: /1/0/,
although w e also in v estigated / /=/0 /: /2/0/, / /=/0 /: /3/0/, and / /=/0 /: /4/0/.
/1/4

<!-- page 15 -->
0
0.05
0.1
0.15
0.2
0.25
1 N/2 N
epsilon(x)
Data Point x
Algorithm A
Algorithm B
Figure /4/: Designed v alues of /
A
/( x /)a n d /
B
/( x /) for an o v erall error rate of / /=/0 /: /1/0/.
/4/./2 Details of the sim ulation of eac h statistical test
Eac h sim ulation is divided in to a series of /1/0/0/0 trials/. In eac h trial/, a data set S of size /3/0/0
is randomly dra wn with replacemen t and then analyzed using eac h of the /v e statistical tests
describ ed ab o v e/. The goal is to measure the prop ortion of trials in whic h the n ull h yp othesis is
rejected/.
F or the /rst t w o tests/, McNemar/'s test and the normal test for the di/erence of t w o prop ortions/,
the data set S is randomly divided in to a training set R con taining t w o thirds of S and a test set
T con taining the remaining one third of S /. The training set is ignored/, b ecause w e do not actually
execute the learning algorithms/. Rather/, the p erformance of eac h algorithm on the test set is
sim ulated b y classifying eac h test example x randomly according to its v alue of /
A
/( x /) and /
B
/( x /)/.
A random n um b er in the range /[/0/,/1/) is dra wn/. If it is less than /
A
/( x /)/, then x is considered to be
misclassi/ed b y algorithm A /. A second random n um be r i s d r a wn/, and x is considered misclassi/ed
b y algorithm B if that n um be r is less than /
B
/( x /)/. The results of these classi/cations are then
pro cessed b y the appropriate statistical test/. All tests w ere p erformed using /2/-sided tests with
con/dence lev el /0 /: /0/5/.
F or the resampled paired t test/, this pro cess of randomly splitting the data set S t w o/-thirds//one/-
thirds w as rep eated /3/0 times/. Eac ht e s t set w as classi/ed as describ ed in the previous paragraph/.
The /3/0 di/erences in the error rates of the t w o algorithms w ere collected and emplo y ed in the t
test/.
F or the k /-fold cross/-v alidated paired t test/, the data set S w as divided in to k /= /1/0 random sub/-
sets of equal size/. Eac h of the /1/0 test sets w as then classi/ed b y b oth algorithms using the random
pro cedure describ ed ab o v e/. Ho w ev er/, during the classi/cation pro cess/, to sim ulate random v aria/-
tion in the qualit yo fe a c h training set/, w e generated a random v alue / in the range /[ /; /0 /: /0/2 /;; /+/0 /: /0/2/]
/1/5

<!-- page 16 -->
0
0.05
0.1
0.15
0.2
0.25
0.3
McNemar Prop Test Resampled t Xval t 5x2cv t
Probability of Type 1 Error
Figure /5/: Probabilit yo f T yp e I error for eac h statistical test/. The four adjacen t bars for eac ht e s t
represen t the probabilit yo f T yp e I error for / /= /0/./1/0/, /0/./2/0/, /0/./3/0/, and /0/./4/0/. Error bars sho w /9/5/%
con/dence in terv als for these probabilities/. The horizon tal line sho ws the target probabilit y of /0/./0/5/.
and added this v alue / to ev ery /
A
/( x /) and /
B
/( x /) b efore generating the classi/cations/. The results
of the classi/cations w ere then collected and sub jected to the t test/.
F or the /5x/2cv test/, /v e replications of /2/-fold cross/-v alidation w ere p erformed/, and the t statistic
w as constructed as describ ed ab o v e/.
It is imp ortan t to note that this exp erimen td o e sn o t s i m ulate training set v ariance/. In particu/-
lar/, it do es not mo del the e/ect of o v erlapping training sets on the b eha vior of the cross/-v alidated t
test or the /5x/2cv test/. W e will correct this shortcoming b elo w in our exp erimen ts with real learning
algorithms/.
/5 Results
Figure /5 sho ws the probabilit yo f making a T yp e I error for eac h of the /v e pro cedures when the
data set S con tains /3/0/0 examples and the o v erall error rate / w as v aried from /0/./1/0 to /0/./4/0/.
Tw o of the /v e tests ha v e a probabilit yo f T yp e I error that exceeds the target v alue of /0/./0/5/:
the di/erence/-of/-prop ortions test and the resampled t test/. The remaining tests ha v e acceptable
probabilit y of making a T yp e I error according to this sim ulation/.
The resampled t test has a m uc h higher probabilit yo f T yp e I error than the other tests/. This
results from the fact that the randomly/-dra wn data set S is lik ely to con tain an im balance of
p oin ts from the /rst half of the p opulation compared to the second half of the p opulation/. The
resampled t test can detect and magnify this di/erence un til it is /\statistically signi/can t/./" Indeed/,
the probabilit y of making a T yp e I error with this test can b e increased b y increasing the n um be r
of resampled training//test splits/. Figure /6 sho ws the e/ect of v arious n um b ers of resampled splits
/1/6

<!-- page 17 -->
0
0.05
0.1
0.15
0.2
0.25
0 20 40 60 80 100
Probability of Type 1 error
Number of replications
Resampled t
Xval t
Figure /6/: Probabilit yo f T yp e I error for the resampled t test and the k /-fold cross/-v alidated t test
as the n um b er of resampling replications is v aried/. The error rate / /=/0 /: /1/0/.
for b oth the resampled t test and the cross/-v alidated t test/. Notice that the cross/-v alidated t test
do es not exhibit this problem/.
The di/erence/-of/-prop ortions test su/ers from essen tially the same problem/. When the sample
S is unrepresen tativ e/, the measured di/erence in the t w o prop ortions will b e large/, esp ecially when
/ is near /0/./5/. It is in teresting that McNemar/'s test do es not share this problem/. The k ey di/erence
is that the di/erence/-of/-prop ortions test only lo oks at the di/erence b et w een t w o prop ortions and
not at their absolute v alues/. Consider the follo wing t w o /2 / /2c o n tingency tables/:
/0
 /4/0
/6/0
 /0
/4/0
 /0
/2/0
 /4/0
Both of these tables ha v e the same di/erence in error rates of /0/./2/0/, so the di/erence/-of/-prop ortions
test treats them iden tically /(and rejects the n ull h yp othesis p /< /0 /: /0/0/5/)/. Ho w ev er/, McNemar/'s
test /nds no signi/can t di/erence in the left table/, but /nds an extremely signi/can t di/erence
/( p/< /0 /: /0/0/1/) in the righ t table/. This is b ecause in the left table/, McNemar/'s test asks the question
/\What is the probabilit y in /1/0/0 tosses of a fair coin that w e will receiv e /4/0 heads and /6/0 tails/?/" In
the righ t table/, it asks the question /\What is the probabilit y in /2/0 tosses of a fair coin that w e will
receiv e /2/0 heads and /0 tails/?/" The w a y w e ha v e constructed our sim ulated learning problems/, w e
are more lik ely to pro duce tables lik e the one on the left/, esp ecially when / is near /0/./5/. Note that if
w e had used the corrected v ersion of the di/erence/-of/-prop ortions test/, it w ould not ha v e su/ered
from this problem/.
Because of the p o or b eha vior /(and high cost/) of the resampled t test/, w e excluded it from further
exp erimen ts/.
/1/7

<!-- page 18 -->
The biggest dra wbac k of the sim ulation is that it do es not capture or measure training set
v ariance or v ariance resulting from the in ternal be h a vior of the learning algorithm/. T o address
these problems/, w e conducted a second set of exp erimen ts with real learning algorithms and real
data sets/.
/6 Exp erimen ts on Realistic Data
/6/./1 Metho ds
T o ev aluate the T yp e I error rates of our four statistical tests with real learning algorithms/, w e
needed to /nd t w o learning algorithms that had iden tical p erformance when trained on training sets
of a giv en size/. W e also needed the learning algorithms to b e v ery e/cien t/, so that the exp erimen ts
could b e replicated man y times/. T oa c hiev e this/, w ec hose C/4/./5 Release /1 /(Quinlan/, /1/9/9/3/) and the
/rst nearest/-neigh b or /(NN/) algorithm /(Dasarath y /,/1 /9 /9 /1 /) /. W e then selected three di/cult problems/:
the EXP/6 problem dev elop ed b y Kong /(/1/9/9/5/)/, the Letter Recognition data set /(F rey /& Slate/, /1/9/9/1/)/,
and the Pima Indians Diab etes T ask /(Merz /& Murph y /,/1 /9 /9 /6 /) /. Of course/, C/4/./5 and NN do not ha v e
the same p erformance on these data sets/. In EXP/6 and Letter Recognition/, NN p erforms m uc h
b etter than C/4/./5/;; the rev erse is true in the Pima data set/.
Our next step w as to /\damage/" the learning algorithms so that their p erformance w as iden tical/.
In the EXP/6 and Letter Recognition tasks/, w e mo di/ed the distance metric emplo y ed b y NN to
be a w eigh ted Euclidean distance with bad w eigh ts/. This allo w ed us to reduce the p erformance of
NN un til it matc hed C/4/./5 on those data sets/. T o equalize the p erformance of the algorithms on the
Pima data set/, w e mo di/ed C/4/./5 so that when classifying new instances/, it w ould mak e random
classi/cation errors at a sp eci/ed rate/.
More precisely /, eac h data set w as pro cessed as follo ws/. F or EXP/6/, w e generated a calibration
set of /2/2/,/8/0/1 examples /(spaced on a uniform grid of resolution /0/./1/)/. W e then generated /1/0/0/0 data
sets/, eac h of size /3/0/0/, to sim ulate /1/0/0/0 separate trials/. F rom eac h of these /1/0/0/0 data sets/, w e
randomly drew subsets of size /2/7/0/, /2/0/0/, and /1/5/0/. These sizes w ere c hosen b ecause they are the
sizes of training sets used in the /1/0/-fold cross/-v alidated t test/, the McNemar and di/erence/-of/-
prop ortions tests/, and the /5x/2cv t test/, resp ectiv ely /, when those tests are giv en an initial data set
of /3/0/0 examples/. F or eac h size of training set /(/2/7/0/, /2/0/0/, and /1/5/0/)/, w e adjusted the distance metric
for NN so that the a v erage p erformance /(o v er all /1/0/0/0 data sets/, measured on the /2/2/,/8/0/1 calibration
examples/) matc hed the a v erage p erformance of C/4/./5 to within /0/./1/%/.
F or Letter Recognition/, w e randomly sub divided the /2/0/,/0/0/0 examples in to a calibration set of
/1/0/,/0/0/0 and an exp erimen tal set of /1/0/,/0/0/0/. W e then drew /1/0/0/0 data sets/, eac h of size /3/0/0/, randomly
from the exp erimen tal set of /1/0/,/0/0/0 examples/. Again/, from eac h of these data sets/, w e drew random
subsets of size /2/7/0/, /2/0/0/, and /1/5/0/. F or eac h size of training set/, w e adjusted the distance metric for
NN so that the a v erage p erformance /(o v er all /1/0/0/0 data sets/, measured on the /1/0/,/0/0/0 calibration
examples/) matc hed the a v erage p erformance of C/4/./5 to within /0/./1/%/.
F or the Pima Indians Diab etes data set/, w e drew /1/0/0/0 data sets of size /3/0/0 from the /7/6/8 a v ailable
examples/. F or eac h of these data sets/, the remaining /4/6/8 examples w ere retained for calibration/.
Eac h of the /1/0/0/0 data sets of size /3/0/0 w as further subsampled to pro duce random subsets of size
/2/7/0/, /2/0/0/, and /1/5/0/. F or eac h size of training set/, w e measured the a v erage error rate of C/4/./5 and NN
/(o v er /1/0/0/0 data sets/, when tested on the /4/6/8 calibration examples corresp onding to eac h data set/)/.
W e then adjusted the random noise rate of C/4/./5 so that the a v erage error rates w ould b e iden tical/.
/1/8

<!-- page 19 -->
0
0.05
0.1
0.15
0.2
McNemar Prop Test Xval t 5x2cv t
Probability of Type 1 Error
Figure /7/: T yp e I error rates for four statistical tests/. The three bars within eac h test corresp ond
to the EXP/6/, Letter Recognition/, and Pima data sets/. Error bars are /9/5/% con/dence in terv als on
the true T yp e I error rate/.
/6/./2 T yp e I Error Results
Figure /7 sho ws the measured T yp e I error rates of the four statistical tests/. The /1/0/-fold cross/-
v alidated t test is the only test whose T yp e I error exceeds /0/./0/5/. All of the other tests/, ev en the
di/erence/-of/-prop ortions test /(/\Prop T est/"/)/, sho w acceptable T yp e I error rates/.
/6/./3 P o w er Measuremen ts
T yp e I error is not the only imp ortan t consideration in c ho osing a statistical test/. It is the most
imp ortan t criterion if one/'s goal is to b e con/den t that an observ ed p erformance di/erence is real/.
But if one/'s goal is to detect whether there is a di/erence be t w een t w o learning algorithms/, then
the p ower of the statistical test is imp ortan t/. The po w er of a test is the probabilit y that it will
reject the n ull h yp othesis when the n ull h yp othesis is false/.
T o measure the p o w er of the tests/, w e recalibrated the distance metric for nearest neigh b or /(for
the EXP/6 and Letter Recognition tasks/) and the random classi/cation error rate /(for Pima/) to
ac hiev e v arious di/erences in the p erformance of C/4/./5 and NN/. Sp eci/cally /,w e did the follo wing/.
First/, w e measured the p erformance for C/4/./5 and NN when trained on /3/0/0 examples and tested
on the appropriate calibration examples as be f o r e /(denote these error rates /
C /4
and /
NN
/)/. Then
w e c hose v arious target error rates be t w een these extremes/. F or eac h target error rate /
tar g et
/, w e
computed the fraction / suc h that /
t a rge t
/= /
C /4 /: /5
/; / /( /
C /4 /: /5
/; /
NN
/)/. W e then calibrated the error
rates of C/4/./5 and NN for training sets of size /1/5/0/, /2/0/0/, and /2/7/0 so that the same v alue of / applied/.
In other w ords/, w e adjusted the learning curv e for the nearest neigh b or algorithm /(with damaged
distance metric/) so that it w as p ositioned at a /xed fraction of the w a yb e t w een the learning curv es
/1/9

<!-- page 20 -->
0.4
0.45
0.5
0.55
0.6
0.65
150 200 250 300
Error rate
Training set size
C4.5
λ=0.1759
λ=0.3500
λ=0.5420
NN (λ=1)
Figure /8/: Learning curv es in terp olated b et w een C/4/./5 and NN for the purp ose of measuring p o w er/.
for C/4/./5 and for NN /(with an undamaged distance metric/)/. Figure /8 sho ws the calibrated learning
curv es for the Letter Recognition task for v arious v alues of / /.
Figures /9/, /1/0/, and /1/1 plot po w er curv es for the four statistical tests/. These curv es sho w that
the cross/-v alidated t test is m uc h more p o w erful than the other three tests/. Hence/, if the goal is to
be con/den t that there is no di/erence be t w een t w o algorithms/, then the cross/-v alidated t test is
the test of c hoice/, ev en though its T yp e I error is unacceptable/.
Of the tests with acceptable T yp e I error/, the /5x/2cv t test is the most p o w erful/. Ho w ev er/, it is
sob ering to note that ev en when the p erformance of the learning algorithms di/ers b y /1/0 p ercen tage
p oin ts /(as in the Letter Recognition task/)/, these statistical tests are only able to detect this ab out
one third of the time/.
/7 Discussion
The exp erimen ts suggest that the /5x/2cv test is the most p o w erful among those statistical tests that
ha v e acceptable T yp e I error/. This test is also the most satisfying/, be c a u s e it assesses the e/ect
of b oth the c hoice of training set /(b y running the learning algorithms on sev eral di/eren t training
sets/) and the c hoice of test set /(b y measuring the p erformance on sev eral test sets/)/.
Despite the fact that McNemar/'s test do es not assess the e/ect of v arying the training sets/, it
still p erforms v ery w ell/. Indeed/, in all of our v arious exp erimen ts/, w e nev er once sa w the T yp e I
error rate of McNemar/'s test exceed the target lev el /(/0/./0/5/)/. In con trast/, w e did observ e cases where
b oth the /5x/2cv and di/erences/-of/-prop ortions tests w ere fo oled/.
The /5x/2cv test will fail in cases where the error rates measured in the v arious /2/-fold cross/-
v alidation replications v ary wildly /(ev en when the di/er enc e in error rates is unc hanged/)/. W ew ere
able to observ e this in some sim ulated data exp erimen ts where the error rates /
uctuated b et w een
/2/0

<!-- page 21 -->
0
0.1
0.2
0.3
0.4
0.5
0.6
0 1 2 3 4 5
Probability of Rejecting H0
Difference in performance between C4.5 and NN
McNemar
Prop Test
5x2cv t
Xval t
Figure /9/: P o w er of four statistical tests on the EXP/6 task/. The horizon tal axis plots the n um be r
of pe r c e n tage po i n ts b y whic h the t w o algorithms /(C/4/./5 and NN/) di/er when trained on training
sets of size /3/0/0/.
/0/./1 and /0/./9/. W e did not observ e it during an y of our exp erimen ts on realistic data/. Wild v ariations
cause bad estimates of the v ariance/. It is therefore advisable to c hec k the measured error rates
when applying this test/.
The di/erence/-of/-prop ortions test will fail in cases where the t w o learning algorithms ha v ev ery
di/eren t /\regions/" of poo r p erformance and where the error rates are close to /0/./5/. W e did not
encoun ter this problem in our exp erimen ts on realistic data/, ev en though C/4/./5 and NN are v ery
di/eren t algorithms/. W e susp ect that this is b ecause most errors committed b y learning algorithms
are near the decision b oundaries/. Hence/, most learning algorithms with comparable error rates ha v e
v ery similar regions of p o or p erformance/, so the pathology that w e observ ed in our sim ulated data
exp erimen ts do es not arise in practice/. Nonetheless/, giv en the sup erior p erformance of McNemar/'s
test and the incorrect assumptions underlying our v ersion of the di/erence/-of/-prop ortions test/, there
can b e no justi/cation for ev er emplo ying the uncorrected di/erence/-of/-prop ortions test/.
The /1/0/-fold cross/-v alidated t test has high T yp e I error/. Ho w ev er/, it also has high p o w er/, and
hence/, it can b e recommended in those cases where T yp e I I error /(i/.e/./, the failure to detect ar e a l
di/erence b et w een algorithms/) is more imp ortan t/.
/8 Conclusions
The starting p oin t for this pap er w as Question /8/: Giv en t w o learning algorithms A and B and a
small data set S /, whic h algorithm will pro duce more accurate classi/ers when trained on data sets
of the same size as S dra wn from the same p opulation/? Unfortunately /, none of the statistical tests
describ ed and ev aluated in this pap er can answ er this question/. All of the statistical tests require
/2/1

<!-- page 22 -->
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0 2 4 6 8 10 12
Probability of Rejecting H0
Difference in performance between C4.5 and NN
McNemar
Prop Test
5x2cv t
Xval t
Figure /1/0/: P o w er of four statistical tests on the Letter Recognition task/. The horizon tal axis plots
the n um be r o f pe r c e n tage po i n ts b y whic ht h e t w o algorithms /(C/4/./5 and NN/) di/er when trained
on training sets of size /3/0/0/.
using holdout or resampling metho ds/, with the consequence that they can only tell us ab out the
relativ e p erformance of the learning algorithms on training sets of size j R j /< j S j /, where j R j is the
size of the training set emplo y ed in the statistical test/.
In addition to this fundamen tal problem/, eac h of the statistical tests has other shortcomings/.
The deriv ation of the /5x/2cv test requires a large n um be r of indep endence assumptions that are
kno wn to be violated/. McNemar/'s test and the di/erence/-of/-prop ortions test do not measure the
v ariation resulting from the c hoice of training sets or in ternal randomness in the algorithm and
therefore do not measure all of the imp ortan t sources of v ariation/. The cross/-v alidated t test
violates the assumptions underlying the t test/, b ecause the training sets o v erlap/.
As a consequence of these problems/, all of the statistical tests describ ed in this pap er m ust
be view ed as appro ximate/, heuristic tests/, rather than as rigorously correct statistical metho ds/.
This pap er has therefore relied on exp erimen tal ev aluations of these metho ds/, and the follo wing
conclusions m ust b e regarded as ten tativ e/, b ecause the exp erimen ts are based on only t w o learning
algorithms and three data sets/.
The exp erimen ts in this pap er lead us to recommend either the /5x/2cv t test/, for situations
in whic h the learning algorithms are e/cien t enough to run ten times/, or McNemar/'s test/, for
situations where the learning algorithms can b e run only once/. Both tests ha v e similar p o w er/.
Our exp erimen ts ha v e also rev ealed the shortcomings of the other statistical tests/, so w e can
con/den tly conclude that the resampled t test should nev er b e emplo y ed/. This test has v ery high
probabilit yo f T yp e I error/, and results obtained using this test cannot b e trusted/. The exp erimen ts
also suggest caution in in terpreting the results of the /1/0/-fold cross/-v alidated t test/. This test has a
elev ated probabilit yo f T yp e I error /(as m uc h as t wice the target lev el/)/, although it is not nearly
/2/2

<!-- page 23 -->
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0.18
0 0.5 1 1.5 2 2.5 3 3.5
Probability of Rejecting H0
Difference in performance between C4.5 and NN
McNemar
Prop Test
5x2cv t
Xval t
Figure /1/1/: P o w er of four statistical tests on the Pima task/. The horizon tal axis plots the n um be r
of pe r c e n tage po i n ts b y whic h the t w o algorithms /(C/4/./5 and NN/) di/er when trained on training
sets of size /3/0/0/.
as sev ere as the problem with the resampled t test/.
W e hop e that the results in this pap er will b e useful to scien tists in the mac hine learning and
neural net w ork comm unities as they dev elop/, understand/, and impro v em a c hine learning algorithms/.
/9 Ac kno wledgemen ts
The author /rst learned of the k /-fold cross/-v alidated t test from Ronn y Koha vi /(p ersonal comm uni/-
cation/)/. The author thanks Jim Kolsky of the OSU Statistics Departmen t for statistical consulting
assistance and Radford Neal/, Ronn y Koha vi/, and T om Mitc hell for helpful suggestions/. The au/-
thor is also v ery grateful to the referees for their careful reading/, whic h iden ti/ed sev eral errors
in an earlier v ersion of this man uscript/. This researc h w as supp orted b y gran ts IRI/-/9/2/0/4/1/2/9 and
IRI/-/9/6/2/6/5/8/4 from the National Science F oundation and gran t n um b er N/0/0/0/1/4/-/9/5/-/1/-/0/5/5/7 from the
O/ce of Na v al Researc h/.
References
Breiman/, L/./, F riedman/, J/. H/./, Olshen/, R/. A/./, /& Stone/, C/. J/. /(/1/9/8/4/)/. Classi/c ation and R e gr ession
T r e es /. W adsw orth In ternational Group/.
Breiman/, L/. /(/1/9/9/4/)/. Heuristics of instabilit ya n d stabilization in mo del selection/. T ec h/. rep/. /4/1/6/,
Departmen t of Statistics/, Univ ersit y of California/, Berk eley /, CA/.
/2/3

<!-- page 24 -->
Breiman/, L/. /(/1/9/9/6/)/. Bagging predictors/. Machine L e arning /, /2/4 /(/2/)/, /1/2/3/{/1/4/0/.
Dasarath y /, B/. V/. /(Ed/./)/. /(/1/9/9/1/)/. Ne ar est neighb or /(NN/) norms/: NN p attern classi/c ation te chniques /.
IEEE Computer So ciet y Press/, Los Alamitos/, CA/.
Dietteric h/, T/. G/./, Hild/, H/./, /& Bakiri/, G/. /(/1/9/9/5/)/. A comparison of ID/3 and bac kpropagation for
English text/-to/-sp eec h mapping/. Machine L e arning /, /1/8 /,/5 /1 /{ /8 /0 /.
Efron/, B/./, /& Tibshirani/, R/. J/. /(/1/9/9/3/)/. A n Intr o duction to the Bo otstr ap /. Chapman and Hall/, New
Y ork/, NY/.
Ev eritt/, B/. S/. /(/1/9/7/7/)/. The analysis of c ontingency tables /. Chapman and Hall/, London/.
F rey /, P /. W/./, /& Slate/, D/. J/. /(/1/9/9/1/)/. Letter recognition using Holland/-st yle adaptiv e classi/ers/.
Machine L e arning /, /6 /, /1/6/1/{/1/8/2/.
Haussler/, D/./, Kearns/, M/./, Seung/, H/. S/./, /& Tish b y /, N/. /(/1/9/9/4/)/. Rigorous learning curv e b ounds from
statistical mec hanics/. In Pr o c/. /7th A nnu/. A CM Workshop on Comput/. L e arning The ory /, pp/.
/7/6/{/8/7/. A CM Press/, New Y ork/, NY/.
Hin ton/, G/. E/./, Neal/, R/. M/./, Tibshirani/, R/./, /& DEL VE team mem b ers /(/1/9/9/5/)/. Assessing learning
pro cedures using DEL VE/. T ec h/. rep/./, Univ ersit yo fT oron to/, Departmen t of Computer Science/,
h ttp/:////www/.cs/.utoron to/.ca//neuron//delv e//delv e/.h tml/.
Koha vi/, R/. /(/1/9/9/5/)/. Wr app ers for p erformanc e enhanc ement and oblivious de cision gr aphs /. Ph/.D/.
thesis/, Stanford Univ ersit y /.
Kolen/, J/. F/./, /& P ollac k/, J/. B/. /(/1/9/9/1/)/. Bac k propagation is sensitiv e to initial conditions/. In A dvanc es
in Neur al Information Pr o c essing Systems /, V ol/. /3/, pp/. /8/6/0/{/8/6/7 San F rancisco/, CA/. Morgan
Kaufmann/.
Kong/, E/. B/./, /& Dietteric h/, T/. G/. /(/1/9/9/5/)/. Error/-correcting output co ding corrects bias and v ariance/.
In Prieditis/, A/./, /& Russell/, S/. /(Eds/./)/, The Twelfth International Confer enc e on Machine
L e arning /, pp/. /3/1/3/{/3/2/1 San F rancisco/, CA/. Morgan Kaufmann/.
Lindman/, H/. R/. /(/1/9/9/2/)/. A nalysis of V arianc ei n Exp erimental Design /. Springer V erlag/, New Y ork/.
Merz/, C/. J/./, /& Murph y /, P /. M/. /(/1/9/9/6/)/. UCI rep ository of mac hine learning databases/.
http/:////www/.ics/.uci/.edu///~m lear n//ML Rep osit ory/. htm l /.
Quinlan/, J/. R/. /(/1/9/9/3/)/. C/4/./5/: Pr o gr ams for Empiric al L e arning/. Morgan Kaufmann/, San F rancisco/,
CA/.
Rasm ussen/, C/. E/. /(/1/9/9/6/)/. Evaluation of Gaussian pr o c esses and other metho ds for non/-line ar
r e gr ession /. Ph/.D/. thesis/, Univ ersit y of T oron to/, Departmen t of Computer Science/, T oron to/,
Canada/.
Snedecor/, G/. W/./, /& Co c hran/, W/. G/. /(/1/9/8/9/)/. Statistic al Metho ds /. Io w a State Univ ersit y Press/,
Ames/, IA/. Eigh th Edition/.
/2/4

<!-- fetch 2: https://api.crossref.org/works/10.1162/089976698300017197 + https://api.openalex.org/works/doi:10.1162/089976698300017197 | fetch.py json-metadata | 2026-11-06T23:14+07:00 | metadata -->
source: Crossref
title: Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms
authors: Dietterich, Thomas G.
container: Neural Computation
published: 1998-10-1
volume: 10
issue: 7
pages: 1895-1923
article number: 
publisher: MIT Press
doi: 10.1162/089976698300017197
type: journal-article
is-referenced-by-count (Crossref citations): 3050

abstract:
This article reviews five approximate statistical tests for determining whether one learning algorithm outperforms another on a particular learning task. These test sare compared experimentally to determine their probability of incorrectly detecting a difference when no difference exists (type I error). Two widely used statistical tests are shown to have high probability of type I error in certain situations and should never be used: a test for the difference of two proportions and a paired-differences t test based on taking several random train-test splits. A third test, a paired-differences t test based on 10-fold cross-validation, exhibits somewhat elevated probability of type I error. A fourth test, McNemar's test, is shown to have low type I error. The fifth test is a new test, 5 × 2 cv, based on five iterations of twofold cross-validation. Experiments show that this test also has acceptable type I error. The article also measures the power (ability to detect algorithm differences when they do exist) of these tests. The cross-validated t test is the most powerful. The 5×2 cv test is shown to be slightly more powerful than McNemar's test. The choice of the best test is determined by the computational cost of running the learning algorithm. For algorithms that can be executed only once, Mc-Nemar's test is the only test with acceptable type I error. For algorithms that can be executed 10 times, the 5 × 2 cv test is recommended, because it is slightly more powerful and because it directly measures variation due to the choice of training set.

source: OpenAlex
title: Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms
authors: Thomas G. Dietterich
institutions: Oregon State University
venue: Neural Computation
publication date: 1998-10-01
volume: 10
issue: 7
pages: 1895–1923
doi: https://doi.org/10.1162/089976698300017197
cited_by_count (OpenAlex): 3889
type: article
location: https://doi.org/10.1162/089976698300017197 (open access: False)
location: https://pubmed.ncbi.nlm.nih.gov/9744903 (open access: False)
location: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.1005.1391 (open access: False)
location: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.129.2536 (open access: False)
location: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.37.3325 (open access: False)

abstract:
This article reviews five approximate statistical tests for determining whether one learning algorithm outperforms another on a particular learning task. These tests are compared experimentally to determine their probability of incorrectly detecting a difference when no difference exists (type I error). Two widely used statistical tests are shown to have high probability of type I error in certain situations and should never be used: a test for difference of two proportions and a paired-differences t test based on taking several random train-test splits. A third test, a paired-differences t test based on 10-fold cross-validation, exhibits somewhat elevated probability of type I error. A fourth test, McNemar's test, is shown to have low type I error. The fifth test is a new test, 5 x 2 cv, based on five iterations of twofold cross-validation. Experiments show that this test also has acceptable type I error. The article also measures the power (ability to detect algorithm differences when they do exist) of these tests. The cross-validated t test is the most powerful. The 5 x 2 cv test is shown to be slightly more powerful than McNemar's test. The choice of the best test is determined by the computational cost of running the learning algorithm. For algorithms that can be executed only once, McNemar's test is the only test with acceptable type I error. For algorithms that can be executed 10 times, the 5 x 2 cv test is recommended, because it is slightly more powerful and because it directly measures variation due to the choice of training set.

<!-- fetch 3: https://sci2s.ugr.es/keel/pdf/algorithm/articulo/dietterich1998.pdf | fetch.py pdfkit | 2026-11-06T23:17+07:00 | unreadable -->
No readable copy was found. Attempts:
- L1 https://sci2s.ugr.es/keel/pdf/algorithm/articulo/dietterich1998.pdf: unreadable (few letters or digits (44% alphanumeric, 24% letters); few function words (1.6%): scrambled or non-text; odd word length (2.8))
- L1 https://sci2s.ugr.es/keel/pdf/algorithm/articulo/dietterich1998.pdf: unreadable (few letters or digits (28% alphanumeric, 16% letters); few function words (1.4%): scrambled or non-text; odd word length (2.7))
- L1 https://sci2s.ugr.es/keel/pdf/algorithm/articulo/dietterich1998.pdf: unreadable (few letters or digits (29% alphanumeric, 24% letters); few function words (0.0%): scrambled or non-text)

<!-- fetch 4: https://core.ac.uk/download/147914793.pdf | fetch.py none | 2026-11-06T23:17+07:00 | error -->
No readable copy was found. Attempts:
- L1 https://core.ac.uk/download/147914793.pdf: error (HTTP 403)
