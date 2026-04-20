# --------------------------------------------------------------------------------------------------
# ---------------------------------- Weatherlight :: Nodes :: Type ---------------------------------
# --------------------------------------------------------------------------------------------------
from Dragon import Attr
from Dragon import Node
from Dragon import Type


# --------------------------------------------------------------------------------------------------
# ----------------------------------------- Node :: Subtype ----------------------------------------
# --------------------------------------------------------------------------------------------------
class Subtype(Node):

	# -----------------------------------------------------------------------------------------
	# --------------------------------- Embedding Annotations ---------------------------------
	# -----------------------------------------------------------------------------------------
	subtype 		: Type

	# artifact
	blood		  	: Attr[None | bool]
	clue		  	: Attr[None | bool]
	equipment	  	: Attr[None | bool]
	food		  	: Attr[None | bool]
	fortification 	: Attr[None | bool]
	gold		  	: Attr[None | bool]
	map		 	  	: Attr[None | bool]
	powerstone	  	: Attr[None | bool]
	treasure	  	: Attr[None | bool]
	vehicle		  	: Attr[None | bool]

	# battle
	siege		  	: Attr[None | bool]

	# creature
	advisor		 	: Attr[None | bool]
	aetherborn	 	: Attr[None | bool]
	alien		 	: Attr[None | bool]
	ally		 	: Attr[None | bool]
	angel		 	: Attr[None | bool]
	antelope	 	: Attr[None | bool]
	ape		 		: Attr[None | bool]
	archer		 	: Attr[None | bool]
	archon		 	: Attr[None | bool]
	armadillo	 	: Attr[None | bool]
	army		 	: Attr[None | bool]
	artificer	 	: Attr[None | bool]
	assassin	 	: Attr[None | bool]
	assembly_worker : Attr[None | bool]
	atog		 	: Attr[None | bool]
	aurochs		 	: Attr[None | bool]
	avatar		 	: Attr[None | bool]
	azra		 	: Attr[None | bool]
	badger		 	: Attr[None | bool]
	balloon		 	: Attr[None | bool]
	barbarian	 	: Attr[None | bool]
	bard		 	: Attr[None | bool]
	basilisk	 	: Attr[None | bool]
	bat		 		: Attr[None | bool]
	bear		 	: Attr[None | bool]
	beast		 	: Attr[None | bool]
	beeble		 	: Attr[None | bool]
	beholder	 	: Attr[None | bool]
	berserker	 	: Attr[None | bool]
	bird		 	: Attr[None | bool]
	blinkmoth	 	: Attr[None | bool]
	boar		 	: Attr[None | bool]
	bringer		 	: Attr[None | bool]
	brushwagg	 	: Attr[None | bool]
	camarid		 	: Attr[None | bool]
	camel		 	: Attr[None | bool]
	caribou		 	: Attr[None | bool]
	carrier		 	: Attr[None | bool]
	cat		 		: Attr[None | bool]
	centaur		 	: Attr[None | bool]
	cephalid	 	: Attr[None | bool]
	chimera		 	: Attr[None | bool]
	citizen		 	: Attr[None | bool]
	cleric		 	: Attr[None | bool]
	cockatrice	 	: Attr[None | bool]
	construct	 	: Attr[None | bool]
	coward		 	: Attr[None | bool]
	crab		 	: Attr[None | bool]
	crocodile	 	: Attr[None | bool]
	cyclops		 	: Attr[None | bool]
	dauthi		 	: Attr[None | bool]
	demigod		 	: Attr[None | bool]
	demon		 	: Attr[None | bool]
	deserter	 	: Attr[None | bool]
	devil		 	: Attr[None | bool]
	dinosaur	 	: Attr[None | bool]
	djinn		 	: Attr[None | bool]
	dog		 		: Attr[None | bool]
	dragon		 	: Attr[None | bool]
	drake		 	: Attr[None | bool]
	dreadnought	 	: Attr[None | bool]
	drone		 	: Attr[None | bool]
	druid		 	: Attr[None | bool]
	dryad		 	: Attr[None | bool]
	dwarf		 	: Attr[None | bool]
	efreet		 	: Attr[None | bool]
	egg		 		: Attr[None | bool]
	elder		 	: Attr[None | bool]
	eldrazi	 		: Attr[None | bool]
	elemental	 	: Attr[None | bool]
	elephant	 	: Attr[None | bool]
	elf		 		: Attr[None | bool]
	elk		 		: Attr[None | bool]
	eye		 		: Attr[None | bool]
	faerie		 	: Attr[None | bool]
	ferret		 	: Attr[None | bool]
	fish		 	: Attr[None | bool]
	flagbearer	 	: Attr[None | bool]
	fox		 		: Attr[None | bool]
	fractal	 		: Attr[None | bool]
	frog		 	: Attr[None | bool]
	fungus		 	: Attr[None | bool]
	gargoyle	 	: Attr[None | bool]
	germ		 	: Attr[None | bool]
	giant		 	: Attr[None | bool]
	gnoll		 	: Attr[None | bool]
	gnome		 	: Attr[None | bool]
	goat		 	: Attr[None | bool]
	goblin		 	: Attr[None | bool]
	god		 		: Attr[None | bool]
	golem		 	: Attr[None | bool]
	gorgon		 	: Attr[None | bool]
	graveborn	 	: Attr[None | bool]
	gremlin	 		: Attr[None | bool]
	griffin	 		: Attr[None | bool]
	hag		 		: Attr[None | bool]
	harpy		 	: Attr[None | bool]
	hellion	 		: Attr[None | bool]
	hippo		 	: Attr[None | bool]
	hippogriff	 	: Attr[None | bool]
	homarid	 		: Attr[None | bool]
	homunculus	 	: Attr[None | bool]
	horror		 	: Attr[None | bool]
	horse		 	: Attr[None | bool]
	human		 	: Attr[None | bool]
	hydra		 	: Attr[None | bool]
	hyena		 	: Attr[None | bool]
	illusion	 	: Attr[None | bool]
	imp		 		: Attr[None | bool]
	incarnation	 	: Attr[None | bool]
	inkling	 		: Attr[None | bool]
	insect		 	: Attr[None | bool]
	jackal		 	: Attr[None | bool]
	jellyfish	 	: Attr[None | bool]
	juggernaut	 	: Attr[None | bool]
	kavu		 	: Attr[None | bool]
	kirin		 	: Attr[None | bool]
	kithkin	 		: Attr[None | bool]
	knight		 	: Attr[None | bool]
	kobold		 	: Attr[None | bool]
	kor		 		: Attr[None | bool]
	kraken		 	: Attr[None | bool]
	lamia		 	: Attr[None | bool]
	lammasu	 		: Attr[None | bool]
	leech		 	: Attr[None | bool]
	leviathan	 	: Attr[None | bool]
	lhurgoyf	 	: Attr[None | bool]
	licid		 	: Attr[None | bool]
	lizard		 	: Attr[None | bool]
	manticore	 	: Attr[None | bool]
	masticore	 	: Attr[None | bool]
	mercenary	 	: Attr[None | bool]
	merfolk	 		: Attr[None | bool]
	metathran	 	: Attr[None | bool]
	minion		 	: Attr[None | bool]
	minotaur	 	: Attr[None | bool]
	mite		 	: Attr[None | bool]
	mole		 	: Attr[None | bool]
	mongoose	 	: Attr[None | bool]
	monk		 	: Attr[None | bool]
	monkey		 	: Attr[None | bool]
	moonfolk	 	: Attr[None | bool]
	mount		 	: Attr[None | bool]
	mouse		 	: Attr[None | bool]
	mutant		 	: Attr[None | bool]
	myr		 		: Attr[None | bool]
	mystic		 	: Attr[None | bool]
	naga		 	: Attr[None | bool]
	nautilus	 	: Attr[None | bool]
	nephilim	 	: Attr[None | bool]
	nightmare	 	: Attr[None | bool]
	nightstalker 	: Attr[None | bool]
	ninja		 	: Attr[None | bool]
	noble		 	: Attr[None | bool]
	noggle		 	: Attr[None | bool]
	nomad		 	: Attr[None | bool]
	nymph		 	: Attr[None | bool]
	octopus	 		: Attr[None | bool]
	ogre		 	: Attr[None | bool]
	ooze		 	: Attr[None | bool]
	orb		 		: Attr[None | bool]
	orc		 		: Attr[None | bool]
	orgg		 	: Attr[None | bool]
	otter		 	: Attr[None | bool]
	ouphe		 	: Attr[None | bool]
	ox		 		: Attr[None | bool]
	oyster		 	: Attr[None | bool]
	pangolin	 	: Attr[None | bool]
	peasant	 		: Attr[None | bool]
	pegasus	 		: Attr[None | bool]
	pentavite	 	: Attr[None | bool]
	pest		 	: Attr[None | bool]
	phelddagrif	 	: Attr[None | bool]
	phoenix	 		: Attr[None | bool]
	phyrexian	 	: Attr[None | bool]
	pilot		 	: Attr[None | bool]
	pincher	 		: Attr[None | bool]
	pirate		 	: Attr[None | bool]
	plant		 	: Attr[None | bool]
	praetor	 		: Attr[None | bool]
	primordial	 	: Attr[None | bool]
	prism		 	: Attr[None | bool]
	processor	 	: Attr[None | bool]
	rabbit		 	: Attr[None | bool]
	raccoon	 		: Attr[None | bool]
	rat		 		: Attr[None | bool]
	rebel		 	: Attr[None | bool]
	reflection	 	: Attr[None | bool]
	rhino		 	: Attr[None | bool]
	rigger		 	: Attr[None | bool]
	rogue		 	: Attr[None | bool]
	sable		 	: Attr[None | bool]
	salamander	 	: Attr[None | bool]
	samurai	 		: Attr[None | bool]
	sand		 	: Attr[None | bool]
	saproling	 	: Attr[None | bool]
	satyr		 	: Attr[None | bool]
	scarecrow	 	: Attr[None | bool]
	scientist	 	: Attr[None | bool]
	scion		 	: Attr[None | bool]
	scorpion	 	: Attr[None | bool]
	scout		 	: Attr[None | bool]
	serf		 	: Attr[None | bool]
	serpent	 		: Attr[None | bool]
	servo		 	: Attr[None | bool]
	shade		 	: Attr[None | bool]
	shaman		 	: Attr[None | bool]
	shapeshifter 	: Attr[None | bool]
	shark		 	: Attr[None | bool]
	sheep		 	: Attr[None | bool]
	siren		 	: Attr[None | bool]
	skeleton	 	: Attr[None | bool]
	slith		 	: Attr[None | bool]
	sliver		 	: Attr[None | bool]
	slug		 	: Attr[None | bool]
	snake		 	: Attr[None | bool]
	soldier	 		: Attr[None | bool]
	soltari	 		: Attr[None | bool]
	spawn		 	: Attr[None | bool]
	specter	 		: Attr[None | bool]
	spellshaper	 	: Attr[None | bool]
	sphinx		 	: Attr[None | bool]
	spider		 	: Attr[None | bool]
	spike		 	: Attr[None | bool]
	spirit		 	: Attr[None | bool]
	splinter	 	: Attr[None | bool]
	sponge		 	: Attr[None | bool]
	squid		 	: Attr[None | bool]
	squirrel	 	: Attr[None | bool]
	starfish	 	: Attr[None | bool]
	surrakar	 	: Attr[None | bool]
	survivor	 	: Attr[None | bool]
	tentacle	 	: Attr[None | bool]
	tetravite	 	: Attr[None | bool]
	thalakos	 	: Attr[None | bool]
	thopter	 		: Attr[None | bool]
	thrull		 	: Attr[None | bool]
	tiefling	 	: Attr[None | bool]
	treefolk	 	: Attr[None | bool]
	trilobite	 	: Attr[None | bool]
	triskelavite 	: Attr[None | bool]
	troll		 	: Attr[None | bool]
	turtle		 	: Attr[None | bool]
	tyranid	 		: Attr[None | bool]
	unicorn	 		: Attr[None | bool]
	vampire	 		: Attr[None | bool]
	vedalken	 	: Attr[None | bool]
	viashino	 	: Attr[None | bool]
	voliver	 		: Attr[None | bool]
	wall		 	: Attr[None | bool]
	warlock	 		: Attr[None | bool]
	warrior	 		: Attr[None | bool]
	weird		 	: Attr[None | bool]
	werewolf	 	: Attr[None | bool]
	whale		 	: Attr[None | bool]
	wizard		 	: Attr[None | bool]
	wolf		 	: Attr[None | bool]
	wolverine	 	: Attr[None | bool]
	wombat		 	: Attr[None | bool]
	worm		 	: Attr[None | bool]
	wraith		 	: Attr[None | bool]
	wurm		 	: Attr[None | bool]
	yeti		 	: Attr[None | bool]
	zombie		 	: Attr[None | bool]
	zubera		 	: Attr[None | bool]

	# enchantment
	aura		 	: Attr[None | bool]
	background	 	: Attr[None | bool]
	cartouche	 	: Attr[None | bool]
	function		: Attr[None | bool] # alias for 'class'
	curse		 	: Attr[None | bool]
	rune		 	: Attr[None | bool]
	saga		 	: Attr[None | bool]
	shrine		 	: Attr[None | bool]
	role		 	: Attr[None | bool]

	# land
	desert			: Attr[None | bool]
	forest		 	: Attr[None | bool]
	gate		 	: Attr[None | bool]
	island		 	: Attr[None | bool]
	lair		 	: Attr[None | bool]
	locus		 	: Attr[None | bool]
	mine		 	: Attr[None | bool]
	mountain	 	: Attr[None | bool]
	plains		 	: Attr[None | bool]
	power_plant	 	: Attr[None | bool]
	sphere		 	: Attr[None | bool]
	swamp		 	: Attr[None | bool]
	tower		 	: Attr[None | bool]
	urzas		 	: Attr[None | bool]

	# planeswalker
	ajani           : Attr[None | bool]
	angrath         : Attr[None | bool]
	arlinn          : Attr[None | bool]
	ashiok          : Attr[None | bool]
	basri           : Attr[None | bool]
	bolas           : Attr[None | bool]
	calix           : Attr[None | bool]
	chandra         : Attr[None | bool]
	dack            : Attr[None | bool]
	dakkon          : Attr[None | bool]
	davriel         : Attr[None | bool]
	domri           : Attr[None | bool]
	dovin           : Attr[None | bool]
	elspeth         : Attr[None | bool]
	estrid          : Attr[None | bool]
	freyalise       : Attr[None | bool]
	garruk          : Attr[None | bool]
	gideon          : Attr[None | bool]
	hualti          : Attr[None | bool]
	jace            : Attr[None | bool]
	jared           : Attr[None | bool]
	jaya            : Attr[None | bool]
	jeska           : Attr[None | bool]
	kaito           : Attr[None | bool]
	karn            : Attr[None | bool]
	kasmina         : Attr[None | bool]
	kaya            : Attr[None | bool]
	kiora           : Attr[None | bool]
	koth            : Attr[None | bool]
	liliana         : Attr[None | bool]
	lukka           : Attr[None | bool]
	narset          : Attr[None | bool]
	nahiri          : Attr[None | bool]
	niko            : Attr[None | bool]
	nissa           : Attr[None | bool]
	obi             : Attr[None | bool]
	ob              : Attr[None | bool]
	oko             : Attr[None | bool]
	ral             : Attr[None | bool]
	rowan           : Attr[None | bool]
	saheeli         : Attr[None | bool]
	samut           : Attr[None | bool]
	sarkhan         : Attr[None | bool]
	serra           : Attr[None | bool]
	sorin           : Attr[None | bool]
	tamiyo          : Attr[None | bool]
	teferi          : Attr[None | bool]
	teyo            : Attr[None | bool]
	tezzeret        : Attr[None | bool]
	tibalt          : Attr[None | bool]
	tyvar           : Attr[None | bool]
	ugin            : Attr[None | bool]
	venser          : Attr[None | bool]
	vivien          : Attr[None | bool]
	vraska          : Attr[None | bool]
	will            : Attr[None | bool]
	windgrace       : Attr[None | bool]
	wrenn           : Attr[None | bool]
	xenagos         : Attr[None | bool]
	yanggu          : Attr[None | bool]
	yanling         : Attr[None | bool]

	# instant and sorcery
	adventure 		: Attr[None | bool]
	arcane			: Attr[None | bool]
	lesson 			: Attr[None | bool]
	trap			: Attr[None | bool]
	
	# -----------------------------------------------------------------------------------------
	# -------------------------------- Operator :: Constructor --------------------------------
	# -----------------------------------------------------------------------------------------
	def __init__(self, *components: Node | str, **attributes: bool | int | float) -> None:
		super().__init__(*components, **attributes)

		# artifact
		blood		  	= attributes.get('blood')
		clue		  	= attributes.get('clue')
		equipment	  	= attributes.get('equipment')
		food		  	= attributes.get('food')
		fortificaon 	= attributes.get('fortificaon')
		gold		  	= attributes.get('gold')
		map		 	  	= attributes.get('map')
		powerstone	  	= attributes.get('powerstone')
		treasure	  	= attributes.get('treasure')
		vehicle		  	= attributes.get('vehicle')

		# battle
		siege		  	= attributes.get('siege')

		# creature
		advisor		 	= attributes.get('advisor')
		aetherborn	 	= attributes.get('aetherborn')
		alien		 	= attributes.get('alien')
		ally		 	= attributes.get('ally')
		angel		 	= attributes.get('angel')
		antelope	 	= attributes.get('antelope')
		ape		 		= attributes.get('ape')
		archer		 	= attributes.get('archer')
		archon		 	= attributes.get('archon')
		armadillo	 	= attributes.get('armadillo')
		army		 	= attributes.get('army')
		artificer	 	= attributes.get('artificer')
		assassin	 	= attributes.get('assassin')
		assembly_worker = attributes.get('assembly_worker')
		atog		 	= attributes.get('atog')
		aurochs		 	= attributes.get('aurochs')
		avatar		 	= attributes.get('avatar')
		azra		 	= attributes.get('azra')
		badger		 	= attributes.get('badger')
		balloon		 	= attributes.get('balloon')
		barbarian	 	= attributes.get('barbarian')
		bard		 	= attributes.get('bard')
		basilisk	 	= attributes.get('basilisk')
		bat		 		= attributes.get('bat')
		bear		 	= attributes.get('bear')
		beast		 	= attributes.get('beast')
		beeble		 	= attributes.get('beeble')
		beholder	 	= attributes.get('beholder')
		berserker	 	= attributes.get('berserker')
		bird		 	= attributes.get('bird')
		blinkmoth	 	= attributes.get('blinkmoth')
		boar		 	= attributes.get('boar')
		bringer		 	= attributes.get('bringer')
		brushwagg	 	= attributes.get('brushwagg')
		camarid		 	= attributes.get('camarid')
		camel		 	= attributes.get('camel')
		caribou		 	= attributes.get('caribou')
		carrier		 	= attributes.get('carrier')
		cat		 		= attributes.get('cat')
		centaur		 	= attributes.get('centaur')
		cephalid	 	= attributes.get('cephalid')
		chimera		 	= attributes.get('chimera')
		citizen		 	= attributes.get('citizen')
		cleric		 	= attributes.get('cleric')
		cockatrice	 	= attributes.get('cockatrice')
		construct	 	= attributes.get('construct')
		coward		 	= attributes.get('coward')
		crab		 	= attributes.get('crab')
		crocodile	 	= attributes.get('crocodile')
		cyclops		 	= attributes.get('cyclops')
		dauthi		 	= attributes.get('dauthi')
		demigod		 	= attributes.get('demigod')
		demon		 	= attributes.get('demon')
		deserter	 	= attributes.get('deserter')
		devil		 	= attributes.get('devil')
		dinosaur	 	= attributes.get('dinosaur')
		djinn		 	= attributes.get('djinn')
		dog		 		= attributes.get('dog')
		dragon		 	= attributes.get('dragon')
		drake		 	= attributes.get('drake')
		dreadnought	 	= attributes.get('dreadnought')
		drone		 	= attributes.get('drone')
		druid		 	= attributes.get('druid')
		dryad		 	= attributes.get('dryad')
		dwarf		 	= attributes.get('dwarf')
		efreet		 	= attributes.get('efreet')
		egg		 		= attributes.get('egg')
		elder		 	= attributes.get('elder')
		eldrazi	 		= attributes.get('eldrazi')
		elemental	 	= attributes.get('elemental')
		elephant	 	= attributes.get('elephant')
		elf		 		= attributes.get('elf')
		elk		 		= attributes.get('elk')
		eye		 		= attributes.get('eye')
		faerie		 	= attributes.get('faerie')
		ferret		 	= attributes.get('ferret')
		fish		 	= attributes.get('fish')
		flagbearer	 	= attributes.get('flagbearer')
		fox		 		= attributes.get('fox')
		fractal	 		= attributes.get('fractal')
		frog		 	= attributes.get('frog')
		fungus		 	= attributes.get('fungus')
		gargoyle	 	= attributes.get('gargoyle')
		germ		 	= attributes.get('germ')
		giant		 	= attributes.get('giant')
		gnoll		 	= attributes.get('gnoll')
		gnome		 	= attributes.get('gnome')
		goat		 	= attributes.get('goat')
		goblin		 	= attributes.get('goblin')
		god		 		= attributes.get('god')
		golem		 	= attributes.get('golem')
		gorgon		 	= attributes.get('gorgon')
		graveborn	 	= attributes.get('graveborn')
		gremlin	 		= attributes.get('gremlin')
		griffin	 		= attributes.get('griffin')
		hag		 		= attributes.get('hag')
		harpy		 	= attributes.get('harpy')
		hellion	 		= attributes.get('hellion')
		hippo		 	= attributes.get('hippo')
		hippogriff	 	= attributes.get('hippogriff')
		homarid	 		= attributes.get('homarid')
		homunculus	 	= attributes.get('homunculus')
		horror		 	= attributes.get('horror')
		horse		 	= attributes.get('horse')
		human		 	= attributes.get('human')
		hydra		 	= attributes.get('hydra')
		hyena		 	= attributes.get('hyena')
		illusion	 	= attributes.get('illusion')
		imp		 		= attributes.get('imp')
		incarnation	 	= attributes.get('incarnation')
		inkling	 		= attributes.get('inkling')
		insect		 	= attributes.get('insect')
		jackal		 	= attributes.get('jackal')
		jellyfish	 	= attributes.get('jellyfish')
		juggernaut	 	= attributes.get('juggernaut')
		kavu		 	= attributes.get('kavu')
		kirin		 	= attributes.get('kirin')
		kithkin	 		= attributes.get('kithkin')
		knight		 	= attributes.get('knight')
		kobold		 	= attributes.get('kobold')
		kor		 		= attributes.get('kor')
		kraken		 	= attributes.get('kraken')
		lamia		 	= attributes.get('lamia')
		lammasu	 		= attributes.get('lammasu')
		leech		 	= attributes.get('leech')
		leviathan	 	= attributes.get('leviathan')
		lhurgoyf	 	= attributes.get('lhurgoyf')
		licid		 	= attributes.get('licid')
		lizard		 	= attributes.get('lizard')
		manticore	 	= attributes.get('manticore')
		masticore	 	= attributes.get('masticore')
		mercenary	 	= attributes.get('mercenary')
		merfolk	 		= attributes.get('merfolk')
		metathran	 	= attributes.get('metathran')
		minion		 	= attributes.get('minion')
		minotaur	 	= attributes.get('minotaur')
		mite		 	= attributes.get('mite')
		mole		 	= attributes.get('mole')
		mongoose	 	= attributes.get('mongoose')
		monk		 	= attributes.get('monk')
		monkey		 	= attributes.get('monkey')
		moonfolk	 	= attributes.get('moonfolk')
		mount		 	= attributes.get('mount')
		mouse		 	= attributes.get('mouse')
		mutant		 	= attributes.get('mutant')
		myr		 		= attributes.get('myr')
		mystic		 	= attributes.get('mystic')
		naga		 	= attributes.get('naga')
		nautilus	 	= attributes.get('nautilus')
		nephilim	 	= attributes.get('nephilim')
		nightmare	 	= attributes.get('nightmare')
		nightstalker 	= attributes.get('nightstalker')
		ninja		 	= attributes.get('ninja')
		noble		 	= attributes.get('noble')
		noggle		 	= attributes.get('noggle')
		nomad		 	= attributes.get('nomad')
		nymph		 	= attributes.get('nymph')
		octopus	 		= attributes.get('octopus')
		ogre		 	= attributes.get('ogre')
		ooze		 	= attributes.get('ooze')
		orb		 		= attributes.get('orb')
		orc		 		= attributes.get('orc')
		orgg		 	= attributes.get('orgg')
		otter		 	= attributes.get('otter')
		ouphe		 	= attributes.get('ouphe')
		ox		 		= attributes.get('ox')
		oyster		 	= attributes.get('oyster')
		pangolin	 	= attributes.get('pangolin')
		peasant	 		= attributes.get('peasant')
		pegasus	 		= attributes.get('pegasus')
		pentavite	 	= attributes.get('pentavite')
		pest		 	= attributes.get('pest')
		phelddagrif	 	= attributes.get('phelddagrif')
		phoenix	 		= attributes.get('phoenix')
		phyrexian	 	= attributes.get('phyrexian')
		pilot		 	= attributes.get('pilot')
		pincher	 		= attributes.get('pincher')
		pirate		 	= attributes.get('pirate')
		plant		 	= attributes.get('plant')
		praetor	 		= attributes.get('praetor')
		primordial	 	= attributes.get('primordial')
		prism		 	= attributes.get('prism')
		processor	 	= attributes.get('processor')
		rabbit		 	= attributes.get('rabbit')
		raccoon	 		= attributes.get('raccoon')
		rat		 		= attributes.get('rat')
		rebel		 	= attributes.get('rebel')
		reflection	 	= attributes.get('reflection')
		rhino		 	= attributes.get('rhino')
		rigger		 	= attributes.get('rigger')
		rogue		 	= attributes.get('rogue')
		sable		 	= attributes.get('sable')
		salamander	 	= attributes.get('salamander')
		samurai	 		= attributes.get('samurai')
		sand		 	= attributes.get('sand')
		saproling	 	= attributes.get('saproling')
		satyr		 	= attributes.get('satyr')
		scarecrow	 	= attributes.get('scarecrow')
		scientist	 	= attributes.get('scientist')
		scion		 	= attributes.get('scion')
		scorpion	 	= attributes.get('scorpion')
		scout		 	= attributes.get('scout')
		serf		 	= attributes.get('serf')
		serpent	 		= attributes.get('serpent')
		servo		 	= attributes.get('servo')
		shade		 	= attributes.get('shade')
		shaman		 	= attributes.get('shaman')
		shapeshifter 	= attributes.get('shapeshifter')
		shark		 	= attributes.get('shark')
		sheep		 	= attributes.get('sheep')
		siren		 	= attributes.get('siren')
		skeleton	 	= attributes.get('skeleton')
		slith		 	= attributes.get('slith')
		sliver		 	= attributes.get('sliver')
		slug		 	= attributes.get('slug')
		snake		 	= attributes.get('snake')
		soldier	 		= attributes.get('soldier')
		soltari	 		= attributes.get('soltari')
		spawn		 	= attributes.get('spawn')
		specter	 		= attributes.get('specter')
		spellshaper	 	= attributes.get('spellshaper')
		sphinx		 	= attributes.get('sphinx')
		spider		 	= attributes.get('spider')
		spike		 	= attributes.get('spike')
		spirit		 	= attributes.get('spirit')
		splinter	 	= attributes.get('splinter')
		sponge		 	= attributes.get('sponge')
		squid		 	= attributes.get('squid')
		squirrel	 	= attributes.get('squirrel')
		starfish	 	= attributes.get('starfish')
		surrakar	 	= attributes.get('surrakar')
		survivor	 	= attributes.get('survivor')
		tentacle	 	= attributes.get('tentacle')
		tetravite	 	= attributes.get('tetravite')
		thalakos	 	= attributes.get('thalakos')
		thopter	 		= attributes.get('thopter')
		thrull		 	= attributes.get('thrull')
		tiefling	 	= attributes.get('tiefling')
		treefolk	 	= attributes.get('treefolk')
		trilobite	 	= attributes.get('trilobite')
		triskelavite 	= attributes.get('triskelavite')
		troll		 	= attributes.get('troll')
		turtle		 	= attributes.get('turtle')
		tyranid	 		= attributes.get('tyranid')
		unicorn	 		= attributes.get('unicorn')
		vampire	 		= attributes.get('vampire')
		vedalken	 	= attributes.get('vedalken')
		viashino	 	= attributes.get('viashino')
		voliver	 		= attributes.get('voliver')
		wall		 	= attributes.get('wall')
		warlock	 		= attributes.get('warlock')
		warrior	 		= attributes.get('warrior')
		weird		 	= attributes.get('weird')
		werewolf	 	= attributes.get('werewolf')
		whale		 	= attributes.get('whale')
		wizard		 	= attributes.get('wizard')
		wolf		 	= attributes.get('wolf')
		wolverine	 	= attributes.get('wolverine')
		wombat		 	= attributes.get('wombat')
		worm		 	= attributes.get('worm')
		wraith		 	= attributes.get('wraith')
		wurm		 	= attributes.get('wurm')
		yeti		 	= attributes.get('yeti')
		zombie		 	= attributes.get('zombie')
		zubera		 	= attributes.get('zubera')

		# enchantment
		aura		 	= attributes.get('aura')
		background	 	= attributes.get('background')
		cartouche	 	= attributes.get('cartouche')
		function		= attributes.get('function') # alias for 'class'
		curse		 	= attributes.get('curse')
		rune		 	= attributes.get('rune')
		saga		 	= attributes.get('saga')
		shrine		 	= attributes.get('shrine')
		role		 	= attributes.get('role')

		# land
		desert			= attributes.get('desert')
		forest		 	= attributes.get('forest')
		gate		 	= attributes.get('gate')
		island		 	= attributes.get('island')
		lair		 	= attributes.get('lair')
		locus		 	= attributes.get('locus')
		mine		 	= attributes.get('mine')
		mountain	 	= attributes.get('mountain')
		plains		 	= attributes.get('plains')
		power_plant	 	= attributes.get('power_plant')
		sphere		 	= attributes.get('sphere')
		swamp		 	= attributes.get('swamp')
		tower		 	= attributes.get('tower')
		urzas		 	= attributes.get('urzas')

		# planeswalker
		ajani           = attributes.get('ajani')
		angrath         = attributes.get('angrath')
		arlinn          = attributes.get('arlinn')
		ashiok          = attributes.get('ashiok')
		basri           = attributes.get('basri')
		bolas           = attributes.get('bolas')
		calix           = attributes.get('calix')
		chandra         = attributes.get('chandra')
		dack            = attributes.get('dack')
		dakkon          = attributes.get('dakkon')
		davriel         = attributes.get('davriel')
		domri           = attributes.get('domri')
		dovin           = attributes.get('dovin')
		elspeth         = attributes.get('elspeth')
		estrid          = attributes.get('estrid')
		freyalise       = attributes.get('freyalise')
		garruk          = attributes.get('garruk')
		gideon          = attributes.get('gideon')
		hualti          = attributes.get('hualti')
		jace            = attributes.get('jace')
		jared           = attributes.get('jared')
		jaya            = attributes.get('jaya')
		jeska           = attributes.get('jeska')
		kaito           = attributes.get('kaito')
		karn            = attributes.get('karn')
		kasmina         = attributes.get('kasmina')
		kaya            = attributes.get('kaya')
		kiora           = attributes.get('kiora')
		koth            = attributes.get('koth')
		liliana         = attributes.get('liliana')
		lukka           = attributes.get('lukka')
		narset          = attributes.get('narset')
		nahiri          = attributes.get('nahiri')
		niko            = attributes.get('niko')
		nissa           = attributes.get('nissa')
		obi             = attributes.get('obi')
		ob              = attributes.get('ob')
		oko             = attributes.get('oko')
		ral             = attributes.get('ral')
		rowan           = attributes.get('rowan')
		saheeli         = attributes.get('saheeli')
		samut           = attributes.get('samut')
		sarkhan         = attributes.get('sarkhan')
		serra           = attributes.get('serra')
		sorin           = attributes.get('sorin')
		tamiyo          = attributes.get('tamiyo')
		teferi          = attributes.get('teferi')
		teyo            = attributes.get('teyo')
		tezzeret        = attributes.get('tezzeret')
		tibalt          = attributes.get('tibalt')
		tyvar           = attributes.get('tyvar')
		ugin            = attributes.get('ugin')
		venser          = attributes.get('venser')
		vivien          = attributes.get('vivien')
		vraska          = attributes.get('vraska')
		will            = attributes.get('will')
		windgrace       = attributes.get('windgrace')
		wrenn           = attributes.get('wrenn')
		xenagos         = attributes.get('xenagos')
		yanggu          = attributes.get('yanggu')
		yanling         = attributes.get('yanling')

		# instant and sorcery
		adventure 		= attributes.get('adventure')
		arcane			= attributes.get('arcane')
		lesson 			= attributes.get('lesson')
		trap			= attributes.get('trap')
		
		
