| Optimal | Decision | Making: | 5,253 |
| ------- | -------- | ------- | ----- |
IntroductiontoOptimization
TobiasSutter

Course Organization
▶ Lecturer: TobiasSutter(tobias.sutter@unisg.ch)
▶
Lectureslides,andexercisesheetsareavailableatCANVAS
▶
Therewillbeweeklyexercisesheets;somewewillsolveinclass,
therestishomework;detailedsamplesolutionswillbeprovided
▶
OfficeHours: EveryWednesday4.15-5.00pminC83-2217
(HouseWashington)
▶
Grade(100%finalexam)
Disclaimer: MostofthelectureslideswerekindlyprovidedbyDaniel
KuhnfromEPFL.

Prerequisites
Required:
▶
Calculusandlinearalgebra
Familiaritywithbasicmatrixmanipulationsanddifferentiationof
multivariatefunctionsetc.isexpected.
Useful:
▶
Abasiccourseonprobabilitytheory

Recommended Books
▶
DimitrisBertsimasandJohnTsitsiklis,IntroductiontoLinear
Optimization,DynamicIdeas&AthenaScientific,2008.
▶
Thisbookprovidesaunified,insightful,andmoderntreatmentof
linearoptimization,thatis,linearprogramming,networkflow
problems,anddiscreteoptimization. Itincludesclassicaltopicsas
wellasthestateoftheart,inboththeoryandpractice.
▶
DimitriP.Bertsekas,NonlinearProgramming,AthenaScientific,
2016.
▶
Abest-sellingnonlinearprogrammingbookfocusingonalgorithms
forconstrainedandunconstrainedoptimization,Lagrange
multipliersanddualityaswellaslargescaleproblems.

(Tentative) Course Outline
Part I: Linear Optimization
▶
Applications
▶
TheSimplexMethod
▶
Duality
▶
Large-ScaleOptimization(iftime)
Part II: Discrete Optimization
▶
Applications
▶
Branch&BoundandCuttingPlanes
▶
LagrangianMethods(iftime)
▶
ApproximationAlgorithms(iftime)
Part III: Nonlinear Optimization
▶
Applications
▶
OptimalityConditions
▶
LocalOptimization(iftime)

Lecture Outline
MathematicalOptimization: History&Formulation
LinearOptimization: History&Formulation
BuildingaModel: ExamplesofFormulations
Extensions: ConvexPiecewiseLinearObjective
WideApplicabilityofLinearOptimization

Lecture Outline
MathematicalOptimization: History&Formulation
LinearOptimization: History&Formulation
BuildingaModel: ExamplesofFormulations
Extensions: ConvexPiecewiseLinearObjective
WideApplicabilityofLinearOptimization

Mathematical Optimization
f(x ,x )
1 2
OptimizationProblem:
minimize f(x)
subjectto g (x)≤b
1 1 feasible set
.
.
.
g (x)≤b
m m x 1 x 2
▶
x :=(x ,...,x )istheoptimizationordecisionvariable
1 n
▶ f :Rn →Ristheobjectivefunction
▶ g :Rn →R,i =1,...,m,aretheconstraintfunctions
i
▶
b ,...,b arethebounds,limits,orright-handsides
1 m

Mathematical Optimization
|     | f(x ,x | )   |
| --- | ------ | --- |
|     | 1 2    |     |
OptimizationProblem:
minimize f(x)
subjectto g (x)≤b
| 1   | 1   | feasible set |
| --- | --- | ------------ |
.
.
.
g (x)≤b
| m   | m x |     |
| --- | --- | --- |
1 x 2
Avectorx⋆
iscalledoptimal,orasolutiontotheproblem,ifitis
feasibleandsatisfies
| f(x⋆)≤f(z) | ∀z :g(z)≤b, | i =1,...,m. |
| ---------- | ----------- | ----------- |
|            | i           | i           |

History of Optimization
Fermat(1638)andNewton(1670):
df(x)
| min f(x) | x :scalar | =0  |
| -------- | --------- | --- |
dx

History of Optimization
▶ Euler(1755):
| min f(x) | =⇒  | ∇f(x)=0 |
| -------- | --- | ------- |
x∈Rn
▶ Lagrange(1797):
| min f(x) s.t. | g k (x)=0, | k =1,...,m |
| ------------- | ---------- | ---------- |
▶
Euler,Lagrange:
Problemsininfinitedimensions,calculusofvariations

