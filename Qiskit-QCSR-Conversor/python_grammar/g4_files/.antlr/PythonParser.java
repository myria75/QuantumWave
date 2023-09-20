// Generated from c:\Users\Miriam\Desktop\Patrones\Qiskit-QCSR-Conversor\python_grammar\g4_files\PythonParser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PythonParser extends PythonParserBase {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INDENT=1, DEDENT=2, LINE_BREAK=3, DEF=4, RETURN=5, RAISE=6, FROM=7, IMPORT=8, 
		NONLOCAL=9, AS=10, GLOBAL=11, ASSERT=12, IF=13, ELIF=14, ELSE=15, WHILE=16, 
		FOR=17, IN=18, TRY=19, NONE=20, FINALLY=21, WITH=22, EXCEPT=23, LAMBDA=24, 
		OR=25, AND=26, NOT=27, IS=28, CLASS=29, YIELD=30, DEL=31, PASS=32, CONTINUE=33, 
		BREAK=34, ASYNC=35, AWAIT=36, PRINT=37, EXEC=38, TRUE=39, FALSE=40, HADAMARD=41, 
		CONTROLLEDX=42, MEASURE=43, Z=44, S=45, T=46, Y=47, SWAP=48, X=49, DOT=50, 
		ELLIPSIS=51, REVERSE_QUOTE=52, STAR=53, COMMA=54, COLON=55, SEMI_COLON=56, 
		POWER=57, ASSIGN=58, OR_OP=59, XOR=60, AND_OP=61, LEFT_SHIFT=62, RIGHT_SHIFT=63, 
		ADD=64, MINUS=65, DIV=66, MOD=67, IDIV=68, NOT_OP=69, LESS_THAN=70, GREATER_THAN=71, 
		EQUALS=72, GT_EQ=73, LT_EQ=74, NOT_EQ_1=75, NOT_EQ_2=76, AT=77, ARROW=78, 
		ADD_ASSIGN=79, SUB_ASSIGN=80, MULT_ASSIGN=81, AT_ASSIGN=82, DIV_ASSIGN=83, 
		MOD_ASSIGN=84, AND_ASSIGN=85, OR_ASSIGN=86, XOR_ASSIGN=87, LEFT_SHIFT_ASSIGN=88, 
		RIGHT_SHIFT_ASSIGN=89, POWER_ASSIGN=90, IDIV_ASSIGN=91, STRING=92, DECIMAL_INTEGER=93, 
		OCT_INTEGER=94, HEX_INTEGER=95, BIN_INTEGER=96, IMAG_NUMBER=97, FLOAT_NUMBER=98, 
		OPEN_PAREN=99, CLOSE_PAREN=100, OPEN_BRACE=101, CLOSE_BRACE=102, OPEN_BRACKET=103, 
		CLOSE_BRACKET=104, NAME=105, LINE_JOIN=106, NEWLINE=107, WS=108, COMMENT=109;
	public static final int
		RULE_root = 0, RULE_single_input = 1, RULE_file_input = 2, RULE_eval_input = 3, 
		RULE_stmt = 4, RULE_compound_stmt = 5, RULE_suite = 6, RULE_decorator = 7, 
		RULE_elif_clause = 8, RULE_else_clause = 9, RULE_finally_clause = 10, 
		RULE_with_item = 11, RULE_except_clause = 12, RULE_classdef = 13, RULE_funcdef = 14, 
		RULE_typedargslist = 15, RULE_args = 16, RULE_kwargs = 17, RULE_def_parameters = 18, 
		RULE_def_parameter = 19, RULE_named_parameter = 20, RULE_simple_stmt = 21, 
		RULE_small_stmt = 22, RULE_testlist_star_expr = 23, RULE_star_expr = 24, 
		RULE_assign_part = 25, RULE_exprlist = 26, RULE_import_as_names = 27, 
		RULE_import_as_name = 28, RULE_dotted_as_names = 29, RULE_dotted_as_name = 30, 
		RULE_test = 31, RULE_varargslist = 32, RULE_vardef_parameters = 33, RULE_vardef_parameter = 34, 
		RULE_varargs = 35, RULE_varkwargs = 36, RULE_logical_test = 37, RULE_comparison = 38, 
		RULE_expr = 39, RULE_atom = 40, RULE_dictorsetmaker = 41, RULE_testlist_comp = 42, 
		RULE_testlist = 43, RULE_dotted_name = 44, RULE_name = 45, RULE_number = 46, 
		RULE_integer = 47, RULE_yield_expr = 48, RULE_yield_arg = 49, RULE_trailer = 50, 
		RULE_arguments = 51, RULE_arglist = 52, RULE_argument = 53, RULE_subscriptlist = 54, 
		RULE_subscript = 55, RULE_sliceop = 56, RULE_comp_for = 57, RULE_comp_iter = 58, 
		RULE_quantum_gates_definition = 59;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "single_input", "file_input", "eval_input", "stmt", "compound_stmt", 
			"suite", "decorator", "elif_clause", "else_clause", "finally_clause", 
			"with_item", "except_clause", "classdef", "funcdef", "typedargslist", 
			"args", "kwargs", "def_parameters", "def_parameter", "named_parameter", 
			"simple_stmt", "small_stmt", "testlist_star_expr", "star_expr", "assign_part", 
			"exprlist", "import_as_names", "import_as_name", "dotted_as_names", "dotted_as_name", 
			"test", "varargslist", "vardef_parameters", "vardef_parameter", "varargs", 
			"varkwargs", "logical_test", "comparison", "expr", "atom", "dictorsetmaker", 
			"testlist_comp", "testlist", "dotted_name", "name", "number", "integer", 
			"yield_expr", "yield_arg", "trailer", "arguments", "arglist", "argument", 
			"subscriptlist", "subscript", "sliceop", "comp_for", "comp_iter", "quantum_gates_definition"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, "'def'", "'return'", "'raise'", "'from'", "'import'", 
			"'nonlocal'", "'as'", "'global'", "'assert'", "'if'", "'elif'", "'else'", 
			"'while'", "'for'", "'in'", "'try'", "'None'", "'finally'", "'with'", 
			"'except'", "'lambda'", "'or'", "'and'", "'not'", "'is'", "'class'", 
			"'yield'", "'del'", "'pass'", "'continue'", "'break'", "'async'", "'await'", 
			"'print'", "'exec'", "'True'", "'False'", "'h'", "'cx'", "'measure'", 
			"'z'", "'s'", "'t'", "'y'", "'swap'", "'x'", "'.'", "'...'", "'`'", "'*'", 
			"','", "':'", "';'", "'**'", "'='", "'|'", "'^'", "'&'", "'<<'", "'>>'", 
			"'+'", "'-'", "'/'", "'%'", "'//'", "'~'", "'<'", "'>'", "'=='", "'>='", 
			"'<='", "'<>'", "'!='", "'@'", "'->'", "'+='", "'-='", "'*='", "'@='", 
			"'/='", "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", "'**='", "'//='", 
			null, null, null, null, null, null, null, "'('", "')'", "'{'", "'}'", 
			"'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INDENT", "DEDENT", "LINE_BREAK", "DEF", "RETURN", "RAISE", "FROM", 
			"IMPORT", "NONLOCAL", "AS", "GLOBAL", "ASSERT", "IF", "ELIF", "ELSE", 
			"WHILE", "FOR", "IN", "TRY", "NONE", "FINALLY", "WITH", "EXCEPT", "LAMBDA", 
			"OR", "AND", "NOT", "IS", "CLASS", "YIELD", "DEL", "PASS", "CONTINUE", 
			"BREAK", "ASYNC", "AWAIT", "PRINT", "EXEC", "TRUE", "FALSE", "HADAMARD", 
			"CONTROLLEDX", "MEASURE", "Z", "S", "T", "Y", "SWAP", "X", "DOT", "ELLIPSIS", 
			"REVERSE_QUOTE", "STAR", "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN", 
			"OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", 
			"DIV", "MOD", "IDIV", "NOT_OP", "LESS_THAN", "GREATER_THAN", "EQUALS", 
			"GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", "ADD_ASSIGN", 
			"SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
			"AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN", 
			"POWER_ASSIGN", "IDIV_ASSIGN", "STRING", "DECIMAL_INTEGER", "OCT_INTEGER", 
			"HEX_INTEGER", "BIN_INTEGER", "IMAG_NUMBER", "FLOAT_NUMBER", "OPEN_PAREN", 
			"CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", 
			"NAME", "LINE_JOIN", "NEWLINE", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PythonParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PythonParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RootContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(PythonParser.EOF, 0); }
		public List<Single_inputContext> single_input() {
			return getRuleContexts(Single_inputContext.class);
		}
		public Single_inputContext single_input(int i) {
			return getRuleContext(Single_inputContext.class,i);
		}
		public List<File_inputContext> file_input() {
			return getRuleContexts(File_inputContext.class);
		}
		public File_inputContext file_input(int i) {
			return getRuleContext(File_inputContext.class,i);
		}
		public List<Eval_inputContext> eval_input() {
			return getRuleContexts(Eval_inputContext.class);
		}
		public Eval_inputContext eval_input(int i) {
			return getRuleContext(Eval_inputContext.class,i);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LINE_BREAK) | (1L << DEF) | (1L << RETURN) | (1L << RAISE) | (1L << FROM) | (1L << IMPORT) | (1L << NONLOCAL) | (1L << GLOBAL) | (1L << ASSERT) | (1L << IF) | (1L << WHILE) | (1L << FOR) | (1L << TRY) | (1L << NONE) | (1L << WITH) | (1L << LAMBDA) | (1L << NOT) | (1L << CLASS) | (1L << YIELD) | (1L << DEL) | (1L << PASS) | (1L << CONTINUE) | (1L << BREAK) | (1L << ASYNC) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE) | (1L << STAR))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (AT - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0)) {
				{
				setState(123);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(120);
					single_input();
					}
					break;
				case 2:
					{
					setState(121);
					file_input();
					}
					break;
				case 3:
					{
					setState(122);
					eval_input();
					}
					break;
				}
				}
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(128);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Single_inputContext extends ParserRuleContext {
		public TerminalNode LINE_BREAK() { return getToken(PythonParser.LINE_BREAK, 0); }
		public Simple_stmtContext simple_stmt() {
			return getRuleContext(Simple_stmtContext.class,0);
		}
		public Compound_stmtContext compound_stmt() {
			return getRuleContext(Compound_stmtContext.class,0);
		}
		public Single_inputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_single_input; }
	}

	public final Single_inputContext single_input() throws RecognitionException {
		Single_inputContext _localctx = new Single_inputContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_single_input);
		try {
			setState(135);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LINE_BREAK:
				enterOuterAlt(_localctx, 1);
				{
				setState(130);
				match(LINE_BREAK);
				}
				break;
			case RETURN:
			case RAISE:
			case FROM:
			case IMPORT:
			case NONLOCAL:
			case GLOBAL:
			case ASSERT:
			case NONE:
			case LAMBDA:
			case NOT:
			case YIELD:
			case DEL:
			case PASS:
			case CONTINUE:
			case BREAK:
			case AWAIT:
			case PRINT:
			case EXEC:
			case TRUE:
			case FALSE:
			case ELLIPSIS:
			case REVERSE_QUOTE:
			case STAR:
			case ADD:
			case MINUS:
			case NOT_OP:
			case STRING:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case IMAG_NUMBER:
			case FLOAT_NUMBER:
			case OPEN_PAREN:
			case OPEN_BRACE:
			case OPEN_BRACKET:
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(131);
				simple_stmt();
				}
				break;
			case DEF:
			case IF:
			case WHILE:
			case FOR:
			case TRY:
			case WITH:
			case CLASS:
			case ASYNC:
			case AT:
				enterOuterAlt(_localctx, 3);
				{
				setState(132);
				compound_stmt();
				setState(133);
				match(LINE_BREAK);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class File_inputContext extends ParserRuleContext {
		public List<TerminalNode> LINE_BREAK() { return getTokens(PythonParser.LINE_BREAK); }
		public TerminalNode LINE_BREAK(int i) {
			return getToken(PythonParser.LINE_BREAK, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public File_inputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_file_input; }
	}

	public final File_inputContext file_input() throws RecognitionException {
		File_inputContext _localctx = new File_inputContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_file_input);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(139); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(139);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case LINE_BREAK:
						{
						setState(137);
						match(LINE_BREAK);
						}
						break;
					case DEF:
					case RETURN:
					case RAISE:
					case FROM:
					case IMPORT:
					case NONLOCAL:
					case GLOBAL:
					case ASSERT:
					case IF:
					case WHILE:
					case FOR:
					case TRY:
					case NONE:
					case WITH:
					case LAMBDA:
					case NOT:
					case CLASS:
					case YIELD:
					case DEL:
					case PASS:
					case CONTINUE:
					case BREAK:
					case ASYNC:
					case AWAIT:
					case PRINT:
					case EXEC:
					case TRUE:
					case FALSE:
					case ELLIPSIS:
					case REVERSE_QUOTE:
					case STAR:
					case ADD:
					case MINUS:
					case NOT_OP:
					case AT:
					case STRING:
					case DECIMAL_INTEGER:
					case OCT_INTEGER:
					case HEX_INTEGER:
					case BIN_INTEGER:
					case IMAG_NUMBER:
					case FLOAT_NUMBER:
					case OPEN_PAREN:
					case OPEN_BRACE:
					case OPEN_BRACKET:
					case NAME:
						{
						setState(138);
						stmt();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(141); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Eval_inputContext extends ParserRuleContext {
		public TestlistContext testlist() {
			return getRuleContext(TestlistContext.class,0);
		}
		public List<TerminalNode> LINE_BREAK() { return getTokens(PythonParser.LINE_BREAK); }
		public TerminalNode LINE_BREAK(int i) {
			return getToken(PythonParser.LINE_BREAK, i);
		}
		public Eval_inputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eval_input; }
	}

	public final Eval_inputContext eval_input() throws RecognitionException {
		Eval_inputContext _localctx = new Eval_inputContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_eval_input);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			testlist();
			setState(147);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(144);
					match(LINE_BREAK);
					}
					} 
				}
				setState(149);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public Simple_stmtContext simple_stmt() {
			return getRuleContext(Simple_stmtContext.class,0);
		}
		public Compound_stmtContext compound_stmt() {
			return getRuleContext(Compound_stmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_stmt);
		try {
			setState(152);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RETURN:
			case RAISE:
			case FROM:
			case IMPORT:
			case NONLOCAL:
			case GLOBAL:
			case ASSERT:
			case NONE:
			case LAMBDA:
			case NOT:
			case YIELD:
			case DEL:
			case PASS:
			case CONTINUE:
			case BREAK:
			case AWAIT:
			case PRINT:
			case EXEC:
			case TRUE:
			case FALSE:
			case ELLIPSIS:
			case REVERSE_QUOTE:
			case STAR:
			case ADD:
			case MINUS:
			case NOT_OP:
			case STRING:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case IMAG_NUMBER:
			case FLOAT_NUMBER:
			case OPEN_PAREN:
			case OPEN_BRACE:
			case OPEN_BRACKET:
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				simple_stmt();
				}
				break;
			case DEF:
			case IF:
			case WHILE:
			case FOR:
			case TRY:
			case WITH:
			case CLASS:
			case ASYNC:
			case AT:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				compound_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Compound_stmtContext extends ParserRuleContext {
		public Compound_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compound_stmt; }
	 
		public Compound_stmtContext() { }
		public void copyFrom(Compound_stmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class While_stmtContext extends Compound_stmtContext {
		public TerminalNode WHILE() { return getToken(PythonParser.WHILE, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public Else_clauseContext else_clause() {
			return getRuleContext(Else_clauseContext.class,0);
		}
		public While_stmtContext(Compound_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Try_stmtContext extends Compound_stmtContext {
		public TerminalNode TRY() { return getToken(PythonParser.TRY, 0); }
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public Finally_clauseContext finally_clause() {
			return getRuleContext(Finally_clauseContext.class,0);
		}
		public List<Except_clauseContext> except_clause() {
			return getRuleContexts(Except_clauseContext.class);
		}
		public Except_clauseContext except_clause(int i) {
			return getRuleContext(Except_clauseContext.class,i);
		}
		public Else_clauseContext else_clause() {
			return getRuleContext(Else_clauseContext.class,0);
		}
		public Try_stmtContext(Compound_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class If_stmtContext extends Compound_stmtContext {
		public TestContext cond;
		public TerminalNode IF() { return getToken(PythonParser.IF, 0); }
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public List<Elif_clauseContext> elif_clause() {
			return getRuleContexts(Elif_clauseContext.class);
		}
		public Elif_clauseContext elif_clause(int i) {
			return getRuleContext(Elif_clauseContext.class,i);
		}
		public Else_clauseContext else_clause() {
			return getRuleContext(Else_clauseContext.class,0);
		}
		public If_stmtContext(Compound_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class With_stmtContext extends Compound_stmtContext {
		public TerminalNode WITH() { return getToken(PythonParser.WITH, 0); }
		public List<With_itemContext> with_item() {
			return getRuleContexts(With_itemContext.class);
		}
		public With_itemContext with_item(int i) {
			return getRuleContext(With_itemContext.class,i);
		}
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public TerminalNode ASYNC() { return getToken(PythonParser.ASYNC, 0); }
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public With_stmtContext(Compound_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Class_or_func_def_stmtContext extends Compound_stmtContext {
		public ClassdefContext classdef() {
			return getRuleContext(ClassdefContext.class,0);
		}
		public FuncdefContext funcdef() {
			return getRuleContext(FuncdefContext.class,0);
		}
		public List<DecoratorContext> decorator() {
			return getRuleContexts(DecoratorContext.class);
		}
		public DecoratorContext decorator(int i) {
			return getRuleContext(DecoratorContext.class,i);
		}
		public Class_or_func_def_stmtContext(Compound_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class For_stmtContext extends Compound_stmtContext {
		public TerminalNode FOR() { return getToken(PythonParser.FOR, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public TerminalNode IN() { return getToken(PythonParser.IN, 0); }
		public TestlistContext testlist() {
			return getRuleContext(TestlistContext.class,0);
		}
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public TerminalNode ASYNC() { return getToken(PythonParser.ASYNC, 0); }
		public Else_clauseContext else_clause() {
			return getRuleContext(Else_clauseContext.class,0);
		}
		public For_stmtContext(Compound_stmtContext ctx) { copyFrom(ctx); }
	}

	public final Compound_stmtContext compound_stmt() throws RecognitionException {
		Compound_stmtContext _localctx = new Compound_stmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_compound_stmt);
		int _la;
		try {
			int _alt;
			setState(228);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				_localctx = new If_stmtContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(154);
				match(IF);
				setState(155);
				((If_stmtContext)_localctx).cond = test();
				setState(156);
				match(COLON);
				setState(157);
				suite();
				setState(161);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(158);
						elif_clause();
						}
						} 
					}
					setState(163);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
				}
				setState(165);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
				case 1:
					{
					setState(164);
					else_clause();
					}
					break;
				}
				}
				break;
			case 2:
				_localctx = new While_stmtContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(167);
				match(WHILE);
				setState(168);
				test();
				setState(169);
				match(COLON);
				setState(170);
				suite();
				setState(172);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
				case 1:
					{
					setState(171);
					else_clause();
					}
					break;
				}
				}
				break;
			case 3:
				_localctx = new For_stmtContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASYNC) {
					{
					setState(174);
					match(ASYNC);
					}
				}

				setState(177);
				match(FOR);
				setState(178);
				exprlist();
				setState(179);
				match(IN);
				setState(180);
				testlist();
				setState(181);
				match(COLON);
				setState(182);
				suite();
				setState(184);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
				case 1:
					{
					setState(183);
					else_clause();
					}
					break;
				}
				}
				break;
			case 4:
				_localctx = new Try_stmtContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(186);
				match(TRY);
				setState(187);
				match(COLON);
				setState(188);
				suite();
				setState(201);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case EXCEPT:
					{
					setState(190); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(189);
							except_clause();
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(192); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					setState(195);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
					case 1:
						{
						setState(194);
						else_clause();
						}
						break;
					}
					setState(198);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						setState(197);
						finally_clause();
						}
						break;
					}
					}
					break;
				case FINALLY:
					{
					setState(200);
					finally_clause();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 5:
				_localctx = new With_stmtContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(204);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASYNC) {
					{
					setState(203);
					match(ASYNC);
					}
				}

				setState(206);
				match(WITH);
				setState(207);
				with_item();
				setState(212);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(208);
					match(COMMA);
					setState(209);
					with_item();
					}
					}
					setState(214);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(215);
				match(COLON);
				setState(216);
				suite();
				}
				break;
			case 6:
				_localctx = new Class_or_func_def_stmtContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(221);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==AT) {
					{
					{
					setState(218);
					decorator();
					}
					}
					setState(223);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(226);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case CLASS:
					{
					setState(224);
					classdef();
					}
					break;
				case DEF:
				case ASYNC:
					{
					setState(225);
					funcdef();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SuiteContext extends ParserRuleContext {
		public Simple_stmtContext simple_stmt() {
			return getRuleContext(Simple_stmtContext.class,0);
		}
		public Compound_stmtContext compound_stmt() {
			return getRuleContext(Compound_stmtContext.class,0);
		}
		public TerminalNode LINE_BREAK() { return getToken(PythonParser.LINE_BREAK, 0); }
		public TerminalNode INDENT() { return getToken(PythonParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(PythonParser.DEDENT, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public SuiteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_suite; }
	}

	public final SuiteContext suite() throws RecognitionException {
		SuiteContext _localctx = new SuiteContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_suite);
		int _la;
		try {
			setState(241);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RETURN:
			case RAISE:
			case FROM:
			case IMPORT:
			case NONLOCAL:
			case GLOBAL:
			case ASSERT:
			case NONE:
			case LAMBDA:
			case NOT:
			case YIELD:
			case DEL:
			case PASS:
			case CONTINUE:
			case BREAK:
			case AWAIT:
			case PRINT:
			case EXEC:
			case TRUE:
			case FALSE:
			case ELLIPSIS:
			case REVERSE_QUOTE:
			case STAR:
			case ADD:
			case MINUS:
			case NOT_OP:
			case STRING:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case IMAG_NUMBER:
			case FLOAT_NUMBER:
			case OPEN_PAREN:
			case OPEN_BRACE:
			case OPEN_BRACKET:
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(230);
				simple_stmt();
				}
				break;
			case DEF:
			case IF:
			case WHILE:
			case FOR:
			case TRY:
			case WITH:
			case CLASS:
			case ASYNC:
			case AT:
				enterOuterAlt(_localctx, 2);
				{
				setState(231);
				compound_stmt();
				}
				break;
			case LINE_BREAK:
				enterOuterAlt(_localctx, 3);
				{
				setState(232);
				match(LINE_BREAK);
				setState(233);
				match(INDENT);
				setState(235); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(234);
					stmt();
					}
					}
					setState(237); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DEF) | (1L << RETURN) | (1L << RAISE) | (1L << FROM) | (1L << IMPORT) | (1L << NONLOCAL) | (1L << GLOBAL) | (1L << ASSERT) | (1L << IF) | (1L << WHILE) | (1L << FOR) | (1L << TRY) | (1L << NONE) | (1L << WITH) | (1L << LAMBDA) | (1L << NOT) | (1L << CLASS) | (1L << YIELD) | (1L << DEL) | (1L << PASS) | (1L << CONTINUE) | (1L << BREAK) | (1L << ASYNC) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE) | (1L << STAR))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (AT - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0) );
				setState(239);
				match(DEDENT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DecoratorContext extends ParserRuleContext {
		public TerminalNode AT() { return getToken(PythonParser.AT, 0); }
		public Dotted_nameContext dotted_name() {
			return getRuleContext(Dotted_nameContext.class,0);
		}
		public TerminalNode LINE_BREAK() { return getToken(PythonParser.LINE_BREAK, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(PythonParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(PythonParser.CLOSE_PAREN, 0); }
		public ArglistContext arglist() {
			return getRuleContext(ArglistContext.class,0);
		}
		public DecoratorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decorator; }
	}

	public final DecoratorContext decorator() throws RecognitionException {
		DecoratorContext _localctx = new DecoratorContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_decorator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			match(AT);
			setState(244);
			dotted_name(0);
			setState(250);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPEN_PAREN) {
				{
				setState(245);
				match(OPEN_PAREN);
				setState(247);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NONE) | (1L << LAMBDA) | (1L << NOT) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE) | (1L << STAR) | (1L << POWER))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0)) {
					{
					setState(246);
					arglist();
					}
				}

				setState(249);
				match(CLOSE_PAREN);
				}
			}

			setState(252);
			match(LINE_BREAK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Elif_clauseContext extends ParserRuleContext {
		public TerminalNode ELIF() { return getToken(PythonParser.ELIF, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public Elif_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elif_clause; }
	}

	public final Elif_clauseContext elif_clause() throws RecognitionException {
		Elif_clauseContext _localctx = new Elif_clauseContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_elif_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			match(ELIF);
			setState(255);
			test();
			setState(256);
			match(COLON);
			setState(257);
			suite();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Else_clauseContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(PythonParser.ELSE, 0); }
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public Else_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_clause; }
	}

	public final Else_clauseContext else_clause() throws RecognitionException {
		Else_clauseContext _localctx = new Else_clauseContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_else_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			match(ELSE);
			setState(260);
			match(COLON);
			setState(261);
			suite();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Finally_clauseContext extends ParserRuleContext {
		public TerminalNode FINALLY() { return getToken(PythonParser.FINALLY, 0); }
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public Finally_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_finally_clause; }
	}

	public final Finally_clauseContext finally_clause() throws RecognitionException {
		Finally_clauseContext _localctx = new Finally_clauseContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_finally_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			match(FINALLY);
			setState(264);
			match(COLON);
			setState(265);
			suite();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class With_itemContext extends ParserRuleContext {
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TerminalNode AS() { return getToken(PythonParser.AS, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public With_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_with_item; }
	}

	public final With_itemContext with_item() throws RecognitionException {
		With_itemContext _localctx = new With_itemContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_with_item);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			test();
			setState(270);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(268);
				match(AS);
				setState(269);
				expr(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Except_clauseContext extends ParserRuleContext {
		public TerminalNode EXCEPT() { return getToken(PythonParser.EXCEPT, 0); }
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TerminalNode AS() { return getToken(PythonParser.AS, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Except_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_except_clause; }
	}

	public final Except_clauseContext except_clause() throws RecognitionException {
		Except_clauseContext _localctx = new Except_clauseContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_except_clause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			match(EXCEPT);
			setState(278);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NONE) | (1L << LAMBDA) | (1L << NOT) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0)) {
				{
				setState(273);
				test();
				setState(276);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==AS) {
					{
					setState(274);
					match(AS);
					setState(275);
					name();
					}
				}

				}
			}

			setState(280);
			match(COLON);
			setState(281);
			suite();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassdefContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(PythonParser.CLASS, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(PythonParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(PythonParser.CLOSE_PAREN, 0); }
		public ArglistContext arglist() {
			return getRuleContext(ArglistContext.class,0);
		}
		public ClassdefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classdef; }
	}

	public final ClassdefContext classdef() throws RecognitionException {
		ClassdefContext _localctx = new ClassdefContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_classdef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			match(CLASS);
			setState(284);
			name();
			setState(290);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPEN_PAREN) {
				{
				setState(285);
				match(OPEN_PAREN);
				setState(287);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NONE) | (1L << LAMBDA) | (1L << NOT) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE) | (1L << STAR) | (1L << POWER))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0)) {
					{
					setState(286);
					arglist();
					}
				}

				setState(289);
				match(CLOSE_PAREN);
				}
			}

			setState(292);
			match(COLON);
			setState(293);
			suite();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncdefContext extends ParserRuleContext {
		public TerminalNode DEF() { return getToken(PythonParser.DEF, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(PythonParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(PythonParser.CLOSE_PAREN, 0); }
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SuiteContext suite() {
			return getRuleContext(SuiteContext.class,0);
		}
		public TerminalNode ASYNC() { return getToken(PythonParser.ASYNC, 0); }
		public TypedargslistContext typedargslist() {
			return getRuleContext(TypedargslistContext.class,0);
		}
		public TerminalNode ARROW() { return getToken(PythonParser.ARROW, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public FuncdefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcdef; }
	}

	public final FuncdefContext funcdef() throws RecognitionException {
		FuncdefContext _localctx = new FuncdefContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_funcdef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(296);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASYNC) {
				{
				setState(295);
				match(ASYNC);
				}
			}

			setState(298);
			match(DEF);
			setState(299);
			name();
			setState(300);
			match(OPEN_PAREN);
			setState(302);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TRUE) | (1L << FALSE) | (1L << STAR) | (1L << POWER))) != 0) || _la==NAME) {
				{
				setState(301);
				typedargslist();
				}
			}

			setState(304);
			match(CLOSE_PAREN);
			setState(307);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ARROW) {
				{
				setState(305);
				match(ARROW);
				setState(306);
				test();
				}
			}

			setState(309);
			match(COLON);
			setState(310);
			suite();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypedargslistContext extends ParserRuleContext {
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public KwargsContext kwargs() {
			return getRuleContext(KwargsContext.class,0);
		}
		public List<Def_parametersContext> def_parameters() {
			return getRuleContexts(Def_parametersContext.class);
		}
		public Def_parametersContext def_parameters(int i) {
			return getRuleContext(Def_parametersContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public TypedargslistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedargslist; }
	}

	public final TypedargslistContext typedargslist() throws RecognitionException {
		TypedargslistContext _localctx = new TypedargslistContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_typedargslist);
		int _la;
		try {
			setState(336);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(315);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
				case 1:
					{
					setState(312);
					def_parameters();
					setState(313);
					match(COMMA);
					}
					break;
				}
				setState(327);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case STAR:
					{
					setState(317);
					args();
					setState(320);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
					case 1:
						{
						setState(318);
						match(COMMA);
						setState(319);
						def_parameters();
						}
						break;
					}
					setState(324);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
					case 1:
						{
						setState(322);
						match(COMMA);
						setState(323);
						kwargs();
						}
						break;
					}
					}
					break;
				case POWER:
					{
					setState(326);
					kwargs();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(330);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(329);
					match(COMMA);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(332);
				def_parameters();
				setState(334);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(333);
					match(COMMA);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgsContext extends ParserRuleContext {
		public TerminalNode STAR() { return getToken(PythonParser.STAR, 0); }
		public Named_parameterContext named_parameter() {
			return getRuleContext(Named_parameterContext.class,0);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_args);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(338);
			match(STAR);
			setState(339);
			named_parameter();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class KwargsContext extends ParserRuleContext {
		public TerminalNode POWER() { return getToken(PythonParser.POWER, 0); }
		public Named_parameterContext named_parameter() {
			return getRuleContext(Named_parameterContext.class,0);
		}
		public KwargsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_kwargs; }
	}

	public final KwargsContext kwargs() throws RecognitionException {
		KwargsContext _localctx = new KwargsContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_kwargs);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(341);
			match(POWER);
			setState(342);
			named_parameter();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Def_parametersContext extends ParserRuleContext {
		public List<Def_parameterContext> def_parameter() {
			return getRuleContexts(Def_parameterContext.class);
		}
		public Def_parameterContext def_parameter(int i) {
			return getRuleContext(Def_parameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public Def_parametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_def_parameters; }
	}

	public final Def_parametersContext def_parameters() throws RecognitionException {
		Def_parametersContext _localctx = new Def_parametersContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_def_parameters);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(344);
			def_parameter();
			setState(349);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(345);
					match(COMMA);
					setState(346);
					def_parameter();
					}
					} 
				}
				setState(351);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Def_parameterContext extends ParserRuleContext {
		public Named_parameterContext named_parameter() {
			return getRuleContext(Named_parameterContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(PythonParser.ASSIGN, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TerminalNode STAR() { return getToken(PythonParser.STAR, 0); }
		public Def_parameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_def_parameter; }
	}

	public final Def_parameterContext def_parameter() throws RecognitionException {
		Def_parameterContext _localctx = new Def_parameterContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_def_parameter);
		int _la;
		try {
			setState(358);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TRUE:
			case FALSE:
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(352);
				named_parameter();
				setState(355);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(353);
					match(ASSIGN);
					setState(354);
					test();
					}
				}

				}
				break;
			case STAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(357);
				match(STAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Named_parameterContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public Named_parameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_named_parameter; }
	}

	public final Named_parameterContext named_parameter() throws RecognitionException {
		Named_parameterContext _localctx = new Named_parameterContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_named_parameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(360);
			name();
			setState(363);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLON) {
				{
				setState(361);
				match(COLON);
				setState(362);
				test();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_stmtContext extends ParserRuleContext {
		public List<Small_stmtContext> small_stmt() {
			return getRuleContexts(Small_stmtContext.class);
		}
		public Small_stmtContext small_stmt(int i) {
			return getRuleContext(Small_stmtContext.class,i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(PythonParser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(PythonParser.SEMI_COLON, i);
		}
		public TerminalNode LINE_BREAK() { return getToken(PythonParser.LINE_BREAK, 0); }
		public Simple_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_stmt; }
	}

	public final Simple_stmtContext simple_stmt() throws RecognitionException {
		Simple_stmtContext _localctx = new Simple_stmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_simple_stmt);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(365);
			small_stmt();
			setState(370);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,44,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(366);
					match(SEMI_COLON);
					setState(367);
					small_stmt();
					}
					} 
				}
				setState(372);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,44,_ctx);
			}
			setState(374);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI_COLON) {
				{
				setState(373);
				match(SEMI_COLON);
				}
			}

			setState(377);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				{
				setState(376);
				match(LINE_BREAK);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Small_stmtContext extends ParserRuleContext {
		public Small_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_small_stmt; }
	 
		public Small_stmtContext() { }
		public void copyFrom(Small_stmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Assert_stmtContext extends Small_stmtContext {
		public TerminalNode ASSERT() { return getToken(PythonParser.ASSERT, 0); }
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(PythonParser.COMMA, 0); }
		public Assert_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Nonlocal_stmtContext extends Small_stmtContext {
		public TerminalNode NONLOCAL() { return getToken(PythonParser.NONLOCAL, 0); }
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public Nonlocal_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Pass_stmtContext extends Small_stmtContext {
		public TerminalNode PASS() { return getToken(PythonParser.PASS, 0); }
		public Pass_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Import_stmtContext extends Small_stmtContext {
		public TerminalNode IMPORT() { return getToken(PythonParser.IMPORT, 0); }
		public Dotted_as_namesContext dotted_as_names() {
			return getRuleContext(Dotted_as_namesContext.class,0);
		}
		public Import_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_stmtContext extends Small_stmtContext {
		public Testlist_star_exprContext testlist_star_expr() {
			return getRuleContext(Testlist_star_exprContext.class,0);
		}
		public Assign_partContext assign_part() {
			return getRuleContext(Assign_partContext.class,0);
		}
		public Expr_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Raise_stmtContext extends Small_stmtContext {
		public TerminalNode RAISE() { return getToken(PythonParser.RAISE, 0); }
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public TerminalNode FROM() { return getToken(PythonParser.FROM, 0); }
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public Raise_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Yield_stmtContext extends Small_stmtContext {
		public Yield_exprContext yield_expr() {
			return getRuleContext(Yield_exprContext.class,0);
		}
		public Yield_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class From_stmtContext extends Small_stmtContext {
		public TerminalNode FROM() { return getToken(PythonParser.FROM, 0); }
		public TerminalNode IMPORT() { return getToken(PythonParser.IMPORT, 0); }
		public Dotted_nameContext dotted_name() {
			return getRuleContext(Dotted_nameContext.class,0);
		}
		public TerminalNode STAR() { return getToken(PythonParser.STAR, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(PythonParser.OPEN_PAREN, 0); }
		public Import_as_namesContext import_as_names() {
			return getRuleContext(Import_as_namesContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(PythonParser.CLOSE_PAREN, 0); }
		public List<TerminalNode> DOT() { return getTokens(PythonParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(PythonParser.DOT, i);
		}
		public List<TerminalNode> ELLIPSIS() { return getTokens(PythonParser.ELLIPSIS); }
		public TerminalNode ELLIPSIS(int i) {
			return getToken(PythonParser.ELLIPSIS, i);
		}
		public From_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Global_stmtContext extends Small_stmtContext {
		public TerminalNode GLOBAL() { return getToken(PythonParser.GLOBAL, 0); }
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public Global_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Continue_stmtContext extends Small_stmtContext {
		public TerminalNode CONTINUE() { return getToken(PythonParser.CONTINUE, 0); }
		public Continue_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Break_stmtContext extends Small_stmtContext {
		public TerminalNode BREAK() { return getToken(PythonParser.BREAK, 0); }
		public Break_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Del_stmtContext extends Small_stmtContext {
		public TerminalNode DEL() { return getToken(PythonParser.DEL, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public Del_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}
	public static class Return_stmtContext extends Small_stmtContext {
		public TerminalNode RETURN() { return getToken(PythonParser.RETURN, 0); }
		public TestlistContext testlist() {
			return getRuleContext(TestlistContext.class,0);
		}
		public Return_stmtContext(Small_stmtContext ctx) { copyFrom(ctx); }
	}

	public final Small_stmtContext small_stmt() throws RecognitionException {
		Small_stmtContext _localctx = new Small_stmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_small_stmt);
		int _la;
		try {
			setState(459);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NONE:
			case LAMBDA:
			case NOT:
			case AWAIT:
			case PRINT:
			case EXEC:
			case TRUE:
			case FALSE:
			case ELLIPSIS:
			case REVERSE_QUOTE:
			case STAR:
			case ADD:
			case MINUS:
			case NOT_OP:
			case STRING:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case IMAG_NUMBER:
			case FLOAT_NUMBER:
			case OPEN_PAREN:
			case OPEN_BRACE:
			case OPEN_BRACKET:
			case NAME:
				_localctx = new Expr_stmtContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(379);
				testlist_star_expr();
				setState(381);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 55)) & ~0x3f) == 0 && ((1L << (_la - 55)) & ((1L << (COLON - 55)) | (1L << (ASSIGN - 55)) | (1L << (ADD_ASSIGN - 55)) | (1L << (SUB_ASSIGN - 55)) | (1L << (MULT_ASSIGN - 55)) | (1L << (AT_ASSIGN - 55)) | (1L << (DIV_ASSIGN - 55)) | (1L << (MOD_ASSIGN - 55)) | (1L << (AND_ASSIGN - 55)) | (1L << (OR_ASSIGN - 55)) | (1L << (XOR_ASSIGN - 55)) | (1L << (LEFT_SHIFT_ASSIGN - 55)) | (1L << (RIGHT_SHIFT_ASSIGN - 55)) | (1L << (POWER_ASSIGN - 55)) | (1L << (IDIV_ASSIGN - 55)))) != 0)) {
					{
					setState(380);
					assign_part();
					}
				}

				}
				break;
			case DEL:
				_localctx = new Del_stmtContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(383);
				match(DEL);
				setState(384);
				exprlist();
				}
				break;
			case PASS:
				_localctx = new Pass_stmtContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(385);
				match(PASS);
				}
				break;
			case BREAK:
				_localctx = new Break_stmtContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(386);
				match(BREAK);
				}
				break;
			case CONTINUE:
				_localctx = new Continue_stmtContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(387);
				match(CONTINUE);
				}
				break;
			case RETURN:
				_localctx = new Return_stmtContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(388);
				match(RETURN);
				setState(390);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
				case 1:
					{
					setState(389);
					testlist();
					}
					break;
				}
				}
				break;
			case RAISE:
				_localctx = new Raise_stmtContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(392);
				match(RAISE);
				setState(402);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,51,_ctx) ) {
				case 1:
					{
					setState(393);
					test();
					setState(400);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==COMMA) {
						{
						setState(394);
						match(COMMA);
						setState(395);
						test();
						setState(398);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==COMMA) {
							{
							setState(396);
							match(COMMA);
							setState(397);
							test();
							}
						}

						}
					}

					}
					break;
				}
				setState(406);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,52,_ctx) ) {
				case 1:
					{
					setState(404);
					match(FROM);
					setState(405);
					test();
					}
					break;
				}
				}
				break;
			case YIELD:
				_localctx = new Yield_stmtContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(408);
				yield_expr();
				}
				break;
			case IMPORT:
				_localctx = new Import_stmtContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(409);
				match(IMPORT);
				setState(410);
				dotted_as_names();
				}
				break;
			case FROM:
				_localctx = new From_stmtContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(411);
				match(FROM);
				setState(424);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,55,_ctx) ) {
				case 1:
					{
					setState(415);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==DOT || _la==ELLIPSIS) {
						{
						{
						setState(412);
						_la = _input.LA(1);
						if ( !(_la==DOT || _la==ELLIPSIS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						}
						}
						setState(417);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(418);
					dotted_name(0);
					}
					break;
				case 2:
					{
					setState(420); 
					_errHandler.sync(this);
					_la = _input.LA(1);
					do {
						{
						{
						setState(419);
						_la = _input.LA(1);
						if ( !(_la==DOT || _la==ELLIPSIS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						}
						}
						setState(422); 
						_errHandler.sync(this);
						_la = _input.LA(1);
					} while ( _la==DOT || _la==ELLIPSIS );
					}
					break;
				}
				setState(426);
				match(IMPORT);
				setState(433);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case STAR:
					{
					setState(427);
					match(STAR);
					}
					break;
				case OPEN_PAREN:
					{
					setState(428);
					match(OPEN_PAREN);
					setState(429);
					import_as_names();
					setState(430);
					match(CLOSE_PAREN);
					}
					break;
				case TRUE:
				case FALSE:
				case NAME:
					{
					setState(432);
					import_as_names();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case GLOBAL:
				_localctx = new Global_stmtContext(_localctx);
				enterOuterAlt(_localctx, 11);
				{
				setState(435);
				match(GLOBAL);
				setState(436);
				name();
				setState(441);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(437);
					match(COMMA);
					setState(438);
					name();
					}
					}
					setState(443);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case ASSERT:
				_localctx = new Assert_stmtContext(_localctx);
				enterOuterAlt(_localctx, 12);
				{
				setState(444);
				match(ASSERT);
				setState(445);
				test();
				setState(448);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(446);
					match(COMMA);
					setState(447);
					test();
					}
				}

				}
				break;
			case NONLOCAL:
				_localctx = new Nonlocal_stmtContext(_localctx);
				enterOuterAlt(_localctx, 13);
				{
				setState(450);
				match(NONLOCAL);
				setState(451);
				name();
				setState(456);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(452);
					match(COMMA);
					setState(453);
					name();
					}
					}
					setState(458);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Testlist_star_exprContext extends ParserRuleContext {
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public List<Star_exprContext> star_expr() {
			return getRuleContexts(Star_exprContext.class);
		}
		public Star_exprContext star_expr(int i) {
			return getRuleContext(Star_exprContext.class,i);
		}
		public TestlistContext testlist() {
			return getRuleContext(TestlistContext.class,0);
		}
		public Testlist_star_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_testlist_star_expr; }
	}

	public final Testlist_star_exprContext testlist_star_expr() throws RecognitionException {
		Testlist_star_exprContext _localctx = new Testlist_star_exprContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_testlist_star_expr);
		try {
			int _alt;
			setState(476);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,64,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(467); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(463);
						_errHandler.sync(this);
						switch (_input.LA(1)) {
						case NONE:
						case LAMBDA:
						case NOT:
						case AWAIT:
						case PRINT:
						case EXEC:
						case TRUE:
						case FALSE:
						case ELLIPSIS:
						case REVERSE_QUOTE:
						case ADD:
						case MINUS:
						case NOT_OP:
						case STRING:
						case DECIMAL_INTEGER:
						case OCT_INTEGER:
						case HEX_INTEGER:
						case BIN_INTEGER:
						case IMAG_NUMBER:
						case FLOAT_NUMBER:
						case OPEN_PAREN:
						case OPEN_BRACE:
						case OPEN_BRACKET:
						case NAME:
							{
							setState(461);
							test();
							}
							break;
						case STAR:
							{
							setState(462);
							star_expr();
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(465);
						match(COMMA);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(469); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,62,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				setState(473);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,63,_ctx) ) {
				case 1:
					{
					setState(471);
					test();
					}
					break;
				case 2:
					{
					setState(472);
					star_expr();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(475);
				testlist();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Star_exprContext extends ParserRuleContext {
		public TerminalNode STAR() { return getToken(PythonParser.STAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Star_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_star_expr; }
	}

	public final Star_exprContext star_expr() throws RecognitionException {
		Star_exprContext _localctx = new Star_exprContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_star_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(478);
			match(STAR);
			setState(479);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_partContext extends ParserRuleContext {
		public Token op;
		public List<TerminalNode> ASSIGN() { return getTokens(PythonParser.ASSIGN); }
		public TerminalNode ASSIGN(int i) {
			return getToken(PythonParser.ASSIGN, i);
		}
		public List<Testlist_star_exprContext> testlist_star_expr() {
			return getRuleContexts(Testlist_star_exprContext.class);
		}
		public Testlist_star_exprContext testlist_star_expr(int i) {
			return getRuleContext(Testlist_star_exprContext.class,i);
		}
		public Yield_exprContext yield_expr() {
			return getRuleContext(Yield_exprContext.class,0);
		}
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TestlistContext testlist() {
			return getRuleContext(TestlistContext.class,0);
		}
		public TerminalNode ADD_ASSIGN() { return getToken(PythonParser.ADD_ASSIGN, 0); }
		public TerminalNode SUB_ASSIGN() { return getToken(PythonParser.SUB_ASSIGN, 0); }
		public TerminalNode MULT_ASSIGN() { return getToken(PythonParser.MULT_ASSIGN, 0); }
		public TerminalNode AT_ASSIGN() { return getToken(PythonParser.AT_ASSIGN, 0); }
		public TerminalNode DIV_ASSIGN() { return getToken(PythonParser.DIV_ASSIGN, 0); }
		public TerminalNode MOD_ASSIGN() { return getToken(PythonParser.MOD_ASSIGN, 0); }
		public TerminalNode AND_ASSIGN() { return getToken(PythonParser.AND_ASSIGN, 0); }
		public TerminalNode OR_ASSIGN() { return getToken(PythonParser.OR_ASSIGN, 0); }
		public TerminalNode XOR_ASSIGN() { return getToken(PythonParser.XOR_ASSIGN, 0); }
		public TerminalNode LEFT_SHIFT_ASSIGN() { return getToken(PythonParser.LEFT_SHIFT_ASSIGN, 0); }
		public TerminalNode RIGHT_SHIFT_ASSIGN() { return getToken(PythonParser.RIGHT_SHIFT_ASSIGN, 0); }
		public TerminalNode POWER_ASSIGN() { return getToken(PythonParser.POWER_ASSIGN, 0); }
		public TerminalNode IDIV_ASSIGN() { return getToken(PythonParser.IDIV_ASSIGN, 0); }
		public Assign_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_part; }
	}

	public final Assign_partContext assign_part() throws RecognitionException {
		Assign_partContext _localctx = new Assign_partContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_assign_part);
		int _la;
		try {
			int _alt;
			setState(508);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ASSIGN:
				enterOuterAlt(_localctx, 1);
				{
				setState(481);
				match(ASSIGN);
				setState(495);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case NONE:
				case LAMBDA:
				case NOT:
				case AWAIT:
				case PRINT:
				case EXEC:
				case TRUE:
				case FALSE:
				case ELLIPSIS:
				case REVERSE_QUOTE:
				case STAR:
				case ADD:
				case MINUS:
				case NOT_OP:
				case STRING:
				case DECIMAL_INTEGER:
				case OCT_INTEGER:
				case HEX_INTEGER:
				case BIN_INTEGER:
				case IMAG_NUMBER:
				case FLOAT_NUMBER:
				case OPEN_PAREN:
				case OPEN_BRACE:
				case OPEN_BRACKET:
				case NAME:
					{
					setState(482);
					testlist_star_expr();
					setState(487);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,65,_ctx);
					while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
						if ( _alt==1 ) {
							{
							{
							setState(483);
							match(ASSIGN);
							setState(484);
							testlist_star_expr();
							}
							} 
						}
						setState(489);
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,65,_ctx);
					}
					setState(492);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==ASSIGN) {
						{
						setState(490);
						match(ASSIGN);
						setState(491);
						yield_expr();
						}
					}

					}
					break;
				case YIELD:
					{
					setState(494);
					yield_expr();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case COLON:
				enterOuterAlt(_localctx, 2);
				{
				setState(497);
				match(COLON);
				setState(498);
				test();
				setState(501);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(499);
					match(ASSIGN);
					setState(500);
					testlist();
					}
				}

				}
				break;
			case ADD_ASSIGN:
			case SUB_ASSIGN:
			case MULT_ASSIGN:
			case AT_ASSIGN:
			case DIV_ASSIGN:
			case MOD_ASSIGN:
			case AND_ASSIGN:
			case OR_ASSIGN:
			case XOR_ASSIGN:
			case LEFT_SHIFT_ASSIGN:
			case RIGHT_SHIFT_ASSIGN:
			case POWER_ASSIGN:
			case IDIV_ASSIGN:
				enterOuterAlt(_localctx, 3);
				{
				setState(503);
				((Assign_partContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(((((_la - 79)) & ~0x3f) == 0 && ((1L << (_la - 79)) & ((1L << (ADD_ASSIGN - 79)) | (1L << (SUB_ASSIGN - 79)) | (1L << (MULT_ASSIGN - 79)) | (1L << (AT_ASSIGN - 79)) | (1L << (DIV_ASSIGN - 79)) | (1L << (MOD_ASSIGN - 79)) | (1L << (AND_ASSIGN - 79)) | (1L << (OR_ASSIGN - 79)) | (1L << (XOR_ASSIGN - 79)) | (1L << (LEFT_SHIFT_ASSIGN - 79)) | (1L << (RIGHT_SHIFT_ASSIGN - 79)) | (1L << (POWER_ASSIGN - 79)) | (1L << (IDIV_ASSIGN - 79)))) != 0)) ) {
					((Assign_partContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(506);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case YIELD:
					{
					setState(504);
					yield_expr();
					}
					break;
				case NONE:
				case LAMBDA:
				case NOT:
				case AWAIT:
				case PRINT:
				case EXEC:
				case TRUE:
				case FALSE:
				case ELLIPSIS:
				case REVERSE_QUOTE:
				case ADD:
				case MINUS:
				case NOT_OP:
				case STRING:
				case DECIMAL_INTEGER:
				case OCT_INTEGER:
				case HEX_INTEGER:
				case BIN_INTEGER:
				case IMAG_NUMBER:
				case FLOAT_NUMBER:
				case OPEN_PAREN:
				case OPEN_BRACE:
				case OPEN_BRACKET:
				case NAME:
					{
					setState(505);
					testlist();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprlistContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public ExprlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprlist; }
	}

	public final ExprlistContext exprlist() throws RecognitionException {
		ExprlistContext _localctx = new ExprlistContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_exprlist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(510);
			expr(0);
			setState(515);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,71,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(511);
					match(COMMA);
					setState(512);
					expr(0);
					}
					} 
				}
				setState(517);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,71,_ctx);
			}
			setState(519);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(518);
				match(COMMA);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Import_as_namesContext extends ParserRuleContext {
		public List<Import_as_nameContext> import_as_name() {
			return getRuleContexts(Import_as_nameContext.class);
		}
		public Import_as_nameContext import_as_name(int i) {
			return getRuleContext(Import_as_nameContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public Import_as_namesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_import_as_names; }
	}

	public final Import_as_namesContext import_as_names() throws RecognitionException {
		Import_as_namesContext _localctx = new Import_as_namesContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_import_as_names);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(521);
			import_as_name();
			setState(526);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,73,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(522);
					match(COMMA);
					setState(523);
					import_as_name();
					}
					} 
				}
				setState(528);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,73,_ctx);
			}
			setState(530);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(529);
				match(COMMA);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Import_as_nameContext extends ParserRuleContext {
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public TerminalNode AS() { return getToken(PythonParser.AS, 0); }
		public Import_as_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_import_as_name; }
	}

	public final Import_as_nameContext import_as_name() throws RecognitionException {
		Import_as_nameContext _localctx = new Import_as_nameContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_import_as_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(532);
			name();
			setState(535);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(533);
				match(AS);
				setState(534);
				name();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Dotted_as_namesContext extends ParserRuleContext {
		public List<Dotted_as_nameContext> dotted_as_name() {
			return getRuleContexts(Dotted_as_nameContext.class);
		}
		public Dotted_as_nameContext dotted_as_name(int i) {
			return getRuleContext(Dotted_as_nameContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public Dotted_as_namesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dotted_as_names; }
	}

	public final Dotted_as_namesContext dotted_as_names() throws RecognitionException {
		Dotted_as_namesContext _localctx = new Dotted_as_namesContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_dotted_as_names);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(537);
			dotted_as_name();
			setState(542);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(538);
				match(COMMA);
				setState(539);
				dotted_as_name();
				}
				}
				setState(544);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Dotted_as_nameContext extends ParserRuleContext {
		public Dotted_nameContext dotted_name() {
			return getRuleContext(Dotted_nameContext.class,0);
		}
		public TerminalNode AS() { return getToken(PythonParser.AS, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Dotted_as_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dotted_as_name; }
	}

	public final Dotted_as_nameContext dotted_as_name() throws RecognitionException {
		Dotted_as_nameContext _localctx = new Dotted_as_nameContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_dotted_as_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(545);
			dotted_name(0);
			setState(548);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(546);
				match(AS);
				setState(547);
				name();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TestContext extends ParserRuleContext {
		public List<Logical_testContext> logical_test() {
			return getRuleContexts(Logical_testContext.class);
		}
		public Logical_testContext logical_test(int i) {
			return getRuleContext(Logical_testContext.class,i);
		}
		public TerminalNode IF() { return getToken(PythonParser.IF, 0); }
		public TerminalNode ELSE() { return getToken(PythonParser.ELSE, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TerminalNode LAMBDA() { return getToken(PythonParser.LAMBDA, 0); }
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public VarargslistContext varargslist() {
			return getRuleContext(VarargslistContext.class,0);
		}
		public TestContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_test; }
	}

	public final TestContext test() throws RecognitionException {
		TestContext _localctx = new TestContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_test);
		int _la;
		try {
			setState(564);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NONE:
			case NOT:
			case AWAIT:
			case PRINT:
			case EXEC:
			case TRUE:
			case FALSE:
			case ELLIPSIS:
			case REVERSE_QUOTE:
			case ADD:
			case MINUS:
			case NOT_OP:
			case STRING:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case IMAG_NUMBER:
			case FLOAT_NUMBER:
			case OPEN_PAREN:
			case OPEN_BRACE:
			case OPEN_BRACKET:
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(550);
				logical_test(0);
				setState(556);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,78,_ctx) ) {
				case 1:
					{
					setState(551);
					match(IF);
					setState(552);
					logical_test(0);
					setState(553);
					match(ELSE);
					setState(554);
					test();
					}
					break;
				}
				}
				break;
			case LAMBDA:
				enterOuterAlt(_localctx, 2);
				{
				setState(558);
				match(LAMBDA);
				setState(560);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TRUE) | (1L << FALSE) | (1L << STAR) | (1L << POWER))) != 0) || _la==NAME) {
					{
					setState(559);
					varargslist();
					}
				}

				setState(562);
				match(COLON);
				setState(563);
				test();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarargslistContext extends ParserRuleContext {
		public VarargsContext varargs() {
			return getRuleContext(VarargsContext.class,0);
		}
		public VarkwargsContext varkwargs() {
			return getRuleContext(VarkwargsContext.class,0);
		}
		public List<Vardef_parametersContext> vardef_parameters() {
			return getRuleContexts(Vardef_parametersContext.class);
		}
		public Vardef_parametersContext vardef_parameters(int i) {
			return getRuleContext(Vardef_parametersContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public VarargslistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varargslist; }
	}

	public final VarargslistContext varargslist() throws RecognitionException {
		VarargslistContext _localctx = new VarargslistContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_varargslist);
		int _la;
		try {
			setState(590);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,87,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(569);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,81,_ctx) ) {
				case 1:
					{
					setState(566);
					vardef_parameters();
					setState(567);
					match(COMMA);
					}
					break;
				}
				setState(581);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case STAR:
					{
					setState(571);
					varargs();
					setState(574);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,82,_ctx) ) {
					case 1:
						{
						setState(572);
						match(COMMA);
						setState(573);
						vardef_parameters();
						}
						break;
					}
					setState(578);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,83,_ctx) ) {
					case 1:
						{
						setState(576);
						match(COMMA);
						setState(577);
						varkwargs();
						}
						break;
					}
					}
					break;
				case POWER:
					{
					setState(580);
					varkwargs();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(584);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(583);
					match(COMMA);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(586);
				vardef_parameters();
				setState(588);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(587);
					match(COMMA);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Vardef_parametersContext extends ParserRuleContext {
		public List<Vardef_parameterContext> vardef_parameter() {
			return getRuleContexts(Vardef_parameterContext.class);
		}
		public Vardef_parameterContext vardef_parameter(int i) {
			return getRuleContext(Vardef_parameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public Vardef_parametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardef_parameters; }
	}

	public final Vardef_parametersContext vardef_parameters() throws RecognitionException {
		Vardef_parametersContext _localctx = new Vardef_parametersContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_vardef_parameters);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(592);
			vardef_parameter();
			setState(597);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,88,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(593);
					match(COMMA);
					setState(594);
					vardef_parameter();
					}
					} 
				}
				setState(599);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,88,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Vardef_parameterContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(PythonParser.ASSIGN, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TerminalNode STAR() { return getToken(PythonParser.STAR, 0); }
		public Vardef_parameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardef_parameter; }
	}

	public final Vardef_parameterContext vardef_parameter() throws RecognitionException {
		Vardef_parameterContext _localctx = new Vardef_parameterContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_vardef_parameter);
		int _la;
		try {
			setState(606);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TRUE:
			case FALSE:
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(600);
				name();
				setState(603);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(601);
					match(ASSIGN);
					setState(602);
					test();
					}
				}

				}
				break;
			case STAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(605);
				match(STAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarargsContext extends ParserRuleContext {
		public TerminalNode STAR() { return getToken(PythonParser.STAR, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public VarargsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varargs; }
	}

	public final VarargsContext varargs() throws RecognitionException {
		VarargsContext _localctx = new VarargsContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_varargs);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(608);
			match(STAR);
			setState(609);
			name();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarkwargsContext extends ParserRuleContext {
		public TerminalNode POWER() { return getToken(PythonParser.POWER, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public VarkwargsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varkwargs; }
	}

	public final VarkwargsContext varkwargs() throws RecognitionException {
		VarkwargsContext _localctx = new VarkwargsContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_varkwargs);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(611);
			match(POWER);
			setState(612);
			name();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Logical_testContext extends ParserRuleContext {
		public Token op;
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public TerminalNode NOT() { return getToken(PythonParser.NOT, 0); }
		public List<Logical_testContext> logical_test() {
			return getRuleContexts(Logical_testContext.class);
		}
		public Logical_testContext logical_test(int i) {
			return getRuleContext(Logical_testContext.class,i);
		}
		public TerminalNode AND() { return getToken(PythonParser.AND, 0); }
		public TerminalNode OR() { return getToken(PythonParser.OR, 0); }
		public Logical_testContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_test; }
	}

	public final Logical_testContext logical_test() throws RecognitionException {
		return logical_test(0);
	}

	private Logical_testContext logical_test(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Logical_testContext _localctx = new Logical_testContext(_ctx, _parentState);
		Logical_testContext _prevctx = _localctx;
		int _startState = 74;
		enterRecursionRule(_localctx, 74, RULE_logical_test, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(618);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NONE:
			case AWAIT:
			case PRINT:
			case EXEC:
			case TRUE:
			case FALSE:
			case ELLIPSIS:
			case REVERSE_QUOTE:
			case ADD:
			case MINUS:
			case NOT_OP:
			case STRING:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case IMAG_NUMBER:
			case FLOAT_NUMBER:
			case OPEN_PAREN:
			case OPEN_BRACE:
			case OPEN_BRACKET:
			case NAME:
				{
				setState(615);
				comparison(0);
				}
				break;
			case NOT:
				{
				setState(616);
				match(NOT);
				setState(617);
				logical_test(3);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(628);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,93,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(626);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,92,_ctx) ) {
					case 1:
						{
						_localctx = new Logical_testContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_logical_test);
						setState(620);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(621);
						((Logical_testContext)_localctx).op = match(AND);
						setState(622);
						logical_test(3);
						}
						break;
					case 2:
						{
						_localctx = new Logical_testContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_logical_test);
						setState(623);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(624);
						((Logical_testContext)_localctx).op = match(OR);
						setState(625);
						logical_test(2);
						}
						break;
					}
					} 
				}
				setState(630);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,93,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ComparisonContext extends ParserRuleContext {
		public Token optional;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<ComparisonContext> comparison() {
			return getRuleContexts(ComparisonContext.class);
		}
		public ComparisonContext comparison(int i) {
			return getRuleContext(ComparisonContext.class,i);
		}
		public TerminalNode LESS_THAN() { return getToken(PythonParser.LESS_THAN, 0); }
		public TerminalNode GREATER_THAN() { return getToken(PythonParser.GREATER_THAN, 0); }
		public TerminalNode EQUALS() { return getToken(PythonParser.EQUALS, 0); }
		public TerminalNode GT_EQ() { return getToken(PythonParser.GT_EQ, 0); }
		public TerminalNode LT_EQ() { return getToken(PythonParser.LT_EQ, 0); }
		public TerminalNode NOT_EQ_1() { return getToken(PythonParser.NOT_EQ_1, 0); }
		public TerminalNode NOT_EQ_2() { return getToken(PythonParser.NOT_EQ_2, 0); }
		public TerminalNode IN() { return getToken(PythonParser.IN, 0); }
		public TerminalNode IS() { return getToken(PythonParser.IS, 0); }
		public TerminalNode NOT() { return getToken(PythonParser.NOT, 0); }
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		return comparison(0);
	}

	private ComparisonContext comparison(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ComparisonContext _localctx = new ComparisonContext(_ctx, _parentState);
		ComparisonContext _prevctx = _localctx;
		int _startState = 76;
		enterRecursionRule(_localctx, 76, RULE_comparison, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(632);
			expr(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(655);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,97,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ComparisonContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_comparison);
					setState(634);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(650);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case LESS_THAN:
						{
						setState(635);
						match(LESS_THAN);
						}
						break;
					case GREATER_THAN:
						{
						setState(636);
						match(GREATER_THAN);
						}
						break;
					case EQUALS:
						{
						setState(637);
						match(EQUALS);
						}
						break;
					case GT_EQ:
						{
						setState(638);
						match(GT_EQ);
						}
						break;
					case LT_EQ:
						{
						setState(639);
						match(LT_EQ);
						}
						break;
					case NOT_EQ_1:
						{
						setState(640);
						match(NOT_EQ_1);
						}
						break;
					case NOT_EQ_2:
						{
						setState(641);
						match(NOT_EQ_2);
						}
						break;
					case IN:
					case NOT:
						{
						setState(643);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==NOT) {
							{
							setState(642);
							((ComparisonContext)_localctx).optional = match(NOT);
							}
						}

						setState(645);
						match(IN);
						}
						break;
					case IS:
						{
						setState(646);
						match(IS);
						setState(648);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==NOT) {
							{
							setState(647);
							((ComparisonContext)_localctx).optional = match(NOT);
							}
						}

						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(652);
					comparison(3);
					}
					} 
				}
				setState(657);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,97,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public Token op;
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public TerminalNode AWAIT() { return getToken(PythonParser.AWAIT, 0); }
		public List<TrailerContext> trailer() {
			return getRuleContexts(TrailerContext.class);
		}
		public TrailerContext trailer(int i) {
			return getRuleContext(TrailerContext.class,i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(PythonParser.ADD, 0); }
		public TerminalNode MINUS() { return getToken(PythonParser.MINUS, 0); }
		public TerminalNode NOT_OP() { return getToken(PythonParser.NOT_OP, 0); }
		public TerminalNode POWER() { return getToken(PythonParser.POWER, 0); }
		public TerminalNode STAR() { return getToken(PythonParser.STAR, 0); }
		public TerminalNode DIV() { return getToken(PythonParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(PythonParser.MOD, 0); }
		public TerminalNode IDIV() { return getToken(PythonParser.IDIV, 0); }
		public TerminalNode AT() { return getToken(PythonParser.AT, 0); }
		public TerminalNode LEFT_SHIFT() { return getToken(PythonParser.LEFT_SHIFT, 0); }
		public TerminalNode RIGHT_SHIFT() { return getToken(PythonParser.RIGHT_SHIFT, 0); }
		public TerminalNode AND_OP() { return getToken(PythonParser.AND_OP, 0); }
		public TerminalNode XOR() { return getToken(PythonParser.XOR, 0); }
		public TerminalNode OR_OP() { return getToken(PythonParser.OR_OP, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 78;
		enterRecursionRule(_localctx, 78, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(671);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,100,_ctx) ) {
			case 1:
				{
				setState(660);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==AWAIT) {
					{
					setState(659);
					match(AWAIT);
					}
				}

				setState(662);
				atom();
				setState(666);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,99,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(663);
						trailer();
						}
						} 
					}
					setState(668);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,99,_ctx);
				}
				}
				break;
			case 2:
				{
				setState(669);
				((ExprContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)))) != 0)) ) {
					((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(670);
				expr(7);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(696);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,102,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(694);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,101,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(673);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(674);
						((ExprContext)_localctx).op = match(POWER);
						setState(675);
						expr(8);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(676);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(677);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(((((_la - 53)) & ~0x3f) == 0 && ((1L << (_la - 53)) & ((1L << (STAR - 53)) | (1L << (DIV - 53)) | (1L << (MOD - 53)) | (1L << (IDIV - 53)) | (1L << (AT - 53)))) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(678);
						expr(7);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(679);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(680);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==MINUS) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(681);
						expr(6);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(682);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(683);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==LEFT_SHIFT || _la==RIGHT_SHIFT) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(684);
						expr(5);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(685);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(686);
						((ExprContext)_localctx).op = match(AND_OP);
						setState(687);
						expr(4);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(688);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(689);
						((ExprContext)_localctx).op = match(XOR);
						setState(690);
						expr(3);
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(691);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(692);
						((ExprContext)_localctx).op = match(OR_OP);
						setState(693);
						expr(2);
						}
						break;
					}
					} 
				}
				setState(698);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,102,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class AtomContext extends ParserRuleContext {
		public TerminalNode OPEN_PAREN() { return getToken(PythonParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(PythonParser.CLOSE_PAREN, 0); }
		public Yield_exprContext yield_expr() {
			return getRuleContext(Yield_exprContext.class,0);
		}
		public Testlist_compContext testlist_comp() {
			return getRuleContext(Testlist_compContext.class,0);
		}
		public TerminalNode OPEN_BRACKET() { return getToken(PythonParser.OPEN_BRACKET, 0); }
		public TerminalNode CLOSE_BRACKET() { return getToken(PythonParser.CLOSE_BRACKET, 0); }
		public TerminalNode OPEN_BRACE() { return getToken(PythonParser.OPEN_BRACE, 0); }
		public TerminalNode CLOSE_BRACE() { return getToken(PythonParser.CLOSE_BRACE, 0); }
		public DictorsetmakerContext dictorsetmaker() {
			return getRuleContext(DictorsetmakerContext.class,0);
		}
		public List<TerminalNode> REVERSE_QUOTE() { return getTokens(PythonParser.REVERSE_QUOTE); }
		public TerminalNode REVERSE_QUOTE(int i) {
			return getToken(PythonParser.REVERSE_QUOTE, i);
		}
		public TestlistContext testlist() {
			return getRuleContext(TestlistContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(PythonParser.COMMA, 0); }
		public TerminalNode ELLIPSIS() { return getToken(PythonParser.ELLIPSIS, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public TerminalNode PRINT() { return getToken(PythonParser.PRINT, 0); }
		public TerminalNode EXEC() { return getToken(PythonParser.EXEC, 0); }
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(PythonParser.MINUS, 0); }
		public TerminalNode NONE() { return getToken(PythonParser.NONE, 0); }
		public List<TerminalNode> STRING() { return getTokens(PythonParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(PythonParser.STRING, i);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_atom);
		int _la;
		try {
			int _alt;
			setState(736);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(699);
				match(OPEN_PAREN);
				setState(702);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case YIELD:
					{
					setState(700);
					yield_expr();
					}
					break;
				case NONE:
				case LAMBDA:
				case NOT:
				case AWAIT:
				case PRINT:
				case EXEC:
				case TRUE:
				case FALSE:
				case ELLIPSIS:
				case REVERSE_QUOTE:
				case STAR:
				case ADD:
				case MINUS:
				case NOT_OP:
				case STRING:
				case DECIMAL_INTEGER:
				case OCT_INTEGER:
				case HEX_INTEGER:
				case BIN_INTEGER:
				case IMAG_NUMBER:
				case FLOAT_NUMBER:
				case OPEN_PAREN:
				case OPEN_BRACE:
				case OPEN_BRACKET:
				case NAME:
					{
					setState(701);
					testlist_comp();
					}
					break;
				case CLOSE_PAREN:
					break;
				default:
					break;
				}
				setState(704);
				match(CLOSE_PAREN);
				}
				break;
			case OPEN_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				setState(705);
				match(OPEN_BRACKET);
				setState(707);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NONE) | (1L << LAMBDA) | (1L << NOT) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE) | (1L << STAR))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0)) {
					{
					setState(706);
					testlist_comp();
					}
				}

				setState(709);
				match(CLOSE_BRACKET);
				}
				break;
			case OPEN_BRACE:
				enterOuterAlt(_localctx, 3);
				{
				setState(710);
				match(OPEN_BRACE);
				setState(712);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NONE) | (1L << LAMBDA) | (1L << NOT) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE) | (1L << STAR) | (1L << POWER))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0)) {
					{
					setState(711);
					dictorsetmaker();
					}
				}

				setState(714);
				match(CLOSE_BRACE);
				}
				break;
			case REVERSE_QUOTE:
				enterOuterAlt(_localctx, 4);
				{
				setState(715);
				match(REVERSE_QUOTE);
				setState(716);
				testlist();
				setState(718);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(717);
					match(COMMA);
					}
				}

				setState(720);
				match(REVERSE_QUOTE);
				}
				break;
			case ELLIPSIS:
				enterOuterAlt(_localctx, 5);
				{
				setState(722);
				match(ELLIPSIS);
				}
				break;
			case TRUE:
			case FALSE:
			case NAME:
				enterOuterAlt(_localctx, 6);
				{
				setState(723);
				name();
				}
				break;
			case PRINT:
				enterOuterAlt(_localctx, 7);
				{
				setState(724);
				match(PRINT);
				}
				break;
			case EXEC:
				enterOuterAlt(_localctx, 8);
				{
				setState(725);
				match(EXEC);
				}
				break;
			case MINUS:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case IMAG_NUMBER:
			case FLOAT_NUMBER:
				enterOuterAlt(_localctx, 9);
				{
				setState(727);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==MINUS) {
					{
					setState(726);
					match(MINUS);
					}
				}

				setState(729);
				number();
				}
				break;
			case NONE:
				enterOuterAlt(_localctx, 10);
				{
				setState(730);
				match(NONE);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 11);
				{
				setState(732); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(731);
						match(STRING);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(734); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,108,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DictorsetmakerContext extends ParserRuleContext {
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public List<TerminalNode> COLON() { return getTokens(PythonParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(PythonParser.COLON, i);
		}
		public List<TerminalNode> POWER() { return getTokens(PythonParser.POWER); }
		public TerminalNode POWER(int i) {
			return getToken(PythonParser.POWER, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public Comp_forContext comp_for() {
			return getRuleContext(Comp_forContext.class,0);
		}
		public Testlist_compContext testlist_comp() {
			return getRuleContext(Testlist_compContext.class,0);
		}
		public DictorsetmakerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dictorsetmaker; }
	}

	public final DictorsetmakerContext dictorsetmaker() throws RecognitionException {
		DictorsetmakerContext _localctx = new DictorsetmakerContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_dictorsetmaker);
		int _la;
		try {
			int _alt;
			setState(769);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,114,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(744);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case NONE:
				case LAMBDA:
				case NOT:
				case AWAIT:
				case PRINT:
				case EXEC:
				case TRUE:
				case FALSE:
				case ELLIPSIS:
				case REVERSE_QUOTE:
				case ADD:
				case MINUS:
				case NOT_OP:
				case STRING:
				case DECIMAL_INTEGER:
				case OCT_INTEGER:
				case HEX_INTEGER:
				case BIN_INTEGER:
				case IMAG_NUMBER:
				case FLOAT_NUMBER:
				case OPEN_PAREN:
				case OPEN_BRACE:
				case OPEN_BRACKET:
				case NAME:
					{
					setState(738);
					test();
					setState(739);
					match(COLON);
					setState(740);
					test();
					}
					break;
				case POWER:
					{
					setState(742);
					match(POWER);
					setState(743);
					expr(0);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(757);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,112,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(746);
						match(COMMA);
						setState(753);
						_errHandler.sync(this);
						switch (_input.LA(1)) {
						case NONE:
						case LAMBDA:
						case NOT:
						case AWAIT:
						case PRINT:
						case EXEC:
						case TRUE:
						case FALSE:
						case ELLIPSIS:
						case REVERSE_QUOTE:
						case ADD:
						case MINUS:
						case NOT_OP:
						case STRING:
						case DECIMAL_INTEGER:
						case OCT_INTEGER:
						case HEX_INTEGER:
						case BIN_INTEGER:
						case IMAG_NUMBER:
						case FLOAT_NUMBER:
						case OPEN_PAREN:
						case OPEN_BRACE:
						case OPEN_BRACKET:
						case NAME:
							{
							setState(747);
							test();
							setState(748);
							match(COLON);
							setState(749);
							test();
							}
							break;
						case POWER:
							{
							setState(751);
							match(POWER);
							setState(752);
							expr(0);
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						}
						} 
					}
					setState(759);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,112,_ctx);
				}
				setState(761);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(760);
					match(COMMA);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(763);
				test();
				setState(764);
				match(COLON);
				setState(765);
				test();
				setState(766);
				comp_for();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(768);
				testlist_comp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Testlist_compContext extends ParserRuleContext {
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public List<Star_exprContext> star_expr() {
			return getRuleContexts(Star_exprContext.class);
		}
		public Star_exprContext star_expr(int i) {
			return getRuleContext(Star_exprContext.class,i);
		}
		public Comp_forContext comp_for() {
			return getRuleContext(Comp_forContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public Testlist_compContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_testlist_comp; }
	}

	public final Testlist_compContext testlist_comp() throws RecognitionException {
		Testlist_compContext _localctx = new Testlist_compContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_testlist_comp);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(773);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NONE:
			case LAMBDA:
			case NOT:
			case AWAIT:
			case PRINT:
			case EXEC:
			case TRUE:
			case FALSE:
			case ELLIPSIS:
			case REVERSE_QUOTE:
			case ADD:
			case MINUS:
			case NOT_OP:
			case STRING:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case IMAG_NUMBER:
			case FLOAT_NUMBER:
			case OPEN_PAREN:
			case OPEN_BRACE:
			case OPEN_BRACKET:
			case NAME:
				{
				setState(771);
				test();
				}
				break;
			case STAR:
				{
				setState(772);
				star_expr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(789);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FOR:
				{
				setState(775);
				comp_for();
				}
				break;
			case COMMA:
			case CLOSE_PAREN:
			case CLOSE_BRACE:
			case CLOSE_BRACKET:
				{
				setState(783);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,117,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(776);
						match(COMMA);
						setState(779);
						_errHandler.sync(this);
						switch (_input.LA(1)) {
						case NONE:
						case LAMBDA:
						case NOT:
						case AWAIT:
						case PRINT:
						case EXEC:
						case TRUE:
						case FALSE:
						case ELLIPSIS:
						case REVERSE_QUOTE:
						case ADD:
						case MINUS:
						case NOT_OP:
						case STRING:
						case DECIMAL_INTEGER:
						case OCT_INTEGER:
						case HEX_INTEGER:
						case BIN_INTEGER:
						case IMAG_NUMBER:
						case FLOAT_NUMBER:
						case OPEN_PAREN:
						case OPEN_BRACE:
						case OPEN_BRACKET:
						case NAME:
							{
							setState(777);
							test();
							}
							break;
						case STAR:
							{
							setState(778);
							star_expr();
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						}
						} 
					}
					setState(785);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,117,_ctx);
				}
				setState(787);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(786);
					match(COMMA);
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TestlistContext extends ParserRuleContext {
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public TestlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_testlist; }
	}

	public final TestlistContext testlist() throws RecognitionException {
		TestlistContext _localctx = new TestlistContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_testlist);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(791);
			test();
			setState(796);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,120,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(792);
					match(COMMA);
					setState(793);
					test();
					}
					} 
				}
				setState(798);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,120,_ctx);
			}
			setState(800);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,121,_ctx) ) {
			case 1:
				{
				setState(799);
				match(COMMA);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Dotted_nameContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Dotted_nameContext dotted_name() {
			return getRuleContext(Dotted_nameContext.class,0);
		}
		public TerminalNode DOT() { return getToken(PythonParser.DOT, 0); }
		public Dotted_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dotted_name; }
	}

	public final Dotted_nameContext dotted_name() throws RecognitionException {
		return dotted_name(0);
	}

	private Dotted_nameContext dotted_name(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Dotted_nameContext _localctx = new Dotted_nameContext(_ctx, _parentState);
		Dotted_nameContext _prevctx = _localctx;
		int _startState = 88;
		enterRecursionRule(_localctx, 88, RULE_dotted_name, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(803);
			name();
			}
			_ctx.stop = _input.LT(-1);
			setState(810);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,122,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Dotted_nameContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_dotted_name);
					setState(805);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(806);
					match(DOT);
					setState(807);
					name();
					}
					} 
				}
				setState(812);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,122,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class NameContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(PythonParser.NAME, 0); }
		public TerminalNode TRUE() { return getToken(PythonParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(PythonParser.FALSE, 0); }
		public NameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_name; }
	}

	public final NameContext name() throws RecognitionException {
		NameContext _localctx = new NameContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(813);
			_la = _input.LA(1);
			if ( !(_la==TRUE || _la==FALSE || _la==NAME) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumberContext extends ParserRuleContext {
		public IntegerContext integer() {
			return getRuleContext(IntegerContext.class,0);
		}
		public TerminalNode IMAG_NUMBER() { return getToken(PythonParser.IMAG_NUMBER, 0); }
		public TerminalNode FLOAT_NUMBER() { return getToken(PythonParser.FLOAT_NUMBER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_number);
		try {
			setState(818);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(815);
				integer();
				}
				break;
			case IMAG_NUMBER:
				enterOuterAlt(_localctx, 2);
				{
				setState(816);
				match(IMAG_NUMBER);
				}
				break;
			case FLOAT_NUMBER:
				enterOuterAlt(_localctx, 3);
				{
				setState(817);
				match(FLOAT_NUMBER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntegerContext extends ParserRuleContext {
		public TerminalNode DECIMAL_INTEGER() { return getToken(PythonParser.DECIMAL_INTEGER, 0); }
		public TerminalNode OCT_INTEGER() { return getToken(PythonParser.OCT_INTEGER, 0); }
		public TerminalNode HEX_INTEGER() { return getToken(PythonParser.HEX_INTEGER, 0); }
		public TerminalNode BIN_INTEGER() { return getToken(PythonParser.BIN_INTEGER, 0); }
		public IntegerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_integer; }
	}

	public final IntegerContext integer() throws RecognitionException {
		IntegerContext _localctx = new IntegerContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_integer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(820);
			_la = _input.LA(1);
			if ( !(((((_la - 93)) & ~0x3f) == 0 && ((1L << (_la - 93)) & ((1L << (DECIMAL_INTEGER - 93)) | (1L << (OCT_INTEGER - 93)) | (1L << (HEX_INTEGER - 93)) | (1L << (BIN_INTEGER - 93)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Yield_exprContext extends ParserRuleContext {
		public TerminalNode YIELD() { return getToken(PythonParser.YIELD, 0); }
		public Yield_argContext yield_arg() {
			return getRuleContext(Yield_argContext.class,0);
		}
		public Yield_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_yield_expr; }
	}

	public final Yield_exprContext yield_expr() throws RecognitionException {
		Yield_exprContext _localctx = new Yield_exprContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_yield_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(822);
			match(YIELD);
			setState(824);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,124,_ctx) ) {
			case 1:
				{
				setState(823);
				yield_arg();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Yield_argContext extends ParserRuleContext {
		public TerminalNode FROM() { return getToken(PythonParser.FROM, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public TestlistContext testlist() {
			return getRuleContext(TestlistContext.class,0);
		}
		public Yield_argContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_yield_arg; }
	}

	public final Yield_argContext yield_arg() throws RecognitionException {
		Yield_argContext _localctx = new Yield_argContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_yield_arg);
		try {
			setState(829);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FROM:
				enterOuterAlt(_localctx, 1);
				{
				setState(826);
				match(FROM);
				setState(827);
				test();
				}
				break;
			case NONE:
			case LAMBDA:
			case NOT:
			case AWAIT:
			case PRINT:
			case EXEC:
			case TRUE:
			case FALSE:
			case ELLIPSIS:
			case REVERSE_QUOTE:
			case ADD:
			case MINUS:
			case NOT_OP:
			case STRING:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case IMAG_NUMBER:
			case FLOAT_NUMBER:
			case OPEN_PAREN:
			case OPEN_BRACE:
			case OPEN_BRACKET:
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(828);
				testlist();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TrailerContext extends ParserRuleContext {
		public TerminalNode DOT() { return getToken(PythonParser.DOT, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public Quantum_gates_definitionContext quantum_gates_definition() {
			return getRuleContext(Quantum_gates_definitionContext.class,0);
		}
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public TrailerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_trailer; }
	}

	public final TrailerContext trailer() throws RecognitionException {
		TrailerContext _localctx = new TrailerContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_trailer);
		try {
			setState(840);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(831);
				match(DOT);
				setState(834);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case TRUE:
				case FALSE:
				case NAME:
					{
					setState(832);
					name();
					}
					break;
				case HADAMARD:
				case CONTROLLEDX:
				case MEASURE:
				case Z:
				case S:
				case T:
				case Y:
				case SWAP:
				case X:
					{
					setState(833);
					quantum_gates_definition();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(837);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,127,_ctx) ) {
				case 1:
					{
					setState(836);
					arguments();
					}
					break;
				}
				}
				break;
			case OPEN_PAREN:
			case OPEN_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				setState(839);
				arguments();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentsContext extends ParserRuleContext {
		public TerminalNode OPEN_PAREN() { return getToken(PythonParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(PythonParser.CLOSE_PAREN, 0); }
		public ArglistContext arglist() {
			return getRuleContext(ArglistContext.class,0);
		}
		public TerminalNode OPEN_BRACKET() { return getToken(PythonParser.OPEN_BRACKET, 0); }
		public SubscriptlistContext subscriptlist() {
			return getRuleContext(SubscriptlistContext.class,0);
		}
		public TerminalNode CLOSE_BRACKET() { return getToken(PythonParser.CLOSE_BRACKET, 0); }
		public ArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arguments; }
	}

	public final ArgumentsContext arguments() throws RecognitionException {
		ArgumentsContext _localctx = new ArgumentsContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_arguments);
		int _la;
		try {
			setState(851);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(842);
				match(OPEN_PAREN);
				setState(844);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NONE) | (1L << LAMBDA) | (1L << NOT) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE) | (1L << STAR) | (1L << POWER))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0)) {
					{
					setState(843);
					arglist();
					}
				}

				setState(846);
				match(CLOSE_PAREN);
				}
				break;
			case OPEN_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				setState(847);
				match(OPEN_BRACKET);
				setState(848);
				subscriptlist();
				setState(849);
				match(CLOSE_BRACKET);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArglistContext extends ParserRuleContext {
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public ArglistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arglist; }
	}

	public final ArglistContext arglist() throws RecognitionException {
		ArglistContext _localctx = new ArglistContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_arglist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(853);
			argument();
			setState(858);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,131,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(854);
					match(COMMA);
					setState(855);
					argument();
					}
					} 
				}
				setState(860);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,131,_ctx);
			}
			setState(862);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(861);
				match(COMMA);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentContext extends ParserRuleContext {
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public Comp_forContext comp_for() {
			return getRuleContext(Comp_forContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(PythonParser.ASSIGN, 0); }
		public TerminalNode POWER() { return getToken(PythonParser.POWER, 0); }
		public TerminalNode STAR() { return getToken(PythonParser.STAR, 0); }
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_argument);
		int _la;
		try {
			setState(872);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NONE:
			case LAMBDA:
			case NOT:
			case AWAIT:
			case PRINT:
			case EXEC:
			case TRUE:
			case FALSE:
			case ELLIPSIS:
			case REVERSE_QUOTE:
			case ADD:
			case MINUS:
			case NOT_OP:
			case STRING:
			case DECIMAL_INTEGER:
			case OCT_INTEGER:
			case HEX_INTEGER:
			case BIN_INTEGER:
			case IMAG_NUMBER:
			case FLOAT_NUMBER:
			case OPEN_PAREN:
			case OPEN_BRACE:
			case OPEN_BRACKET:
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(864);
				test();
				setState(868);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case FOR:
					{
					setState(865);
					comp_for();
					}
					break;
				case ASSIGN:
					{
					setState(866);
					match(ASSIGN);
					setState(867);
					test();
					}
					break;
				case COMMA:
				case CLOSE_PAREN:
					break;
				default:
					break;
				}
				}
				break;
			case STAR:
			case POWER:
				enterOuterAlt(_localctx, 2);
				{
				setState(870);
				_la = _input.LA(1);
				if ( !(_la==STAR || _la==POWER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(871);
				test();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubscriptlistContext extends ParserRuleContext {
		public List<SubscriptContext> subscript() {
			return getRuleContexts(SubscriptContext.class);
		}
		public SubscriptContext subscript(int i) {
			return getRuleContext(SubscriptContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonParser.COMMA, i);
		}
		public SubscriptlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subscriptlist; }
	}

	public final SubscriptlistContext subscriptlist() throws RecognitionException {
		SubscriptlistContext _localctx = new SubscriptlistContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_subscriptlist);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(874);
			subscript();
			setState(879);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,135,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(875);
					match(COMMA);
					setState(876);
					subscript();
					}
					} 
				}
				setState(881);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,135,_ctx);
			}
			setState(883);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(882);
				match(COMMA);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubscriptContext extends ParserRuleContext {
		public TerminalNode ELLIPSIS() { return getToken(PythonParser.ELLIPSIS, 0); }
		public List<TestContext> test() {
			return getRuleContexts(TestContext.class);
		}
		public TestContext test(int i) {
			return getRuleContext(TestContext.class,i);
		}
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public SliceopContext sliceop() {
			return getRuleContext(SliceopContext.class,0);
		}
		public SubscriptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subscript; }
	}

	public final SubscriptContext subscript() throws RecognitionException {
		SubscriptContext _localctx = new SubscriptContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_subscript);
		int _la;
		try {
			setState(903);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,142,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(885);
				match(ELLIPSIS);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(886);
				test();
				setState(894);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COLON) {
					{
					setState(887);
					match(COLON);
					setState(889);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NONE) | (1L << LAMBDA) | (1L << NOT) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0)) {
						{
						setState(888);
						test();
						}
					}

					setState(892);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==COLON) {
						{
						setState(891);
						sliceop();
						}
					}

					}
				}

				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(896);
				match(COLON);
				setState(898);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NONE) | (1L << LAMBDA) | (1L << NOT) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0)) {
					{
					setState(897);
					test();
					}
				}

				setState(901);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COLON) {
					{
					setState(900);
					sliceop();
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SliceopContext extends ParserRuleContext {
		public TerminalNode COLON() { return getToken(PythonParser.COLON, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public SliceopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sliceop; }
	}

	public final SliceopContext sliceop() throws RecognitionException {
		SliceopContext _localctx = new SliceopContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_sliceop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(905);
			match(COLON);
			setState(907);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NONE) | (1L << LAMBDA) | (1L << NOT) | (1L << AWAIT) | (1L << PRINT) | (1L << EXEC) | (1L << TRUE) | (1L << FALSE) | (1L << ELLIPSIS) | (1L << REVERSE_QUOTE))) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & ((1L << (ADD - 64)) | (1L << (MINUS - 64)) | (1L << (NOT_OP - 64)) | (1L << (STRING - 64)) | (1L << (DECIMAL_INTEGER - 64)) | (1L << (OCT_INTEGER - 64)) | (1L << (HEX_INTEGER - 64)) | (1L << (BIN_INTEGER - 64)) | (1L << (IMAG_NUMBER - 64)) | (1L << (FLOAT_NUMBER - 64)) | (1L << (OPEN_PAREN - 64)) | (1L << (OPEN_BRACE - 64)) | (1L << (OPEN_BRACKET - 64)) | (1L << (NAME - 64)))) != 0)) {
				{
				setState(906);
				test();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Comp_forContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(PythonParser.FOR, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public TerminalNode IN() { return getToken(PythonParser.IN, 0); }
		public Logical_testContext logical_test() {
			return getRuleContext(Logical_testContext.class,0);
		}
		public Comp_iterContext comp_iter() {
			return getRuleContext(Comp_iterContext.class,0);
		}
		public Comp_forContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comp_for; }
	}

	public final Comp_forContext comp_for() throws RecognitionException {
		Comp_forContext _localctx = new Comp_forContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_comp_for);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(909);
			match(FOR);
			setState(910);
			exprlist();
			setState(911);
			match(IN);
			setState(912);
			logical_test(0);
			setState(914);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IF || _la==FOR) {
				{
				setState(913);
				comp_iter();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Comp_iterContext extends ParserRuleContext {
		public Comp_forContext comp_for() {
			return getRuleContext(Comp_forContext.class,0);
		}
		public TerminalNode IF() { return getToken(PythonParser.IF, 0); }
		public TestContext test() {
			return getRuleContext(TestContext.class,0);
		}
		public Comp_iterContext comp_iter() {
			return getRuleContext(Comp_iterContext.class,0);
		}
		public Comp_iterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comp_iter; }
	}

	public final Comp_iterContext comp_iter() throws RecognitionException {
		Comp_iterContext _localctx = new Comp_iterContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_comp_iter);
		int _la;
		try {
			setState(922);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FOR:
				enterOuterAlt(_localctx, 1);
				{
				setState(916);
				comp_for();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 2);
				{
				setState(917);
				match(IF);
				setState(918);
				test();
				setState(920);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==IF || _la==FOR) {
					{
					setState(919);
					comp_iter();
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Quantum_gates_definitionContext extends ParserRuleContext {
		public TerminalNode HADAMARD() { return getToken(PythonParser.HADAMARD, 0); }
		public TerminalNode MEASURE() { return getToken(PythonParser.MEASURE, 0); }
		public TerminalNode CONTROLLEDX() { return getToken(PythonParser.CONTROLLEDX, 0); }
		public TerminalNode Z() { return getToken(PythonParser.Z, 0); }
		public TerminalNode S() { return getToken(PythonParser.S, 0); }
		public TerminalNode T() { return getToken(PythonParser.T, 0); }
		public TerminalNode Y() { return getToken(PythonParser.Y, 0); }
		public TerminalNode SWAP() { return getToken(PythonParser.SWAP, 0); }
		public TerminalNode X() { return getToken(PythonParser.X, 0); }
		public Quantum_gates_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_quantum_gates_definition; }
	}

	public final Quantum_gates_definitionContext quantum_gates_definition() throws RecognitionException {
		Quantum_gates_definitionContext _localctx = new Quantum_gates_definitionContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_quantum_gates_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(924);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << HADAMARD) | (1L << CONTROLLEDX) | (1L << MEASURE) | (1L << Z) | (1L << S) | (1L << T) | (1L << Y) | (1L << SWAP) | (1L << X))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 37:
			return logical_test_sempred((Logical_testContext)_localctx, predIndex);
		case 38:
			return comparison_sempred((ComparisonContext)_localctx, predIndex);
		case 39:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 44:
			return dotted_name_sempred((Dotted_nameContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean logical_test_sempred(Logical_testContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean comparison_sempred(ComparisonContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 8);
		case 4:
			return precpred(_ctx, 6);
		case 5:
			return precpred(_ctx, 5);
		case 6:
			return precpred(_ctx, 4);
		case 7:
			return precpred(_ctx, 3);
		case 8:
			return precpred(_ctx, 2);
		case 9:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean dotted_name_sempred(Dotted_nameContext _localctx, int predIndex) {
		switch (predIndex) {
		case 10:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3o\u03a1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\3\2\3\2\3\2\7\2~\n\2\f\2\16\2\u0081\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3"+
		"\5\3\u008a\n\3\3\4\3\4\6\4\u008e\n\4\r\4\16\4\u008f\3\5\3\5\7\5\u0094"+
		"\n\5\f\5\16\5\u0097\13\5\3\6\3\6\5\6\u009b\n\6\3\7\3\7\3\7\3\7\3\7\7\7"+
		"\u00a2\n\7\f\7\16\7\u00a5\13\7\3\7\5\7\u00a8\n\7\3\7\3\7\3\7\3\7\3\7\5"+
		"\7\u00af\n\7\3\7\5\7\u00b2\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00bb\n"+
		"\7\3\7\3\7\3\7\3\7\6\7\u00c1\n\7\r\7\16\7\u00c2\3\7\5\7\u00c6\n\7\3\7"+
		"\5\7\u00c9\n\7\3\7\5\7\u00cc\n\7\3\7\5\7\u00cf\n\7\3\7\3\7\3\7\3\7\7\7"+
		"\u00d5\n\7\f\7\16\7\u00d8\13\7\3\7\3\7\3\7\3\7\7\7\u00de\n\7\f\7\16\7"+
		"\u00e1\13\7\3\7\3\7\5\7\u00e5\n\7\5\7\u00e7\n\7\3\b\3\b\3\b\3\b\3\b\6"+
		"\b\u00ee\n\b\r\b\16\b\u00ef\3\b\3\b\5\b\u00f4\n\b\3\t\3\t\3\t\3\t\5\t"+
		"\u00fa\n\t\3\t\5\t\u00fd\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13"+
		"\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u0111\n\r\3\16\3\16\3\16\3\16\5"+
		"\16\u0117\n\16\5\16\u0119\n\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17"+
		"\u0122\n\17\3\17\5\17\u0125\n\17\3\17\3\17\3\17\3\20\5\20\u012b\n\20\3"+
		"\20\3\20\3\20\3\20\5\20\u0131\n\20\3\20\3\20\3\20\5\20\u0136\n\20\3\20"+
		"\3\20\3\20\3\21\3\21\3\21\5\21\u013e\n\21\3\21\3\21\3\21\5\21\u0143\n"+
		"\21\3\21\3\21\5\21\u0147\n\21\3\21\5\21\u014a\n\21\3\21\5\21\u014d\n\21"+
		"\3\21\3\21\5\21\u0151\n\21\5\21\u0153\n\21\3\22\3\22\3\22\3\23\3\23\3"+
		"\23\3\24\3\24\3\24\7\24\u015e\n\24\f\24\16\24\u0161\13\24\3\25\3\25\3"+
		"\25\5\25\u0166\n\25\3\25\5\25\u0169\n\25\3\26\3\26\3\26\5\26\u016e\n\26"+
		"\3\27\3\27\3\27\7\27\u0173\n\27\f\27\16\27\u0176\13\27\3\27\5\27\u0179"+
		"\n\27\3\27\5\27\u017c\n\27\3\30\3\30\5\30\u0180\n\30\3\30\3\30\3\30\3"+
		"\30\3\30\3\30\3\30\5\30\u0189\n\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30"+
		"\u0191\n\30\5\30\u0193\n\30\5\30\u0195\n\30\3\30\3\30\5\30\u0199\n\30"+
		"\3\30\3\30\3\30\3\30\3\30\7\30\u01a0\n\30\f\30\16\30\u01a3\13\30\3\30"+
		"\3\30\6\30\u01a7\n\30\r\30\16\30\u01a8\5\30\u01ab\n\30\3\30\3\30\3\30"+
		"\3\30\3\30\3\30\3\30\5\30\u01b4\n\30\3\30\3\30\3\30\3\30\7\30\u01ba\n"+
		"\30\f\30\16\30\u01bd\13\30\3\30\3\30\3\30\3\30\5\30\u01c3\n\30\3\30\3"+
		"\30\3\30\3\30\7\30\u01c9\n\30\f\30\16\30\u01cc\13\30\5\30\u01ce\n\30\3"+
		"\31\3\31\5\31\u01d2\n\31\3\31\3\31\6\31\u01d6\n\31\r\31\16\31\u01d7\3"+
		"\31\3\31\5\31\u01dc\n\31\3\31\5\31\u01df\n\31\3\32\3\32\3\32\3\33\3\33"+
		"\3\33\3\33\7\33\u01e8\n\33\f\33\16\33\u01eb\13\33\3\33\3\33\5\33\u01ef"+
		"\n\33\3\33\5\33\u01f2\n\33\3\33\3\33\3\33\3\33\5\33\u01f8\n\33\3\33\3"+
		"\33\3\33\5\33\u01fd\n\33\5\33\u01ff\n\33\3\34\3\34\3\34\7\34\u0204\n\34"+
		"\f\34\16\34\u0207\13\34\3\34\5\34\u020a\n\34\3\35\3\35\3\35\7\35\u020f"+
		"\n\35\f\35\16\35\u0212\13\35\3\35\5\35\u0215\n\35\3\36\3\36\3\36\5\36"+
		"\u021a\n\36\3\37\3\37\3\37\7\37\u021f\n\37\f\37\16\37\u0222\13\37\3 \3"+
		" \3 \5 \u0227\n \3!\3!\3!\3!\3!\3!\5!\u022f\n!\3!\3!\5!\u0233\n!\3!\3"+
		"!\5!\u0237\n!\3\"\3\"\3\"\5\"\u023c\n\"\3\"\3\"\3\"\5\"\u0241\n\"\3\""+
		"\3\"\5\"\u0245\n\"\3\"\5\"\u0248\n\"\3\"\5\"\u024b\n\"\3\"\3\"\5\"\u024f"+
		"\n\"\5\"\u0251\n\"\3#\3#\3#\7#\u0256\n#\f#\16#\u0259\13#\3$\3$\3$\5$\u025e"+
		"\n$\3$\5$\u0261\n$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\5\'\u026d\n\'\3\'"+
		"\3\'\3\'\3\'\3\'\3\'\7\'\u0275\n\'\f\'\16\'\u0278\13\'\3(\3(\3(\3(\3("+
		"\3(\3(\3(\3(\3(\3(\3(\5(\u0286\n(\3(\3(\3(\5(\u028b\n(\5(\u028d\n(\3("+
		"\7(\u0290\n(\f(\16(\u0293\13(\3)\3)\5)\u0297\n)\3)\3)\7)\u029b\n)\f)\16"+
		")\u029e\13)\3)\3)\5)\u02a2\n)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3"+
		")\3)\3)\3)\3)\3)\3)\3)\7)\u02b9\n)\f)\16)\u02bc\13)\3*\3*\3*\5*\u02c1"+
		"\n*\3*\3*\3*\5*\u02c6\n*\3*\3*\3*\5*\u02cb\n*\3*\3*\3*\3*\5*\u02d1\n*"+
		"\3*\3*\3*\3*\3*\3*\3*\5*\u02da\n*\3*\3*\3*\6*\u02df\n*\r*\16*\u02e0\5"+
		"*\u02e3\n*\3+\3+\3+\3+\3+\3+\5+\u02eb\n+\3+\3+\3+\3+\3+\3+\3+\5+\u02f4"+
		"\n+\7+\u02f6\n+\f+\16+\u02f9\13+\3+\5+\u02fc\n+\3+\3+\3+\3+\3+\3+\5+\u0304"+
		"\n+\3,\3,\5,\u0308\n,\3,\3,\3,\3,\5,\u030e\n,\7,\u0310\n,\f,\16,\u0313"+
		"\13,\3,\5,\u0316\n,\5,\u0318\n,\3-\3-\3-\7-\u031d\n-\f-\16-\u0320\13-"+
		"\3-\5-\u0323\n-\3.\3.\3.\3.\3.\3.\7.\u032b\n.\f.\16.\u032e\13.\3/\3/\3"+
		"\60\3\60\3\60\5\60\u0335\n\60\3\61\3\61\3\62\3\62\5\62\u033b\n\62\3\63"+
		"\3\63\3\63\5\63\u0340\n\63\3\64\3\64\3\64\5\64\u0345\n\64\3\64\5\64\u0348"+
		"\n\64\3\64\5\64\u034b\n\64\3\65\3\65\5\65\u034f\n\65\3\65\3\65\3\65\3"+
		"\65\3\65\5\65\u0356\n\65\3\66\3\66\3\66\7\66\u035b\n\66\f\66\16\66\u035e"+
		"\13\66\3\66\5\66\u0361\n\66\3\67\3\67\3\67\3\67\5\67\u0367\n\67\3\67\3"+
		"\67\5\67\u036b\n\67\38\38\38\78\u0370\n8\f8\168\u0373\138\38\58\u0376"+
		"\n8\39\39\39\39\59\u037c\n9\39\59\u037f\n9\59\u0381\n9\39\39\59\u0385"+
		"\n9\39\59\u0388\n9\59\u038a\n9\3:\3:\5:\u038e\n:\3;\3;\3;\3;\3;\5;\u0395"+
		"\n;\3<\3<\3<\3<\5<\u039b\n<\5<\u039d\n<\3=\3=\3=\2\6LNPZ>\2\4\6\b\n\f"+
		"\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^"+
		"`bdfhjlnprtvx\2\f\3\2\64\65\3\2Q]\4\2BCGG\5\2\67\67DFOO\3\2BC\3\2@A\4"+
		"\2)*kk\3\2_b\4\2\67\67;;\3\2+\63\2\u0426\2\177\3\2\2\2\4\u0089\3\2\2\2"+
		"\6\u008d\3\2\2\2\b\u0091\3\2\2\2\n\u009a\3\2\2\2\f\u00e6\3\2\2\2\16\u00f3"+
		"\3\2\2\2\20\u00f5\3\2\2\2\22\u0100\3\2\2\2\24\u0105\3\2\2\2\26\u0109\3"+
		"\2\2\2\30\u010d\3\2\2\2\32\u0112\3\2\2\2\34\u011d\3\2\2\2\36\u012a\3\2"+
		"\2\2 \u0152\3\2\2\2\"\u0154\3\2\2\2$\u0157\3\2\2\2&\u015a\3\2\2\2(\u0168"+
		"\3\2\2\2*\u016a\3\2\2\2,\u016f\3\2\2\2.\u01cd\3\2\2\2\60\u01de\3\2\2\2"+
		"\62\u01e0\3\2\2\2\64\u01fe\3\2\2\2\66\u0200\3\2\2\28\u020b\3\2\2\2:\u0216"+
		"\3\2\2\2<\u021b\3\2\2\2>\u0223\3\2\2\2@\u0236\3\2\2\2B\u0250\3\2\2\2D"+
		"\u0252\3\2\2\2F\u0260\3\2\2\2H\u0262\3\2\2\2J\u0265\3\2\2\2L\u026c\3\2"+
		"\2\2N\u0279\3\2\2\2P\u02a1\3\2\2\2R\u02e2\3\2\2\2T\u0303\3\2\2\2V\u0307"+
		"\3\2\2\2X\u0319\3\2\2\2Z\u0324\3\2\2\2\\\u032f\3\2\2\2^\u0334\3\2\2\2"+
		"`\u0336\3\2\2\2b\u0338\3\2\2\2d\u033f\3\2\2\2f\u034a\3\2\2\2h\u0355\3"+
		"\2\2\2j\u0357\3\2\2\2l\u036a\3\2\2\2n\u036c\3\2\2\2p\u0389\3\2\2\2r\u038b"+
		"\3\2\2\2t\u038f\3\2\2\2v\u039c\3\2\2\2x\u039e\3\2\2\2z~\5\4\3\2{~\5\6"+
		"\4\2|~\5\b\5\2}z\3\2\2\2}{\3\2\2\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2"+
		"\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083"+
		"\7\2\2\3\u0083\3\3\2\2\2\u0084\u008a\7\5\2\2\u0085\u008a\5,\27\2\u0086"+
		"\u0087\5\f\7\2\u0087\u0088\7\5\2\2\u0088\u008a\3\2\2\2\u0089\u0084\3\2"+
		"\2\2\u0089\u0085\3\2\2\2\u0089\u0086\3\2\2\2\u008a\5\3\2\2\2\u008b\u008e"+
		"\7\5\2\2\u008c\u008e\5\n\6\2\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e"+
		"\u008f\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\7\3\2\2\2"+
		"\u0091\u0095\5X-\2\u0092\u0094\7\5\2\2\u0093\u0092\3\2\2\2\u0094\u0097"+
		"\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\t\3\2\2\2\u0097"+
		"\u0095\3\2\2\2\u0098\u009b\5,\27\2\u0099\u009b\5\f\7\2\u009a\u0098\3\2"+
		"\2\2\u009a\u0099\3\2\2\2\u009b\13\3\2\2\2\u009c\u009d\7\17\2\2\u009d\u009e"+
		"\5@!\2\u009e\u009f\79\2\2\u009f\u00a3\5\16\b\2\u00a0\u00a2\5\22\n\2\u00a1"+
		"\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2"+
		"\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a8\5\24\13\2\u00a7"+
		"\u00a6\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00e7\3\2\2\2\u00a9\u00aa\7\22"+
		"\2\2\u00aa\u00ab\5@!\2\u00ab\u00ac\79\2\2\u00ac\u00ae\5\16\b\2\u00ad\u00af"+
		"\5\24\13\2\u00ae\u00ad\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00e7\3\2\2\2"+
		"\u00b0\u00b2\7%\2\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3"+
		"\3\2\2\2\u00b3\u00b4\7\23\2\2\u00b4\u00b5\5\66\34\2\u00b5\u00b6\7\24\2"+
		"\2\u00b6\u00b7\5X-\2\u00b7\u00b8\79\2\2\u00b8\u00ba\5\16\b\2\u00b9\u00bb"+
		"\5\24\13\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00e7\3\2\2\2"+
		"\u00bc\u00bd\7\25\2\2\u00bd\u00be\79\2\2\u00be\u00cb\5\16\b\2\u00bf\u00c1"+
		"\5\32\16\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c0\3\2\2\2"+
		"\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00c6\5\24\13\2\u00c5\u00c4"+
		"\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00c9\5\26\f\2"+
		"\u00c8\u00c7\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00cc"+
		"\5\26\f\2\u00cb\u00c0\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00e7\3\2\2\2"+
		"\u00cd\u00cf\7%\2\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0"+
		"\3\2\2\2\u00d0\u00d1\7\30\2\2\u00d1\u00d6\5\30\r\2\u00d2\u00d3\78\2\2"+
		"\u00d3\u00d5\5\30\r\2\u00d4\u00d2\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4"+
		"\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9"+
		"\u00da\79\2\2\u00da\u00db\5\16\b\2\u00db\u00e7\3\2\2\2\u00dc\u00de\5\20"+
		"\t\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df"+
		"\u00e0\3\2\2\2\u00e0\u00e4\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e5\5\34"+
		"\17\2\u00e3\u00e5\5\36\20\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5"+
		"\u00e7\3\2\2\2\u00e6\u009c\3\2\2\2\u00e6\u00a9\3\2\2\2\u00e6\u00b1\3\2"+
		"\2\2\u00e6\u00bc\3\2\2\2\u00e6\u00ce\3\2\2\2\u00e6\u00df\3\2\2\2\u00e7"+
		"\r\3\2\2\2\u00e8\u00f4\5,\27\2\u00e9\u00f4\5\f\7\2\u00ea\u00eb\7\5\2\2"+
		"\u00eb\u00ed\7\3\2\2\u00ec\u00ee\5\n\6\2\u00ed\u00ec\3\2\2\2\u00ee\u00ef"+
		"\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1"+
		"\u00f2\7\4\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00e8\3\2\2\2\u00f3\u00e9\3\2"+
		"\2\2\u00f3\u00ea\3\2\2\2\u00f4\17\3\2\2\2\u00f5\u00f6\7O\2\2\u00f6\u00fc"+
		"\5Z.\2\u00f7\u00f9\7e\2\2\u00f8\u00fa\5j\66\2\u00f9\u00f8\3\2\2\2\u00f9"+
		"\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fd\7f\2\2\u00fc\u00f7\3\2"+
		"\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\7\5\2\2\u00ff"+
		"\21\3\2\2\2\u0100\u0101\7\20\2\2\u0101\u0102\5@!\2\u0102\u0103\79\2\2"+
		"\u0103\u0104\5\16\b\2\u0104\23\3\2\2\2\u0105\u0106\7\21\2\2\u0106\u0107"+
		"\79\2\2\u0107\u0108\5\16\b\2\u0108\25\3\2\2\2\u0109\u010a\7\27\2\2\u010a"+
		"\u010b\79\2\2\u010b\u010c\5\16\b\2\u010c\27\3\2\2\2\u010d\u0110\5@!\2"+
		"\u010e\u010f\7\f\2\2\u010f\u0111\5P)\2\u0110\u010e\3\2\2\2\u0110\u0111"+
		"\3\2\2\2\u0111\31\3\2\2\2\u0112\u0118\7\31\2\2\u0113\u0116\5@!\2\u0114"+
		"\u0115\7\f\2\2\u0115\u0117\5\\/\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2"+
		"\2\2\u0117\u0119\3\2\2\2\u0118\u0113\3\2\2\2\u0118\u0119\3\2\2\2\u0119"+
		"\u011a\3\2\2\2\u011a\u011b\79\2\2\u011b\u011c\5\16\b\2\u011c\33\3\2\2"+
		"\2\u011d\u011e\7\37\2\2\u011e\u0124\5\\/\2\u011f\u0121\7e\2\2\u0120\u0122"+
		"\5j\66\2\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\3\2\2\2\u0123"+
		"\u0125\7f\2\2\u0124\u011f\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126\3\2"+
		"\2\2\u0126\u0127\79\2\2\u0127\u0128\5\16\b\2\u0128\35\3\2\2\2\u0129\u012b"+
		"\7%\2\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c"+
		"\u012d\7\6\2\2\u012d\u012e\5\\/\2\u012e\u0130\7e\2\2\u012f\u0131\5 \21"+
		"\2\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0135"+
		"\7f\2\2\u0133\u0134\7P\2\2\u0134\u0136\5@!\2\u0135\u0133\3\2\2\2\u0135"+
		"\u0136\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\79\2\2\u0138\u0139\5\16"+
		"\b\2\u0139\37\3\2\2\2\u013a\u013b\5&\24\2\u013b\u013c\78\2\2\u013c\u013e"+
		"\3\2\2\2\u013d\u013a\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0149\3\2\2\2\u013f"+
		"\u0142\5\"\22\2\u0140\u0141\78\2\2\u0141\u0143\5&\24\2\u0142\u0140\3\2"+
		"\2\2\u0142\u0143\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0145\78\2\2\u0145"+
		"\u0147\5$\23\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u014a\3\2"+
		"\2\2\u0148\u014a\5$\23\2\u0149\u013f\3\2\2\2\u0149\u0148\3\2\2\2\u014a"+
		"\u014c\3\2\2\2\u014b\u014d\78\2\2\u014c\u014b\3\2\2\2\u014c\u014d\3\2"+
		"\2\2\u014d\u0153\3\2\2\2\u014e\u0150\5&\24\2\u014f\u0151\78\2\2\u0150"+
		"\u014f\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u013d\3\2"+
		"\2\2\u0152\u014e\3\2\2\2\u0153!\3\2\2\2\u0154\u0155\7\67\2\2\u0155\u0156"+
		"\5*\26\2\u0156#\3\2\2\2\u0157\u0158\7;\2\2\u0158\u0159\5*\26\2\u0159%"+
		"\3\2\2\2\u015a\u015f\5(\25\2\u015b\u015c\78\2\2\u015c\u015e\5(\25\2\u015d"+
		"\u015b\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2"+
		"\2\2\u0160\'\3\2\2\2\u0161\u015f\3\2\2\2\u0162\u0165\5*\26\2\u0163\u0164"+
		"\7<\2\2\u0164\u0166\5@!\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166"+
		"\u0169\3\2\2\2\u0167\u0169\7\67\2\2\u0168\u0162\3\2\2\2\u0168\u0167\3"+
		"\2\2\2\u0169)\3\2\2\2\u016a\u016d\5\\/\2\u016b\u016c\79\2\2\u016c\u016e"+
		"\5@!\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e+\3\2\2\2\u016f\u0174"+
		"\5.\30\2\u0170\u0171\7:\2\2\u0171\u0173\5.\30\2\u0172\u0170\3\2\2\2\u0173"+
		"\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0178\3\2"+
		"\2\2\u0176\u0174\3\2\2\2\u0177\u0179\7:\2\2\u0178\u0177\3\2\2\2\u0178"+
		"\u0179\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u017c\7\5\2\2\u017b\u017a\3\2"+
		"\2\2\u017b\u017c\3\2\2\2\u017c-\3\2\2\2\u017d\u017f\5\60\31\2\u017e\u0180"+
		"\5\64\33\2\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u01ce\3\2\2\2"+
		"\u0181\u0182\7!\2\2\u0182\u01ce\5\66\34\2\u0183\u01ce\7\"\2\2\u0184\u01ce"+
		"\7$\2\2\u0185\u01ce\7#\2\2\u0186\u0188\7\7\2\2\u0187\u0189\5X-\2\u0188"+
		"\u0187\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u01ce\3\2\2\2\u018a\u0194\7\b"+
		"\2\2\u018b\u0192\5@!\2\u018c\u018d\78\2\2\u018d\u0190\5@!\2\u018e\u018f"+
		"\78\2\2\u018f\u0191\5@!\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191"+
		"\u0193\3\2\2\2\u0192\u018c\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195\3\2"+
		"\2\2\u0194\u018b\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0198\3\2\2\2\u0196"+
		"\u0197\7\t\2\2\u0197\u0199\5@!\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2"+
		"\2\u0199\u01ce\3\2\2\2\u019a\u01ce\5b\62\2\u019b\u019c\7\n\2\2\u019c\u01ce"+
		"\5<\37\2\u019d\u01aa\7\t\2\2\u019e\u01a0\t\2\2\2\u019f\u019e\3\2\2\2\u01a0"+
		"\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2"+
		"\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01ab\5Z.\2\u01a5\u01a7\t\2\2\2\u01a6\u01a5"+
		"\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9"+
		"\u01ab\3\2\2\2\u01aa\u01a1\3\2\2\2\u01aa\u01a6\3\2\2\2\u01ab\u01ac\3\2"+
		"\2\2\u01ac\u01b3\7\n\2\2\u01ad\u01b4\7\67\2\2\u01ae\u01af\7e\2\2\u01af"+
		"\u01b0\58\35\2\u01b0\u01b1\7f\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b4\58\35"+
		"\2\u01b3\u01ad\3\2\2\2\u01b3\u01ae\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01ce"+
		"\3\2\2\2\u01b5\u01b6\7\r\2\2\u01b6\u01bb\5\\/\2\u01b7\u01b8\78\2\2\u01b8"+
		"\u01ba\5\\/\2\u01b9\u01b7\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2"+
		"\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01ce\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be"+
		"\u01bf\7\16\2\2\u01bf\u01c2\5@!\2\u01c0\u01c1\78\2\2\u01c1\u01c3\5@!\2"+
		"\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01ce\3\2\2\2\u01c4\u01c5"+
		"\7\13\2\2\u01c5\u01ca\5\\/\2\u01c6\u01c7\78\2\2\u01c7\u01c9\5\\/\2\u01c8"+
		"\u01c6\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2"+
		"\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u017d\3\2\2\2\u01cd"+
		"\u0181\3\2\2\2\u01cd\u0183\3\2\2\2\u01cd\u0184\3\2\2\2\u01cd\u0185\3\2"+
		"\2\2\u01cd\u0186\3\2\2\2\u01cd\u018a\3\2\2\2\u01cd\u019a\3\2\2\2\u01cd"+
		"\u019b\3\2\2\2\u01cd\u019d\3\2\2\2\u01cd\u01b5\3\2\2\2\u01cd\u01be\3\2"+
		"\2\2\u01cd\u01c4\3\2\2\2\u01ce/\3\2\2\2\u01cf\u01d2\5@!\2\u01d0\u01d2"+
		"\5\62\32\2\u01d1\u01cf\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2"+
		"\u01d3\u01d4\78\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01d1\3\2\2\2\u01d6\u01d7"+
		"\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9"+
		"\u01dc\5@!\2\u01da\u01dc\5\62\32\2\u01db\u01d9\3\2\2\2\u01db\u01da\3\2"+
		"\2\2\u01db\u01dc\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01df\5X-\2\u01de\u01d5"+
		"\3\2\2\2\u01de\u01dd\3\2\2\2\u01df\61\3\2\2\2\u01e0\u01e1\7\67\2\2\u01e1"+
		"\u01e2\5P)\2\u01e2\63\3\2\2\2\u01e3\u01f1\7<\2\2\u01e4\u01e9\5\60\31\2"+
		"\u01e5\u01e6\7<\2\2\u01e6\u01e8\5\60\31\2\u01e7\u01e5\3\2\2\2\u01e8\u01eb"+
		"\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01ee\3\2\2\2\u01eb"+
		"\u01e9\3\2\2\2\u01ec\u01ed\7<\2\2\u01ed\u01ef\5b\62\2\u01ee\u01ec\3\2"+
		"\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01f2\5b\62\2\u01f1"+
		"\u01e4\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01ff\3\2\2\2\u01f3\u01f4\79"+
		"\2\2\u01f4\u01f7\5@!\2\u01f5\u01f6\7<\2\2\u01f6\u01f8\5X-\2\u01f7\u01f5"+
		"\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01ff\3\2\2\2\u01f9\u01fc\t\3\2\2\u01fa"+
		"\u01fd\5b\62\2\u01fb\u01fd\5X-\2\u01fc\u01fa\3\2\2\2\u01fc\u01fb\3\2\2"+
		"\2\u01fd\u01ff\3\2\2\2\u01fe\u01e3\3\2\2\2\u01fe\u01f3\3\2\2\2\u01fe\u01f9"+
		"\3\2\2\2\u01ff\65\3\2\2\2\u0200\u0205\5P)\2\u0201\u0202\78\2\2\u0202\u0204"+
		"\5P)\2\u0203\u0201\3\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205"+
		"\u0206\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u020a\78"+
		"\2\2\u0209\u0208\3\2\2\2\u0209\u020a\3\2\2\2\u020a\67\3\2\2\2\u020b\u0210"+
		"\5:\36\2\u020c\u020d\78\2\2\u020d\u020f\5:\36\2\u020e\u020c\3\2\2\2\u020f"+
		"\u0212\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0214\3\2"+
		"\2\2\u0212\u0210\3\2\2\2\u0213\u0215\78\2\2\u0214\u0213\3\2\2\2\u0214"+
		"\u0215\3\2\2\2\u02159\3\2\2\2\u0216\u0219\5\\/\2\u0217\u0218\7\f\2\2\u0218"+
		"\u021a\5\\/\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021a;\3\2\2\2\u021b"+
		"\u0220\5> \2\u021c\u021d\78\2\2\u021d\u021f\5> \2\u021e\u021c\3\2\2\2"+
		"\u021f\u0222\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u0221\3\2\2\2\u0221=\3"+
		"\2\2\2\u0222\u0220\3\2\2\2\u0223\u0226\5Z.\2\u0224\u0225\7\f\2\2\u0225"+
		"\u0227\5\\/\2\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227?\3\2\2\2\u0228"+
		"\u022e\5L\'\2\u0229\u022a\7\17\2\2\u022a\u022b\5L\'\2\u022b\u022c\7\21"+
		"\2\2\u022c\u022d\5@!\2\u022d\u022f\3\2\2\2\u022e\u0229\3\2\2\2\u022e\u022f"+
		"\3\2\2\2\u022f\u0237\3\2\2\2\u0230\u0232\7\32\2\2\u0231\u0233\5B\"\2\u0232"+
		"\u0231\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235\79"+
		"\2\2\u0235\u0237\5@!\2\u0236\u0228\3\2\2\2\u0236\u0230\3\2\2\2\u0237A"+
		"\3\2\2\2\u0238\u0239\5D#\2\u0239\u023a\78\2\2\u023a\u023c\3\2\2\2\u023b"+
		"\u0238\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u0247\3\2\2\2\u023d\u0240\5H"+
		"%\2\u023e\u023f\78\2\2\u023f\u0241\5D#\2\u0240\u023e\3\2\2\2\u0240\u0241"+
		"\3\2\2\2\u0241\u0244\3\2\2\2\u0242\u0243\78\2\2\u0243\u0245\5J&\2\u0244"+
		"\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0248\5J"+
		"&\2\u0247\u023d\3\2\2\2\u0247\u0246\3\2\2\2\u0248\u024a\3\2\2\2\u0249"+
		"\u024b\78\2\2\u024a\u0249\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u0251\3\2"+
		"\2\2\u024c\u024e\5D#\2\u024d\u024f\78\2\2\u024e\u024d\3\2\2\2\u024e\u024f"+
		"\3\2\2\2\u024f\u0251\3\2\2\2\u0250\u023b\3\2\2\2\u0250\u024c\3\2\2\2\u0251"+
		"C\3\2\2\2\u0252\u0257\5F$\2\u0253\u0254\78\2\2\u0254\u0256\5F$\2\u0255"+
		"\u0253\3\2\2\2\u0256\u0259\3\2\2\2\u0257\u0255\3\2\2\2\u0257\u0258\3\2"+
		"\2\2\u0258E\3\2\2\2\u0259\u0257\3\2\2\2\u025a\u025d\5\\/\2\u025b\u025c"+
		"\7<\2\2\u025c\u025e\5@!\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e"+
		"\u0261\3\2\2\2\u025f\u0261\7\67\2\2\u0260\u025a\3\2\2\2\u0260\u025f\3"+
		"\2\2\2\u0261G\3\2\2\2\u0262\u0263\7\67\2\2\u0263\u0264\5\\/\2\u0264I\3"+
		"\2\2\2\u0265\u0266\7;\2\2\u0266\u0267\5\\/\2\u0267K\3\2\2\2\u0268\u0269"+
		"\b\'\1\2\u0269\u026d\5N(\2\u026a\u026b\7\35\2\2\u026b\u026d\5L\'\5\u026c"+
		"\u0268\3\2\2\2\u026c\u026a\3\2\2\2\u026d\u0276\3\2\2\2\u026e\u026f\f\4"+
		"\2\2\u026f\u0270\7\34\2\2\u0270\u0275\5L\'\5\u0271\u0272\f\3\2\2\u0272"+
		"\u0273\7\33\2\2\u0273\u0275\5L\'\4\u0274\u026e\3\2\2\2\u0274\u0271\3\2"+
		"\2\2\u0275\u0278\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277"+
		"M\3\2\2\2\u0278\u0276\3\2\2\2\u0279\u027a\b(\1\2\u027a\u027b\5P)\2\u027b"+
		"\u0291\3\2\2\2\u027c\u028c\f\4\2\2\u027d\u028d\7H\2\2\u027e\u028d\7I\2"+
		"\2\u027f\u028d\7J\2\2\u0280\u028d\7K\2\2\u0281\u028d\7L\2\2\u0282\u028d"+
		"\7M\2\2\u0283\u028d\7N\2\2\u0284\u0286\7\35\2\2\u0285\u0284\3\2\2\2\u0285"+
		"\u0286\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u028d\7\24\2\2\u0288\u028a\7"+
		"\36\2\2\u0289\u028b\7\35\2\2\u028a\u0289\3\2\2\2\u028a\u028b\3\2\2\2\u028b"+
		"\u028d\3\2\2\2\u028c\u027d\3\2\2\2\u028c\u027e\3\2\2\2\u028c\u027f\3\2"+
		"\2\2\u028c\u0280\3\2\2\2\u028c\u0281\3\2\2\2\u028c\u0282\3\2\2\2\u028c"+
		"\u0283\3\2\2\2\u028c\u0285\3\2\2\2\u028c\u0288\3\2\2\2\u028d\u028e\3\2"+
		"\2\2\u028e\u0290\5N(\5\u028f\u027c\3\2\2\2\u0290\u0293\3\2\2\2\u0291\u028f"+
		"\3\2\2\2\u0291\u0292\3\2\2\2\u0292O\3\2\2\2\u0293\u0291\3\2\2\2\u0294"+
		"\u0296\b)\1\2\u0295\u0297\7&\2\2\u0296\u0295\3\2\2\2\u0296\u0297\3\2\2"+
		"\2\u0297\u0298\3\2\2\2\u0298\u029c\5R*\2\u0299\u029b\5f\64\2\u029a\u0299"+
		"\3\2\2\2\u029b\u029e\3\2\2\2\u029c\u029a\3\2\2\2\u029c\u029d\3\2\2\2\u029d"+
		"\u02a2\3\2\2\2\u029e\u029c\3\2\2\2\u029f\u02a0\t\4\2\2\u02a0\u02a2\5P"+
		")\t\u02a1\u0294\3\2\2\2\u02a1\u029f\3\2\2\2\u02a2\u02ba\3\2\2\2\u02a3"+
		"\u02a4\f\n\2\2\u02a4\u02a5\7;\2\2\u02a5\u02b9\5P)\n\u02a6\u02a7\f\b\2"+
		"\2\u02a7\u02a8\t\5\2\2\u02a8\u02b9\5P)\t\u02a9\u02aa\f\7\2\2\u02aa\u02ab"+
		"\t\6\2\2\u02ab\u02b9\5P)\b\u02ac\u02ad\f\6\2\2\u02ad\u02ae\t\7\2\2\u02ae"+
		"\u02b9\5P)\7\u02af\u02b0\f\5\2\2\u02b0\u02b1\7?\2\2\u02b1\u02b9\5P)\6"+
		"\u02b2\u02b3\f\4\2\2\u02b3\u02b4\7>\2\2\u02b4\u02b9\5P)\5\u02b5\u02b6"+
		"\f\3\2\2\u02b6\u02b7\7=\2\2\u02b7\u02b9\5P)\4\u02b8\u02a3\3\2\2\2\u02b8"+
		"\u02a6\3\2\2\2\u02b8\u02a9\3\2\2\2\u02b8\u02ac\3\2\2\2\u02b8\u02af\3\2"+
		"\2\2\u02b8\u02b2\3\2\2\2\u02b8\u02b5\3\2\2\2\u02b9\u02bc\3\2\2\2\u02ba"+
		"\u02b8\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bbQ\3\2\2\2\u02bc\u02ba\3\2\2\2"+
		"\u02bd\u02c0\7e\2\2\u02be\u02c1\5b\62\2\u02bf\u02c1\5V,\2\u02c0\u02be"+
		"\3\2\2\2\u02c0\u02bf\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c2\3\2\2\2\u02c2"+
		"\u02e3\7f\2\2\u02c3\u02c5\7i\2\2\u02c4\u02c6\5V,\2\u02c5\u02c4\3\2\2\2"+
		"\u02c5\u02c6\3\2\2\2\u02c6\u02c7\3\2\2\2\u02c7\u02e3\7j\2\2\u02c8\u02ca"+
		"\7g\2\2\u02c9\u02cb\5T+\2\u02ca\u02c9\3\2\2\2\u02ca\u02cb\3\2\2\2\u02cb"+
		"\u02cc\3\2\2\2\u02cc\u02e3\7h\2\2\u02cd\u02ce\7\66\2\2\u02ce\u02d0\5X"+
		"-\2\u02cf\u02d1\78\2\2\u02d0\u02cf\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u02d2"+
		"\3\2\2\2\u02d2\u02d3\7\66\2\2\u02d3\u02e3\3\2\2\2\u02d4\u02e3\7\65\2\2"+
		"\u02d5\u02e3\5\\/\2\u02d6\u02e3\7\'\2\2\u02d7\u02e3\7(\2\2\u02d8\u02da"+
		"\7C\2\2\u02d9\u02d8\3\2\2\2\u02d9\u02da\3\2\2\2\u02da\u02db\3\2\2\2\u02db"+
		"\u02e3\5^\60\2\u02dc\u02e3\7\26\2\2\u02dd\u02df\7^\2\2\u02de\u02dd\3\2"+
		"\2\2\u02df\u02e0\3\2\2\2\u02e0\u02de\3\2\2\2\u02e0\u02e1\3\2\2\2\u02e1"+
		"\u02e3\3\2\2\2\u02e2\u02bd\3\2\2\2\u02e2\u02c3\3\2\2\2\u02e2\u02c8\3\2"+
		"\2\2\u02e2\u02cd\3\2\2\2\u02e2\u02d4\3\2\2\2\u02e2\u02d5\3\2\2\2\u02e2"+
		"\u02d6\3\2\2\2\u02e2\u02d7\3\2\2\2\u02e2\u02d9\3\2\2\2\u02e2\u02dc\3\2"+
		"\2\2\u02e2\u02de\3\2\2\2\u02e3S\3\2\2\2\u02e4\u02e5\5@!\2\u02e5\u02e6"+
		"\79\2\2\u02e6\u02e7\5@!\2\u02e7\u02eb\3\2\2\2\u02e8\u02e9\7;\2\2\u02e9"+
		"\u02eb\5P)\2\u02ea\u02e4\3\2\2\2\u02ea\u02e8\3\2\2\2\u02eb\u02f7\3\2\2"+
		"\2\u02ec\u02f3\78\2\2\u02ed\u02ee\5@!\2\u02ee\u02ef\79\2\2\u02ef\u02f0"+
		"\5@!\2\u02f0\u02f4\3\2\2\2\u02f1\u02f2\7;\2\2\u02f2\u02f4\5P)\2\u02f3"+
		"\u02ed\3\2\2\2\u02f3\u02f1\3\2\2\2\u02f4\u02f6\3\2\2\2\u02f5\u02ec\3\2"+
		"\2\2\u02f6\u02f9\3\2\2\2\u02f7\u02f5\3\2\2\2\u02f7\u02f8\3\2\2\2\u02f8"+
		"\u02fb\3\2\2\2\u02f9\u02f7\3\2\2\2\u02fa\u02fc\78\2\2\u02fb\u02fa\3\2"+
		"\2\2\u02fb\u02fc\3\2\2\2\u02fc\u0304\3\2\2\2\u02fd\u02fe\5@!\2\u02fe\u02ff"+
		"\79\2\2\u02ff\u0300\5@!\2\u0300\u0301\5t;\2\u0301\u0304\3\2\2\2\u0302"+
		"\u0304\5V,\2\u0303\u02ea\3\2\2\2\u0303\u02fd\3\2\2\2\u0303\u0302\3\2\2"+
		"\2\u0304U\3\2\2\2\u0305\u0308\5@!\2\u0306\u0308\5\62\32\2\u0307\u0305"+
		"\3\2\2\2\u0307\u0306\3\2\2\2\u0308\u0317\3\2\2\2\u0309\u0318\5t;\2\u030a"+
		"\u030d\78\2\2\u030b\u030e\5@!\2\u030c\u030e\5\62\32\2\u030d\u030b\3\2"+
		"\2\2\u030d\u030c\3\2\2\2\u030e\u0310\3\2\2\2\u030f\u030a\3\2\2\2\u0310"+
		"\u0313\3\2\2\2\u0311\u030f\3\2\2\2\u0311\u0312\3\2\2\2\u0312\u0315\3\2"+
		"\2\2\u0313\u0311\3\2\2\2\u0314\u0316\78\2\2\u0315\u0314\3\2\2\2\u0315"+
		"\u0316\3\2\2\2\u0316\u0318\3\2\2\2\u0317\u0309\3\2\2\2\u0317\u0311\3\2"+
		"\2\2\u0318W\3\2\2\2\u0319\u031e\5@!\2\u031a\u031b\78\2\2\u031b\u031d\5"+
		"@!\2\u031c\u031a\3\2\2\2\u031d\u0320\3\2\2\2\u031e\u031c\3\2\2\2\u031e"+
		"\u031f\3\2\2\2\u031f\u0322\3\2\2\2\u0320\u031e\3\2\2\2\u0321\u0323\78"+
		"\2\2\u0322\u0321\3\2\2\2\u0322\u0323\3\2\2\2\u0323Y\3\2\2\2\u0324\u0325"+
		"\b.\1\2\u0325\u0326\5\\/\2\u0326\u032c\3\2\2\2\u0327\u0328\f\4\2\2\u0328"+
		"\u0329\7\64\2\2\u0329\u032b\5\\/\2\u032a\u0327\3\2\2\2\u032b\u032e\3\2"+
		"\2\2\u032c\u032a\3\2\2\2\u032c\u032d\3\2\2\2\u032d[\3\2\2\2\u032e\u032c"+
		"\3\2\2\2\u032f\u0330\t\b\2\2\u0330]\3\2\2\2\u0331\u0335\5`\61\2\u0332"+
		"\u0335\7c\2\2\u0333\u0335\7d\2\2\u0334\u0331\3\2\2\2\u0334\u0332\3\2\2"+
		"\2\u0334\u0333\3\2\2\2\u0335_\3\2\2\2\u0336\u0337\t\t\2\2\u0337a\3\2\2"+
		"\2\u0338\u033a\7 \2\2\u0339\u033b\5d\63\2\u033a\u0339\3\2\2\2\u033a\u033b"+
		"\3\2\2\2\u033bc\3\2\2\2\u033c\u033d\7\t\2\2\u033d\u0340\5@!\2\u033e\u0340"+
		"\5X-\2\u033f\u033c\3\2\2\2\u033f\u033e\3\2\2\2\u0340e\3\2\2\2\u0341\u0344"+
		"\7\64\2\2\u0342\u0345\5\\/\2\u0343\u0345\5x=\2\u0344\u0342\3\2\2\2\u0344"+
		"\u0343\3\2\2\2\u0345\u0347\3\2\2\2\u0346\u0348\5h\65\2\u0347\u0346\3\2"+
		"\2\2\u0347\u0348\3\2\2\2\u0348\u034b\3\2\2\2\u0349\u034b\5h\65\2\u034a"+
		"\u0341\3\2\2\2\u034a\u0349\3\2\2\2\u034bg\3\2\2\2\u034c\u034e\7e\2\2\u034d"+
		"\u034f\5j\66\2\u034e\u034d\3\2\2\2\u034e\u034f\3\2\2\2\u034f\u0350\3\2"+
		"\2\2\u0350\u0356\7f\2\2\u0351\u0352\7i\2\2\u0352\u0353\5n8\2\u0353\u0354"+
		"\7j\2\2\u0354\u0356\3\2\2\2\u0355\u034c\3\2\2\2\u0355\u0351\3\2\2\2\u0356"+
		"i\3\2\2\2\u0357\u035c\5l\67\2\u0358\u0359\78\2\2\u0359\u035b\5l\67\2\u035a"+
		"\u0358\3\2\2\2\u035b\u035e\3\2\2\2\u035c\u035a\3\2\2\2\u035c\u035d\3\2"+
		"\2\2\u035d\u0360\3\2\2\2\u035e\u035c\3\2\2\2\u035f\u0361\78\2\2\u0360"+
		"\u035f\3\2\2\2\u0360\u0361\3\2\2\2\u0361k\3\2\2\2\u0362\u0366\5@!\2\u0363"+
		"\u0367\5t;\2\u0364\u0365\7<\2\2\u0365\u0367\5@!\2\u0366\u0363\3\2\2\2"+
		"\u0366\u0364\3\2\2\2\u0366\u0367\3\2\2\2\u0367\u036b\3\2\2\2\u0368\u0369"+
		"\t\n\2\2\u0369\u036b\5@!\2\u036a\u0362\3\2\2\2\u036a\u0368\3\2\2\2\u036b"+
		"m\3\2\2\2\u036c\u0371\5p9\2\u036d\u036e\78\2\2\u036e\u0370\5p9\2\u036f"+
		"\u036d\3\2\2\2\u0370\u0373\3\2\2\2\u0371\u036f\3\2\2\2\u0371\u0372\3\2"+
		"\2\2\u0372\u0375\3\2\2\2\u0373\u0371\3\2\2\2\u0374\u0376\78\2\2\u0375"+
		"\u0374\3\2\2\2\u0375\u0376\3\2\2\2\u0376o\3\2\2\2\u0377\u038a\7\65\2\2"+
		"\u0378\u0380\5@!\2\u0379\u037b\79\2\2\u037a\u037c\5@!\2\u037b\u037a\3"+
		"\2\2\2\u037b\u037c\3\2\2\2\u037c\u037e\3\2\2\2\u037d\u037f\5r:\2\u037e"+
		"\u037d\3\2\2\2\u037e\u037f\3\2\2\2\u037f\u0381\3\2\2\2\u0380\u0379\3\2"+
		"\2\2\u0380\u0381\3\2\2\2\u0381\u038a\3\2\2\2\u0382\u0384\79\2\2\u0383"+
		"\u0385\5@!\2\u0384\u0383\3\2\2\2\u0384\u0385\3\2\2\2\u0385\u0387\3\2\2"+
		"\2\u0386\u0388\5r:\2\u0387\u0386\3\2\2\2\u0387\u0388\3\2\2\2\u0388\u038a"+
		"\3\2\2\2\u0389\u0377\3\2\2\2\u0389\u0378\3\2\2\2\u0389\u0382\3\2\2\2\u038a"+
		"q\3\2\2\2\u038b\u038d\79\2\2\u038c\u038e\5@!\2\u038d\u038c\3\2\2\2\u038d"+
		"\u038e\3\2\2\2\u038es\3\2\2\2\u038f\u0390\7\23\2\2\u0390\u0391\5\66\34"+
		"\2\u0391\u0392\7\24\2\2\u0392\u0394\5L\'\2\u0393\u0395\5v<\2\u0394\u0393"+
		"\3\2\2\2\u0394\u0395\3\2\2\2\u0395u\3\2\2\2\u0396\u039d\5t;\2\u0397\u0398"+
		"\7\17\2\2\u0398\u039a\5@!\2\u0399\u039b\5v<\2\u039a\u0399\3\2\2\2\u039a"+
		"\u039b\3\2\2\2\u039b\u039d\3\2\2\2\u039c\u0396\3\2\2\2\u039c\u0397\3\2"+
		"\2\2\u039dw\3\2\2\2\u039e\u039f\t\13\2\2\u039fy\3\2\2\2\u0095}\177\u0089"+
		"\u008d\u008f\u0095\u009a\u00a3\u00a7\u00ae\u00b1\u00ba\u00c2\u00c5\u00c8"+
		"\u00cb\u00ce\u00d6\u00df\u00e4\u00e6\u00ef\u00f3\u00f9\u00fc\u0110\u0116"+
		"\u0118\u0121\u0124\u012a\u0130\u0135\u013d\u0142\u0146\u0149\u014c\u0150"+
		"\u0152\u015f\u0165\u0168\u016d\u0174\u0178\u017b\u017f\u0188\u0190\u0192"+
		"\u0194\u0198\u01a1\u01a8\u01aa\u01b3\u01bb\u01c2\u01ca\u01cd\u01d1\u01d7"+
		"\u01db\u01de\u01e9\u01ee\u01f1\u01f7\u01fc\u01fe\u0205\u0209\u0210\u0214"+
		"\u0219\u0220\u0226\u022e\u0232\u0236\u023b\u0240\u0244\u0247\u024a\u024e"+
		"\u0250\u0257\u025d\u0260\u026c\u0274\u0276\u0285\u028a\u028c\u0291\u0296"+
		"\u029c\u02a1\u02b8\u02ba\u02c0\u02c5\u02ca\u02d0\u02d9\u02e0\u02e2\u02ea"+
		"\u02f3\u02f7\u02fb\u0303\u0307\u030d\u0311\u0315\u0317\u031e\u0322\u032c"+
		"\u0334\u033a\u033f\u0344\u0347\u034a\u034e\u0355\u035c\u0360\u0366\u036a"+
		"\u0371\u0375\u037b\u037e\u0380\u0384\u0387\u0389\u038d\u0394\u039a\u039c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}