# artifact
Blood          = Subtype(blood=True)
Clue           = Subtype(clue=True)
Equipment      = Subtype(equipment=True)
Food           = Subtype(food=True)
Fortification  = Subtype(fortification=True)
Gold           = Subtype(gold=True)
Map            = Subtype(map=True)
Powerstone     = Subtype(powerstone=True)
Treasure       = Subtype(treasure=True)
Vehicle        = Subtype(vehicle=True)

# battle
Siege          = Subtype(siege=True)

# creature
Advisor        = Subtype(advisor=True)
Aetherborn     = Subtype(aetherborn=True)
Alien          = Subtype(alien=True)
Ally           = Subtype(ally=True)
Angel          = Subtype(angel=True)
Antelope       = Subtype(antelope=True)
Ape            = Subtype(ape=True)
Archer         = Subtype(archer=True)
Archon         = Subtype(archon=True)
Armadillo      = Subtype(armadillo=True)
Army           = Subtype(army=True)
Artificer      = Subtype(artificer=True)
Assassin       = Subtype(assassin=True)
AssemblyWorker = Subtype(assembly_worker=True)
Atog           = Subtype(atog=True)
Aurochs        = Subtype(aurochs=True)
Avatar         = Subtype(avatar=True)
Azra           = Subtype(azra=True)
Badger         = Subtype(badger=True)
Balloon        = Subtype(balloon=True)
Barbarian      = Subtype(barbarian=True)
Bard           = Subtype(bard=True)
Basilisk       = Subtype(basilisk=True)
Bat            = Subtype(bat=True)
Bear           = Subtype(bear=True)
Beast          = Subtype(beast=True)
Beeble         = Subtype(beeble=True)
Beholder       = Subtype(beholder=True)
Berserker      = Subtype(berserker=True)
Bird           = Subtype(bird=True)
Blinkmoth      = Subtype(blinkmoth=True)
Boar           = Subtype(boar=True)
Bringer        = Subtype(bringer=True)
Brushwagg      = Subtype(brushwagg=True)
Camarid        = Subtype(camarid=True)
Camel          = Subtype(camel=True)
Caribou        = Subtype(caribou=True)
Carrier        = Subtype(carrier=True)
Cat            = Subtype(cat=True)
Centaur        = Subtype(centaur=True)
Cephalid       = Subtype(cephalid=True)
Chimera        = Subtype(chimera=True)
Citizen        = Subtype(citizen=True)
Cleric         = Subtype(cleric=True)
Cockatrice     = Subtype(cockatrice=True)
Construct      = Subtype(construct=True)
Coward         = Subtype(coward=True)
Crab           = Subtype(crab=True)
Crocodile      = Subtype(crocodile=True)
Cyclops        = Subtype(cyclops=True)
Dauthi         = Subtype(dauthi=True)
Demigod        = Subtype(demigod=True)
Demon          = Subtype(demon=True)
Deserter       = Subtype(deserter=True)
Devil          = Subtype(devil=True)
Dinosaur       = Subtype(dinosaur=True)
Djinn          = Subtype(djinn=True)
Dog            = Subtype(dog=True)
Dragon         = Subtype(dragon=True)
Drake          = Subtype(drake=True)
Dreadnought    = Subtype(dreadnought=True)
Drone          = Subtype(drone=True)
Druid          = Subtype(druid=True)
Dryad          = Subtype(dryad=True)
Dwarf          = Subtype(dwarf=True)
Efreet         = Subtype(efreet=True)
Egg            = Subtype(egg=True)
Elder          = Subtype(elder=True)
Eldrazi        = Subtype(eldrazi=True)
Elemental      = Subtype(elemental=True)
Elephant       = Subtype(elephant=True)
Elf            = Subtype(elf=True)
Elk            = Subtype(elk=True)
Eye            = Subtype(eye=True)
Faerie         = Subtype(faerie=True)
Ferret         = Subtype(ferret=True)
Fish           = Subtype(fish=True)
Flagbearer     = Subtype(flagbearer=True)
Fox            = Subtype(fox=True)
Fractal        = Subtype(fractal=True)
Frog           = Subtype(frog=True)
Fungus         = Subtype(fungus=True)
Gargoyle       = Subtype(gargoyle=True)
Germ           = Subtype(germ=True)
Giant          = Subtype(giant=True)
Gnoll          = Subtype(gnoll=True)
Gnome          = Subtype(gnome=True)
Goat           = Subtype(goat=True)
Goblin         = Subtype(goblin=True)
God            = Subtype(god=True)
Golem          = Subtype(golem=True)
Gorgon         = Subtype(gorgon=True)
Graveborn      = Subtype(graveborn=True)
Gremlin        = Subtype(gremlin=True)
Griffin        = Subtype(griffin=True)
Hag            = Subtype(hag=True)
Harpy          = Subtype(harpy=True)
Hellion        = Subtype(hellion=True)
Hippo          = Subtype(hippo=True)
Hippogriff     = Subtype(hippogriff=True)
Homarid        = Subtype(homarid=True)
Homunculus     = Subtype(homunculus=True)
Horror         = Subtype(horror=True)
Horse          = Subtype(horse=True)
Human          = Subtype(human=True)
Hydra          = Subtype(hydra=True)
Hyena          = Subtype(hyena=True)
Illusion       = Subtype(illusion=True)
Imp            = Subtype(imp=True)
Incarnation    = Subtype(incarnation=True)
Inkling        = Subtype(inkling=True)
Insect         = Subtype(insect=True)
Jackal         = Subtype(jackal=True)
Jellyfish      = Subtype(jellyfish=True)
Juggernaut     = Subtype(juggernaut=True)
Kavu           = Subtype(kavu=True)
Kirin          = Subtype(kirin=True)
Kithkin        = Subtype(kithkin=True)
Knight         = Subtype(knight=True)
Kobold         = Subtype(kobold=True)
Kor            = Subtype(kor=True)
Kraken         = Subtype(kraken=True)
Lamia          = Subtype(lamia=True)
Lammasu        = Subtype(lammasu=True)
Leech          = Subtype(leech=True)
Leviathan      = Subtype(leviathan=True)
Lhurgoyf       = Subtype(lhurgoyf=True)
Licid          = Subtype(licid=True)
Lizard         = Subtype(lizard=True)
Manticore      = Subtype(manticore=True)
Masticore      = Subtype(masticore=True)
Mercenary      = Subtype(mercenary=True)
Merfolk        = Subtype(merfolk=True)
Metathran      = Subtype(metathran=True)
Minion         = Subtype(minion=True)
Minotaur       = Subtype(minotaur=True)
Mite           = Subtype(mite=True)
Mole           = Subtype(mole=True)
Mongoose       = Subtype(mongoose=True)
Monk           = Subtype(monk=True)
Monkey         = Subtype(monkey=True)
Moonfolk       = Subtype(moonfolk=True)
Mount          = Subtype(mount=True)
Mouse          = Subtype(mouse=True)
Mutant         = Subtype(mutant=True)
Myr            = Subtype(myr=True)
Mystic         = Subtype(mystic=True)
Naga           = Subtype(naga=True)
Nautilus       = Subtype(nautilus=True)
Nephilim       = Subtype(nephilim=True)
Nightmare      = Subtype(nightmare=True)
Nightstalker   = Subtype(nightstalker=True)
Ninja          = Subtype(ninja=True)
Noble          = Subtype(noble=True)
Noggle         = Subtype(noggle=True)
Nomad          = Subtype(nomad=True)
Nymph          = Subtype(nymph=True)
Octopus        = Subtype(octopus=True)
Ogre           = Subtype(ogre=True)
Ooze           = Subtype(ooze=True)
Orb            = Subtype(orb=True)
Orc            = Subtype(orc=True)
Orgg           = Subtype(orgg=True)
Otter          = Subtype(otter=True)
Ouphe          = Subtype(ouphe=True)
Ox             = Subtype(ox=True)
Oyster         = Subtype(oyster=True)
Pangolin       = Subtype(pangolin=True)
Peasant        = Subtype(peasant=True)
Pegasus        = Subtype(pegasus=True)
Pentavite      = Subtype(pentavite=True)
Pest           = Subtype(pest=True)
Phelddagrif    = Subtype(phelddagrif=True)
Phoenix        = Subtype(phoenix=True)
Phyrexian      = Subtype(phyrexian=True)
Pilot          = Subtype(pilot=True)
Pincher        = Subtype(pincher=True)
Pirate         = Subtype(pirate=True)
Plant          = Subtype(plant=True)
Praetor        = Subtype(praetor=True)
Primordial     = Subtype(primordial=True)
Prism          = Subtype(prism=True)
Processor      = Subtype(processor=True)
Rabbit         = Subtype(rabbit=True)
Raccoon        = Subtype(raccoon=True)
Rat            = Subtype(rat=True)
Rebel          = Subtype(rebel=True)
Reflection     = Subtype(reflection=True)
Rhino          = Subtype(rhino=True)
Rigger         = Subtype(rigger=True)
Rogue          = Subtype(rogue=True)
Sable          = Subtype(sable=True)
Salamander     = Subtype(salamander=True)
Samurai        = Subtype(samurai=True)
Sand           = Subtype(sand=True)
Saproling      = Subtype(saproling=True)
Satyr          = Subtype(satyr=True)
Scarecrow      = Subtype(scarecrow=True)
Scientist      = Subtype(scientist=True)
Scion          = Subtype(scion=True)
Scorpion       = Subtype(scorpion=True)
Scout          = Subtype(scout=True)
Serf           = Subtype(serf=True)
Serpent        = Subtype(serpent=True)
Servo          = Subtype(servo=True)
Shade          = Subtype(shade=True)
Shaman         = Subtype(shaman=True)
Shapeshifter   = Subtype(shapeshifter=True)
Shark          = Subtype(shark=True)
Sheep          = Subtype(sheep=True)
Siren          = Subtype(siren=True)
Skeleton       = Subtype(skeleton=True)
Slith          = Subtype(slith=True)
Sliver         = Subtype(sliver=True)
Slug           = Subtype(slug=True)
Snake          = Subtype(snake=True)
Soldier        = Subtype(soldier=True)
Soltari        = Subtype(soltari=True)
Spawn          = Subtype(spawn=True)
Specter        = Subtype(specter=True)
Spellshaper    = Subtype(spellshaper=True)
Sphinx         = Subtype(sphinx=True)
Spider         = Subtype(spider=True)
Spike          = Subtype(spike=True)
Spirit         = Subtype(spirit=True)
Splinter       = Subtype(splinter=True)
Sponge         = Subtype(sponge=True)
Squid          = Subtype(squid=True)
Squirrel       = Subtype(squirrel=True)
Starfish       = Subtype(starfish=True)
Surrakar       = Subtype(surrakar=True)
Survivor       = Subtype(survivor=True)
Tentacle       = Subtype(tentacle=True)
Tetravite      = Subtype(tetravite=True)
Thalakos       = Subtype(thalakos=True)
Thopter        = Subtype(thopter=True)
Thrull         = Subtype(thrull=True)
Tiefling       = Subtype(tiefling=True)
Treefolk       = Subtype(treefolk=True)
Trilobite      = Subtype(trilobite=True)
Triskelavite   = Subtype(triskelavite=True)
Troll          = Subtype(troll=True)
Turtle         = Subtype(turtle=True)
Tyranid        = Subtype(tyranid=True)
Unicorn        = Subtype(unicorn=True)
Vampire        = Subtype(vampire=True)
Vedalken       = Subtype(vedalken=True)
Viashino       = Subtype(viashino=True)
Voliver        = Subtype(voliver=True)
Wall           = Subtype(wall=True)
Warlock        = Subtype(warlock=True)
Warrior        = Subtype(warrior=True)
Weird          = Subtype(weird=True)
Werewolf       = Subtype(werewolf=True)
Whale          = Subtype(whale=True)
Wizard         = Subtype(wizard=True)
Wolf           = Subtype(wolf=True)
Wolverine      = Subtype(wolverine=True)
Wombat         = Subtype(wombat=True)
Worm           = Subtype(worm=True)
Wraith         = Subtype(wraith=True)
Wurm           = Subtype(wurm=True)
Yeti           = Subtype(yeti=True)
Zombie         = Subtype(zombie=True)
Zubera         = Subtype(zubera=True)