Lecture Outline
MathematicalOptimization: History&Formulation
LinearOptimization: History&Formulation
BuildingaModel: ExamplesofFormulations
Extensions: ConvexPiecewiseLinearObjective
WideApplicabilityofLinearOptimization

Linear Optimization
ALinearOptimizationorLinearProgrammingProblem:
min c x + c x + ... + c x
1 1 2 2 n n
s.t. a x + a x + ... + a x ≤ b ∀i ∈M
i1 1 i2 2 in n i 1
a x + a x + ... + a x ≥ b ∀i ∈M
i1 1 i2 2 in n i 2
a x + a x + ... + a x = b ∀i ∈M
i1 1 i2 2 in n i 3
x ≥0 ∀j ∈N , x ≤0 ∀j ∈N
j 1 j 2
▶
M ,M ,M ={1,...,m},N ,N ⊆{1,...,n}
1 2 3 1 2
▶
x ,...,x arethedecisionvariables
1 n
▶
Theparametersc,b anda ,i =1,...,m,j =1,...,narefixed
j i ij
realconstants(problemdata)

Linear Optimization
ALinearOptimizationorLinearProgrammingProblem:
min c x + c x + ... + c x
1 1 2 2 n n
s.t. a x + a x + ... + a x ≤ b ∀i ∈M
i1 1 i2 2 in n i 1
a x + a x + ... + a x ≥ b ∀i ∈M
i1 1 i2 2 in n i 2
a x + a x + ... + a x = b ∀i ∈M
i1 1 i2 2 in n i 3
x ≥0 ∀j ∈N , x ≤0 ∀j ∈N
j 1 j 2
▶
Ifj ∈/ N ∪N ,x isafreeorunrestrictedvariable
1 2 j
▶
x isafeasiblesolutionifitsatisfiesalltheconstraints
▶
Thesetofallfeasiblesolutionsiscalledthefeasibleset,or
feasibleregion

Linear Optimization
ALinearOptimizationorLinearProgrammingProblem:
min c x + c x + ... + c x
1 1 2 2 n n
s.t. a x + a x + ... + a x ≤ b ∀i ∈M
i1 1 i2 2 in n i 1
a x + a x + ... + a x ≥ b ∀i ∈M
i1 1 i2 2 in n i 2
a x + a x + ... + a x = b ∀i ∈M
i1 1 i2 2 in n i 3
x ≥0 ∀j ∈N , x ≤0 ∀j ∈N
j 1 j 2
▶ c⊤x = (cid:80)n cx iscalledtheobjectiveorcostfunction
j=1 j j
▶ Afeasiblesolutionx⋆ thatminimizestheobjectivefunctionis
calledoptimal(feasible)solution
▶ Thevaluec⊤x⋆ isthencalledtheoptimalcost

Linear Optimization
ALinearOptimizationorLinearProgrammingProblem:
min c x + c x + ... + c x
1 1 2 2 n n
s.t. a x + a x + ... + a x ≤ b ∀i ∈M
i1 1 i2 2 in n i 1
a x + a x + ... + a x ≥ b ∀i ∈M
i1 1 i2 2 in n i 2
a x + a x + ... + a x = b ∀i ∈M
i1 1 i2 2 in n i 3
x ≥0 ∀j ∈N , x ≤0 ∀j ∈N
j 1 j 2
▶ IfforanyK ∈R,thereexistsafeasiblesolutionx suchthat
c⊤x ≤K,wesaythattheoptimalcostisunboundedbelow,or
thattheproblemisunbounded
▶
Noneedtostudymaximizationproblems. Why?

History of Linear Optimization
Thepre-algorithmicperiod
▶
Fourier,1826: methodforsolvingsystemoflinearinequalities
▶
delaValléePoussin,1911: simplex-likemethodforobjective
functionwithabsolutevalues
▶
Kantorovich,Koopmans,1930s: formulationsandsolution
method–NobelPrizeinEconomicsin1975
▶
vonNeumann,1928: gametheory,duality
▶
Farkas,Minkowski,Carathéodory,1870-1930: foundations

History of Linear Optimization
Themodernperiod
▶
GeorgeDantzig,1947: simplexmethod
▶
1950s: applications
▶
1960s: largescaleoptimization
▶
1970s: complexitytheory
▶
Khachiyan,1979: theellipsoidmethod
▶
Karmarkar,1984: interiorpointalgorithms

