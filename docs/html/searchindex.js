Search.setIndex({docnames:["api","api/modules","api/pyshgp","api/pyshgp.gp","api/pyshgp.gp.estimators","api/pyshgp.gp.evaluation","api/pyshgp.gp.genome","api/pyshgp.gp.individual","api/pyshgp.gp.population","api/pyshgp.gp.search","api/pyshgp.gp.selection","api/pyshgp.gp.variation","api/pyshgp.push","api/pyshgp.push.atoms","api/pyshgp.push.instruction","api/pyshgp.push.instruction_set","api/pyshgp.push.instructions","api/pyshgp.push.instructions.code","api/pyshgp.push.instructions.common","api/pyshgp.push.instructions.io","api/pyshgp.push.instructions.logical","api/pyshgp.push.instructions.numeric","api/pyshgp.push.instructions.text","api/pyshgp.push.interpreter","api/pyshgp.push.stack","api/pyshgp.push.state","api/pyshgp.push.types","api/pyshgp.utils","contributing","index"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.cpp":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.todo":1,"sphinx.ext.viewcode":1,sphinx:55},filenames:["api.rst","api/modules.rst","api/pyshgp.rst","api/pyshgp.gp.rst","api/pyshgp.gp.estimators.rst","api/pyshgp.gp.evaluation.rst","api/pyshgp.gp.genome.rst","api/pyshgp.gp.individual.rst","api/pyshgp.gp.population.rst","api/pyshgp.gp.search.rst","api/pyshgp.gp.selection.rst","api/pyshgp.gp.variation.rst","api/pyshgp.push.rst","api/pyshgp.push.atoms.rst","api/pyshgp.push.instruction.rst","api/pyshgp.push.instruction_set.rst","api/pyshgp.push.instructions.rst","api/pyshgp.push.instructions.code.rst","api/pyshgp.push.instructions.common.rst","api/pyshgp.push.instructions.io.rst","api/pyshgp.push.instructions.logical.rst","api/pyshgp.push.instructions.numeric.rst","api/pyshgp.push.instructions.text.rst","api/pyshgp.push.interpreter.rst","api/pyshgp.push.stack.rst","api/pyshgp.push.state.rst","api/pyshgp.push.types.rst","api/pyshgp.utils.rst","contributing.rst","index.rst"],objects:{"":{pyshgp:[2,0,0,"-"]},"pyshgp.gp":{estimators:[4,0,0,"-"],evaluation:[5,0,0,"-"],genome:[6,0,0,"-"],individual:[7,0,0,"-"],population:[8,0,0,"-"],search:[9,0,0,"-"],selection:[10,0,0,"-"],variation:[11,0,0,"-"]},"pyshgp.gp.estimators":{PushEstimator:[4,1,1,""],SearchResult:[4,1,1,""],VariationStrategy:[4,1,1,""],random:[4,4,1,""]},"pyshgp.gp.estimators.PushEstimator":{fit:[4,2,1,""],load:[4,2,1,""],predict:[4,2,1,""],save:[4,2,1,""],score:[4,2,1,""]},"pyshgp.gp.estimators.SearchResult":{from_json_file:[4,3,1,""],from_json_str:[4,3,1,""],jsonify:[4,2,1,""]},"pyshgp.gp.estimators.VariationStrategy":{add:[4,2,1,""]},"pyshgp.gp.evaluation":{DatasetEvaluator:[5,1,1,""],Evaluator:[5,1,1,""],FunctionEvaluator:[5,1,1,""],damerau_levenshtein_distance:[5,4,1,""]},"pyshgp.gp.evaluation.DatasetEvaluator":{evaluate:[5,2,1,""]},"pyshgp.gp.evaluation.Evaluator":{default_error_function:[5,2,1,""],evaluate:[5,2,1,""]},"pyshgp.gp.evaluation.FunctionEvaluator":{evaluate:[5,2,1,""]},"pyshgp.gp.genome":{GeneSpawner:[6,1,1,""],Genome:[6,1,1,""],GenomeSimplifier:[6,1,1,""],Opener:[6,1,1,""]},"pyshgp.gp.genome.GeneSpawner":{random_erc:[6,2,1,""],random_instruction:[6,2,1,""],random_literal:[6,2,1,""],spawn_atom:[6,2,1,""],spawn_genome:[6,2,1,""]},"pyshgp.gp.genome.Genome":{append:[6,2,1,""],copy:[6,2,1,""],jsonify:[6,2,1,""],simplify:[6,2,1,""],to_code_block:[6,2,1,""]},"pyshgp.gp.genome.GenomeSimplifier":{simplify:[6,2,1,""]},"pyshgp.gp.genome.Opener":{count:[6,5,1,""],dec:[6,2,1,""]},"pyshgp.gp.individual":{Individual:[7,1,1,""]},"pyshgp.gp.individual.Individual":{error_vector:[7,5,1,""],genome:[7,5,1,""],program:[7,5,1,""],total_error:[7,5,1,""]},"pyshgp.gp.population":{Population:[8,1,1,""]},"pyshgp.gp.population.Population":{add:[8,2,1,""],all_error_vectors:[8,2,1,""],all_total_errors:[8,2,1,""],best:[8,2,1,""],best_n:[8,2,1,""],error_diversity:[8,2,1,""],evaluate:[8,2,1,""],evaluated:[8,5,1,""],genome_diversity:[8,2,1,""],median_error:[8,2,1,""],unevaluated:[8,5,1,""]},"pyshgp.gp.search":{GeneticAlgorithm:[9,1,1,""],SearchAlgorithm:[9,1,1,""],SearchConfiguration:[9,1,1,""],SimulatedAnnealing:[9,1,1,""],random:[9,4,1,""]},"pyshgp.gp.search.GeneticAlgorithm":{step:[9,2,1,""]},"pyshgp.gp.search.SearchAlgorithm":{init_population:[9,2,1,""],run:[9,2,1,""],step:[9,2,1,""]},"pyshgp.gp.search.SearchConfiguration":{get_selector:[9,2,1,""],get_spawner:[9,2,1,""],get_variation_operator:[9,2,1,""]},"pyshgp.gp.search.SimulatedAnnealing":{step:[9,2,1,""]},"pyshgp.gp.selection":{Elite:[10,1,1,""],FitnessProportionate:[10,1,1,""],Lexicase:[10,1,1,""],Selector:[10,1,1,""],Tournament:[10,1,1,""],choice:[10,4,1,""],median_absolute_deviation:[10,4,1,""],random:[10,4,1,""],shuffle:[10,4,1,""]},"pyshgp.gp.selection.Elite":{select:[10,2,1,""],select_one:[10,2,1,""]},"pyshgp.gp.selection.FitnessProportionate":{select:[10,2,1,""],select_one:[10,2,1,""]},"pyshgp.gp.selection.Lexicase":{select_one:[10,2,1,""]},"pyshgp.gp.selection.Selector":{select:[10,2,1,""],select_one:[10,2,1,""]},"pyshgp.gp.selection.Tournament":{select_one:[10,2,1,""]},"pyshgp.gp.variation":{AdditionMutation:[11,1,1,""],Alternation:[11,1,1,""],Cloning:[11,1,1,""],DeletionMutation:[11,1,1,""],Genesis:[11,1,1,""],LiteralMutation:[11,1,1,""],VariationOperator:[11,1,1,""],VariationPipeline:[11,1,1,""],choice:[11,4,1,""],random:[11,4,1,""]},"pyshgp.gp.variation.AdditionMutation":{produce:[11,2,1,""]},"pyshgp.gp.variation.Alternation":{produce:[11,2,1,""]},"pyshgp.gp.variation.Cloning":{produce:[11,2,1,""]},"pyshgp.gp.variation.DeletionMutation":{produce:[11,2,1,""]},"pyshgp.gp.variation.Genesis":{produce:[11,2,1,""]},"pyshgp.gp.variation.LiteralMutation":{produce:[11,2,1,""]},"pyshgp.gp.variation.VariationOperator":{checknum_parents:[11,2,1,""],produce:[11,2,1,""]},"pyshgp.gp.variation.VariationPipeline":{produce:[11,2,1,""]},"pyshgp.push":{atoms:[13,0,0,"-"],instruction:[14,0,0,"-"],instruction_set:[15,0,0,"-"],instructions:[16,0,0,"-"],interpreter:[23,0,0,"-"],stack:[24,0,0,"-"],state:[25,0,0,"-"],types:[26,0,0,"-"]},"pyshgp.push.atoms":{Atom:[13,1,1,""],Closer:[13,1,1,""],CodeBlock:[13,1,1,""],Instruction:[13,1,1,""],JitInstructionRef:[13,1,1,""],Literal:[13,1,1,""]},"pyshgp.push.atoms.Atom":{coerce:[13,3,1,""],is_instance:[13,3,1,""]},"pyshgp.push.atoms.Closer":{jsonify:[13,2,1,""]},"pyshgp.push.atoms.CodeBlock":{code_at_point:[13,2,1,""],copy:[13,2,1,""],depth:[13,2,1,""],from_json_str:[13,6,1,""],from_list:[13,6,1,""],jsonify:[13,2,1,""],size:[13,2,1,""]},"pyshgp.push.atoms.Instruction":{code_block:[13,5,1,""],docstring:[13,5,1,""],evaluate:[13,2,1,""],jsonify:[13,2,1,""],name:[13,5,1,""],relevant_types:[13,2,1,""]},"pyshgp.push.atoms.JitInstructionRef":{jsonify:[13,2,1,""],name:[13,5,1,""]},"pyshgp.push.atoms.Literal":{jsonify:[13,2,1,""],push_type:[13,5,1,""],value:[13,5,1,""]},"pyshgp.push.instruction":{ProducesManyOfTypeInstruction:[14,1,1,""],SimpleInstruction:[14,1,1,""],StateToStateInstruction:[14,1,1,""],TakesStateInstruction:[14,1,1,""]},"pyshgp.push.instruction.ProducesManyOfTypeInstruction":{code_blocks:[14,5,1,""],docstring:[14,5,1,""],evaluate:[14,2,1,""],f:[14,5,1,""],input_types:[14,5,1,""],name:[14,5,1,""],output_type:[14,5,1,""],relevant_types:[14,2,1,""]},"pyshgp.push.instruction.SimpleInstruction":{code_blocks:[14,5,1,""],docstring:[14,5,1,""],evaluate:[14,2,1,""],f:[14,5,1,""],input_types:[14,5,1,""],name:[14,5,1,""],output_types:[14,5,1,""],relevant_types:[14,2,1,""]},"pyshgp.push.instruction.StateToStateInstruction":{code_blocks:[14,5,1,""],docstring:[14,5,1,""],evaluate:[14,2,1,""],f:[14,5,1,""],name:[14,5,1,""],relevant_types:[14,2,1,""],types_used:[14,5,1,""]},"pyshgp.push.instruction.TakesStateInstruction":{code_blocks:[14,5,1,""],docstring:[14,5,1,""],evaluate:[14,2,1,""],f:[14,5,1,""],name:[14,5,1,""],other_types:[14,5,1,""],output_types:[14,5,1,""],relevant_types:[14,2,1,""]},"pyshgp.push.instruction_set":{InstructionSet:[15,1,1,""]},"pyshgp.push.instruction_set.InstructionSet":{register:[15,2,1,""],register_all:[15,2,1,""],register_by_name:[15,2,1,""],register_by_type:[15,2,1,""],register_list:[15,2,1,""],register_n_inputs:[15,2,1,""],supported_types:[15,2,1,""],unregister:[15,2,1,""]},"pyshgp.push.instructions":{code:[17,0,0,"-"],common:[18,0,0,"-"],io:[19,0,0,"-"],logical:[20,0,0,"-"],numeric:[21,0,0,"-"],text:[22,0,0,"-"]},"pyshgp.push.instructions.code":{instructions:[17,4,1,""]},"pyshgp.push.instructions.common":{instructions:[18,4,1,""]},"pyshgp.push.instructions.io":{instructions:[19,4,1,""],make_input_instruction:[19,4,1,""],make_input_instructions:[19,4,1,""]},"pyshgp.push.instructions.logical":{instructions:[20,4,1,""]},"pyshgp.push.instructions.numeric":{instructions:[21,4,1,""]},"pyshgp.push.instructions.text":{instructions:[22,4,1,""]},"pyshgp.push.interpreter":{PushInterpreter:[23,1,1,""],PushInterpreterConfig:[23,1,1,""]},"pyshgp.push.interpreter.PushInterpreter":{evaluate_atom:[23,2,1,""],reset:[23,2,1,""],run:[23,2,1,""]},"pyshgp.push.stack":{PushStack:[24,1,1,""]},"pyshgp.push.stack.PushStack":{flush:[24,2,1,""],insert:[24,2,1,""],is_empty:[24,2,1,""],nth:[24,2,1,""],pop:[24,2,1,""],push:[24,2,1,""],push_type:[24,5,1,""],set_nth:[24,2,1,""],take:[24,2,1,""],top:[24,2,1,""]},"pyshgp.push.state":{PushState:[25,1,1,""]},"pyshgp.push.state.PushState":{from_dict:[25,3,1,""],inputs:[25,5,1,""],load_inputs:[25,2,1,""],load_program:[25,2,1,""],observe_stacks:[25,2,1,""],pop_from_stacks:[25,2,1,""],pretty_print:[25,2,1,""],push_to_stacks:[25,2,1,""],stdout:[25,5,1,""]},"pyshgp.push.types":{Char:[26,1,1,""],PushType:[26,1,1,""],push_type_by_name:[26,4,1,""],push_type_for_type:[26,4,1,""],push_type_of:[26,4,1,""]},"pyshgp.push.types.Char":{"char":[26,5,1,""]},"pyshgp.push.types.PushType":{coerce:[26,2,1,""],is_instance:[26,2,1,""]},"pyshgp.utils":{DiscreteProbDistrib:[27,1,1,""],JSONable:[27,1,1,""],PushError:[27,7,1,""],Token:[27,1,1,""],choice:[27,4,1,""],jsonify_collection:[27,4,1,""]},"pyshgp.utils.DiscreteProbDistrib":{add:[27,2,1,""],elements:[27,5,1,""],sample:[27,2,1,""],sample_n:[27,2,1,""]},"pyshgp.utils.JSONable":{jsonify:[27,2,1,""],to_json:[27,2,1,""]},"pyshgp.utils.PushError":{empty_character:[27,3,1,""],failed_coerce:[27,3,1,""],long_character:[27,3,1,""],no_type:[27,3,1,""],wrong_vec_el_type:[27,3,1,""]},"pyshgp.utils.Token":{no_stack_item:[27,5,1,""],revert:[27,5,1,""],whole_state:[27,5,1,""]},pyshgp:{gp:[3,0,0,"-"],push:[12,0,0,"-"],utils:[27,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","classmethod","Python class method"],"4":["py","function","Python function"],"5":["py","attribute","Python attribute"],"6":["py","staticmethod","Python static method"],"7":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:classmethod","4":"py:function","5":"py:attribute","6":"py:staticmethod","7":"py:exception"},terms:{"2e10":[],"5e5":[],"93levenshtein_dist":5,"abstract":27,"boolean":[10,11,27],"case":[9,10,11,27,28,29],"char":26,"class":[4,5,6,7,8,9,10,11,13,14,15,23,24,25,26,27],"default":[4,5,9,10,11,23,27],"enum":27,"final":23,"float":[5,6,9,10,11],"function":[5,10,13,23,27,28],"import":28,"int":[4,5,6,8,9,10,11,13,14,15,19,24,27],"new":[10,11,23,24,27,28],"public":29,"return":[4,5,6,8,9,10,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27],"static":13,"switch":11,"true":[10,11,15,23,24,26,27],"while":6,Adding:28,For:[10,11,27,29],NOT:25,One:29,Thats:29,The:[4,5,6,7,8,9,10,11,13,15,23,24,25,27,28,29],There:25,These:[],Used:[14,26],aa_milne_arr:[10,11,27],abbrevi:[],abc:[5,8,9,10,11,13,27],about:29,abov:[10,11,27,28],accept:[28,29],acheiv:29,acm:[],actual:5,add:[4,8,9,10,11,27,28],added:[],adding:[],addit:[15,29],additionmut:11,address:28,after:[25,28],against:[],aim:29,aka:11,algebra:29,algorith:[],algorithm:[4,9,10,11],alia:24,alignment_devi:11,all:[4,5,8,9,10,11,13,15,17,18,19,20,21,22,25,27,28,29],all_error_vector:8,all_total_error:8,allow:28,almost:28,along:10,also:[10,28],altern:11,although:29,alwai:[8,28],ani:[10,11,13,26,27],anneal:9,anoth:[],anticip:28,anyth:[],append:[6,24],appli:11,applic:[],appropri:28,arang:[10,11,27],arbitarili:14,arbitrari:[10,11,27],arg:13,argument:[],arr:10,arrai:[4,5,7,8,9,10,11,27],array_lik:10,assign:[],associ:[10,11,27],assum:[10,11,27,28],atom:[2,4,5,6,11,12,14,15,23,25],atom_limit:23,atomfactori:[],attempt:29,attribut:[],autodoc:28,autom:28,automat:[],avail:28,axi:10,base:[4,5,6,7,8,9,10,11,13,14,15,23,24,25,26,27,28,29],becom:[],been:28,befor:[25,28],behavior:[],being:[11,28],benchmark:29,best:[4,8],best_n:8,best_seen:[],better:[],between:[11,26],block:13,board:28,bodi:28,bool:[4,5,6,9,10,15,23,24,26,27],both:[5,28],branch:28,bring:29,bug:29,build:[],built:28,call:29,callabl:[5,6,14],can:[10,11,13,25,27,28,29],candid:[],cannot:[],capabl:[23,29],certain:24,cfm:[],chang:[10,28,29],check:[25,29],checknum_par:11,child:11,children:[],choic:[10,11,27],christoph:[10,11,27],citat:10,classif:4,classmethod:[4,13,25,27],classself:24,clear:24,climb:[],clojur:29,clojush:29,clone:[11,28,29],close:13,closer:13,cobdeblock:[],codaci:28,code:[2,5,11,12,13,16,29],code_at_point:13,code_block:[13,14],codeblock:[4,5,6,13,23,25],coerc:[13,25,26],collect:[4,8,15,25],com:5,come:29,common:[2,12,16,29],compar:29,compat:29,competit:29,complet:29,comput:[5,29],conain:[],concret:14,condit:[],confer:[],config:[9,14,23],configu:[],configur:[9,14,23],confirm:25,conform:28,conftest:[],consid:[],constant:13,constantli:29,construct:28,contain:[6,8,23,24,28,29],content:[0,1,10],continu:[9,10,11],contrast:29,contributor:28,control:[25,29],convent:28,convert:[13,25,26],copi:[6,11,13,19],core:[5,15,17,18,19,20,21,22,23],correct:25,correspond:[],count:6,cover:28,coverag:28,creat:[4,11,13,15,23,28],creation:6,crucial:[],current:28,cut:28,damerau:5,damerau_levenshtein_dist:5,data:[28,29],datafram:4,dataset:[4,5],datasetevalu:5,dec:6,decod:[],decrement:6,dedic:13,deep:6,deeper:25,default_error_funct:5,defin:[4,5,6,7,8,9,10,11,13,15,23,24,25],definit:[17,19,21,22,24,28],deletionmut:11,demonstr:28,denot:[13,23,25],depth:13,describ:[],deseri:[],desir:23,detail:29,determin:28,dev:[],develop:29,deviat:11,dict:[13,15,25,27],dictat:28,dictionari:25,diff:28,differ:[10,11,27,28],difficulti:29,dimension:[10,11,27],directori:29,discours:29,discov:29,discret:27,discreteprobdistrib:[4,6,9,27],distanc:5,distinguish:26,distribut:[6,9,10,11,27],distributin:27,doc:28,docs_sourc:28,docstr:[13,14,28],document:10,doe:[25,29],doi:[],done:28,down:28,download:28,drawn:[9,10,11,27],driven:5,dtype:[10,11,27],duplic:28,dure:27,each:[6,10,11,14,25,27],earli:[],easier:29,easili:29,edward:[],effect:[],either:27,el_typ:27,element:[4,10,11,13,24,27],elit:10,els:23,embed:[],empti:[23,24],empty_charact:27,end:6,enount:[],entir:[11,14],entri:[10,11,27],ephemer:[],epsilon:10,equal:[],equival:[10,11,27],erc:6,erc_gener:6,error:[5,6,7,8,10,11,27],error_divers:8,error_funct:5,error_threshold:9,error_vector:[5,7],estim:[2,3],evalu:[2,3,6,8,9,13,14,23],evaluate_atom:23,evalut:[],even:[],eventu:28,everi:24,evolut:[25,29],evolutionar:9,evolutionari:[7,8,11,29],evolv:[],exampl:[9,10,11,27],exceed:[],except:27,exclud:15,exec:23,execut:[4,23,25,27,29],exit:26,expect:[5,23,25,28],experiment:29,express:13,extend:29,extens:29,extra:[],extrem:29,factori:6,failed_coerc:27,fals:[4,5,6,9,10,11,15,23,24,27],far:[11,29],farthest:13,featur:29,few:[11,29],field:29,file:[4,27,28],filepath:[4,27],find:29,finish:28,finit:29,first:[10,13,28,29],fit:[4,10],fitness_proportionate_select:10,fitnessproportion:10,flat:[6,13],float64:10,flow:23,flush:24,focus:29,folder:[28,29],follow:[],foo_pyshgp:[],footprint:[],forc:[],fork:28,found:[4,28,29],framework:29,freitag:[],frequent:4,from:[4,6,7,9,10,11,13,14,23,24,25,27,28],from_dict:25,from_json_fil:4,from_json_str:[4,13],from_list:13,full:29,functionevalu:5,fundament:13,further:29,gecco:[],gene:6,geneom:[],gener:[6,9,10,11,23,27,29],genesi:11,genespawn:[4,6,9,11],genet:[9,11,27,29],geneticalgorithm:9,genom:[2,3,4,7,8,9,11],genome_divers:8,genomesimplifi:6,genomespawn:[6,9,11],genomesself:[],geom:6,get:[14,24,29],get_selector:9,get_spawn:9,get_variation_oper:9,github:[5,28,29],give:[],given:[5,6,9,10,11,13,14,15,19,23,24,25,26,27],googl:[],gradient:29,great:28,greater:[10,11,24,27],ground:[],growth_cap:23,guid:29,half:[9,10,11],handl:[],has:[15,28,29],have:[10,11,27,28,29],heavili:[5,29],hello:[],helmuth:[],help:[15,28],high:29,hill:[],hold:[13,24,25,26],homepag:29,how:[4,11,29],howev:29,http:[5,10],human:29,ieee:10,ieeexplor:10,implemen:5,implement:[5,14,29],importantli:[],imporv:[],impress:29,improv:6,includ:[19,28,29],index:[19,24,29],indic:[11,25],individaul:[7,8],individu:[2,3,8,10,11],induct:29,inf:[],infer:14,inform:[26,29],init_popul:9,initi:[9,29],initial_genome_s:[4,9],input:[4,14,15,19,23,25],input_typ:14,insctuct:19,insert:[24,28],insert_code_at_point:[],inspir:5,instal:28,instanc:[10,11,26,27],instanci:[],instansi:[],instead:[10,11,27,28],instr:15,instruciton:[],instruct:[2,6,12,13,15,24,29],instruction_nam:15,instruction_set:[2,4,6,12,13,23],instruction_test_spec:[],instructionset:[4,6,15,23],instrut:[],insturct:[],integ:[6,10,11,27],integer_regress:[],intellig:29,intent:[],interpret:[2,4,5,12,14,26],interpreter_config:[13,14],interv:[4,9,10,11],introduc:[],intruct:[],is_empti:24,is_inst:[13,26],isn:29,issu:[],item:[10,11,24,25,27],iter:[],its:[6,10,11,13,14,27,29],itself:29,jamesturk:5,jellyfish:5,jit:13,jitinstructionref:13,json:[4,6,13,27],json_dict:[],json_dict_to_atom:[],json_list:[],json_list_to_code_block:[],json_str:[4,13],json_str_to_atom_list:[],jsonabl:[4,6,13,27],jsonifi:[4,6,13,27],jsonify_collect:27,jump:11,just:[10,11,13,27],kei:29,kept:[8,28],keyword:[],kind:[],known:10,kwarg:4,label:[4,5],langdon:[],languag:[13,29],lead:29,leaky_relu:[],least:28,lee:[],len:24,length:[10,11,26,27],less:[10,11,24,27],levenshtein:5,lexicas:[4,9,10],like:[4,10,11,27,28,29],likelyhood:[],limit:14,linear:[],list:[4,5,6,8,10,11,13,14,15,24,25,27,28,29],liter:[6,11,13,26],literalmut:11,load:[4,23,25],load_input:25,load_program:25,lock:28,log:28,logic:[2,12,16],long_charact:27,mad:10,made:[],mai:[11,23],main:29,maintain:[6,28],major:29,make:[15,24,28],make_input_instruct:19,mani:[14,29],manipul:[13,25,29],manual:28,mark:6,master:28,match:[15,25],materi:6,max:[],max_gener:[4,9],mcphee:[],meant:[28,29],median:8,median_absolute_devi:10,median_error:8,memori:[],mention:28,merg:28,method:[15,29],mileston:29,millisecond:[],model:29,modifi:[10,13,14,29],modul:[0,1,28,29],more:[6,24,29],most:29,much:[28,29],multi:10,multiarrai:5,multipl:[11,25],multipli:[9,10,11],must:[11,28],mutat:[11,13,14],n_featur:4,n_output:[4,5],n_sampl:[4,5],name:[13,14,15,26,28],name_pattern:15,nativ:[],ndarrai:[5,6,9,10,11,27],ndx:[13,19],need:[11,13,23,28,29],nest:[6,13],never:28,next:28,nice:29,nichola:[],no_stack_item:[23,24,27],no_typ:27,non:[10,11,27],none:[6,8,9,10,11,13,15,23,24,26,27],novel:29,nth:24,num_input:19,num_par:11,number:[4,6,9,10,11,24,28],numer:[2,7,12,16,18,20,29],numpi:[5,6,7,10,26],object:[4,6,7,9,13,15,23,24,25,26,27],observe_stack:25,occasion:[],occur:25,odd:[],off:[24,25,29],offici:29,often:[],ojbect:15,onc:28,one:[6,9,13,29],onli:[10,28],onto:[24,25],open:[6,9,10,11,28],oper:11,optim:29,option:[9,10,11,24,26,27],order:[8,10,11,29],org:[5,10],origional_error:6,other:[11,13,29],other_typ:14,otherwis:24,out:[9,10,11,29],output:[4,5,9,10,11,14,23,25,27,29],output_typ:[4,14,23,25],over:[9,10,11,27],overwrit:24,own:[],packag:[0,1,5,27,28],page:[28,29],pair:6,panda:4,pantridg:[],paramet:[4,5,9,10,11,14,23,24,25,27,29],parent:11,pars:[],part:25,particip:[],particular:14,pass:[],path:28,pattern:[15,29],peic:13,penalti:5,pep8:28,per:29,perform:[9,28],permut:[10,11,27],piglet:[10,11,27],pipelin:29,place:[10,28],placehold:[],plai:29,plush:7,point:[],poli:[],pooh:[10,11,27],pop:[14,23,24,25],pop_from_stack:25,popul:[2,3,7,9,10,11,27],popular:29,population_s:[4,9],posit:24,positon:24,possibl:[14,28,29],power:29,pre:28,predict:4,preserv:6,pretty_print:25,prevent:28,previou:29,previous:29,primari:29,print:[19,23,25],probabl:[4,10,11,27],probablil:11,problem:29,proceed:[],process:23,produc:[4,5,11,14,25,29],producesmanyoftypeinstruct:14,program:[4,5,7,9,11,13,23,25,26,27,29],progress:25,project:[28,29],proport:[6,8],proportion:10,proven:29,pull:[23,28],push3:29,push:[0,1,2,4,5,6,7,9,11,27,29],push_stat:[13,14],push_to_stack:25,push_typ:[11,13,24,25,27],push_type_by_nam:26,push_type_for_typ:26,push_type_nam:26,push_type_of:26,pusherror:27,pushestim:4,pushgp:[],pushinterpret:[4,5,23],pushinterpreterconfig:[14,23],pushsolut:4,pushstack:[24,25],pushstat:[13,14,23,24,25],pushstateself:[],pushtyp:[4,11,13,14,15,18,23,24,25,26],put:28,pyghgp:[],pypi:28,pyshgp:28,pyshgp_cli:[],python:[26,29],quantum:29,quit:29,rabbit:[10,11,27],rais:[10,11,27],randint:[10,11,27],random:[4,6,9,10,11,27],random_erc:6,random_instruct:6,random_liter:6,random_sampl:[9,10,11],randomli:11,rang:[6,29],rate:11,rather:29,read:28,readi:29,real:4,reasearch:[],reboot:[],reduc:[],redux:29,refer:[13,29],referenc:[],regex:[],regist:15,register_al:15,register_by_nam:15,register_by_typ:15,register_list:15,register_n_input:15,regress:4,rel:[4,27,28],relat:6,releas:29,relev:[13,14],relevant_typ:[13,14],remain:10,remov:11,repeat:[10,11,27],replac:[10,11,27],repo:29,report:29,repositori:[28,29],repres:29,represent:[],represents:13,request:29,requir:[28,29],research:29,resembl:[],reset:23,reset_on_run:23,reshap:10,resolv:28,respect:[],result:[9,10,11,14,24,29],retreiv:15,revert:27,review:[],riccardo:[],root:27,roulett:10,rout:[],run:[4,9,23,29],runtim:29,runtime_limit:23,s11:[10,11,27],same:[10,14,25],sampl:[4,9,10,11,27],sample_n:27,save:4,score:4,scratch:[],seach:[],search:[2,3,4,29],searchalgorithm:[4,9],searchconfigur:9,searchresult:4,secenc:23,second:28,section:[],see:29,seen:29,select:[2,3,4,9],select_on:10,selectionself:10,selector:[4,9,10],self:24,sens:29,sequenc:[4,5,6,8,9,10,11,13,14,15,19,23,25],sequenci:11,serial:[],set:[6,14,15,25,28,29],set_nth:24,setup:25,shape:[4,5,9,10,11,27],should:[9,28],shuffl:[10,11,27],signatur:[],simpl:14,simpleinstruct:[14,17],simpli:[],simplif:[],simplifi:6,simplification_step:[4,9],simplifii:[],simul:9,simulatedann:9,singl:[9,10,11,27],sinlg:24,situat:[],size:[6,9,10,11,13,24,27],size_neutral_umad:[],sklearn:4,slowli:29,small:[],smaller:[],softwar:29,solut:4,solv:29,some:[11,23,29],sort:8,sourc:[4,5,6,7,8,9,10,11,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28],space:29,spawn:9,spawn_atom:6,spawn_genom:6,spawner:[4,11],specif:29,specifi:6,spector:[],sphinx:28,stabl:29,stack:[2,12,14,23,25,29],standard:11,start:6,state:[2,9,10,11,12,13,14,23],statetostateinstruct:14,statu:23,stdout:25,step:[6,9,23],still:29,stochast:29,stop:[],store:15,str:[4,6,13,14,15,23,25,26,27],strategi:[],string:[4,5,6,13,25,26,27],string_demo:[],strip_docstr:15,strive:28,structur:29,studi:29,style:[],sub:[10,27],subclass:[],submodul:[0,1],subpackag:[0,1],subset:15,subtl:[],success:29,suffic:[],suit:29,sum:7,superflu:[],suppli:[],support:[13,29],supported_typ:15,sync:28,synthes:[4,9],synthesi:29,system:29,t_co:[],tab:29,tack:24,take:[14,24,25],taken:[7,25],takesstateinstruct:[14,19],target:4,teporarili:6,term:29,termin:9,test:[25,29],test_atom:[],test_evalu:[],test_genom:[],test_individu:[],test_instruct:[],test_instruction_set:[],test_interpret:[],test_popul:[],test_push_valid:[],test_select:[],test_stack:[],test_stat:[],test_translate_valid:[],test_typ:[],text:[2,12,16,28],than:[10,11,24,27],thei:28,them:[4,25],thi:[5,10,11,23,25,27,28,29],thing:[13,26,27],thoma:[],three:[9,10,11],through:[15,27,29],throughout:[],thu:[],time:13,tmp:[],to_code_block:6,to_json:27,togeth:29,token:[23,24,25,27],too:11,top:[10,24,25],total:[8,10],total_error:7,tournament:10,tournament_s:10,tournament_select:10,track:28,train:4,transform:[27,29],translat:6,travers:13,truth:[],tupl:[4,6,9,10,11,26,27],ture:29,tutori:[],two:[6,9,10,11],type:[2,4,5,9,10,11,12,13,14,15,23,24,25,27,28,29],type_nam:15,types_us:14,typic:29,umad:4,undergo:28,underli:[13,26],understand:[],unevalu:8,unif:[9,10,11],uniform:[9,10,11,27],uniformli:11,union:[4,6,9,10,11,23,25,27],uniqu:8,unit:[],univers:[],unknown:29,unless:[9,10,11],unregist:15,until:[9,28],upgrad:29,upon:[],usa:[],use:[4,11,15,23,28],use_epsilon_lexicas:[],used:[11,13,15,24,25,26,27],user:[28,29],uses:28,using:[11,13,28,29],usual:29,util:[0,1,2,4,6,9,13,23,25,29],valid:25,valu:[4,7,9,10,11,13,14,19,23,24,25,26,27,29],value_typ:25,valueerror:[10,11,27],variaiton:[],variat:[2,3,9],variation_strategi:4,variationoper:[4,9,11],variationpipelin:[9,11],variationstrategi:4,variou:14,vec_typ:27,vector:[5,7,8,10,11,25,27],verbos:[4,5,6,9,23],vers:[],version:[10,11,27,28],via:28,violat:28,wai:28,websit:29,well:[],were:[10,11,27],what:[25,28],wheel:10,when:[11,13],where:[6,28,29],whether:[10,11,27],which:[9,10,11,13,14,24,27,28,29],whole_st:27,whose:15,wider:29,wiki:[5,10],wikipedia:[5,10],william:[],without:[10,11,27],word:[],work:5,world:[],wors:[],would:28,wrap:13,write:[13,14,27],written:[25,29],wrong_vec_el_typ:27,www:[],y_hat:[4,5],york:[],you:28,your:28,zero:[10,11,24,27]},titles:["PyshGP API","pyshgp","pyshgp package","pyshgp.gp package","pyshgp.gp.estimators module","pyshgp.gp.evaluation module","pyshgp.gp.genome module","pyshgp.gp.individual module","pyshgp.gp.population module","pyshgp.gp.search module","pyshgp.gp.selection module","pyshgp.gp.variation module","pyshgp.push package","pyshgp.push.atoms module","pyshgp.push.instruction module","pyshgp.push.instruction_set module","pyshgp.push.instructions package","pyshgp.push.instructions.code module","pyshgp.push.instructions.common module","pyshgp.push.instructions.io module","pyshgp.push.instructions.logical module","pyshgp.push.instructions.numeric module","pyshgp.push.instructions.text module","pyshgp.push.interpreter module","pyshgp.push.stack module","pyshgp.push.state module","pyshgp.push.types module","pyshgp.utils module","Contributing","PyghGP"],titleterms:{api:[0,29],art:[],atom:13,bug:28,build:29,code:[17,28],common:18,conftest:[],content:[2,3,12,16,29],contribut:[28,29],dev:[],docs_sourc:[],document:[28,29],estim:4,evalu:5,exampl:[28,29],featur:28,foo_pyshgp:[],from:29,frome:29,genom:6,goal:29,indic:29,individu:7,instal:29,instruct:[14,16,17,18,19,20,21,22],instruction_set:15,instruction_test_spec:[],integer_regress:[],interpret:23,issu:28,leaky_relu:[],logic:20,modul:[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],motiv:29,numer:21,odd:[],other:28,packag:[2,3,12,16],pattern:28,pip:29,popul:8,push:[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26],pushgp:29,pyghgp:29,pysh:29,pyshgp:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29],pyshgp_cli:[],reboot:[],releas:28,report:28,request:28,review:28,roadmap:29,scratch:[],search:9,select:10,setup:[],sourc:29,stack:24,state:25,string_demo:[],style:28,submodul:[2,3,12,16],subpackag:[2,12],tabl:29,test:28,test_atom:[],test_evalu:[],test_genom:[],test_individu:[],test_instruct:[],test_instruction_set:[],test_interpret:[],test_popul:[],test_push_valid:[],test_select:[],test_stack:[],test_stat:[],test_translate_valid:[],test_typ:[],text:22,tmp:[],tutori:[],type:26,unit:28,usag:29,use:29,util:27,variat:11,welcom:[],what:29,why:29}})