# enchantment
Aura           = Subtype(aura=True)
Background     = Subtype(background=True)
Cartouche      = Subtype(cartouche=True)
Function       = Subtype(function=True)
Curse          = Subtype(curse=True)
Rune           = Subtype(rune=True)
Saga           = Subtype(saga=True)
Shrine         = Subtype(shrine=True)
Role           = Subtype(role=True)

# land
Desert         = Subtype(desert=True)
Forest         = Subtype(forest=True)
Gate           = Subtype(gate=True)
Island         = Subtype(island=True)
Lair           = Subtype(lair=True)
Locus          = Subtype(locus=True)
Mine           = Subtype(mine=True)
Mountain       = Subtype(mountain=True)
Plains         = Subtype(plains=True)
PowerPlant     = Subtype(power_plant=True)
Sphere         = Subtype(sphere=True)
Swamp          = Subtype(swamp=True)
Tower          = Subtype(tower=True)
Urzas          = Subtype(urzas=True)

# planeswalker
Ajani          = Subtype(ajani=True)
Angrath        = Subtype(angrath=True)
Arlinn         = Subtype(arlinn=True)
Ashiok         = Subtype(ashiok=True)
Basri          = Subtype(basri=True)
Bolas          = Subtype(bolas=True)
Calix          = Subtype(calix=True)
Chandra        = Subtype(chandra=True)
Dack           = Subtype(dack=True)
Dakkon         = Subtype(dakkon=True)
Davriel        = Subtype(davriel=True)
Domri          = Subtype(domri=True)
Dovin          = Subtype(dovin=True)
Elspeth        = Subtype(elspeth=True)
Estrid         = Subtype(estrid=True)
Freyalise      = Subtype(freyalise=True)
Garruk         = Subtype(garruk=True)
Gideon         = Subtype(gideon=True)
Hualti         = Subtype(hualti=True)
Jace           = Subtype(jace=True)
Jared          = Subtype(jared=True)
Jaya           = Subtype(jaya=True)
Jeska          = Subtype(jeska=True)
Kaito          = Subtype(kaito=True)
Karn           = Subtype(karn=True)
Kasmina        = Subtype(kasmina=True)
Kaya           = Subtype(kaya=True)
Kiora          = Subtype(kiora=True)
Koth           = Subtype(koth=True)
Liliana        = Subtype(liliana=True)
Lukka          = Subtype(lukka=True)
Narset         = Subtype(narset=True)
Nahiri         = Subtype(nahiri=True)
Niko           = Subtype(niko=True)
Nissa          = Subtype(nissa=True)
Obi            = Subtype(obi=True)
Ob             = Subtype(ob=True)
Oko            = Subtype(oko=True)
Ral            = Subtype(ral=True)
Rowan          = Subtype(rowan=True)
Saheeli        = Subtype(saheeli=True)
Samut          = Subtype(samut=True)
Sarkhan        = Subtype(sarkhan=True)
Serra          = Subtype(serra=True)
Sorin          = Subtype(sorin=True)
Tamiyo         = Subtype(tamiyo=True)
Teferi         = Subtype(teferi=True)
Teyo           = Subtype(teyo=True)
Tezzeret       = Subtype(tezzeret=True)
Tibalt         = Subtype(tibalt=True)
Tyvar          = Subtype(tyvar=True)
Ugin           = Subtype(ugin=True)
Venser         = Subtype(venser=True)
Vivien         = Subtype(vivien=True)
Vraska         = Subtype(vraska=True)
Will           = Subtype(will=True)
Windgrace      = Subtype(windgrace=True)
Wrenn          = Subtype(wrenn=True)
Xenagos        = Subtype(xenagos=True)
Yanggu         = Subtype(yanggu=True)
Yanling        = Subtype(yanling=True)

# instant and sorcery
Adventure 	   = Subtype(adventure=True)
Arcane 		   = Subtype(arcane=True)
Lesson 		   = Subtype(lesson=True)
Trap 		   = Subtype(trap=True)