| Linear Programming |     |             | in the | Headlines |              |     |
| ------------------ | --- | ----------- | ------ | --------- | ------------ | --- |
| Interior-Point     |     | Methods—The |        |           | Breakthrough |     |
| Interior-Point     |     | Methods—The |        |           | Breakthrough |     |
BreakthroughinProblemSolving
BreakthroughinProblemSolving
ByJAMESGLEICK

|     |     |     |     | data.NowNarendraKarmarkar,a28-year-old | sides.Eachcornerofafacetonthedome                                                                                          

Linear Optimization
AnyLPcanbewrittenintheform:
min c x + c x + ... + c x
1 1 2 2 n n
s.t. a x + a x + ... + a x ≤ b
11 1 12 2 1n n 1
a x + a x + ... + a x ≤ b
21 1 22 2 2n n 2
. . . . .
. . . . .
. . . . .
a x + a x + ... + a x ≤ b
m1 1 m2 2 mn n m

Linear Optimization
▶
Collectinputdatainmatricesandvectors
|     |     |          |      |        |        |
| --- | ---- | -------- | ----- | -------- | -------- |
|     | a 11 | a 12 ··· | a 1n  | b 1      | c 1      |
|     | a   | a ···    | a 2n | b 2    | c 2    |
|     | 21   | 22       |       |          |          |
| A= | .    | . ...    | .    | b = .  | c = .  |
|     |  .  | .        | .    |  .     |  .     |
|     |  .  | .        | .    |  .     |  .     |
|     | a    | a ···    | a     | b        | c        |
|     | m1   | m2       | mn    | m        | n        |
▶ Collectdecisionvariablesinvector
 
x
1
x
2
|     |     |     | x = .  |     |     |
| --- | --- | --- | -------- | --- | --- |
 . 
 . 
x
n

Linear Optimization
▶
Collectinputdatainmatricesandvectors
minimize c⊤x
subjectto Ax ≤b
▶
Example:
minimize 3x +x
1 2
subjectto x +2x ≥2
1 2
2x +x ≥3
1 2
x ≥0,x ≥0
1 2

Lecture Outline
MathematicalOptimization: History&Formulation
LinearOptimization: History&Formulation
BuildingaModel: ExamplesofFormulations
Extensions: ConvexPiecewiseLinearObjective
WideApplicabilityofLinearOptimization

Building A Model
Buildingamodelforadecision-makingproblem:
1. Whatarethedecisionalternatives?
2. Underwhatrestrictionsarethedecisionsmade?
3. Whatisanappropriateobjectivecriterionforevaluatingthe
alternatives?

The Diet Problem
gpergoffood
| Food Protein | Sodium | Cost($/g) |
| ------------ | ------ | --------- |
| Salad 0.09   | 0.02   | 0.03      |
| Meat 0.60    | 0.06   | 0.9       |
▶
Dietaryrequirements:
▶
Atleast50gofprotein
▶
Atmost5.1gofsodium
Whatistheminimumcostdietsatisfyingallthedietaryrequirements?

The Diet Problem
Decisionvariables
▶ x : gramsofsaladinthediet
s
▶ x : gramsofmeatinthediet
m
Formulation
| min 0.03x  | s +0.9x | m     | ← costofdiet     |
| ---------- | ------- | ----- | ---------------- |
| s.t. 0.09x | s +0.6x | m ≥50 | ← gramsofprotein |
| 0.02x      | +0.06x  | ≤5.1  | ← gramsofsodium  |
s m
| x , | x ≥0 |     |     |
| --- | ---- | --- | --- |
| s   | m    |     |     |

Manufacturing Problem
Problemdescriptionanddata
▶
nproducts(e.g.,alloys),mrawmaterials(e.g.,metals)
▶
c: revenueofproductj (perunit)
j
▶
b: availableunitsofmateriali
i
▶
a : #unitsofmateriali productj needsinordertobeproduced
ij
Howmuchofeachgoodtoproducetomaximizetotalrevenue?

Manufacturing Problem
Decisionvariables
▶
x =amountofproductj produced
j
Formulation
(cid:88) n
| max | cx j j |     |
| --- | ------ | --- |
j=1
| s.t. a | x +···+a | x ≤b |
| ------ | -------- | ---- |
|        | 11 1 1n  | n 1  |
.
.
.
| a   | x +···+a    | x ≤b   |
| --- | ----------- | ------ |
|     | m1 1        | mn n m |
| x j | ≥0 j =1...n |        |

Transportation Problem
Problemdescriptionanddata
▶
P plants,W warehouses
▶
s supplyofpthplant,p =1...P
p
▶
d demandofwthwarehouse,w =1...W
w
▶
c : costoftransportationp →w
pw
Whatistheminimumcostwayofsatisfyingdemand?

| Transportation | Problem |     |     |
| -------------- | ------- | --- | --- |
Decisionvariables
| ▶ x =numberofunitstosendp |     | →w  |     |
| ------------------------- | --- | --- | --- |
pw
Formulation
| P   | W   |     |     |
| --- | --- | --- | --- |
(cid:88)(cid:88)
| min | c x | →transportationcost |     |
| --- | --- | ------------------- | --- |
pw pw
p=1w=1
P
(cid:88)
| s.t. | x =d ∀w =1...W | →meetdemand |     |
| ---- | -------------- | ----------- | --- |
pw w
p=1
W
(cid:88)
|     | x pw ≤s p ∀p =1...P | →donotexceedsupply |     |
| --- | ------------------- | ------------------ | --- |
w=1
| x pw | ≥0  | →moveitemsp | →w  |
| ---- | --- | ----------- | --- |

Scheduling
Problemdescriptionanddata
▶
Hospitalwantstodetermineweeklyshiftforitsnurses
▶
d: demandfornursesondayj,j =1...7
j
▶
Everynurseworks5daysinarow
▶
Goal: hireminimumnumberofnurses

Scheduling
DecisionVariables
▶
x: #nursesstartingtheirweekondayj
j
Formulation
7
(cid:80)
min x
j
j=1
s.t. x + x + x + x + x ≥ d
1 4 5 6 7 1
x + x + x + x + x ≥ d
1 2 5 6 7 2
x + x + x + x + x ≥ d
1 2 3 6 7 3
x + x + x + x + x ≥ d
1 2 3 4 7 4
x + x + x + x + x ≥ d
1 2 3 4 5 5
x + x + x + x + x ≥ d
2 3 4 5 6 6
x + x + x + x + x ≥ d
3 4 5 6 7 7
x ≥0
j

Messages
Howtoformulate?
1. Defineyourdecisionvariablesclearly
2. Writeconstraints
3. Writeobjectivefunction
=⇒ Nosystematicmethodavailable
Whatisagoodlinearoptimizationformulation?
▶
Smallnumberofvariables
▶
Smallnumberofconstraints
▶
SparseAmatrix

Lecture Outline
MathematicalOptimization: History&Formulation
LinearOptimization: History&Formulation
BuildingaModel: ExamplesofFormulations
Extensions: ConvexPiecewiseLinearObjective
WideApplicabilityofLinearOptimization

Convex Sets
Definition: AsetC isconvexifforanyx ,x ∈C andanyλ∈[0,1],it
1 2
holdsthat
λx +(1−λ)x ∈C
1 2

Convex Functions
| Definition:    | Afunctionf | :Rn →Risconvexifdomf   | isaconvexset |
| -------------- | ---------- | ---------------------- | ------------ |
| andifforallx,y | ∈domf      | andλ∈[0,1],itholdsthat |              |
f(λx +(1−λ)y)≤λf(x)+(1−λ)f(y)

|     |     |     |     |
| --- | --- | --- | --- |

|     |     |     |     |
| --- | --- | --- | --- |

Piecewise Linear Objective
Minimizepointwisemaximumoflinearfunctions
(cid:18) (cid:19)
min f(x)=max d⊤x +c
k k k
s.t. Ax ≥b
Equivalenttothelinearprogram:
min z
s.t. d⊤x +c ≤z ∀k
k k
Ax ≥b

Absolute Value Objective
Problemswith|·|
(cid:80)
| min c|x|   | (assumethatc | ≥0forallj) |
| ---------- | ------------ | ---------- |
| j j j      |              | j          |
| s.t. Ax ≥b |              |            |
Idea: |x|=max{x,−x}
Equivalenttothelinearprogram:
(cid:80)
min cz
|     | j j |     |
| --- | --- | --- |
s.t. Ax ≥b
x ≤z
|     | j j |     |
| --- | --- | --- |
−x ≤z
|     | j j |     |
| --- | --- | --- |
Message:
▶
Minimizingapiecewiselinearconvexfunctioncanbemodeledby
linearoptimization.

Lecture Outline
MathematicalOptimization: History&Formulation
LinearOptimization: History&Formulation
BuildingaModel: ExamplesofFormulations
Extensions: ConvexPiecewiseLinearObjective
WideApplicabilityofLinearOptimization

Wide Applicability
▶
Transportation
▶
Airtrafficcontrol
▶
Crewscheduling
▶
Vehiclerouting

Wide Applicability
▶
Telecommunications
▶
Antennadesign
▶
Networkdesign
▶
Manufacturing

Wide Applicability
▶
Medicine
▶
Engineering
▶
Typesetting(TEX,LATEX)

Capacity Expansion
Data
▶
D : forecasteddemandforelectricityinyeart
t
▶
E : existingcapacity(inoil)availableinyeart
t
▶
w : costtoinstall1MWofwindcapacity
t
▶
g : costtoinstall1MWofgascapacity
t
▶
Nomorethan20%wind
▶
Windgeneratorslast20years
▶
Gasturbinepowerplantslast15years

Capacity Expansion
DecisionVariables
▶
x : amountofwindcapacitynewlyinstalledatthestartofyeart
t
▶
y : amountofgascapacitynewlyinstalledatthestartofyeart
t
▶
u : totalwindcapacityinyeart
t
▶
v : totalgascapacityinyeart
t
Formulation
| min (cid:80)T w x +g | y   |          |
| -------------------- | --- | -------- |
| t=1 t t              | t t |          |
| s.t. u = (cid:80)t   | x t | =1,...,T |
| t s=max(1,t−19)      | s   |          |
(cid:80)t
| v =             | y t | =1,...,T |
| --------------- | --- | -------- |
| t s=max(1,t−14) | s   |          |

| u +v +E     | ≥D   |             |
| ----------- | ---- | ----------- |
| t t t       | t  |             |
| v ≤0.2(u +v | +E ) | ∀t =1,...,T |
| t t         | t t  |             |

| x ,y ,u ,v ≥0 |     |     |
| ------------- | --- | --- |
| t t t t       |     |     |

Revenue Management
TheAirlineIndustry
▶
PriortoDeregulation(1978)
▶
Carriersonlyallowedtoflycertainroutes
→Northwest,Eastern,Southwest,etc.
▶
FaresdeterminedbyCivilAeronauticsBoard(CAB)basedon
mileageandothercosts(CABnolongerexists)
▶
PostDeregulation
▶
Anyonecanfly,anywhere
▶
Faresdeterminedbycarrier(andthemarket)

Revenue Management
Economics
▶
Hugesunkandfixedcosts
▶ Verylowvariablecostsperpassenger(≲$10/passenger)
▶
Strongeconomicallycompetitiveenvironment
▶
Near-perfectinformationandnegligiblecostofinformation
▶
Highlyperishableinventory
▶
Result: Multiplefares

Revenue Management
Data
▶ norigins,ndestinations
▶ 1hub
▶ 2classes(forsimplicity),Q-class,Y-class
▶ RevenuesrQ,rY
ij ij
| ▶ Capacities:      | C ,i =1,...,n;C | ,j =1,...,n |
| ------------------ | --------------- | ----------- |
|                    | i0              | 0j          |
| ▶ Expecteddemands: | DQ,DY           |             |
ij ij

Revenue Management
DecisionVariables
▶
Q : #ofQ-classcustomersweacceptfromitoj
ij
▶
Y : #ofY-classcustomersweacceptfromitoj
ij
Formulation
(cid:88)
maximize rQQ +rYY
ij ij ij ij
i,j
n
(cid:88)
subjectto (Q +Y )≤C
ij ij i0
j=0
n
(cid:88)
(Q +Y )≤C
ij ij 0j
i=0
0≤Q ≤DQ, 0≤Y ≤DY
ij ij ij ij

Revenue Management
| We estimate | that RM | has generated $1.4 | billion in in- |
| ----------- | ------- | ------------------ | -------------- |
crementalrevenueforAmericanAirlinesinthelastthree
| years alone.   | This is not | a one-time benefit. | We expect        |
| -------------- | ----------- | ------------------- | ---------------- |
| RM to generate | at least    | $500 million        | annually for the |
foreseeablefuture.
RobertCrandall
formerCEOofAmericanAirlines