# Generated from Java8Parser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3m")
        buf.write("\u0b1e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write("q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4")
        buf.write("z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080")
        buf.write("\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084")
        buf.write("\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087")
        buf.write("\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b")
        buf.write("\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e")
        buf.write("\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092")
        buf.write("\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095")
        buf.write("\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099")
        buf.write("\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c")
        buf.write("\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0")
        buf.write("\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3")
        buf.write("\4\u00a4\t\u00a4\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7")
        buf.write("\t\u00a7\4\u00a8\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa")
        buf.write("\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae")
        buf.write("\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1")
        buf.write("\4\u00b2\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5")
        buf.write("\t\u00b5\4\u00b6\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8")
        buf.write("\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc")
        buf.write("\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf")
        buf.write("\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3")
        buf.write("\t\u00c3\4\u00c4\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6")
        buf.write("\4\u00c7\t\u00c7\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca")
        buf.write("\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd")
        buf.write("\4\u00ce\t\u00ce\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1")
        buf.write("\t\u00d1\4\u00d2\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4")
        buf.write("\4\u00d5\t\u00d5\4\u00d6\t\u00d6\4\u00d7\t\u00d7\4\u00d8")
        buf.write("\t\u00d8\4\u00d9\t\u00d9\4\u00da\t\u00da\4\u00db\t\u00db")
        buf.write("\4\u00dc\t\u00dc\4\u00dd\t\u00dd\4\u00de\t\u00de\4\u00df")
        buf.write("\t\u00df\4\u00e0\t\u00e0\4\u00e1\t\u00e1\4\u00e2\t\u00e2")
        buf.write("\4\u00e3\t\u00e3\4\u00e4\t\u00e4\4\u00e5\t\u00e5\4\u00e6")
        buf.write("\t\u00e6\4\u00e7\t\u00e7\4\u00e8\t\u00e8\4\u00e9\t\u00e9")
        buf.write("\4\u00ea\t\u00ea\4\u00eb\t\u00eb\4\u00ec\t\u00ec\4\u00ed")
        buf.write("\t\u00ed\3\2\3\2\3\3\7\3\u01de\n\3\f\3\16\3\u01e1\13\3")
        buf.write("\3\3\3\3\7\3\u01e5\n\3\f\3\16\3\u01e8\13\3\3\3\5\3\u01eb")
        buf.write("\n\3\3\4\3\4\5\4\u01ef\n\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7")
        buf.write("\5\7\u01f8\n\7\3\b\3\b\5\b\u01fc\n\b\3\b\3\b\7\b\u0200")
        buf.write("\n\b\f\b\16\b\u0203\13\b\3\t\7\t\u0206\n\t\f\t\16\t\u0209")
        buf.write("\13\t\3\t\3\t\5\t\u020d\n\t\3\t\3\t\3\t\7\t\u0212\n\t")
        buf.write("\f\t\16\t\u0215\13\t\3\t\3\t\5\t\u0219\n\t\5\t\u021b\n")
        buf.write("\t\3\n\3\n\7\n\u021f\n\n\f\n\16\n\u0222\13\n\3\n\3\n\5")
        buf.write("\n\u0226\n\n\3\13\7\13\u0229\n\13\f\13\16\13\u022c\13")
        buf.write("\13\3\13\3\13\5\13\u0230\n\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\7\17\u0239\n\17\f\17\16\17\u023c\13\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0249")
        buf.write("\n\20\3\21\7\21\u024c\n\21\f\21\16\21\u024f\13\21\3\21")
        buf.write("\3\21\3\21\7\21\u0254\n\21\f\21\16\21\u0257\13\21\3\21")
        buf.write("\3\21\7\21\u025b\n\21\f\21\16\21\u025e\13\21\3\22\7\22")
        buf.write("\u0261\n\22\f\22\16\22\u0264\13\22\3\22\3\22\5\22\u0268")
        buf.write("\n\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\7\24\u0271\n")
        buf.write("\24\f\24\16\24\u0274\13\24\5\24\u0276\n\24\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\7\27\u0282\n\27")
        buf.write("\f\27\16\27\u0285\13\27\3\30\3\30\5\30\u0289\n\30\3\31")
        buf.write("\7\31\u028c\n\31\f\31\16\31\u028f\13\31\3\31\3\31\5\31")
        buf.write("\u0293\n\31\3\32\3\32\3\32\3\32\5\32\u0299\n\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\7\33\u02a1\n\33\f\33\16\33\u02a4")
        buf.write("\13\33\3\34\3\34\3\34\3\34\3\34\5\34\u02ab\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\7\35\u02b3\n\35\f\35\16\35\u02b6")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\36\5\36\u02bd\n\36\3\37\3")
        buf.write("\37\3 \3 \3 \3 \3 \3 \7 \u02c7\n \f \16 \u02ca\13 \3!")
        buf.write("\5!\u02cd\n!\3!\7!\u02d0\n!\f!\16!\u02d3\13!\3!\7!\u02d6")
        buf.write("\n!\f!\16!\u02d9\13!\3!\3!\3\"\7\"\u02de\n\"\f\"\16\"")
        buf.write("\u02e1\13\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3$\3$\5$\u02ed")
        buf.write("\n$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\5)\u030a\n)\3*")
        buf.write("\3*\5*\u030e\n*\3+\7+\u0311\n+\f+\16+\u0314\13+\3+\3+")
        buf.write("\3+\5+\u0319\n+\3+\5+\u031c\n+\3+\5+\u031f\n+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\5,\u032b\n,\3-\3-\3-\3-\3.\3.\3")
        buf.write(".\7.\u0334\n.\f.\16.\u0337\13.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\7\61\u0342\n\61\f\61\16\61\u0345\13\61")
        buf.write("\3\62\3\62\7\62\u0349\n\62\f\62\16\62\u034c\13\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\5\63\u0354\n\63\3\64\3\64\3")
        buf.write("\64\3\64\3\64\5\64\u035b\n\64\3\65\7\65\u035e\n\65\f\65")
        buf.write("\16\65\u0361\13\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u036f\n\66\3\67\3\67\3")
        buf.write("\67\7\67\u0374\n\67\f\67\16\67\u0377\13\67\38\38\38\5")
        buf.write("8\u037c\n8\39\39\59\u0380\n9\3:\3:\5:\u0384\n:\3;\3;\5")
        buf.write(";\u0388\n;\3<\3<\5<\u038c\n<\3=\3=\3=\5=\u0391\n=\3>\3")
        buf.write(">\5>\u0395\n>\3>\3>\7>\u0399\n>\f>\16>\u039c\13>\3?\3")
        buf.write("?\5?\u03a0\n?\3?\3?\3?\7?\u03a5\n?\f?\16?\u03a8\13?\3")
        buf.write("?\3?\5?\u03ac\n?\5?\u03ae\n?\3@\3@\7@\u03b2\n@\f@\16@")
        buf.write("\u03b5\13@\3@\3@\5@\u03b9\n@\3A\3A\5A\u03bd\nA\3B\3B\3")
        buf.write("C\3C\3D\3D\3E\3E\3F\3F\3F\3F\3F\3F\3F\3F\3F\5F\u03d0\n")
        buf.write("F\3G\7G\u03d3\nG\fG\16G\u03d6\13G\3G\3G\3G\3H\3H\3H\3")
        buf.write("H\3H\3H\3H\3H\3H\3H\5H\u03e5\nH\3I\3I\3I\5I\u03ea\nI\3")
        buf.write("I\3I\7I\u03ee\nI\fI\16I\u03f1\13I\3I\3I\3I\5I\u03f6\n")
        buf.write("I\5I\u03f8\nI\3J\3J\5J\u03fc\nJ\3K\3K\3K\5K\u0401\nK\3")
        buf.write("K\3K\5K\u0405\nK\3L\3L\3L\3L\3L\3L\5L\u040d\nL\3M\3M\3")
        buf.write("M\7M\u0412\nM\fM\16M\u0415\13M\3M\3M\3M\7M\u041a\nM\f")
        buf.write("M\16M\u041d\13M\5M\u041f\nM\3N\7N\u0422\nN\fN\16N\u0425")
        buf.write("\13N\3N\3N\3N\3O\3O\5O\u042c\nO\3P\7P\u042f\nP\fP\16P")
        buf.write("\u0432\13P\3P\3P\7P\u0436\nP\fP\16P\u0439\13P\3P\3P\3")
        buf.write("P\3P\5P\u043f\nP\3Q\7Q\u0442\nQ\fQ\16Q\u0445\13Q\3Q\3")
        buf.write("Q\3Q\5Q\u044a\nQ\3Q\3Q\3R\3R\3R\3S\3S\3S\7S\u0454\nS\f")
        buf.write("S\16S\u0457\13S\3T\3T\5T\u045b\nT\3U\3U\5U\u045f\nU\3")
        buf.write("V\3V\3W\3W\3W\3X\7X\u0467\nX\fX\16X\u046a\13X\3X\3X\5")
        buf.write("X\u046e\nX\3X\3X\3Y\3Y\3Y\3Y\5Y\u0476\nY\3Z\5Z\u0479\n")
        buf.write("Z\3Z\3Z\3Z\5Z\u047e\nZ\3Z\3Z\3[\3[\3\\\3\\\5\\\u0486\n")
        buf.write("\\\3\\\5\\\u0489\n\\\3\\\3\\\3]\5]\u048e\n]\3]\3]\3]\5")
        buf.write("]\u0493\n]\3]\3]\3]\5]\u0498\n]\3]\3]\3]\5]\u049d\n]\3")
        buf.write("]\3]\3]\3]\3]\5]\u04a4\n]\3]\3]\3]\5]\u04a9\n]\3]\3]\3")
        buf.write("]\3]\3]\3]\5]\u04b1\n]\3]\3]\3]\5]\u04b6\n]\3]\3]\3]\5")
        buf.write("]\u04bb\n]\3^\7^\u04be\n^\f^\16^\u04c1\13^\3^\3^\3^\5")
        buf.write("^\u04c6\n^\3^\3^\3_\3_\5_\u04cc\n_\3_\5_\u04cf\n_\3_\5")
        buf.write("_\u04d2\n_\3_\3_\3`\3`\3`\7`\u04d9\n`\f`\16`\u04dc\13")
        buf.write("`\3a\7a\u04df\na\fa\16a\u04e2\13a\3a\3a\3a\5a\u04e7\n")
        buf.write("a\3a\5a\u04ea\na\3a\5a\u04ed\na\3b\3b\3c\3c\7c\u04f3\n")
        buf.write("c\fc\16c\u04f6\13c\3d\3d\5d\u04fa\nd\3e\7e\u04fd\ne\f")
        buf.write("e\16e\u0500\13e\3e\3e\3e\5e\u0505\ne\3e\5e\u0508\ne\3")
        buf.write("e\3e\3f\3f\3f\3f\3f\3f\3f\5f\u0513\nf\3g\3g\3g\3h\3h\7")
        buf.write("h\u051a\nh\fh\16h\u051d\13h\3h\3h\3i\3i\3i\3i\3i\5i\u0526")
        buf.write("\ni\3j\7j\u0529\nj\fj\16j\u052c\13j\3j\3j\3j\3j\3k\3k")
        buf.write("\3k\3k\5k\u0536\nk\3l\7l\u0539\nl\fl\16l\u053c\13l\3l")
        buf.write("\3l\3l\3m\3m\3m\3m\3m\3m\5m\u0547\nm\3n\7n\u054a\nn\f")
        buf.write("n\16n\u054d\13n\3n\3n\3n\3n\3n\3o\3o\7o\u0556\no\fo\16")
        buf.write("o\u0559\13o\3o\3o\3p\3p\3p\3p\3p\5p\u0562\np\3q\7q\u0565")
        buf.write("\nq\fq\16q\u0568\13q\3q\3q\3q\3q\3q\5q\u056f\nq\3q\5q")
        buf.write("\u0572\nq\3q\3q\3r\3r\3r\5r\u0579\nr\3s\3s\3s\3t\3t\3")
        buf.write("t\5t\u0581\nt\3u\3u\3u\3u\5u\u0587\nu\3u\3u\3v\3v\3v\7")
        buf.write("v\u058e\nv\fv\16v\u0591\13v\3w\3w\3w\3w\3x\3x\3x\5x\u059a")
        buf.write("\nx\3y\3y\5y\u059e\ny\3y\5y\u05a1\ny\3y\3y\3z\3z\3z\7")
        buf.write("z\u05a8\nz\fz\16z\u05ab\13z\3{\3{\3{\3|\3|\3|\3|\3|\3")
        buf.write("|\3}\3}\5}\u05b8\n}\3}\5}\u05bb\n}\3}\3}\3~\3~\3~\7~\u05c2")
        buf.write("\n~\f~\16~\u05c5\13~\3\177\3\177\5\177\u05c9\n\177\3\177")
        buf.write("\3\177\3\u0080\6\u0080\u05ce\n\u0080\r\u0080\16\u0080")
        buf.write("\u05cf\3\u0081\3\u0081\3\u0081\5\u0081\u05d5\n\u0081\3")
        buf.write("\u0082\3\u0082\3\u0082\3\u0083\7\u0083\u05db\n\u0083\f")
        buf.write("\u0083\16\u0083\u05de\13\u0083\3\u0083\3\u0083\3\u0083")
        buf.write("\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\5\u0084")
        buf.write("\u05e9\n\u0084\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085")
        buf.write("\5\u0085\u05f0\n\u0085\3\u0086\3\u0086\3\u0086\3\u0086")
        buf.write("\3\u0086\3\u0086\3\u0086\3\u0086\3\u0086\3\u0086\3\u0086")
        buf.write("\3\u0086\5\u0086\u05fe\n\u0086\3\u0087\3\u0087\3\u0088")
        buf.write("\3\u0088\3\u0088\3\u0088\3\u0089\3\u0089\3\u0089\3\u0089")
        buf.write("\3\u008a\3\u008a\3\u008a\3\u008b\3\u008b\3\u008b\3\u008b")
        buf.write("\3\u008b\3\u008b\3\u008b\5\u008b\u0614\n\u008b\3\u008c")
        buf.write("\3\u008c\3\u008c\3\u008c\3\u008c\3\u008c\3\u008d\3\u008d")
        buf.write("\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008e")
        buf.write("\3\u008e\3\u008e\3\u008e\3\u008e\3\u008e\3\u008e\3\u008e")
        buf.write("\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\5\u008f\u0636\n\u008f\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\3\u0091\3\u0091")
        buf.write("\7\u0091\u0640\n\u0091\f\u0091\16\u0091\u0643\13\u0091")
        buf.write("\3\u0091\7\u0091\u0646\n\u0091\f\u0091\16\u0091\u0649")
        buf.write("\13\u0091\3\u0091\3\u0091\3\u0092\3\u0092\3\u0092\3\u0093")
        buf.write("\3\u0093\7\u0093\u0652\n\u0093\f\u0093\16\u0093\u0655")
        buf.write("\13\u0093\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094")
        buf.write("\3\u0094\3\u0094\3\u0094\3\u0094\5\u0094\u0661\n\u0094")
        buf.write("\3\u0095\3\u0095\3\u0096\3\u0096\3\u0096\3\u0096\3\u0096")
        buf.write("\3\u0096\3\u0097\3\u0097\3\u0097\3\u0097\3\u0097\3\u0097")
        buf.write("\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098")
        buf.write("\3\u0098\3\u0099\3\u0099\5\u0099\u067b\n\u0099\3\u009a")
        buf.write("\3\u009a\5\u009a\u067f\n\u009a\3\u009b\3\u009b\3\u009b")
        buf.write("\5\u009b\u0684\n\u009b\3\u009b\3\u009b\5\u009b\u0688\n")
        buf.write("\u009b\3\u009b\3\u009b\5\u009b\u068c\n\u009b\3\u009b\3")
        buf.write("\u009b\3\u009b\3\u009c\3\u009c\3\u009c\5\u009c\u0694\n")
        buf.write("\u009c\3\u009c\3\u009c\5\u009c\u0698\n\u009c\3\u009c\3")
        buf.write("\u009c\5\u009c\u069c\n\u009c\3\u009c\3\u009c\3\u009c\3")
        buf.write("\u009d\3\u009d\5\u009d\u06a3\n\u009d\3\u009e\3\u009e\3")
        buf.write("\u009f\3\u009f\3\u009f\7\u009f\u06aa\n\u009f\f\u009f\16")
        buf.write("\u009f\u06ad\13\u009f\3\u00a0\3\u00a0\3\u00a0\7\u00a0")
        buf.write("\u06b2\n\u00a0\f\u00a0\16\u00a0\u06b5\13\u00a0\3\u00a0")
        buf.write("\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a1")
        buf.write("\3\u00a1\3\u00a1\7\u00a1\u06c1\n\u00a1\f\u00a1\16\u00a1")
        buf.write("\u06c4\13\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1")
        buf.write("\3\u00a1\3\u00a1\3\u00a2\3\u00a2\5\u00a2\u06cf\n\u00a2")
        buf.write("\3\u00a2\3\u00a2\3\u00a3\3\u00a3\5\u00a3\u06d5\n\u00a3")
        buf.write("\3\u00a3\3\u00a3\3\u00a4\3\u00a4\5\u00a4\u06db\n\u00a4")
        buf.write("\3\u00a4\3\u00a4\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a6")
        buf.write("\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a7\3\u00a7")
        buf.write("\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\5\u00a7\u06f0")
        buf.write("\n\u00a7\3\u00a7\3\u00a7\3\u00a7\5\u00a7\u06f5\n\u00a7")
        buf.write("\3\u00a8\3\u00a8\7\u00a8\u06f9\n\u00a8\f\u00a8\16\u00a8")
        buf.write("\u06fc\13\u00a8\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9")
        buf.write("\3\u00a9\3\u00aa\7\u00aa\u0705\n\u00aa\f\u00aa\16\u00aa")
        buf.write("\u0708\13\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00ab\3\u00ab")
        buf.write("\3\u00ab\7\u00ab\u0710\n\u00ab\f\u00ab\16\u00ab\u0713")
        buf.write("\13\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ad\3\u00ad\3\u00ad")
        buf.write("\3\u00ad\5\u00ad\u071c\n\u00ad\3\u00ad\5\u00ad\u071f\n")
        buf.write("\u00ad\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u0724\n\u00ae\3")
        buf.write("\u00ae\3\u00ae\3\u00af\3\u00af\3\u00af\7\u00af\u072b\n")
        buf.write("\u00af\f\u00af\16\u00af\u072e\13\u00af\3\u00b0\7\u00b0")
        buf.write("\u0731\n\u00b0\f\u00b0\16\u00b0\u0734\13\u00b0\3\u00b0")
        buf.write("\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b1\3\u00b1\5\u00b1")
        buf.write("\u073d\n\u00b1\3\u00b1\7\u00b1\u0740\n\u00b1\f\u00b1\16")
        buf.write("\u00b1\u0743\13\u00b1\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write("\7\u00b2\u0749\n\u00b2\f\u00b2\16\u00b2\u074c\13\u00b2")
        buf.write("\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write("\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2")
        buf.write("\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\5\u00b2")
        buf.write("\u0762\n\u00b2\3\u00b3\3\u00b3\3\u00b4\3\u00b4\3\u00b4")
        buf.write("\3\u00b4\7\u00b4\u076a\n\u00b4\f\u00b4\16\u00b4\u076d")
        buf.write("\13\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4")
        buf.write("\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4")
        buf.write("\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\5\u00b4")
        buf.write("\u0782\n\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write("\5\u00b5\u0789\n\u00b5\3\u00b6\3\u00b6\3\u00b7\3\u00b7")
        buf.write("\3\u00b7\3\u00b7\5\u00b7\u0791\n\u00b7\3\u00b8\3\u00b8")
        buf.write("\3\u00b8\3\u00b8\7\u00b8\u0797\n\u00b8\f\u00b8\16\u00b8")
        buf.write("\u079a\13\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8")
        buf.write("\3\u00b8\7\u00b8\u07a2\n\u00b8\f\u00b8\16\u00b8\u07a5")
        buf.write("\13\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8")
        buf.write("\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8")
        buf.write("\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b8")
        buf.write("\5\u00b8\u07bb\n\u00b8\3\u00b9\3\u00b9\3\u00ba\3\u00ba")
        buf.write("\3\u00ba\3\u00ba\7\u00ba\u07c3\n\u00ba\f\u00ba\16\u00ba")
        buf.write("\u07c6\13\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba")
        buf.write("\3\u00ba\7\u00ba\u07ce\n\u00ba\f\u00ba\16\u00ba\u07d1")
        buf.write("\13\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba")
        buf.write("\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba")
        buf.write("\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\5\u00ba")
        buf.write("\u07e6\n\u00ba\3\u00bb\3\u00bb\5\u00bb\u07ea\n\u00bb\3")
        buf.write("\u00bb\7\u00bb\u07ed\n\u00bb\f\u00bb\16\u00bb\u07f0\13")
        buf.write("\u00bb\3\u00bb\3\u00bb\3\u00bb\7\u00bb\u07f5\n\u00bb\f")
        buf.write("\u00bb\16\u00bb\u07f8\13\u00bb\3\u00bb\7\u00bb\u07fb\n")
        buf.write("\u00bb\f\u00bb\16\u00bb\u07fe\13\u00bb\3\u00bb\5\u00bb")
        buf.write("\u0801\n\u00bb\3\u00bb\3\u00bb\5\u00bb\u0805\n\u00bb\3")
        buf.write("\u00bb\3\u00bb\5\u00bb\u0809\n\u00bb\3\u00bb\3\u00bb\3")
        buf.write("\u00bb\3\u00bb\5\u00bb\u080f\n\u00bb\3\u00bb\7\u00bb\u0812")
        buf.write("\n\u00bb\f\u00bb\16\u00bb\u0815\13\u00bb\3\u00bb\3\u00bb")
        buf.write("\5\u00bb\u0819\n\u00bb\3\u00bb\3\u00bb\5\u00bb\u081d\n")
        buf.write("\u00bb\3\u00bb\3\u00bb\5\u00bb\u0821\n\u00bb\3\u00bb\3")
        buf.write("\u00bb\3\u00bb\3\u00bb\5\u00bb\u0827\n\u00bb\3\u00bb\7")
        buf.write("\u00bb\u082a\n\u00bb\f\u00bb\16\u00bb\u082d\13\u00bb\3")
        buf.write("\u00bb\3\u00bb\5\u00bb\u0831\n\u00bb\3\u00bb\3\u00bb\5")
        buf.write("\u00bb\u0835\n\u00bb\3\u00bb\3\u00bb\5\u00bb\u0839\n\u00bb")
        buf.write("\5\u00bb\u083b\n\u00bb\3\u00bc\3\u00bc\3\u00bc\5\u00bc")
        buf.write("\u0840\n\u00bc\3\u00bc\7\u00bc\u0843\n\u00bc\f\u00bc\16")
        buf.write("\u00bc\u0846\13\u00bc\3\u00bc\3\u00bc\5\u00bc\u084a\n")
        buf.write("\u00bc\3\u00bc\3\u00bc\5\u00bc\u084e\n\u00bc\3\u00bc\3")
        buf.write("\u00bc\5\u00bc\u0852\n\u00bc\3\u00bd\3\u00bd\5\u00bd\u0856")
        buf.write("\n\u00bd\3\u00bd\7\u00bd\u0859\n\u00bd\f\u00bd\16\u00bd")
        buf.write("\u085c\13\u00bd\3\u00bd\3\u00bd\3\u00bd\7\u00bd\u0861")
        buf.write("\n\u00bd\f\u00bd\16\u00bd\u0864\13\u00bd\3\u00bd\7\u00bd")
        buf.write("\u0867\n\u00bd\f\u00bd\16\u00bd\u086a\13\u00bd\3\u00bd")
        buf.write("\5\u00bd\u086d\n\u00bd\3\u00bd\3\u00bd\5\u00bd\u0871\n")
        buf.write("\u00bd\3\u00bd\3\u00bd\5\u00bd\u0875\n\u00bd\3\u00bd\3")
        buf.write("\u00bd\3\u00bd\3\u00bd\5\u00bd\u087b\n\u00bd\3\u00bd\7")
        buf.write("\u00bd\u087e\n\u00bd\f\u00bd\16\u00bd\u0881\13\u00bd\3")
        buf.write("\u00bd\3\u00bd\5\u00bd\u0885\n\u00bd\3\u00bd\3\u00bd\5")
        buf.write("\u00bd\u0889\n\u00bd\3\u00bd\3\u00bd\5\u00bd\u088d\n\u00bd")
        buf.write("\5\u00bd\u088f\n\u00bd\3\u00be\3\u00be\3\u00be\5\u00be")
        buf.write("\u0894\n\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf")
        buf.write("\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf")
        buf.write("\3\u00bf\5\u00bf\u08a3\n\u00bf\3\u00c0\3\u00c0\3\u00c0")
        buf.write("\3\u00c1\3\u00c1\3\u00c1\3\u00c1\3\u00c1\3\u00c1\3\u00c1")
        buf.write("\3\u00c1\3\u00c1\5\u00c1\u08b1\n\u00c1\3\u00c2\3\u00c2")
        buf.write("\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write("\3\u00c2\5\u00c2\u08bd\n\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write("\3\u00c2\3\u00c2\7\u00c2\u08c4\n\u00c2\f\u00c2\16\u00c2")
        buf.write("\u08c7\13\u00c2\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3")
        buf.write("\3\u00c3\3\u00c3\3\u00c3\3\u00c3\3\u00c3\7\u00c3\u08d3")
        buf.write("\n\u00c3\f\u00c3\16\u00c3\u08d6\13\u00c3\3\u00c4\3\u00c4")
        buf.write("\3\u00c4\3\u00c4\3\u00c4\3\u00c4\3\u00c4\3\u00c4\3\u00c4")
        buf.write("\3\u00c4\5\u00c4\u08e2\n\u00c4\3\u00c4\3\u00c4\3\u00c4")
        buf.write("\3\u00c4\3\u00c4\7\u00c4\u08e9\n\u00c4\f\u00c4\16\u00c4")
        buf.write("\u08ec\13\u00c4\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u08f1")
        buf.write("\n\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5")
        buf.write("\u08f8\n\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u08fd\n")
        buf.write("\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5")
        buf.write("\u0904\n\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u0909\n")
        buf.write("\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5")
        buf.write("\u0910\n\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u0915\n")
        buf.write("\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5")
        buf.write("\u091c\n\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u0921\n")
        buf.write("\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5")
        buf.write("\5\u00c5\u0929\n\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5")
        buf.write("\u092e\n\u00c5\3\u00c5\3\u00c5\5\u00c5\u0932\n\u00c5\3")
        buf.write("\u00c6\3\u00c6\5\u00c6\u0936\n\u00c6\3\u00c6\3\u00c6\3")
        buf.write("\u00c6\5\u00c6\u093b\n\u00c6\3\u00c6\3\u00c6\3\u00c7\3")
        buf.write("\u00c7\3\u00c7\5\u00c7\u0942\n\u00c7\3\u00c7\3\u00c7\3")
        buf.write("\u00c7\3\u00c7\3\u00c7\5\u00c7\u0949\n\u00c7\3\u00c7\3")
        buf.write("\u00c7\3\u00c7\5\u00c7\u094e\n\u00c7\3\u00c7\3\u00c7\3")
        buf.write("\u00c7\3\u00c7\3\u00c7\5\u00c7\u0955\n\u00c7\3\u00c7\3")
        buf.write("\u00c7\3\u00c7\5\u00c7\u095a\n\u00c7\3\u00c7\3\u00c7\3")
        buf.write("\u00c7\3\u00c7\3\u00c7\5\u00c7\u0961\n\u00c7\3\u00c7\3")
        buf.write("\u00c7\3\u00c7\5\u00c7\u0966\n\u00c7\3\u00c7\3\u00c7\3")
        buf.write("\u00c7\3\u00c7\3\u00c7\3\u00c7\5\u00c7\u096e\n\u00c7\3")
        buf.write("\u00c7\3\u00c7\3\u00c7\5\u00c7\u0973\n\u00c7\3\u00c7\3")
        buf.write("\u00c7\5\u00c7\u0977\n\u00c7\3\u00c8\3\u00c8\3\u00c8\7")
        buf.write("\u00c8\u097c\n\u00c8\f\u00c8\16\u00c8\u097f\13\u00c8\3")
        buf.write("\u00c9\3\u00c9\3\u00c9\5\u00c9\u0984\n\u00c9\3\u00c9\3")
        buf.write("\u00c9\3\u00c9\3\u00c9\3\u00c9\5\u00c9\u098b\n\u00c9\3")
        buf.write("\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\5\u00c9\u0992\n")
        buf.write("\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\5\u00c9")
        buf.write("\u0999\n\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9")
        buf.write("\3\u00c9\5\u00c9\u09a1\n\u00c9\3\u00c9\3\u00c9\3\u00c9")
        buf.write("\3\u00c9\3\u00c9\5\u00c9\u09a8\n\u00c9\3\u00c9\3\u00c9")
        buf.write("\3\u00c9\3\u00c9\3\u00c9\3\u00c9\5\u00c9\u09b0\n\u00c9")
        buf.write("\3\u00ca\3\u00ca\5\u00ca\u09b4\n\u00ca\3\u00ca\3\u00ca")
        buf.write("\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u09bb\n\u00cb\3\u00cb")
        buf.write("\3\u00cb\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u09c2\n\u00cb")
        buf.write("\3\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u09c9")
        buf.write("\n\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cb")
        buf.write("\5\u00cb\u09d1\n\u00cb\3\u00cb\3\u00cb\3\u00cb\3\u00cb")
        buf.write("\3\u00cb\5\u00cb\u09d8\n\u00cb\3\u00cb\3\u00cb\3\u00cb")
        buf.write("\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u09e0\n\u00cb\3\u00cc")
        buf.write("\3\u00cc\3\u00cc\3\u00cc\5\u00cc\u09e6\n\u00cc\3\u00cc")
        buf.write("\3\u00cc\3\u00cc\3\u00cc\5\u00cc\u09ec\n\u00cc\3\u00cc")
        buf.write("\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc")
        buf.write("\3\u00cc\3\u00cc\5\u00cc\u09f8\n\u00cc\3\u00cd\3\u00cd")
        buf.write("\7\u00cd\u09fc\n\u00cd\f\u00cd\16\u00cd\u09ff\13\u00cd")
        buf.write("\3\u00ce\7\u00ce\u0a02\n\u00ce\f\u00ce\16\u00ce\u0a05")
        buf.write("\13\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00cf\3\u00cf")
        buf.write("\3\u00d0\3\u00d0\5\u00d0\u0a0f\n\u00d0\3\u00d1\3\u00d1")
        buf.write("\3\u00d1\3\u00d1\3\u00d2\3\u00d2\3\u00d2\5\u00d2\u0a18")
        buf.write("\n\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\5\u00d2")
        buf.write("\u0a1f\n\u00d2\3\u00d3\3\u00d3\3\u00d3\7\u00d3\u0a24\n")
        buf.write("\u00d3\f\u00d3\16\u00d3\u0a27\13\u00d3\3\u00d4\3\u00d4")
        buf.write("\5\u00d4\u0a2b\n\u00d4\3\u00d5\3\u00d5\5\u00d5\u0a2f\n")
        buf.write("\u00d5\3\u00d6\3\u00d6\3\u00d6\3\u00d6\3\u00d7\3\u00d7")
        buf.write("\3\u00d7\5\u00d7\u0a38\n\u00d7\3\u00d8\3\u00d8\3\u00d9")
        buf.write("\3\u00d9\3\u00d9\3\u00d9\3\u00d9\3\u00d9\3\u00d9\5\u00d9")
        buf.write("\u0a43\n\u00d9\3\u00da\3\u00da\3\u00da\3\u00da\3\u00da")
        buf.write("\3\u00da\7\u00da\u0a4b\n\u00da\f\u00da\16\u00da\u0a4e")
        buf.write("\13\u00da\3\u00db\3\u00db\3\u00db\3\u00db\3\u00db\3\u00db")
        buf.write("\7\u00db\u0a56\n\u00db\f\u00db\16\u00db\u0a59\13\u00db")
        buf.write("\3\u00dc\3\u00dc\3\u00dc\3\u00dc\3\u00dc\3\u00dc\7\u00dc")
        buf.write("\u0a61\n\u00dc\f\u00dc\16\u00dc\u0a64\13\u00dc\3\u00dd")
        buf.write("\3\u00dd\3\u00dd\3\u00dd\3\u00dd\3\u00dd\7\u00dd\u0a6c")
        buf.write("\n\u00dd\f\u00dd\16\u00dd\u0a6f\13\u00dd\3\u00de\3\u00de")
        buf.write("\3\u00de\3\u00de\3\u00de\3\u00de\7\u00de\u0a77\n\u00de")
        buf.write("\f\u00de\16\u00de\u0a7a\13\u00de\3\u00df\3\u00df\3\u00df")
        buf.write("\3\u00df\3\u00df\3\u00df\3\u00df\3\u00df\3\u00df\7\u00df")
        buf.write("\u0a85\n\u00df\f\u00df\16\u00df\u0a88\13\u00df\3\u00e0")
        buf.write("\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e0")
        buf.write("\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e0")
        buf.write("\3\u00e0\3\u00e0\3\u00e0\7\u00e0\u0a9c\n\u00e0\f\u00e0")
        buf.write("\16\u00e0\u0a9f\13\u00e0\3\u00e1\3\u00e1\3\u00e1\3\u00e1")
        buf.write("\3\u00e1\3\u00e1\3\u00e1\3\u00e1\3\u00e1\3\u00e1\3\u00e1")
        buf.write("\3\u00e1\3\u00e1\3\u00e1\3\u00e1\3\u00e1\7\u00e1\u0ab1")
        buf.write("\n\u00e1\f\u00e1\16\u00e1\u0ab4\13\u00e1\3\u00e2\3\u00e2")
        buf.write("\3\u00e2\3\u00e2\3\u00e2\3\u00e2\3\u00e2\3\u00e2\3\u00e2")
        buf.write("\7\u00e2\u0abf\n\u00e2\f\u00e2\16\u00e2\u0ac2\13\u00e2")
        buf.write("\3\u00e3\3\u00e3\3\u00e3\3\u00e3\3\u00e3\3\u00e3\3\u00e3")
        buf.write("\3\u00e3\3\u00e3\3\u00e3\3\u00e3\3\u00e3\7\u00e3\u0ad0")
        buf.write("\n\u00e3\f\u00e3\16\u00e3\u0ad3\13\u00e3\3\u00e4\3\u00e4")
        buf.write("\3\u00e4\3\u00e4\3\u00e4\3\u00e4\3\u00e4\5\u00e4\u0adc")
        buf.write("\n\u00e4\3\u00e5\3\u00e5\3\u00e5\3\u00e6\3\u00e6\3\u00e6")
        buf.write("\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7\5\u00e7")
        buf.write("\u0aea\n\u00e7\3\u00e8\3\u00e8\5\u00e8\u0aee\n\u00e8\3")
        buf.write("\u00e8\3\u00e8\7\u00e8\u0af2\n\u00e8\f\u00e8\16\u00e8")
        buf.write("\u0af5\13\u00e8\3\u00e9\3\u00e9\3\u00e9\3\u00ea\3\u00ea")
        buf.write("\3\u00eb\3\u00eb\3\u00eb\3\u00ec\3\u00ec\3\u00ed\3\u00ed")
        buf.write("\3\u00ed\3\u00ed\3\u00ed\3\u00ed\3\u00ed\3\u00ed\7\u00ed")
        buf.write("\u0b09\n\u00ed\f\u00ed\16\u00ed\u0b0c\13\u00ed\3\u00ed")
        buf.write("\3\u00ed\3\u00ed\3\u00ed\3\u00ed\3\u00ed\7\u00ed\u0b14")
        buf.write("\n\u00ed\f\u00ed\16\u00ed\u0b17\13\u00ed\3\u00ed\3\u00ed")
        buf.write("\3\u00ed\5\u00ed\u0b1c\n\u00ed\3\u00ed\2\17\648>\u01b2")
        buf.write("\u01b4\u01b6\u01b8\u01ba\u01bc\u01be\u01c0\u01c2\u01c4")
        buf.write("\u00ee\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write("\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4")
        buf.write("\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6")
        buf.write("\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8")
        buf.write("\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da")
        buf.write("\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec")
        buf.write("\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe")
        buf.write("\u0100\u0102\u0104\u0106\u0108\u010a\u010c\u010e\u0110")
        buf.write("\u0112\u0114\u0116\u0118\u011a\u011c\u011e\u0120\u0122")
        buf.write("\u0124\u0126\u0128\u012a\u012c\u012e\u0130\u0132\u0134")
        buf.write("\u0136\u0138\u013a\u013c\u013e\u0140\u0142\u0144\u0146")
        buf.write("\u0148\u014a\u014c\u014e\u0150\u0152\u0154\u0156\u0158")
        buf.write("\u015a\u015c\u015e\u0160\u0162\u0164\u0166\u0168\u016a")
        buf.write("\u016c\u016e\u0170\u0172\u0174\u0176\u0178\u017a\u017c")
        buf.write("\u017e\u0180\u0182\u0184\u0186\u0188\u018a\u018c\u018e")
        buf.write("\u0190\u0192\u0194\u0196\u0198\u019a\u019c\u019e\u01a0")
        buf.write("\u01a2\u01a4\u01a6\u01a8\u01aa\u01ac\u01ae\u01b0\u01b2")
        buf.write("\u01b4\u01b6\u01b8\u01ba\u01bc\u01be\u01c0\u01c2\u01c4")
        buf.write("\u01c6\u01c8\u01ca\u01cc\u01ce\u01d0\u01d2\u01d4\u01d6")
        buf.write("\u01d8\2\6\3\2\65:\7\2\7\7\n\n\35\35\37\37\'\'\4\2\20")
        buf.write("\20\26\26\4\2DD]g\2\u0c0f\2\u01da\3\2\2\2\4\u01ea\3\2")
        buf.write("\2\2\6\u01ee\3\2\2\2\b\u01f0\3\2\2\2\n\u01f2\3\2\2\2\f")
        buf.write("\u01f7\3\2\2\2\16\u01fb\3\2\2\2\20\u021a\3\2\2\2\22\u021c")
        buf.write("\3\2\2\2\24\u022a\3\2\2\2\26\u0231\3\2\2\2\30\u0233\3")
        buf.write("\2\2\2\32\u0235\3\2\2\2\34\u023a\3\2\2\2\36\u0248\3\2")
        buf.write("\2\2 \u024d\3\2\2\2\"\u0262\3\2\2\2$\u0269\3\2\2\2&\u0275")
        buf.write("\3\2\2\2(\u0277\3\2\2\2*\u027a\3\2\2\2,\u027e\3\2\2\2")
        buf.write(".\u0288\3\2\2\2\60\u028d\3\2\2\2\62\u0298\3\2\2\2\64\u029a")
        buf.write("\3\2\2\2\66\u02aa\3\2\2\28\u02ac\3\2\2\2:\u02bc\3\2\2")
        buf.write("\2<\u02be\3\2\2\2>\u02c0\3\2\2\2@\u02cc\3\2\2\2B\u02df")
        buf.write("\3\2\2\2D\u02e6\3\2\2\2F\u02ec\3\2\2\2H\u02ee\3\2\2\2")
        buf.write("J\u02f2\3\2\2\2L\u02f8\3\2\2\2N\u02ff\3\2\2\2P\u0309\3")
        buf.write("\2\2\2R\u030d\3\2\2\2T\u0312\3\2\2\2V\u032a\3\2\2\2X\u032c")
        buf.write("\3\2\2\2Z\u0330\3\2\2\2\\\u0338\3\2\2\2^\u033b\3\2\2\2")
        buf.write("`\u033e\3\2\2\2b\u0346\3\2\2\2d\u0353\3\2\2\2f\u035a\3")
        buf.write("\2\2\2h\u035f\3\2\2\2j\u036e\3\2\2\2l\u0370\3\2\2\2n\u0378")
        buf.write("\3\2\2\2p\u037d\3\2\2\2r\u0383\3\2\2\2t\u0387\3\2\2\2")
        buf.write("v\u038b\3\2\2\2x\u0390\3\2\2\2z\u0394\3\2\2\2|\u03ad\3")
        buf.write("\2\2\2~\u03af\3\2\2\2\u0080\u03ba\3\2\2\2\u0082\u03be")
        buf.write("\3\2\2\2\u0084\u03c0\3\2\2\2\u0086\u03c2\3\2\2\2\u0088")
        buf.write("\u03c4\3\2\2\2\u008a\u03cf\3\2\2\2\u008c\u03d4\3\2\2\2")
        buf.write("\u008e\u03e4\3\2\2\2\u0090\u03f7\3\2\2\2\u0092\u03fb\3")
        buf.write("\2\2\2\u0094\u03fd\3\2\2\2\u0096\u040c\3\2\2\2\u0098\u041e")
        buf.write("\3\2\2\2\u009a\u0423\3\2\2\2\u009c\u042b\3\2\2\2\u009e")
        buf.write("\u043e\3\2\2\2\u00a0\u0443\3\2\2\2\u00a2\u044d\3\2\2\2")
        buf.write("\u00a4\u0450\3\2\2\2\u00a6\u045a\3\2\2\2\u00a8\u045e\3")
        buf.write("\2\2\2\u00aa\u0460\3\2\2\2\u00ac\u0462\3\2\2\2\u00ae\u0468")
        buf.write("\3\2\2\2\u00b0\u0475\3\2\2\2\u00b2\u0478\3\2\2\2\u00b4")
        buf.write("\u0481\3\2\2\2\u00b6\u0483\3\2\2\2\u00b8\u04ba\3\2\2\2")
        buf.write("\u00ba\u04bf\3\2\2\2\u00bc\u04c9\3\2\2\2\u00be\u04d5\3")
        buf.write("\2\2\2\u00c0\u04e0\3\2\2\2\u00c2\u04ee\3\2\2\2\u00c4\u04f0")
        buf.write("\3\2\2\2\u00c6\u04f9\3\2\2\2\u00c8\u04fe\3\2\2\2\u00ca")
        buf.write("\u0512\3\2\2\2\u00cc\u0514\3\2\2\2\u00ce\u0517\3\2\2\2")
        buf.write("\u00d0\u0525\3\2\2\2\u00d2\u052a\3\2\2\2\u00d4\u0535\3")
        buf.write("\2\2\2\u00d6\u053a\3\2\2\2\u00d8\u0546\3\2\2\2\u00da\u054b")
        buf.write("\3\2\2\2\u00dc\u0553\3\2\2\2\u00de\u0561\3\2\2\2\u00e0")
        buf.write("\u0566\3\2\2\2\u00e2\u0578\3\2\2\2\u00e4\u057a\3\2\2\2")
        buf.write("\u00e6\u0580\3\2\2\2\u00e8\u0582\3\2\2\2\u00ea\u058a\3")
        buf.write("\2\2\2\u00ec\u0592\3\2\2\2\u00ee\u0599\3\2\2\2\u00f0\u059b")
        buf.write("\3\2\2\2\u00f2\u05a4\3\2\2\2\u00f4\u05ac\3\2\2\2\u00f6")
        buf.write("\u05af\3\2\2\2\u00f8\u05b5\3\2\2\2\u00fa\u05be\3\2\2\2")
        buf.write("\u00fc\u05c6\3\2\2\2\u00fe\u05cd\3\2\2\2\u0100\u05d4\3")
        buf.write("\2\2\2\u0102\u05d6\3\2\2\2\u0104\u05dc\3\2\2\2\u0106\u05e8")
        buf.write("\3\2\2\2\u0108\u05ef\3\2\2\2\u010a\u05fd\3\2\2\2\u010c")
        buf.write("\u05ff\3\2\2\2\u010e\u0601\3\2\2\2\u0110\u0605\3\2\2\2")
        buf.write("\u0112\u0609\3\2\2\2\u0114\u0613\3\2\2\2\u0116\u0615\3")
        buf.write("\2\2\2\u0118\u061b\3\2\2\2\u011a\u0623\3\2\2\2\u011c\u0635")
        buf.write("\3\2\2\2\u011e\u0637\3\2\2\2\u0120\u063d\3\2\2\2\u0122")
        buf.write("\u064c\3\2\2\2\u0124\u064f\3\2\2\2\u0126\u0660\3\2\2\2")
        buf.write("\u0128\u0662\3\2\2\2\u012a\u0664\3\2\2\2\u012c\u066a\3")
        buf.write("\2\2\2\u012e\u0670\3\2\2\2\u0130\u067a\3\2\2\2\u0132\u067e")
        buf.write("\3\2\2\2\u0134\u0680\3\2\2\2\u0136\u0690\3\2\2\2\u0138")
        buf.write("\u06a2\3\2\2\2\u013a\u06a4\3\2\2\2\u013c\u06a6\3\2\2\2")
        buf.write("\u013e\u06ae\3\2\2\2\u0140\u06bd\3\2\2\2\u0142\u06cc\3")
        buf.write("\2\2\2\u0144\u06d2\3\2\2\2\u0146\u06d8\3\2\2\2\u0148\u06de")
        buf.write("\3\2\2\2\u014a\u06e2\3\2\2\2\u014c\u06f4\3\2\2\2\u014e")
        buf.write("\u06f6\3\2\2\2\u0150\u06fd\3\2\2\2\u0152\u0706\3\2\2\2")
        buf.write("\u0154\u070c\3\2\2\2\u0156\u0714\3\2\2\2\u0158\u0717\3")
        buf.write("\2\2\2\u015a\u0720\3\2\2\2\u015c\u0727\3\2\2\2\u015e\u0732")
        buf.write("\3\2\2\2\u0160\u073c\3\2\2\2\u0162\u0761\3\2\2\2\u0164")
        buf.write("\u0763\3\2\2\2\u0166\u0781\3\2\2\2\u0168\u0788\3\2\2\2")
        buf.write("\u016a\u078a\3\2\2\2\u016c\u0790\3\2\2\2\u016e\u07ba\3")
        buf.write("\2\2\2\u0170\u07bc\3\2\2\2\u0172\u07e5\3\2\2\2\u0174\u083a")
        buf.write("\3\2\2\2\u0176\u083c\3\2\2\2\u0178\u088e\3\2\2\2\u017a")
        buf.write("\u0893\3\2\2\2\u017c\u08a2\3\2\2\2\u017e\u08a4\3\2\2\2")
        buf.write("\u0180\u08b0\3\2\2\2\u0182\u08bc\3\2\2\2\u0184\u08c8\3")
        buf.write("\2\2\2\u0186\u08e1\3\2\2\2\u0188\u0931\3\2\2\2\u018a\u0933")
        buf.write("\3\2\2\2\u018c\u0976\3\2\2\2\u018e\u0978\3\2\2\2\u0190")
        buf.write("\u09af\3\2\2\2\u0192\u09b1\3\2\2\2\u0194\u09df\3\2\2\2")
        buf.write("\u0196\u09f7\3\2\2\2\u0198\u09f9\3\2\2\2\u019a\u0a03\3")
        buf.write("\2\2\2\u019c\u0a0a\3\2\2\2\u019e\u0a0e\3\2\2\2\u01a0\u0a10")
        buf.write("\3\2\2\2\u01a2\u0a1e\3\2\2\2\u01a4\u0a20\3\2\2\2\u01a6")
        buf.write("\u0a2a\3\2\2\2\u01a8\u0a2e\3\2\2\2\u01aa\u0a30\3\2\2\2")
        buf.write("\u01ac\u0a37\3\2\2\2\u01ae\u0a39\3\2\2\2\u01b0\u0a42\3")
        buf.write("\2\2\2\u01b2\u0a44\3\2\2\2\u01b4\u0a4f\3\2\2\2\u01b6\u0a5a")
        buf.write("\3\2\2\2\u01b8\u0a65\3\2\2\2\u01ba\u0a70\3\2\2\2\u01bc")
        buf.write("\u0a7b\3\2\2\2\u01be\u0a89\3\2\2\2\u01c0\u0aa0\3\2\2\2")
        buf.write("\u01c2\u0ab5\3\2\2\2\u01c4\u0ac3\3\2\2\2\u01c6\u0adb\3")
        buf.write("\2\2\2\u01c8\u0add\3\2\2\2\u01ca\u0ae0\3\2\2\2\u01cc\u0ae9")
        buf.write("\3\2\2\2\u01ce\u0aed\3\2\2\2\u01d0\u0af6\3\2\2\2\u01d2")
        buf.write("\u0af9\3\2\2\2\u01d4\u0afb\3\2\2\2\u01d6\u0afe\3\2\2\2")
        buf.write("\u01d8\u0b1b\3\2\2\2\u01da\u01db\t\2\2\2\u01db\3\3\2\2")
        buf.write("\2\u01dc\u01de\5\u00e6t\2\u01dd\u01dc\3\2\2\2\u01de\u01e1")
        buf.write("\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("\u01e2\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01eb\5\6\4\2")
        buf.write("\u01e3\u01e5\5\u00e6t\2\u01e4\u01e3\3\2\2\2\u01e5\u01e8")
        buf.write("\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u01e9\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9\u01eb\7\5\2\2")
        buf.write("\u01ea\u01df\3\2\2\2\u01ea\u01e6\3\2\2\2\u01eb\5\3\2\2")
        buf.write("\2\u01ec\u01ef\5\b\5\2\u01ed\u01ef\5\n\6\2\u01ee\u01ec")
        buf.write("\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef\7\3\2\2\2\u01f0\u01f1")
        buf.write("\t\3\2\2\u01f1\t\3\2\2\2\u01f2\u01f3\t\4\2\2\u01f3\13")
        buf.write("\3\2\2\2\u01f4\u01f8\5\16\b\2\u01f5\u01f8\5\34\17\2\u01f6")
        buf.write("\u01f8\5\36\20\2\u01f7\u01f4\3\2\2\2\u01f7\u01f5\3\2\2")
        buf.write("\2\u01f7\u01f6\3\2\2\2\u01f8\r\3\2\2\2\u01f9\u01fc\5\24")
        buf.write("\13\2\u01fa\u01fc\5\32\16\2\u01fb\u01f9\3\2\2\2\u01fb")
        buf.write("\u01fa\3\2\2\2\u01fc\u0201\3\2\2\2\u01fd\u0200\5\22\n")
        buf.write("\2\u01fe\u0200\5\30\r\2\u01ff\u01fd\3\2\2\2\u01ff\u01fe")
        buf.write("\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\17\3\2\2\2\u0203\u0201\3\2\2\2\u0204")
        buf.write("\u0206\5\u00e6t\2\u0205\u0204\3\2\2\2\u0206\u0209\3\2")
        buf.write("\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u020a")
        buf.write("\3\2\2\2\u0209\u0207\3\2\2\2\u020a\u020c\7h\2\2\u020b")
        buf.write("\u020d\5*\26\2\u020c\u020b\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020d\u021b\3\2\2\2\u020e\u020f\5\16\b\2\u020f\u0213")
        buf.write("\7C\2\2\u0210\u0212\5\u00e6t\2\u0211\u0210\3\2\2\2\u0212")
        buf.write("\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2")
        buf.write("\u0214\u0216\3\2\2\2\u0215\u0213\3\2\2\2\u0216\u0218\7")
        buf.write("h\2\2\u0217\u0219\5*\26\2\u0218\u0217\3\2\2\2\u0218\u0219")
        buf.write("\3\2\2\2\u0219\u021b\3\2\2\2\u021a\u0207\3\2\2\2\u021a")
        buf.write("\u020e\3\2\2\2\u021b\21\3\2\2\2\u021c\u0220\7C\2\2\u021d")
        buf.write("\u021f\5\u00e6t\2\u021e\u021d\3\2\2\2\u021f\u0222\3\2")
        buf.write("\2\2\u0220\u021e\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0223")
        buf.write("\3\2\2\2\u0222\u0220\3\2\2\2\u0223\u0225\7h\2\2\u0224")
        buf.write("\u0226\5*\26\2\u0225\u0224\3\2\2\2\u0225\u0226\3\2\2\2")
        buf.write("\u0226\23\3\2\2\2\u0227\u0229\5\u00e6t\2\u0228\u0227\3")
        buf.write("\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2\2\2\u022a\u022b")
        buf.write("\3\2\2\2\u022b\u022d\3\2\2\2\u022c\u022a\3\2\2\2\u022d")
        buf.write("\u022f\7h\2\2\u022e\u0230\5*\26\2\u022f\u022e\3\2\2\2")
        buf.write("\u022f\u0230\3\2\2\2\u0230\25\3\2\2\2\u0231\u0232\5\20")
        buf.write("\t\2\u0232\27\3\2\2\2\u0233\u0234\5\22\n\2\u0234\31\3")
        buf.write("\2\2\2\u0235\u0236\5\24\13\2\u0236\33\3\2\2\2\u0237\u0239")
        buf.write("\5\u00e6t\2\u0238\u0237\3\2\2\2\u0239\u023c\3\2\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023d\3\2\2\2")
        buf.write("\u023c\u023a\3\2\2\2\u023d\u023e\7h\2\2\u023e\35\3\2\2")
        buf.write("\2\u023f\u0240\5\4\3\2\u0240\u0241\5 \21\2\u0241\u0249")
        buf.write("\3\2\2\2\u0242\u0243\5\16\b\2\u0243\u0244\5 \21\2\u0244")
        buf.write("\u0249\3\2\2\2\u0245\u0246\5\34\17\2\u0246\u0247\5 \21")
        buf.write("\2\u0247\u0249\3\2\2\2\u0248\u023f\3\2\2\2\u0248\u0242")
        buf.write("\3\2\2\2\u0248\u0245\3\2\2\2\u0249\37\3\2\2\2\u024a\u024c")
        buf.write("\5\u00e6t\2\u024b\u024a\3\2\2\2\u024c\u024f\3\2\2\2\u024d")
        buf.write("\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u0250\3\2\2\2")
        buf.write("\u024f\u024d\3\2\2\2\u0250\u0251\7?\2\2\u0251\u025c\7")
        buf.write("@\2\2\u0252\u0254\5\u00e6t\2\u0253\u0252\3\2\2\2\u0254")
        buf.write("\u0257\3\2\2\2\u0255\u0253\3\2\2\2\u0255\u0256\3\2\2\2")
        buf.write("\u0256\u0258\3\2\2\2\u0257\u0255\3\2\2\2\u0258\u0259\7")
        buf.write("?\2\2\u0259\u025b\7@\2\2\u025a\u0255\3\2\2\2\u025b\u025e")
        buf.write("\3\2\2\2\u025c\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d")
        buf.write("!\3\2\2\2\u025e\u025c\3\2\2\2\u025f\u0261\5$\23\2\u0260")
        buf.write("\u025f\3\2\2\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2")
        buf.write("\u0262\u0263\3\2\2\2\u0263\u0265\3\2\2\2\u0264\u0262\3")
        buf.write("\2\2\2\u0265\u0267\7h\2\2\u0266\u0268\5&\24\2\u0267\u0266")
        buf.write("\3\2\2\2\u0267\u0268\3\2\2\2\u0268#\3\2\2\2\u0269\u026a")
        buf.write("\5\u00e6t\2\u026a%\3\2\2\2\u026b\u026c\7\23\2\2\u026c")
        buf.write("\u0276\5\34\17\2\u026d\u026e\7\23\2\2\u026e\u0272\5\16")
        buf.write("\b\2\u026f\u0271\5(\25\2\u0270\u026f\3\2\2\2\u0271\u0274")
        buf.write("\3\2\2\2\u0272\u0270\3\2\2\2\u0272\u0273\3\2\2\2\u0273")
        buf.write("\u0276\3\2\2\2\u0274\u0272\3\2\2\2\u0275\u026b\3\2\2\2")
        buf.write("\u0275\u026d\3\2\2\2\u0276\'\3\2\2\2\u0277\u0278\7W\2")
        buf.write("\2\u0278\u0279\5\26\f\2\u0279)\3\2\2\2\u027a\u027b\7F")
        buf.write("\2\2\u027b\u027c\5,\27\2\u027c\u027d\7E\2\2\u027d+\3\2")
        buf.write("\2\2\u027e\u0283\5.\30\2\u027f\u0280\7B\2\2\u0280\u0282")
        buf.write("\5.\30\2\u0281\u027f\3\2\2\2\u0282\u0285\3\2\2\2\u0283")
        buf.write("\u0281\3\2\2\2\u0283\u0284\3\2\2\2\u0284-\3\2\2\2\u0285")
        buf.write("\u0283\3\2\2\2\u0286\u0289\5\f\7\2\u0287\u0289\5\60\31")
        buf.write("\2\u0288\u0286\3\2\2\2\u0288\u0287\3\2\2\2\u0289/\3\2")
        buf.write("\2\2\u028a\u028c\5\u00e6t\2\u028b\u028a\3\2\2\2\u028c")
        buf.write("\u028f\3\2\2\2\u028d\u028b\3\2\2\2\u028d\u028e\3\2\2\2")
        buf.write("\u028e\u0290\3\2\2\2\u028f\u028d\3\2\2\2\u0290\u0292\7")
        buf.write("I\2\2\u0291\u0293\5\62\32\2\u0292\u0291\3\2\2\2\u0292")
        buf.write("\u0293\3\2\2\2\u0293\61\3\2\2\2\u0294\u0295\7\23\2\2\u0295")
        buf.write("\u0299\5\f\7\2\u0296\u0297\7*\2\2\u0297\u0299\5\f\7\2")
        buf.write("\u0298\u0294\3\2\2\2\u0298\u0296\3\2\2\2\u0299\63\3\2")
        buf.write("\2\2\u029a\u029b\b\33\1\2\u029b\u029c\7h\2\2\u029c\u02a2")
        buf.write("\3\2\2\2\u029d\u029e\f\3\2\2\u029e\u029f\7C\2\2\u029f")
        buf.write("\u02a1\7h\2\2\u02a0\u029d\3\2\2\2\u02a1\u02a4\3\2\2\2")
        buf.write("\u02a2\u02a0\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3\65\3\2")
        buf.write("\2\2\u02a4\u02a2\3\2\2\2\u02a5\u02ab\7h\2\2\u02a6\u02a7")
        buf.write("\58\35\2\u02a7\u02a8\7C\2\2\u02a8\u02a9\7h\2\2\u02a9\u02ab")
        buf.write("\3\2\2\2\u02aa\u02a5\3\2\2\2\u02aa\u02a6\3\2\2\2\u02ab")
        buf.write("\67\3\2\2\2\u02ac\u02ad\b\35\1\2\u02ad\u02ae\7h\2\2\u02ae")
        buf.write("\u02b4\3\2\2\2\u02af\u02b0\f\3\2\2\u02b0\u02b1\7C\2\2")
        buf.write("\u02b1\u02b3\7h\2\2\u02b2\u02af\3\2\2\2\u02b3\u02b6\3")
        buf.write("\2\2\2\u02b4\u02b2\3\2\2\2\u02b4\u02b5\3\2\2\2\u02b59")
        buf.write("\3\2\2\2\u02b6\u02b4\3\2\2\2\u02b7\u02bd\7h\2\2\u02b8")
        buf.write("\u02b9\5> \2\u02b9\u02ba\7C\2\2\u02ba\u02bb\7h\2\2\u02bb")
        buf.write("\u02bd\3\2\2\2\u02bc\u02b7\3\2\2\2\u02bc\u02b8\3\2\2\2")
        buf.write("\u02bd;\3\2\2\2\u02be\u02bf\7h\2\2\u02bf=\3\2\2\2\u02c0")
        buf.write("\u02c1\b \1\2\u02c1\u02c2\7h\2\2\u02c2\u02c8\3\2\2\2\u02c3")
        buf.write("\u02c4\f\3\2\2\u02c4\u02c5\7C\2\2\u02c5\u02c7\7h\2\2\u02c6")
        buf.write("\u02c3\3\2\2\2\u02c7\u02ca\3\2\2\2\u02c8\u02c6\3\2\2\2")
        buf.write("\u02c8\u02c9\3\2\2\2\u02c9?\3\2\2\2\u02ca\u02c8\3\2\2")
        buf.write("\2\u02cb\u02cd\5B\"\2\u02cc\u02cb\3\2\2\2\u02cc\u02cd")
        buf.write("\3\2\2\2\u02cd\u02d1\3\2\2\2\u02ce\u02d0\5F$\2\u02cf\u02ce")
        buf.write("\3\2\2\2\u02d0\u02d3\3\2\2\2\u02d1\u02cf\3\2\2\2\u02d1")
        buf.write("\u02d2\3\2\2\2\u02d2\u02d7\3\2\2\2\u02d3\u02d1\3\2\2\2")
        buf.write("\u02d4\u02d6\5P)\2\u02d5\u02d4\3\2\2\2\u02d6\u02d9\3\2")
        buf.write("\2\2\u02d7\u02d5\3\2\2\2\u02d7\u02d8\3\2\2\2\u02d8\u02da")
        buf.write("\3\2\2\2\u02d9\u02d7\3\2\2\2\u02da\u02db\7\2\2\3\u02db")
        buf.write("A\3\2\2\2\u02dc\u02de\5D#\2\u02dd\u02dc\3\2\2\2\u02de")
        buf.write("\u02e1\3\2\2\2\u02df\u02dd\3\2\2\2\u02df\u02e0\3\2\2\2")
        buf.write("\u02e0\u02e2\3\2\2\2\u02e1\u02df\3\2\2\2\u02e2\u02e3\7")
        buf.write("\"\2\2\u02e3\u02e4\5\64\33\2\u02e4\u02e5\7A\2\2\u02e5")
        buf.write("C\3\2\2\2\u02e6\u02e7\5\u00e6t\2\u02e7E\3\2\2\2\u02e8")
        buf.write("\u02ed\5H%\2\u02e9\u02ed\5J&\2\u02ea\u02ed\5L\'\2\u02eb")
        buf.write("\u02ed\5N(\2\u02ec\u02e8\3\2\2\2\u02ec\u02e9\3\2\2\2\u02ec")
        buf.write("\u02ea\3\2\2\2\u02ec\u02eb\3\2\2\2\u02edG\3\2\2\2\u02ee")
        buf.write("\u02ef\7\33\2\2\u02ef\u02f0\5\66\34\2\u02f0\u02f1\7A\2")
        buf.write("\2\u02f1I\3\2\2\2\u02f2\u02f3\7\33\2\2\u02f3\u02f4\58")
        buf.write("\35\2\u02f4\u02f5\7C\2\2\u02f5\u02f6\7U\2\2\u02f6\u02f7")
        buf.write("\7A\2\2\u02f7K\3\2\2\2\u02f8\u02f9\7\33\2\2\u02f9\u02fa")
        buf.write("\7(\2\2\u02fa\u02fb\5\66\34\2\u02fb\u02fc\7C\2\2\u02fc")
        buf.write("\u02fd\7h\2\2\u02fd\u02fe\7A\2\2\u02feM\3\2\2\2\u02ff")
        buf.write("\u0300\7\33\2\2\u0300\u0301\7(\2\2\u0301\u0302\5\66\34")
        buf.write("\2\u0302\u0303\7C\2\2\u0303\u0304\7U\2\2\u0304\u0305\7")
        buf.write("A\2\2\u0305O\3\2\2\2\u0306\u030a\5R*\2\u0307\u030a\5\u00c6")
        buf.write("d\2\u0308\u030a\7A\2\2\u0309\u0306\3\2\2\2\u0309\u0307")
        buf.write("\3\2\2\2\u0309\u0308\3\2\2\2\u030aQ\3\2\2\2\u030b\u030e")
        buf.write("\5T+\2\u030c\u030e\5\u00ba^\2\u030d\u030b\3\2\2\2\u030d")
        buf.write("\u030c\3\2\2\2\u030eS\3\2\2\2\u030f\u0311\5V,\2\u0310")
        buf.write("\u030f\3\2\2\2\u0311\u0314\3\2\2\2\u0312\u0310\3\2\2\2")
        buf.write("\u0312\u0313\3\2\2\2\u0313\u0315\3\2\2\2\u0314\u0312\3")
        buf.write("\2\2\2\u0315\u0316\7\13\2\2\u0316\u0318\7h\2\2\u0317\u0319")
        buf.write("\5X-\2\u0318\u0317\3\2\2\2\u0318\u0319\3\2\2\2\u0319\u031b")
        buf.write("\3\2\2\2\u031a\u031c\5\\/\2\u031b\u031a\3\2\2\2\u031b")
        buf.write("\u031c\3\2\2\2\u031c\u031e\3\2\2\2\u031d\u031f\5^\60\2")
        buf.write("\u031e\u031d\3\2\2\2\u031e\u031f\3\2\2\2\u031f\u0320\3")
        buf.write("\2\2\2\u0320\u0321\5b\62\2\u0321U\3\2\2\2\u0322\u032b")
        buf.write("\5\u00e6t\2\u0323\u032b\7%\2\2\u0324\u032b\7$\2\2\u0325")
        buf.write("\u032b\7#\2\2\u0326\u032b\7\3\2\2\u0327\u032b\7(\2\2\u0328")
        buf.write("\u032b\7\24\2\2\u0329\u032b\7)\2\2\u032a\u0322\3\2\2\2")
        buf.write("\u032a\u0323\3\2\2\2\u032a\u0324\3\2\2\2\u032a\u0325\3")
        buf.write("\2\2\2\u032a\u0326\3\2\2\2\u032a\u0327\3\2\2\2\u032a\u0328")
        buf.write("\3\2\2\2\u032a\u0329\3\2\2\2\u032bW\3\2\2\2\u032c\u032d")
        buf.write("\7F\2\2\u032d\u032e\5Z.\2\u032e\u032f\7E\2\2\u032fY\3")
        buf.write("\2\2\2\u0330\u0335\5\"\22\2\u0331\u0332\7B\2\2\u0332\u0334")
        buf.write("\5\"\22\2\u0333\u0331\3\2\2\2\u0334\u0337\3\2\2\2\u0335")
        buf.write("\u0333\3\2\2\2\u0335\u0336\3\2\2\2\u0336[\3\2\2\2\u0337")
        buf.write("\u0335\3\2\2\2\u0338\u0339\7\23\2\2\u0339\u033a\5\20\t")
        buf.write("\2\u033a]\3\2\2\2\u033b\u033c\7\32\2\2\u033c\u033d\5`")
        buf.write("\61\2\u033d_\3\2\2\2\u033e\u0343\5\26\f\2\u033f\u0340")
        buf.write("\7B\2\2\u0340\u0342\5\26\f\2\u0341\u033f\3\2\2\2\u0342")
        buf.write("\u0345\3\2\2\2\u0343\u0341\3\2\2\2\u0343\u0344\3\2\2\2")
        buf.write("\u0344a\3\2\2\2\u0345\u0343\3\2\2\2\u0346\u034a\7=\2\2")
        buf.write("\u0347\u0349\5d\63\2\u0348\u0347\3\2\2\2\u0349\u034c\3")
        buf.write("\2\2\2\u034a\u0348\3\2\2\2\u034a\u034b\3\2\2\2\u034b\u034d")
        buf.write("\3\2\2\2\u034c\u034a\3\2\2\2\u034d\u034e\7>\2\2\u034e")
        buf.write("c\3\2\2\2\u034f\u0354\5f\64\2\u0350\u0354\5\u00aaV\2\u0351")
        buf.write("\u0354\5\u00acW\2\u0352\u0354\5\u00aeX\2\u0353\u034f\3")
        buf.write("\2\2\2\u0353\u0350\3\2\2\2\u0353\u0351\3\2\2\2\u0353\u0352")
        buf.write("\3\2\2\2\u0354e\3\2\2\2\u0355\u035b\5h\65\2\u0356\u035b")
        buf.write("\5\u008cG\2\u0357\u035b\5R*\2\u0358\u035b\5\u00c6d\2\u0359")
        buf.write("\u035b\7A\2\2\u035a\u0355\3\2\2\2\u035a\u0356\3\2\2\2")
        buf.write("\u035a\u0357\3\2\2\2\u035a\u0358\3\2\2\2\u035a\u0359\3")
        buf.write("\2\2\2\u035bg\3\2\2\2\u035c\u035e\5j\66\2\u035d\u035c")
        buf.write("\3\2\2\2\u035e\u0361\3\2\2\2\u035f\u035d\3\2\2\2\u035f")
        buf.write("\u0360\3\2\2\2\u0360\u0362\3\2\2\2\u0361\u035f\3\2\2\2")
        buf.write("\u0362\u0363\5t;\2\u0363\u0364\5l\67\2\u0364\u0365\7A")
        buf.write("\2\2\u0365i\3\2\2\2\u0366\u036f\5\u00e6t\2\u0367\u036f")
        buf.write("\7%\2\2\u0368\u036f\7$\2\2\u0369\u036f\7#\2\2\u036a\u036f")
        buf.write("\7(\2\2\u036b\u036f\7\24\2\2\u036c\u036f\7\60\2\2\u036d")
        buf.write("\u036f\7\63\2\2\u036e\u0366\3\2\2\2\u036e\u0367\3\2\2")
        buf.write("\2\u036e\u0368\3\2\2\2\u036e\u0369\3\2\2\2\u036e\u036a")
        buf.write("\3\2\2\2\u036e\u036b\3\2\2\2\u036e\u036c\3\2\2\2\u036e")
        buf.write("\u036d\3\2\2\2\u036fk\3\2\2\2\u0370\u0375\5n8\2\u0371")
        buf.write("\u0372\7B\2\2\u0372\u0374\5n8\2\u0373\u0371\3\2\2\2\u0374")
        buf.write("\u0377\3\2\2\2\u0375\u0373\3\2\2\2\u0375\u0376\3\2\2\2")
        buf.write("\u0376m\3\2\2\2\u0377\u0375\3\2\2\2\u0378\u037b\5p9\2")
        buf.write("\u0379\u037a\7D\2\2\u037a\u037c\5r:\2\u037b\u0379\3\2")
        buf.write("\2\2\u037b\u037c\3\2\2\2\u037co\3\2\2\2\u037d\u037f\7")
        buf.write("h\2\2\u037e\u0380\5 \21\2\u037f\u037e\3\2\2\2\u037f\u0380")
        buf.write("\3\2\2\2\u0380q\3\2\2\2\u0381\u0384\5\u019e\u00d0\2\u0382")
        buf.write("\u0384\5\u00f8}\2\u0383\u0381\3\2\2\2\u0383\u0382\3\2")
        buf.write("\2\2\u0384s\3\2\2\2\u0385\u0388\5v<\2\u0386\u0388\5x=")
        buf.write("\2\u0387\u0385\3\2\2\2\u0387\u0386\3\2\2\2\u0388u\3\2")
        buf.write("\2\2\u0389\u038c\5\6\4\2\u038a\u038c\7\5\2\2\u038b\u0389")
        buf.write("\3\2\2\2\u038b\u038a\3\2\2\2\u038cw\3\2\2\2\u038d\u0391")
        buf.write("\5z>\2\u038e\u0391\5\u0088E\2\u038f\u0391\5\u008aF\2\u0390")
        buf.write("\u038d\3\2\2\2\u0390\u038e\3\2\2\2\u0390\u038f\3\2\2\2")
        buf.write("\u0391y\3\2\2\2\u0392\u0395\5\u0080A\2\u0393\u0395\5\u0086")
        buf.write("D\2\u0394\u0392\3\2\2\2\u0394\u0393\3\2\2\2\u0395\u039a")
        buf.write("\3\2\2\2\u0396\u0399\5~@\2\u0397\u0399\5\u0084C\2\u0398")
        buf.write("\u0396\3\2\2\2\u0398\u0397\3\2\2\2\u0399\u039c\3\2\2\2")
        buf.write("\u039a\u0398\3\2\2\2\u039a\u039b\3\2\2\2\u039b{\3\2\2")
        buf.write("\2\u039c\u039a\3\2\2\2\u039d\u039f\7h\2\2\u039e\u03a0")
        buf.write("\5*\26\2\u039f\u039e\3\2\2\2\u039f\u03a0\3\2\2\2\u03a0")
        buf.write("\u03ae\3\2\2\2\u03a1\u03a2\5z>\2\u03a2\u03a6\7C\2\2\u03a3")
        buf.write("\u03a5\5\u00e6t\2\u03a4\u03a3\3\2\2\2\u03a5\u03a8\3\2")
        buf.write("\2\2\u03a6\u03a4\3\2\2\2\u03a6\u03a7\3\2\2\2\u03a7\u03a9")
        buf.write("\3\2\2\2\u03a8\u03a6\3\2\2\2\u03a9\u03ab\7h\2\2\u03aa")
        buf.write("\u03ac\5*\26\2\u03ab\u03aa\3\2\2\2\u03ab\u03ac\3\2\2\2")
        buf.write("\u03ac\u03ae\3\2\2\2\u03ad\u039d\3\2\2\2\u03ad\u03a1\3")
        buf.write("\2\2\2\u03ae}\3\2\2\2\u03af\u03b3\7C\2\2\u03b0\u03b2\5")
        buf.write("\u00e6t\2\u03b1\u03b0\3\2\2\2\u03b2\u03b5\3\2\2\2\u03b3")
        buf.write("\u03b1\3\2\2\2\u03b3\u03b4\3\2\2\2\u03b4\u03b6\3\2\2\2")
        buf.write("\u03b5\u03b3\3\2\2\2\u03b6\u03b8\7h\2\2\u03b7\u03b9\5")
        buf.write("*\26\2\u03b8\u03b7\3\2\2\2\u03b8\u03b9\3\2\2\2\u03b9\177")
        buf.write("\3\2\2\2\u03ba\u03bc\7h\2\2\u03bb\u03bd\5*\26\2\u03bc")
        buf.write("\u03bb\3\2\2\2\u03bc\u03bd\3\2\2\2\u03bd\u0081\3\2\2\2")
        buf.write("\u03be\u03bf\5|?\2\u03bf\u0083\3\2\2\2\u03c0\u03c1\5~")
        buf.write("@\2\u03c1\u0085\3\2\2\2\u03c2\u03c3\5\u0080A\2\u03c3\u0087")
        buf.write("\3\2\2\2\u03c4\u03c5\7h\2\2\u03c5\u0089\3\2\2\2\u03c6")
        buf.write("\u03c7\5v<\2\u03c7\u03c8\5 \21\2\u03c8\u03d0\3\2\2\2\u03c9")
        buf.write("\u03ca\5z>\2\u03ca\u03cb\5 \21\2\u03cb\u03d0\3\2\2\2\u03cc")
        buf.write("\u03cd\5\u0088E\2\u03cd\u03ce\5 \21\2\u03ce\u03d0\3\2")
        buf.write("\2\2\u03cf\u03c6\3\2\2\2\u03cf\u03c9\3\2\2\2\u03cf\u03cc")
        buf.write("\3\2\2\2\u03d0\u008b\3\2\2\2\u03d1\u03d3\5\u008eH\2\u03d2")
        buf.write("\u03d1\3\2\2\2\u03d3\u03d6\3\2\2\2\u03d4\u03d2\3\2\2\2")
        buf.write("\u03d4\u03d5\3\2\2\2\u03d5\u03d7\3\2\2\2\u03d6\u03d4\3")
        buf.write("\2\2\2\u03d7\u03d8\5\u0090I\2\u03d8\u03d9\5\u00a8U\2\u03d9")
        buf.write("\u008d\3\2\2\2\u03da\u03e5\5\u00e6t\2\u03db\u03e5\7%\2")
        buf.write("\2\u03dc\u03e5\7$\2\2\u03dd\u03e5\7#\2\2\u03de\u03e5\7")
        buf.write("\3\2\2\u03df\u03e5\7(\2\2\u03e0\u03e5\7\24\2\2\u03e1\u03e5")
        buf.write("\7,\2\2\u03e2\u03e5\7 \2\2\u03e3\u03e5\7)\2\2\u03e4\u03da")
        buf.write("\3\2\2\2\u03e4\u03db\3\2\2\2\u03e4\u03dc\3\2\2\2\u03e4")
        buf.write("\u03dd\3\2\2\2\u03e4\u03de\3\2\2\2\u03e4\u03df\3\2\2\2")
        buf.write("\u03e4\u03e0\3\2\2\2\u03e4\u03e1\3\2\2\2\u03e4\u03e2\3")
        buf.write("\2\2\2\u03e4\u03e3\3\2\2\2\u03e5\u008f\3\2\2\2\u03e6\u03e7")
        buf.write("\5\u0092J\2\u03e7\u03e9\5\u0094K\2\u03e8\u03ea\5\u00a2")
        buf.write("R\2\u03e9\u03e8\3\2\2\2\u03e9\u03ea\3\2\2\2\u03ea\u03f8")
        buf.write("\3\2\2\2\u03eb\u03ef\5X-\2\u03ec\u03ee\5\u00e6t\2\u03ed")
        buf.write("\u03ec\3\2\2\2\u03ee\u03f1\3\2\2\2\u03ef\u03ed\3\2\2\2")
        buf.write("\u03ef\u03f0\3\2\2\2\u03f0\u03f2\3\2\2\2\u03f1\u03ef\3")
        buf.write("\2\2\2\u03f2\u03f3\5\u0092J\2\u03f3\u03f5\5\u0094K\2\u03f4")
        buf.write("\u03f6\5\u00a2R\2\u03f5\u03f4\3\2\2\2\u03f5\u03f6\3\2")
        buf.write("\2\2\u03f6\u03f8\3\2\2\2\u03f7\u03e6\3\2\2\2\u03f7\u03eb")
        buf.write("\3\2\2\2\u03f8\u0091\3\2\2\2\u03f9\u03fc\5t;\2\u03fa\u03fc")
        buf.write("\7\62\2\2\u03fb\u03f9\3\2\2\2\u03fb\u03fa\3\2\2\2\u03fc")
        buf.write("\u0093\3\2\2\2\u03fd\u03fe\7h\2\2\u03fe\u0400\7;\2\2\u03ff")
        buf.write("\u0401\5\u0096L\2\u0400\u03ff\3\2\2\2\u0400\u0401\3\2")
        buf.write("\2\2\u0401\u0402\3\2\2\2\u0402\u0404\7<\2\2\u0403\u0405")
        buf.write("\5 \21\2\u0404\u0403\3\2\2\2\u0404\u0405\3\2\2\2\u0405")
        buf.write("\u0095\3\2\2\2\u0406\u040d\5\u00a0Q\2\u0407\u0408\5\u0098")
        buf.write("M\2\u0408\u0409\7B\2\2\u0409\u040a\5\u009eP\2\u040a\u040d")
        buf.write("\3\2\2\2\u040b\u040d\5\u009eP\2\u040c\u0406\3\2\2\2\u040c")
        buf.write("\u0407\3\2\2\2\u040c\u040b\3\2\2\2\u040d\u0097\3\2\2\2")
        buf.write("\u040e\u0413\5\u009aN\2\u040f\u0410\7B\2\2\u0410\u0412")
        buf.write("\5\u009aN\2\u0411\u040f\3\2\2\2\u0412\u0415\3\2\2\2\u0413")
        buf.write("\u0411\3\2\2\2\u0413\u0414\3\2\2\2\u0414\u041f\3\2\2\2")
        buf.write("\u0415\u0413\3\2\2\2\u0416\u041b\5\u00a0Q\2\u0417\u0418")
        buf.write("\7B\2\2\u0418\u041a\5\u009aN\2\u0419\u0417\3\2\2\2\u041a")
        buf.write("\u041d\3\2\2\2\u041b\u0419\3\2\2\2\u041b\u041c\3\2\2\2")
        buf.write("\u041c\u041f\3\2\2\2\u041d\u041b\3\2\2\2\u041e\u040e\3")
        buf.write("\2\2\2\u041e\u0416\3\2\2\2\u041f\u0099\3\2\2\2\u0420\u0422")
        buf.write("\5\u009cO\2\u0421\u0420\3\2\2\2\u0422\u0425\3\2\2\2\u0423")
        buf.write("\u0421\3\2\2\2\u0423\u0424\3\2\2\2\u0424\u0426\3\2\2\2")
        buf.write("\u0425\u0423\3\2\2\2\u0426\u0427\5t;\2\u0427\u0428\5p")
        buf.write("9\2\u0428\u009b\3\2\2\2\u0429\u042c\5\u00e6t\2\u042a\u042c")
        buf.write("\7\24\2\2\u042b\u0429\3\2\2\2\u042b\u042a\3\2\2\2\u042c")
        buf.write("\u009d\3\2\2\2\u042d\u042f\5\u009cO\2\u042e\u042d\3\2")
        buf.write("\2\2\u042f\u0432\3\2\2\2\u0430\u042e\3\2\2\2\u0430\u0431")
        buf.write("\3\2\2\2\u0431\u0433\3\2\2\2\u0432\u0430\3\2\2\2\u0433")
        buf.write("\u0437\5t;\2\u0434\u0436\5\u00e6t\2\u0435\u0434\3\2\2")
        buf.write("\2\u0436\u0439\3\2\2\2\u0437\u0435\3\2\2\2\u0437\u0438")
        buf.write("\3\2\2\2\u0438\u043a\3\2\2\2\u0439\u0437\3\2\2\2\u043a")
        buf.write("\u043b\7j\2\2\u043b\u043c\5p9\2\u043c\u043f\3\2\2\2\u043d")
        buf.write("\u043f\5\u009aN\2\u043e\u0430\3\2\2\2\u043e\u043d\3\2")
        buf.write("\2\2\u043f\u009f\3\2\2\2\u0440\u0442\5\u00e6t\2\u0441")
        buf.write("\u0440\3\2\2\2\u0442\u0445\3\2\2\2\u0443\u0441\3\2\2\2")
        buf.write("\u0443\u0444\3\2\2\2\u0444\u0446\3\2\2\2\u0445\u0443\3")
        buf.write("\2\2\2\u0446\u0449\5t;\2\u0447\u0448\7h\2\2\u0448\u044a")
        buf.write("\7C\2\2\u0449\u0447\3\2\2\2\u0449\u044a\3\2\2\2\u044a")
        buf.write("\u044b\3\2\2\2\u044b\u044c\7-\2\2\u044c\u00a1\3\2\2\2")
        buf.write("\u044d\u044e\7/\2\2\u044e\u044f\5\u00a4S\2\u044f\u00a3")
        buf.write("\3\2\2\2\u0450\u0455\5\u00a6T\2\u0451\u0452\7B\2\2\u0452")
        buf.write("\u0454\5\u00a6T\2\u0453\u0451\3\2\2\2\u0454\u0457\3\2")
        buf.write("\2\2\u0455\u0453\3\2\2\2\u0455\u0456\3\2\2\2\u0456\u00a5")
        buf.write("\3\2\2\2\u0457\u0455\3\2\2\2\u0458\u045b\5\20\t\2\u0459")
        buf.write("\u045b\5\34\17\2\u045a\u0458\3\2\2\2\u045a\u0459\3\2\2")
        buf.write("\2\u045b\u00a7\3\2\2\2\u045c\u045f\5\u00fc\177\2\u045d")
        buf.write("\u045f\7A\2\2\u045e\u045c\3\2\2\2\u045e\u045d\3\2\2\2")
        buf.write("\u045f\u00a9\3\2\2\2\u0460\u0461\5\u00fc\177\2\u0461\u00ab")
        buf.write("\3\2\2\2\u0462\u0463\7(\2\2\u0463\u0464\5\u00fc\177\2")
        buf.write("\u0464\u00ad\3\2\2\2\u0465\u0467\5\u00b0Y\2\u0466\u0465")
        buf.write("\3\2\2\2\u0467\u046a\3\2\2\2\u0468\u0466\3\2\2\2\u0468")
        buf.write("\u0469\3\2\2\2\u0469\u046b\3\2\2\2\u046a\u0468\3\2\2\2")
        buf.write("\u046b\u046d\5\u00b2Z\2\u046c\u046e\5\u00a2R\2\u046d\u046c")
        buf.write("\3\2\2\2\u046d\u046e\3\2\2\2\u046e\u046f\3\2\2\2\u046f")
        buf.write("\u0470\5\u00b6\\\2\u0470\u00af\3\2\2\2\u0471\u0476\5\u00e6")
        buf.write("t\2\u0472\u0476\7%\2\2\u0473\u0476\7$\2\2\u0474\u0476")
        buf.write("\7#\2\2\u0475\u0471\3\2\2\2\u0475\u0472\3\2\2\2\u0475")
        buf.write("\u0473\3\2\2\2\u0475\u0474\3\2\2\2\u0476\u00b1\3\2\2\2")
        buf.write("\u0477\u0479\5X-\2\u0478\u0477\3\2\2\2\u0478\u0479\3\2")
        buf.write("\2\2\u0479\u047a\3\2\2\2\u047a\u047b\5\u00b4[\2\u047b")
        buf.write("\u047d\7;\2\2\u047c\u047e\5\u0096L\2\u047d\u047c\3\2\2")
        buf.write("\2\u047d\u047e\3\2\2\2\u047e\u047f\3\2\2\2\u047f\u0480")
        buf.write("\7<\2\2\u0480\u00b3\3\2\2\2\u0481\u0482\7h\2\2\u0482\u00b5")
        buf.write("\3\2\2\2\u0483\u0485\7=\2\2\u0484\u0486\5\u00b8]\2\u0485")
        buf.write("\u0484\3\2\2\2\u0485\u0486\3\2\2\2\u0486\u0488\3\2\2\2")
        buf.write("\u0487\u0489\5\u00fe\u0080\2\u0488\u0487\3\2\2\2\u0488")
        buf.write("\u0489\3\2\2\2\u0489\u048a\3\2\2\2\u048a\u048b\7>\2\2")
        buf.write("\u048b\u00b7\3\2\2\2\u048c\u048e\5*\26\2\u048d\u048c\3")
        buf.write("\2\2\2\u048d\u048e\3\2\2\2\u048e\u048f\3\2\2\2\u048f\u0490")
        buf.write("\7-\2\2\u0490\u0492\7;\2\2\u0491\u0493\5\u018e\u00c8\2")
        buf.write("\u0492\u0491\3\2\2\2\u0492\u0493\3\2\2\2\u0493\u0494\3")
        buf.write("\2\2\2\u0494\u0495\7<\2\2\u0495\u04bb\7A\2\2\u0496\u0498")
        buf.write("\5*\26\2\u0497\u0496\3\2\2\2\u0497\u0498\3\2\2\2\u0498")
        buf.write("\u0499\3\2\2\2\u0499\u049a\7*\2\2\u049a\u049c\7;\2\2\u049b")
        buf.write("\u049d\5\u018e\u00c8\2\u049c\u049b\3\2\2\2\u049c\u049d")
        buf.write("\3\2\2\2\u049d\u049e\3\2\2\2\u049e\u049f\7<\2\2\u049f")
        buf.write("\u04bb\7A\2\2\u04a0\u04a1\5:\36\2\u04a1\u04a3\7C\2\2\u04a2")
        buf.write("\u04a4\5*\26\2\u04a3\u04a2\3\2\2\2\u04a3\u04a4\3\2\2\2")
        buf.write("\u04a4\u04a5\3\2\2\2\u04a5\u04a6\7*\2\2\u04a6\u04a8\7")
        buf.write(";\2\2\u04a7\u04a9\5\u018e\u00c8\2\u04a8\u04a7\3\2\2\2")
        buf.write("\u04a8\u04a9\3\2\2\2\u04a9\u04aa\3\2\2\2\u04aa\u04ab\7")
        buf.write("<\2\2\u04ab\u04ac\7A\2\2\u04ac\u04bb\3\2\2\2\u04ad\u04ae")
        buf.write("\5\u0160\u00b1\2\u04ae\u04b0\7C\2\2\u04af\u04b1\5*\26")
        buf.write("\2\u04b0\u04af\3\2\2\2\u04b0\u04b1\3\2\2\2\u04b1\u04b2")
        buf.write("\3\2\2\2\u04b2\u04b3\7*\2\2\u04b3\u04b5\7;\2\2\u04b4\u04b6")
        buf.write("\5\u018e\u00c8\2\u04b5\u04b4\3\2\2\2\u04b5\u04b6\3\2\2")
        buf.write("\2\u04b6\u04b7\3\2\2\2\u04b7\u04b8\7<\2\2\u04b8\u04b9")
        buf.write("\7A\2\2\u04b9\u04bb\3\2\2\2\u04ba\u048d\3\2\2\2\u04ba")
        buf.write("\u0497\3\2\2\2\u04ba\u04a0\3\2\2\2\u04ba\u04ad\3\2\2\2")
        buf.write("\u04bb\u00b9\3\2\2\2\u04bc\u04be\5V,\2\u04bd\u04bc\3\2")
        buf.write("\2\2\u04be\u04c1\3\2\2\2\u04bf\u04bd\3\2\2\2\u04bf\u04c0")
        buf.write("\3\2\2\2\u04c0\u04c2\3\2\2\2\u04c1\u04bf\3\2\2\2\u04c2")
        buf.write("\u04c3\7\22\2\2\u04c3\u04c5\7h\2\2\u04c4\u04c6\5^\60\2")
        buf.write("\u04c5\u04c4\3\2\2\2\u04c5\u04c6\3\2\2\2\u04c6\u04c7\3")
        buf.write("\2\2\2\u04c7\u04c8\5\u00bc_\2\u04c8\u00bb\3\2\2\2\u04c9")
        buf.write("\u04cb\7=\2\2\u04ca\u04cc\5\u00be`\2\u04cb\u04ca\3\2\2")
        buf.write("\2\u04cb\u04cc\3\2\2\2\u04cc\u04ce\3\2\2\2\u04cd\u04cf")
        buf.write("\7B\2\2\u04ce\u04cd\3\2\2\2\u04ce\u04cf\3\2\2\2\u04cf")
        buf.write("\u04d1\3\2\2\2\u04d0\u04d2\5\u00c4c\2\u04d1\u04d0\3\2")
        buf.write("\2\2\u04d1\u04d2\3\2\2\2\u04d2\u04d3\3\2\2\2\u04d3\u04d4")
        buf.write("\7>\2\2\u04d4\u00bd\3\2\2\2\u04d5\u04da\5\u00c0a\2\u04d6")
        buf.write("\u04d7\7B\2\2\u04d7\u04d9\5\u00c0a\2\u04d8\u04d6\3\2\2")
        buf.write("\2\u04d9\u04dc\3\2\2\2\u04da\u04d8\3\2\2\2\u04da\u04db")
        buf.write("\3\2\2\2\u04db\u00bf\3\2\2\2\u04dc\u04da\3\2\2\2\u04dd")
        buf.write("\u04df\5\u00c2b\2\u04de\u04dd\3\2\2\2\u04df\u04e2\3\2")
        buf.write("\2\2\u04e0\u04de\3\2\2\2\u04e0\u04e1\3\2\2\2\u04e1\u04e3")
        buf.write("\3\2\2\2\u04e2\u04e0\3\2\2\2\u04e3\u04e9\7h\2\2\u04e4")
        buf.write("\u04e6\7;\2\2\u04e5\u04e7\5\u018e\u00c8\2\u04e6\u04e5")
        buf.write("\3\2\2\2\u04e6\u04e7\3\2\2\2\u04e7\u04e8\3\2\2\2\u04e8")
        buf.write("\u04ea\7<\2\2\u04e9\u04e4\3\2\2\2\u04e9\u04ea\3\2\2\2")
        buf.write("\u04ea\u04ec\3\2\2\2\u04eb\u04ed\5b\62\2\u04ec\u04eb\3")
        buf.write("\2\2\2\u04ec\u04ed\3\2\2\2\u04ed\u00c1\3\2\2\2\u04ee\u04ef")
        buf.write("\5\u00e6t\2\u04ef\u00c3\3\2\2\2\u04f0\u04f4\7A\2\2\u04f1")
        buf.write("\u04f3\5d\63\2\u04f2\u04f1\3\2\2\2\u04f3\u04f6\3\2\2\2")
        buf.write("\u04f4\u04f2\3\2\2\2\u04f4\u04f5\3\2\2\2\u04f5\u00c5\3")
        buf.write("\2\2\2\u04f6\u04f4\3\2\2\2\u04f7\u04fa\5\u00c8e\2\u04f8")
        buf.write("\u04fa\5\u00dan\2\u04f9\u04f7\3\2\2\2\u04f9\u04f8\3\2")
        buf.write("\2\2\u04fa\u00c7\3\2\2\2\u04fb\u04fd\5\u00caf\2\u04fc")
        buf.write("\u04fb\3\2\2\2\u04fd\u0500\3\2\2\2\u04fe\u04fc\3\2\2\2")
        buf.write("\u04fe\u04ff\3\2\2\2\u04ff\u0501\3\2\2\2\u0500\u04fe\3")
        buf.write("\2\2\2\u0501\u0502\7\36\2\2\u0502\u0504\7h\2\2\u0503\u0505")
        buf.write("\5X-\2\u0504\u0503\3\2\2\2\u0504\u0505\3\2\2\2\u0505\u0507")
        buf.write("\3\2\2\2\u0506\u0508\5\u00ccg\2\u0507\u0506\3\2\2\2\u0507")
        buf.write("\u0508\3\2\2\2\u0508\u0509\3\2\2\2\u0509\u050a\5\u00ce")
        buf.write("h\2\u050a\u00c9\3\2\2\2\u050b\u0513\5\u00e6t\2\u050c\u0513")
        buf.write("\7%\2\2\u050d\u0513\7$\2\2\u050e\u0513\7#\2\2\u050f\u0513")
        buf.write("\7\3\2\2\u0510\u0513\7(\2\2\u0511\u0513\7)\2\2\u0512\u050b")
        buf.write("\3\2\2\2\u0512\u050c\3\2\2\2\u0512\u050d\3\2\2\2\u0512")
        buf.write("\u050e\3\2\2\2\u0512\u050f\3\2\2\2\u0512\u0510\3\2\2\2")
        buf.write("\u0512\u0511\3\2\2\2\u0513\u00cb\3\2\2\2\u0514\u0515\7")
        buf.write("\23\2\2\u0515\u0516\5`\61\2\u0516\u00cd\3\2\2\2\u0517")
        buf.write("\u051b\7=\2\2\u0518\u051a\5\u00d0i\2\u0519\u0518\3\2\2")
        buf.write("\2\u051a\u051d\3\2\2\2\u051b\u0519\3\2\2\2\u051b\u051c")
        buf.write("\3\2\2\2\u051c\u051e\3\2\2\2\u051d\u051b\3\2\2\2\u051e")
        buf.write("\u051f\7>\2\2\u051f\u00cf\3\2\2\2\u0520\u0526\5\u00d2")
        buf.write("j\2\u0521\u0526\5\u00d6l\2\u0522\u0526\5R*\2\u0523\u0526")
        buf.write("\5\u00c6d\2\u0524\u0526\7A\2\2\u0525\u0520\3\2\2\2\u0525")
        buf.write("\u0521\3\2\2\2\u0525\u0522\3\2\2\2\u0525\u0523\3\2\2\2")
        buf.write("\u0525\u0524\3\2\2\2\u0526\u00d1\3\2\2\2\u0527\u0529\5")
        buf.write("\u00d4k\2\u0528\u0527\3\2\2\2\u0529\u052c\3\2\2\2\u052a")
        buf.write("\u0528\3\2\2\2\u052a\u052b\3\2\2\2\u052b\u052d\3\2\2\2")
        buf.write("\u052c\u052a\3\2\2\2\u052d\u052e\5t;\2\u052e\u052f\5l")
        buf.write("\67\2\u052f\u0530\7A\2\2\u0530\u00d3\3\2\2\2\u0531\u0536")
        buf.write("\5\u00e6t\2\u0532\u0536\7%\2\2\u0533\u0536\7(\2\2\u0534")
        buf.write("\u0536\7\24\2\2\u0535\u0531\3\2\2\2\u0535\u0532\3\2\2")
        buf.write("\2\u0535\u0533\3\2\2\2\u0535\u0534\3\2\2\2\u0536\u00d5")
        buf.write("\3\2\2\2\u0537\u0539\5\u00d8m\2\u0538\u0537\3\2\2\2\u0539")
        buf.write("\u053c\3\2\2\2\u053a\u0538\3\2\2\2\u053a\u053b\3\2\2\2")
        buf.write("\u053b\u053d\3\2\2\2\u053c\u053a\3\2\2\2\u053d\u053e\5")
        buf.write("\u0090I\2\u053e\u053f\5\u00a8U\2\u053f\u00d7\3\2\2\2\u0540")
        buf.write("\u0547\5\u00e6t\2\u0541\u0547\7%\2\2\u0542\u0547\7\3\2")
        buf.write("\2\u0543\u0547\7\16\2\2\u0544\u0547\7(\2\2\u0545\u0547")
        buf.write("\7)\2\2\u0546\u0540\3\2\2\2\u0546\u0541\3\2\2\2\u0546")
        buf.write("\u0542\3\2\2\2\u0546\u0543\3\2\2\2\u0546\u0544\3\2\2\2")
        buf.write("\u0546\u0545\3\2\2\2\u0547\u00d9\3\2\2\2\u0548\u054a\5")
        buf.write("\u00caf\2\u0549\u0548\3\2\2\2\u054a\u054d\3\2\2\2\u054b")
        buf.write("\u0549\3\2\2\2\u054b\u054c\3\2\2\2\u054c\u054e\3\2\2\2")
        buf.write("\u054d\u054b\3\2\2\2\u054e\u054f\7i\2\2\u054f\u0550\7")
        buf.write("\36\2\2\u0550\u0551\7h\2\2\u0551\u0552\5\u00dco\2\u0552")
        buf.write("\u00db\3\2\2\2\u0553\u0557\7=\2\2\u0554\u0556\5\u00de")
        buf.write("p\2\u0555\u0554\3\2\2\2\u0556\u0559\3\2\2\2\u0557\u0555")
        buf.write("\3\2\2\2\u0557\u0558\3\2\2\2\u0558\u055a\3\2\2\2\u0559")
        buf.write("\u0557\3\2\2\2\u055a\u055b\7>\2\2\u055b\u00dd\3\2\2\2")
        buf.write("\u055c\u0562\5\u00e0q\2\u055d\u0562\5\u00d2j\2\u055e\u0562")
        buf.write("\5R*\2\u055f\u0562\5\u00c6d\2\u0560\u0562\7A\2\2\u0561")
        buf.write("\u055c\3\2\2\2\u0561\u055d\3\2\2\2\u0561\u055e\3\2\2\2")
        buf.write("\u0561\u055f\3\2\2\2\u0561\u0560\3\2\2\2\u0562\u00df\3")
        buf.write("\2\2\2\u0563\u0565\5\u00e2r\2\u0564\u0563\3\2\2\2\u0565")
        buf.write("\u0568\3\2\2\2\u0566\u0564\3\2\2\2\u0566\u0567\3\2\2\2")
        buf.write("\u0567\u0569\3\2\2\2\u0568\u0566\3\2\2\2\u0569\u056a\5")
        buf.write("t;\2\u056a\u056b\7h\2\2\u056b\u056c\7;\2\2\u056c\u056e")
        buf.write("\7<\2\2\u056d\u056f\5 \21\2\u056e\u056d\3\2\2\2\u056e")
        buf.write("\u056f\3\2\2\2\u056f\u0571\3\2\2\2\u0570\u0572\5\u00e4")
        buf.write("s\2\u0571\u0570\3\2\2\2\u0571\u0572\3\2\2\2\u0572\u0573")
        buf.write("\3\2\2\2\u0573\u0574\7A\2\2\u0574\u00e1\3\2\2\2\u0575")
        buf.write("\u0579\5\u00e6t\2\u0576\u0579\7%\2\2\u0577\u0579\7\3\2")
        buf.write("\2\u0578\u0575\3\2\2\2\u0578\u0576\3\2\2\2\u0578\u0577")
        buf.write("\3\2\2\2\u0579\u00e3\3\2\2\2\u057a\u057b\7\16\2\2\u057b")
        buf.write("\u057c\5\u00eex\2\u057c\u00e5\3\2\2\2\u057d\u0581\5\u00e8")
        buf.write("u\2\u057e\u0581\5\u00f4{\2\u057f\u0581\5\u00f6|\2\u0580")
        buf.write("\u057d\3\2\2\2\u0580\u057e\3\2\2\2\u0580\u057f\3\2\2\2")
        buf.write("\u0581\u00e7\3\2\2\2\u0582\u0583\7i\2\2\u0583\u0584\5")
        buf.write("\66\34\2\u0584\u0586\7;\2\2\u0585\u0587\5\u00eav\2\u0586")
        buf.write("\u0585\3\2\2\2\u0586\u0587\3\2\2\2\u0587\u0588\3\2\2\2")
        buf.write("\u0588\u0589\7<\2\2\u0589\u00e9\3\2\2\2\u058a\u058f\5")
        buf.write("\u00ecw\2\u058b\u058c\7B\2\2\u058c\u058e\5\u00ecw\2\u058d")
        buf.write("\u058b\3\2\2\2\u058e\u0591\3\2\2\2\u058f\u058d\3\2\2\2")
        buf.write("\u058f\u0590\3\2\2\2\u0590\u00eb\3\2\2\2\u0591\u058f\3")
        buf.write("\2\2\2\u0592\u0593\7h\2\2\u0593\u0594\7D\2\2\u0594\u0595")
        buf.write("\5\u00eex\2\u0595\u00ed\3\2\2\2\u0596\u059a\5\u01b0\u00d9")
        buf.write("\2\u0597\u059a\5\u00f0y\2\u0598\u059a\5\u00e6t\2\u0599")
        buf.write("\u0596\3\2\2\2\u0599\u0597\3\2\2\2\u0599\u0598\3\2\2\2")
        buf.write("\u059a\u00ef\3\2\2\2\u059b\u059d\7=\2\2\u059c\u059e\5")
        buf.write("\u00f2z\2\u059d\u059c\3\2\2\2\u059d\u059e\3\2\2\2\u059e")
        buf.write("\u05a0\3\2\2\2\u059f\u05a1\7B\2\2\u05a0\u059f\3\2\2\2")
        buf.write("\u05a0\u05a1\3\2\2\2\u05a1\u05a2\3\2\2\2\u05a2\u05a3\7")
        buf.write(">\2\2\u05a3\u00f1\3\2\2\2\u05a4\u05a9\5\u00eex\2\u05a5")
        buf.write("\u05a6\7B\2\2\u05a6\u05a8\5\u00eex\2\u05a7\u05a5\3\2\2")
        buf.write("\2\u05a8\u05ab\3\2\2\2\u05a9\u05a7\3\2\2\2\u05a9\u05aa")
        buf.write("\3\2\2\2\u05aa\u00f3\3\2\2\2\u05ab\u05a9\3\2\2\2\u05ac")
        buf.write("\u05ad\7i\2\2\u05ad\u05ae\5\66\34\2\u05ae\u00f5\3\2\2")
        buf.write("\2\u05af\u05b0\7i\2\2\u05b0\u05b1\5\66\34\2\u05b1\u05b2")
        buf.write("\7;\2\2\u05b2\u05b3\5\u00eex\2\u05b3\u05b4\7<\2\2\u05b4")
        buf.write("\u00f7\3\2\2\2\u05b5\u05b7\7=\2\2\u05b6\u05b8\5\u00fa")
        buf.write("~\2\u05b7\u05b6\3\2\2\2\u05b7\u05b8\3\2\2\2\u05b8\u05ba")
        buf.write("\3\2\2\2\u05b9\u05bb\7B\2\2\u05ba\u05b9\3\2\2\2\u05ba")
        buf.write("\u05bb\3\2\2\2\u05bb\u05bc\3\2\2\2\u05bc\u05bd\7>\2\2")
        buf.write("\u05bd\u00f9\3\2\2\2\u05be\u05c3\5r:\2\u05bf\u05c0\7B")
        buf.write("\2\2\u05c0\u05c2\5r:\2\u05c1\u05bf\3\2\2\2\u05c2\u05c5")
        buf.write("\3\2\2\2\u05c3\u05c1\3\2\2\2\u05c3\u05c4\3\2\2\2\u05c4")
        buf.write("\u00fb\3\2\2\2\u05c5\u05c3\3\2\2\2\u05c6\u05c8\7=\2\2")
        buf.write("\u05c7\u05c9\5\u00fe\u0080\2\u05c8\u05c7\3\2\2\2\u05c8")
        buf.write("\u05c9\3\2\2\2\u05c9\u05ca\3\2\2\2\u05ca\u05cb\7>\2\2")
        buf.write("\u05cb\u00fd\3\2\2\2\u05cc\u05ce\5\u0100\u0081\2\u05cd")
        buf.write("\u05cc\3\2\2\2\u05ce\u05cf\3\2\2\2\u05cf\u05cd\3\2\2\2")
        buf.write("\u05cf\u05d0\3\2\2\2\u05d0\u00ff\3\2\2\2\u05d1\u05d5\5")
        buf.write("\u0102\u0082\2\u05d2\u05d5\5R*\2\u05d3\u05d5\5\u0106\u0084")
        buf.write("\2\u05d4\u05d1\3\2\2\2\u05d4\u05d2\3\2\2\2\u05d4\u05d3")
        buf.write("\3\2\2\2\u05d5\u0101\3\2\2\2\u05d6\u05d7\5\u0104\u0083")
        buf.write("\2\u05d7\u05d8\7A\2\2\u05d8\u0103\3\2\2\2\u05d9\u05db")
        buf.write("\5\u009cO\2\u05da\u05d9\3\2\2\2\u05db\u05de\3\2\2\2\u05dc")
        buf.write("\u05da\3\2\2\2\u05dc\u05dd\3\2\2\2\u05dd\u05df\3\2\2\2")
        buf.write("\u05de\u05dc\3\2\2\2\u05df\u05e0\5t;\2\u05e0\u05e1\5l")
        buf.write("\67\2\u05e1\u0105\3\2\2\2\u05e2\u05e9\5\u010a\u0086\2")
        buf.write("\u05e3\u05e9\5\u010e\u0088\2\u05e4\u05e9\5\u0116\u008c")
        buf.write("\2\u05e5\u05e9\5\u0118\u008d\2\u05e6\u05e9\5\u012a\u0096")
        buf.write("\2\u05e7\u05e9\5\u0130\u0099\2\u05e8\u05e2\3\2\2\2\u05e8")
        buf.write("\u05e3\3\2\2\2\u05e8\u05e4\3\2\2\2\u05e8\u05e5\3\2\2\2")
        buf.write("\u05e8\u05e6\3\2\2\2\u05e8\u05e7\3\2\2\2\u05e9\u0107\3")
        buf.write("\2\2\2\u05ea\u05f0\5\u010a\u0086\2\u05eb\u05f0\5\u0110")
        buf.write("\u0089\2\u05ec\u05f0\5\u011a\u008e\2\u05ed\u05f0\5\u012c")
        buf.write("\u0097\2\u05ee\u05f0\5\u0132\u009a\2\u05ef\u05ea\3\2\2")
        buf.write("\2\u05ef\u05eb\3\2\2\2\u05ef\u05ec\3\2\2\2\u05ef\u05ed")
        buf.write("\3\2\2\2\u05ef\u05ee\3\2\2\2\u05f0\u0109\3\2\2\2\u05f1")
        buf.write("\u05fe\5\u00fc\177\2\u05f2\u05fe\5\u010c\u0087\2\u05f3")
        buf.write("\u05fe\5\u0112\u008a\2\u05f4\u05fe\5\u011c\u008f\2\u05f5")
        buf.write("\u05fe\5\u011e\u0090\2\u05f6\u05fe\5\u012e\u0098\2\u05f7")
        buf.write("\u05fe\5\u0142\u00a2\2\u05f8\u05fe\5\u0144\u00a3\2\u05f9")
        buf.write("\u05fe\5\u0146\u00a4\2\u05fa\u05fe\5\u014a\u00a6\2\u05fb")
        buf.write("\u05fe\5\u0148\u00a5\2\u05fc\u05fe\5\u014c\u00a7\2\u05fd")
        buf.write("\u05f1\3\2\2\2\u05fd\u05f2\3\2\2\2\u05fd\u05f3\3\2\2\2")
        buf.write("\u05fd\u05f4\3\2\2\2\u05fd\u05f5\3\2\2\2\u05fd\u05f6\3")
        buf.write("\2\2\2\u05fd\u05f7\3\2\2\2\u05fd\u05f8\3\2\2\2\u05fd\u05f9")
        buf.write("\3\2\2\2\u05fd\u05fa\3\2\2\2\u05fd\u05fb\3\2\2\2\u05fd")
        buf.write("\u05fc\3\2\2\2\u05fe\u010b\3\2\2\2\u05ff\u0600\7A\2\2")
        buf.write("\u0600\u010d\3\2\2\2\u0601\u0602\7h\2\2\u0602\u0603\7")
        buf.write("J\2\2\u0603\u0604\5\u0106\u0084\2\u0604\u010f\3\2\2\2")
        buf.write("\u0605\u0606\7h\2\2\u0606\u0607\7J\2\2\u0607\u0608\5\u0108")
        buf.write("\u0085\2\u0608\u0111\3\2\2\2\u0609\u060a\5\u0114\u008b")
        buf.write("\2\u060a\u060b\7A\2\2\u060b\u0113\3\2\2\2\u060c\u0614")
        buf.write("\5\u01aa\u00d6\2\u060d\u0614\5\u01c8\u00e5\2\u060e\u0614")
        buf.write("\5\u01ca\u00e6\2\u060f\u0614\5\u01d0\u00e9\2\u0610\u0614")
        buf.write("\5\u01d4\u00eb\2\u0611\u0614\5\u0188\u00c5\2\u0612\u0614")
        buf.write("\5\u0174\u00bb\2\u0613\u060c\3\2\2\2\u0613\u060d\3\2\2")
        buf.write("\2\u0613\u060e\3\2\2\2\u0613\u060f\3\2\2\2\u0613\u0610")
        buf.write("\3\2\2\2\u0613\u0611\3\2\2\2\u0613\u0612\3\2\2\2\u0614")
        buf.write("\u0115\3\2\2\2\u0615\u0616\7\30\2\2\u0616\u0617\7;\2\2")
        buf.write("\u0617\u0618\5\u019e\u00d0\2\u0618\u0619\7<\2\2\u0619")
        buf.write("\u061a\5\u0106\u0084\2\u061a\u0117\3\2\2\2\u061b\u061c")
        buf.write("\7\30\2\2\u061c\u061d\7;\2\2\u061d\u061e\5\u019e\u00d0")
        buf.write("\2\u061e\u061f\7<\2\2\u061f\u0620\5\u0108\u0085\2\u0620")
        buf.write("\u0621\7\21\2\2\u0621\u0622\5\u0106\u0084\2\u0622\u0119")
        buf.write("\3\2\2\2\u0623\u0624\7\30\2\2\u0624\u0625\7;\2\2\u0625")
        buf.write("\u0626\5\u019e\u00d0\2\u0626\u0627\7<\2\2\u0627\u0628")
        buf.write("\5\u0108\u0085\2\u0628\u0629\7\21\2\2\u0629\u062a\5\u0108")
        buf.write("\u0085\2\u062a\u011b\3\2\2\2\u062b\u062c\7\4\2\2\u062c")
        buf.write("\u062d\5\u019e\u00d0\2\u062d\u062e\7A\2\2\u062e\u0636")
        buf.write("\3\2\2\2\u062f\u0630\7\4\2\2\u0630\u0631\5\u019e\u00d0")
        buf.write("\2\u0631\u0632\7J\2\2\u0632\u0633\5\u019e\u00d0\2\u0633")
        buf.write("\u0634\7A\2\2\u0634\u0636\3\2\2\2\u0635\u062b\3\2\2\2")
        buf.write("\u0635\u062f\3\2\2\2\u0636\u011d\3\2\2\2\u0637\u0638\7")
        buf.write("+\2\2\u0638\u0639\7;\2\2\u0639\u063a\5\u019e\u00d0\2\u063a")
        buf.write("\u063b\7<\2\2\u063b\u063c\5\u0120\u0091\2\u063c\u011f")
        buf.write("\3\2\2\2\u063d\u0641\7=\2\2\u063e\u0640\5\u0122\u0092")
        buf.write("\2\u063f\u063e\3\2\2\2\u0640\u0643\3\2\2\2\u0641\u063f")
        buf.write("\3\2\2\2\u0641\u0642\3\2\2\2\u0642\u0647\3\2\2\2\u0643")
        buf.write("\u0641\3\2\2\2\u0644\u0646\5\u0126\u0094\2\u0645\u0644")
        buf.write("\3\2\2\2\u0646\u0649\3\2\2\2\u0647\u0645\3\2\2\2\u0647")
        buf.write("\u0648\3\2\2\2\u0648\u064a\3\2\2\2\u0649\u0647\3\2\2\2")
        buf.write("\u064a\u064b\7>\2\2\u064b\u0121\3\2\2\2\u064c\u064d\5")
        buf.write("\u0124\u0093\2\u064d\u064e\5\u00fe\u0080\2\u064e\u0123")
        buf.write("\3\2\2\2\u064f\u0653\5\u0126\u0094\2\u0650\u0652\5\u0126")
        buf.write("\u0094\2\u0651\u0650\3\2\2\2\u0652\u0655\3\2\2\2\u0653")
        buf.write("\u0651\3\2\2\2\u0653\u0654\3\2\2\2\u0654\u0125\3\2\2\2")
        buf.write("\u0655\u0653\3\2\2\2\u0656\u0657\7\b\2\2\u0657\u0658\5")
        buf.write("\u019c\u00cf\2\u0658\u0659\7J\2\2\u0659\u0661\3\2\2\2")
        buf.write("\u065a\u065b\7\b\2\2\u065b\u065c\5\u0128\u0095\2\u065c")
        buf.write("\u065d\7J\2\2\u065d\u0661\3\2\2\2\u065e\u065f\7\16\2\2")
        buf.write("\u065f\u0661\7J\2\2\u0660\u0656\3\2\2\2\u0660\u065a\3")
        buf.write("\2\2\2\u0660\u065e\3\2\2\2\u0661\u0127\3\2\2\2\u0662\u0663")
        buf.write("\7h\2\2\u0663\u0129\3\2\2\2\u0664\u0665\7\64\2\2\u0665")
        buf.write("\u0666\7;\2\2\u0666\u0667\5\u019e\u00d0\2\u0667\u0668")
        buf.write("\7<\2\2\u0668\u0669\5\u0106\u0084\2\u0669\u012b\3\2\2")
        buf.write("\2\u066a\u066b\7\64\2\2\u066b\u066c\7;\2\2\u066c\u066d")
        buf.write("\5\u019e\u00d0\2\u066d\u066e\7<\2\2\u066e\u066f\5\u0108")
        buf.write("\u0085\2\u066f\u012d\3\2\2\2\u0670\u0671\7\17\2\2\u0671")
        buf.write("\u0672\5\u0106\u0084\2\u0672\u0673\7\64\2\2\u0673\u0674")
        buf.write("\7;\2\2\u0674\u0675\5\u019e\u00d0\2\u0675\u0676\7<\2\2")
        buf.write("\u0676\u0677\7A\2\2\u0677\u012f\3\2\2\2\u0678\u067b\5")
        buf.write("\u0134\u009b\2\u0679\u067b\5\u013e\u00a0\2\u067a\u0678")
        buf.write("\3\2\2\2\u067a\u0679\3\2\2\2\u067b\u0131\3\2\2\2\u067c")
        buf.write("\u067f\5\u0136\u009c\2\u067d\u067f\5\u0140\u00a1\2\u067e")
        buf.write("\u067c\3\2\2\2\u067e\u067d\3\2\2\2\u067f\u0133\3\2\2\2")
        buf.write("\u0680\u0681\7\27\2\2\u0681\u0683\7;\2\2\u0682\u0684\5")
        buf.write("\u0138\u009d\2\u0683\u0682\3\2\2\2\u0683\u0684\3\2\2\2")
        buf.write("\u0684\u0685\3\2\2\2\u0685\u0687\7A\2\2\u0686\u0688\5")
        buf.write("\u019e\u00d0\2\u0687\u0686\3\2\2\2\u0687\u0688\3\2\2\2")
        buf.write("\u0688\u0689\3\2\2\2\u0689\u068b\7A\2\2\u068a\u068c\5")
        buf.write("\u013a\u009e\2\u068b\u068a\3\2\2\2\u068b\u068c\3\2\2\2")
        buf.write("\u068c\u068d\3\2\2\2\u068d\u068e\7<\2\2\u068e\u068f\5")
        buf.write("\u0106\u0084\2\u068f\u0135\3\2\2\2\u0690\u0691\7\27\2")
        buf.write("\2\u0691\u0693\7;\2\2\u0692\u0694\5\u0138\u009d\2\u0693")
        buf.write("\u0692\3\2\2\2\u0693\u0694\3\2\2\2\u0694\u0695\3\2\2\2")
        buf.write("\u0695\u0697\7A\2\2\u0696\u0698\5\u019e\u00d0\2\u0697")
        buf.write("\u0696\3\2\2\2\u0697\u0698\3\2\2\2\u0698\u0699\3\2\2\2")
        buf.write("\u0699\u069b\7A\2\2\u069a\u069c\5\u013a\u009e\2\u069b")
        buf.write("\u069a\3\2\2\2\u069b\u069c\3\2\2\2\u069c\u069d\3\2\2\2")
        buf.write("\u069d\u069e\7<\2\2\u069e\u069f\5\u0108\u0085\2\u069f")
        buf.write("\u0137\3\2\2\2\u06a0\u06a3\5\u013c\u009f\2\u06a1\u06a3")
        buf.write("\5\u0104\u0083\2\u06a2\u06a0\3\2\2\2\u06a2\u06a1\3\2\2")
        buf.write("\2\u06a3\u0139\3\2\2\2\u06a4\u06a5\5\u013c\u009f\2\u06a5")
        buf.write("\u013b\3\2\2\2\u06a6\u06ab\5\u0114\u008b\2\u06a7\u06a8")
        buf.write("\7B\2\2\u06a8\u06aa\5\u0114\u008b\2\u06a9\u06a7\3\2\2")
        buf.write("\2\u06aa\u06ad\3\2\2\2\u06ab\u06a9\3\2\2\2\u06ab\u06ac")
        buf.write("\3\2\2\2\u06ac\u013d\3\2\2\2\u06ad\u06ab\3\2\2\2\u06ae")
        buf.write("\u06af\7\27\2\2\u06af\u06b3\7;\2\2\u06b0\u06b2\5\u009c")
        buf.write("O\2\u06b1\u06b0\3\2\2\2\u06b2\u06b5\3\2\2\2\u06b3\u06b1")
        buf.write("\3\2\2\2\u06b3\u06b4\3\2\2\2\u06b4\u06b6\3\2\2\2\u06b5")
        buf.write("\u06b3\3\2\2\2\u06b6\u06b7\5t;\2\u06b7\u06b8\5p9\2\u06b8")
        buf.write("\u06b9\7J\2\2\u06b9\u06ba\5\u019e\u00d0\2\u06ba\u06bb")
        buf.write("\7<\2\2\u06bb\u06bc\5\u0106\u0084\2\u06bc\u013f\3\2\2")
        buf.write("\2\u06bd\u06be\7\27\2\2\u06be\u06c2\7;\2\2\u06bf\u06c1")
        buf.write("\5\u009cO\2\u06c0\u06bf\3\2\2\2\u06c1\u06c4\3\2\2\2\u06c2")
        buf.write("\u06c0\3\2\2\2\u06c2\u06c3\3\2\2\2\u06c3\u06c5\3\2\2\2")
        buf.write("\u06c4\u06c2\3\2\2\2\u06c5\u06c6\5t;\2\u06c6\u06c7\5p")
        buf.write("9\2\u06c7\u06c8\7J\2\2\u06c8\u06c9\5\u019e\u00d0\2\u06c9")
        buf.write("\u06ca\7<\2\2\u06ca\u06cb\5\u0108\u0085\2\u06cb\u0141")
        buf.write("\3\2\2\2\u06cc\u06ce\7\6\2\2\u06cd\u06cf\7h\2\2\u06ce")
        buf.write("\u06cd\3\2\2\2\u06ce\u06cf\3\2\2\2\u06cf\u06d0\3\2\2\2")
        buf.write("\u06d0\u06d1\7A\2\2\u06d1\u0143\3\2\2\2\u06d2\u06d4\7")
        buf.write("\r\2\2\u06d3\u06d5\7h\2\2\u06d4\u06d3\3\2\2\2\u06d4\u06d5")
        buf.write("\3\2\2\2\u06d5\u06d6\3\2\2\2\u06d6\u06d7\7A\2\2\u06d7")
        buf.write("\u0145\3\2\2\2\u06d8\u06da\7&\2\2\u06d9\u06db\5\u019e")
        buf.write("\u00d0\2\u06da\u06d9\3\2\2\2\u06da\u06db\3\2\2\2\u06db")
        buf.write("\u06dc\3\2\2\2\u06dc\u06dd\7A\2\2\u06dd\u0147\3\2\2\2")
        buf.write("\u06de\u06df\7.\2\2\u06df\u06e0\5\u019e\u00d0\2\u06e0")
        buf.write("\u06e1\7A\2\2\u06e1\u0149\3\2\2\2\u06e2\u06e3\7,\2\2\u06e3")
        buf.write("\u06e4\7;\2\2\u06e4\u06e5\5\u019e\u00d0\2\u06e5\u06e6")
        buf.write("\7<\2\2\u06e6\u06e7\5\u00fc\177\2\u06e7\u014b\3\2\2\2")
        buf.write("\u06e8\u06e9\7\61\2\2\u06e9\u06ea\5\u00fc\177\2\u06ea")
        buf.write("\u06eb\5\u014e\u00a8\2\u06eb\u06f5\3\2\2\2\u06ec\u06ed")
        buf.write("\7\61\2\2\u06ed\u06ef\5\u00fc\177\2\u06ee\u06f0\5\u014e")
        buf.write("\u00a8\2\u06ef\u06ee\3\2\2\2\u06ef\u06f0\3\2\2\2\u06f0")
        buf.write("\u06f1\3\2\2\2\u06f1\u06f2\5\u0156\u00ac\2\u06f2\u06f5")
        buf.write("\3\2\2\2\u06f3\u06f5\5\u0158\u00ad\2\u06f4\u06e8\3\2\2")
        buf.write("\2\u06f4\u06ec\3\2\2\2\u06f4\u06f3\3\2\2\2\u06f5\u014d")
        buf.write("\3\2\2\2\u06f6\u06fa\5\u0150\u00a9\2\u06f7\u06f9\5\u0150")
        buf.write("\u00a9\2\u06f8\u06f7\3\2\2\2\u06f9\u06fc\3\2\2\2\u06fa")
        buf.write("\u06f8\3\2\2\2\u06fa\u06fb\3\2\2\2\u06fb\u014f\3\2\2\2")
        buf.write("\u06fc\u06fa\3\2\2\2\u06fd\u06fe\7\t\2\2\u06fe\u06ff\7")
        buf.write(";\2\2\u06ff\u0700\5\u0152\u00aa\2\u0700\u0701\7<\2\2\u0701")
        buf.write("\u0702\5\u00fc\177\2\u0702\u0151\3\2\2\2\u0703\u0705\5")
        buf.write("\u009cO\2\u0704\u0703\3\2\2\2\u0705\u0708\3\2\2\2\u0706")
        buf.write("\u0704\3\2\2\2\u0706\u0707\3\2\2\2\u0707\u0709\3\2\2\2")
        buf.write("\u0708\u0706\3\2\2\2\u0709\u070a\5\u0154\u00ab\2\u070a")
        buf.write("\u070b\5p9\2\u070b\u0153\3\2\2\2\u070c\u0711\5|?\2\u070d")
        buf.write("\u070e\7X\2\2\u070e\u0710\5\20\t\2\u070f\u070d\3\2\2\2")
        buf.write("\u0710\u0713\3\2\2\2\u0711\u070f\3\2\2\2\u0711\u0712\3")
        buf.write("\2\2\2\u0712\u0155\3\2\2\2\u0713\u0711\3\2\2\2\u0714\u0715")
        buf.write("\7\25\2\2\u0715\u0716\5\u00fc\177\2\u0716\u0157\3\2\2")
        buf.write("\2\u0717\u0718\7\61\2\2\u0718\u0719\5\u015a\u00ae\2\u0719")
        buf.write("\u071b\5\u00fc\177\2\u071a\u071c\5\u014e\u00a8\2\u071b")
        buf.write("\u071a\3\2\2\2\u071b\u071c\3\2\2\2\u071c\u071e\3\2\2\2")
        buf.write("\u071d\u071f\5\u0156\u00ac\2\u071e\u071d\3\2\2\2\u071e")
        buf.write("\u071f\3\2\2\2\u071f\u0159\3\2\2\2\u0720\u0721\7;\2\2")
        buf.write("\u0721\u0723\5\u015c\u00af\2\u0722\u0724\7A\2\2\u0723")
        buf.write("\u0722\3\2\2\2\u0723\u0724\3\2\2\2\u0724\u0725\3\2\2\2")
        buf.write("\u0725\u0726\7<\2\2\u0726\u015b\3\2\2\2\u0727\u072c\5")
        buf.write("\u015e\u00b0\2\u0728\u0729\7A\2\2\u0729\u072b\5\u015e")
        buf.write("\u00b0\2\u072a\u0728\3\2\2\2\u072b\u072e\3\2\2\2\u072c")
        buf.write("\u072a\3\2\2\2\u072c\u072d\3\2\2\2\u072d\u015d\3\2\2\2")
        buf.write("\u072e\u072c\3\2\2\2\u072f\u0731\5\u009cO\2\u0730\u072f")
        buf.write("\3\2\2\2\u0731\u0734\3\2\2\2\u0732\u0730\3\2\2\2\u0732")
        buf.write("\u0733\3\2\2\2\u0733\u0735\3\2\2\2\u0734\u0732\3\2\2\2")
        buf.write("\u0735\u0736\5t;\2\u0736\u0737\5p9\2\u0737\u0738\7D\2")
        buf.write("\2\u0738\u0739\5\u019e\u00d0\2\u0739\u015f\3\2\2\2\u073a")
        buf.write("\u073d\5\u016e\u00b8\2\u073b\u073d\5\u0196\u00cc\2\u073c")
        buf.write("\u073a\3\2\2\2\u073c\u073b\3\2\2\2\u073d\u0741\3\2\2\2")
        buf.write("\u073e\u0740\5\u0168\u00b5\2\u073f\u073e\3\2\2\2\u0740")
        buf.write("\u0743\3\2\2\2\u0741\u073f\3\2\2\2\u0741\u0742\3\2\2\2")
        buf.write("\u0742\u0161\3\2\2\2\u0743\u0741\3\2\2\2\u0744\u0762\5")
        buf.write("\2\2\2\u0745\u074a\5\66\34\2\u0746\u0747\7?\2\2\u0747")
        buf.write("\u0749\7@\2\2\u0748\u0746\3\2\2\2\u0749\u074c\3\2\2\2")
        buf.write("\u074a\u0748\3\2\2\2\u074a\u074b\3\2\2\2\u074b\u074d\3")
        buf.write("\2\2\2\u074c\u074a\3\2\2\2\u074d\u074e\7C\2\2\u074e\u074f")
        buf.write("\7\13\2\2\u074f\u0762\3\2\2\2\u0750\u0751\7\62\2\2\u0751")
        buf.write("\u0752\7C\2\2\u0752\u0762\7\13\2\2\u0753\u0762\7-\2\2")
        buf.write("\u0754\u0755\5\66\34\2\u0755\u0756\7C\2\2\u0756\u0757")
        buf.write("\7-\2\2\u0757\u0762\3\2\2\2\u0758\u0759\7;\2\2\u0759\u075a")
        buf.write("\5\u019e\u00d0\2\u075a\u075b\7<\2\2\u075b\u0762\3\2\2")
        buf.write("\2\u075c\u0762\5\u0174\u00bb\2\u075d\u0762\5\u017c\u00bf")
        buf.write("\2\u075e\u0762\5\u0182\u00c2\2\u075f\u0762\5\u0188\u00c5")
        buf.write("\2\u0760\u0762\5\u0190\u00c9\2\u0761\u0744\3\2\2\2\u0761")
        buf.write("\u0745\3\2\2\2\u0761\u0750\3\2\2\2\u0761\u0753\3\2\2\2")
        buf.write("\u0761\u0754\3\2\2\2\u0761\u0758\3\2\2\2\u0761\u075c\3")
        buf.write("\2\2\2\u0761\u075d\3\2\2\2\u0761\u075e\3\2\2\2\u0761\u075f")
        buf.write("\3\2\2\2\u0761\u0760\3\2\2\2\u0762\u0163\3\2\2\2\u0763")
        buf.write("\u0764\3\2\2\2\u0764\u0165\3\2\2\2\u0765\u0782\5\2\2\2")
        buf.write("\u0766\u076b\5\66\34\2\u0767\u0768\7?\2\2\u0768\u076a")
        buf.write("\7@\2\2\u0769\u0767\3\2\2\2\u076a\u076d\3\2\2\2\u076b")
        buf.write("\u0769\3\2\2\2\u076b\u076c\3\2\2\2\u076c\u076e\3\2\2\2")
        buf.write("\u076d\u076b\3\2\2\2\u076e\u076f\7C\2\2\u076f\u0770\7")
        buf.write("\13\2\2\u0770\u0782\3\2\2\2\u0771\u0772\7\62\2\2\u0772")
        buf.write("\u0773\7C\2\2\u0773\u0782\7\13\2\2\u0774\u0782\7-\2\2")
        buf.write("\u0775\u0776\5\66\34\2\u0776\u0777\7C\2\2\u0777\u0778")
        buf.write("\7-\2\2\u0778\u0782\3\2\2\2\u0779\u077a\7;\2\2\u077a\u077b")
        buf.write("\5\u019e\u00d0\2\u077b\u077c\7<\2\2\u077c\u0782\3\2\2")
        buf.write("\2\u077d\u0782\5\u0174\u00bb\2\u077e\u0782\5\u017c\u00bf")
        buf.write("\2\u077f\u0782\5\u0188\u00c5\2\u0780\u0782\5\u0190\u00c9")
        buf.write("\2\u0781\u0765\3\2\2\2\u0781\u0766\3\2\2\2\u0781\u0771")
        buf.write("\3\2\2\2\u0781\u0774\3\2\2\2\u0781\u0775\3\2\2\2\u0781")
        buf.write("\u0779\3\2\2\2\u0781\u077d\3\2\2\2\u0781\u077e\3\2\2\2")
        buf.write("\u0781\u077f\3\2\2\2\u0781\u0780\3\2\2\2\u0782\u0167\3")
        buf.write("\2\2\2\u0783\u0789\5\u0176\u00bc\2\u0784\u0789\5\u017e")
        buf.write("\u00c0\2\u0785\u0789\5\u0184\u00c3\2\u0786\u0789\5\u018a")
        buf.write("\u00c6\2\u0787\u0789\5\u0192\u00ca\2\u0788\u0783\3\2\2")
        buf.write("\2\u0788\u0784\3\2\2\2\u0788\u0785\3\2\2\2\u0788\u0786")
        buf.write("\3\2\2\2\u0788\u0787\3\2\2\2\u0789\u0169\3\2\2\2\u078a")
        buf.write("\u078b\3\2\2\2\u078b\u016b\3\2\2\2\u078c\u0791\5\u0176")
        buf.write("\u00bc\2\u078d\u0791\5\u017e\u00c0\2\u078e\u0791\5\u018a")
        buf.write("\u00c6\2\u078f\u0791\5\u0192\u00ca\2\u0790\u078c\3\2\2")
        buf.write("\2\u0790\u078d\3\2\2\2\u0790\u078e\3\2\2\2\u0790\u078f")
        buf.write("\3\2\2\2\u0791\u016d\3\2\2\2\u0792\u07bb\5\2\2\2\u0793")
        buf.write("\u0798\5\66\34\2\u0794\u0795\7?\2\2\u0795\u0797\7@\2\2")
        buf.write("\u0796\u0794\3\2\2\2\u0797\u079a\3\2\2\2\u0798\u0796\3")
        buf.write("\2\2\2\u0798\u0799\3\2\2\2\u0799\u079b\3\2\2\2\u079a\u0798")
        buf.write("\3\2\2\2\u079b\u079c\7C\2\2\u079c\u079d\7\13\2\2\u079d")
        buf.write("\u07bb\3\2\2\2\u079e\u07a3\5v<\2\u079f\u07a0\7?\2\2\u07a0")
        buf.write("\u07a2\7@\2\2\u07a1\u079f\3\2\2\2\u07a2\u07a5\3\2\2\2")
        buf.write("\u07a3\u07a1\3\2\2\2\u07a3\u07a4\3\2\2\2\u07a4\u07a6\3")
        buf.write("\2\2\2\u07a5\u07a3\3\2\2\2\u07a6\u07a7\7C\2\2\u07a7\u07a8")
        buf.write("\7\13\2\2\u07a8\u07bb\3\2\2\2\u07a9\u07aa\7\62\2\2\u07aa")
        buf.write("\u07ab\7C\2\2\u07ab\u07bb\7\13\2\2\u07ac\u07bb\7-\2\2")
        buf.write("\u07ad\u07ae\5\66\34\2\u07ae\u07af\7C\2\2\u07af\u07b0")
        buf.write("\7-\2\2\u07b0\u07bb\3\2\2\2\u07b1\u07b2\7;\2\2\u07b2\u07b3")
        buf.write("\5\u019e\u00d0\2\u07b3\u07b4\7<\2\2\u07b4\u07bb\3\2\2")
        buf.write("\2\u07b5\u07bb\5\u0178\u00bd\2\u07b6\u07bb\5\u0180\u00c1")
        buf.write("\2\u07b7\u07bb\5\u0186\u00c4\2\u07b8\u07bb\5\u018c\u00c7")
        buf.write("\2\u07b9\u07bb\5\u0194\u00cb\2\u07ba\u0792\3\2\2\2\u07ba")
        buf.write("\u0793\3\2\2\2\u07ba\u079e\3\2\2\2\u07ba\u07a9\3\2\2\2")
        buf.write("\u07ba\u07ac\3\2\2\2\u07ba\u07ad\3\2\2\2\u07ba\u07b1\3")
        buf.write("\2\2\2\u07ba\u07b5\3\2\2\2\u07ba\u07b6\3\2\2\2\u07ba\u07b7")
        buf.write("\3\2\2\2\u07ba\u07b8\3\2\2\2\u07ba\u07b9\3\2\2\2\u07bb")
        buf.write("\u016f\3\2\2\2\u07bc\u07bd\3\2\2\2\u07bd\u0171\3\2\2\2")
        buf.write("\u07be\u07e6\5\2\2\2\u07bf\u07c4\5\66\34\2\u07c0\u07c1")
        buf.write("\7?\2\2\u07c1\u07c3\7@\2\2\u07c2\u07c0\3\2\2\2\u07c3\u07c6")
        buf.write("\3\2\2\2\u07c4\u07c2\3\2\2\2\u07c4\u07c5\3\2\2\2\u07c5")
        buf.write("\u07c7\3\2\2\2\u07c6\u07c4\3\2\2\2\u07c7\u07c8\7C\2\2")
        buf.write("\u07c8\u07c9\7\13\2\2\u07c9\u07e6\3\2\2\2\u07ca\u07cf")
        buf.write("\5v<\2\u07cb\u07cc\7?\2\2\u07cc\u07ce\7@\2\2\u07cd\u07cb")
        buf.write("\3\2\2\2\u07ce\u07d1\3\2\2\2\u07cf\u07cd\3\2\2\2\u07cf")
        buf.write("\u07d0\3\2\2\2\u07d0\u07d2\3\2\2\2\u07d1\u07cf\3\2\2\2")
        buf.write("\u07d2\u07d3\7C\2\2\u07d3\u07d4\7\13\2\2\u07d4\u07e6\3")
        buf.write("\2\2\2\u07d5\u07d6\7\62\2\2\u07d6\u07d7\7C\2\2\u07d7\u07e6")
        buf.write("\7\13\2\2\u07d8\u07e6\7-\2\2\u07d9\u07da\5\66\34\2\u07da")
        buf.write("\u07db\7C\2\2\u07db\u07dc\7-\2\2\u07dc\u07e6\3\2\2\2\u07dd")
        buf.write("\u07de\7;\2\2\u07de\u07df\5\u019e\u00d0\2\u07df\u07e0")
        buf.write("\7<\2\2\u07e0\u07e6\3\2\2\2\u07e1\u07e6\5\u0178\u00bd")
        buf.write("\2\u07e2\u07e6\5\u0180\u00c1\2\u07e3\u07e6\5\u018c\u00c7")
        buf.write("\2\u07e4\u07e6\5\u0194\u00cb\2\u07e5\u07be\3\2\2\2\u07e5")
        buf.write("\u07bf\3\2\2\2\u07e5\u07ca\3\2\2\2\u07e5\u07d5\3\2\2\2")
        buf.write("\u07e5\u07d8\3\2\2\2\u07e5\u07d9\3\2\2\2\u07e5\u07dd\3")
        buf.write("\2\2\2\u07e5\u07e1\3\2\2\2\u07e5\u07e2\3\2\2\2\u07e5\u07e3")
        buf.write("\3\2\2\2\u07e5\u07e4\3\2\2\2\u07e6\u0173\3\2\2\2\u07e7")
        buf.write("\u07e9\7!\2\2\u07e8\u07ea\5*\26\2\u07e9\u07e8\3\2\2\2")
        buf.write("\u07e9\u07ea\3\2\2\2\u07ea\u07ee\3\2\2\2\u07eb\u07ed\5")
        buf.write("\u00e6t\2\u07ec\u07eb\3\2\2\2\u07ed\u07f0\3\2\2\2\u07ee")
        buf.write("\u07ec\3\2\2\2\u07ee\u07ef\3\2\2\2\u07ef\u07f1\3\2\2\2")
        buf.write("\u07f0\u07ee\3\2\2\2\u07f1\u07fc\7h\2\2\u07f2\u07f6\7")
        buf.write("C\2\2\u07f3\u07f5\5\u00e6t\2\u07f4\u07f3\3\2\2\2\u07f5")
        buf.write("\u07f8\3\2\2\2\u07f6\u07f4\3\2\2\2\u07f6\u07f7\3\2\2\2")
        buf.write("\u07f7\u07f9\3\2\2\2\u07f8\u07f6\3\2\2\2\u07f9\u07fb\7")
        buf.write("h\2\2\u07fa\u07f2\3\2\2\2\u07fb\u07fe\3\2\2\2\u07fc\u07fa")
        buf.write("\3\2\2\2\u07fc\u07fd\3\2\2\2\u07fd\u0800\3\2\2\2\u07fe")
        buf.write("\u07fc\3\2\2\2\u07ff\u0801\5\u017a\u00be\2\u0800\u07ff")
        buf.write("\3\2\2\2\u0800\u0801\3\2\2\2\u0801\u0802\3\2\2\2\u0802")
        buf.write("\u0804\7;\2\2\u0803\u0805\5\u018e\u00c8\2\u0804\u0803")
        buf.write("\3\2\2\2\u0804\u0805\3\2\2\2\u0805\u0806\3\2\2\2\u0806")
        buf.write("\u0808\7<\2\2\u0807\u0809\5b\62\2\u0808\u0807\3\2\2\2")
        buf.write("\u0808\u0809\3\2\2\2\u0809\u083b\3\2\2\2\u080a\u080b\5")
        buf.write(":\36\2\u080b\u080c\7C\2\2\u080c\u080e\7!\2\2\u080d\u080f")
        buf.write("\5*\26\2\u080e\u080d\3\2\2\2\u080e\u080f\3\2\2\2\u080f")
        buf.write("\u0813\3\2\2\2\u0810\u0812\5\u00e6t\2\u0811\u0810\3\2")
        buf.write("\2\2\u0812\u0815\3\2\2\2\u0813\u0811\3\2\2\2\u0813\u0814")
        buf.write("\3\2\2\2\u0814\u0816\3\2\2\2\u0815\u0813\3\2\2\2\u0816")
        buf.write("\u0818\7h\2\2\u0817\u0819\5\u017a\u00be\2\u0818\u0817")
        buf.write("\3\2\2\2\u0818\u0819\3\2\2\2\u0819\u081a\3\2\2\2\u081a")
        buf.write("\u081c\7;\2\2\u081b\u081d\5\u018e\u00c8\2\u081c\u081b")
        buf.write("\3\2\2\2\u081c\u081d\3\2\2\2\u081d\u081e\3\2\2\2\u081e")
        buf.write("\u0820\7<\2\2\u081f\u0821\5b\62\2\u0820\u081f\3\2\2\2")
        buf.write("\u0820\u0821\3\2\2\2\u0821\u083b\3\2\2\2\u0822\u0823\5")
        buf.write("\u0160\u00b1\2\u0823\u0824\7C\2\2\u0824\u0826\7!\2\2\u0825")
        buf.write("\u0827\5*\26\2\u0826\u0825\3\2\2\2\u0826\u0827\3\2\2\2")
        buf.write("\u0827\u082b\3\2\2\2\u0828\u082a\5\u00e6t\2\u0829\u0828")
        buf.write("\3\2\2\2\u082a\u082d\3\2\2\2\u082b\u0829\3\2\2\2\u082b")
        buf.write("\u082c\3\2\2\2\u082c\u082e\3\2\2\2\u082d\u082b\3\2\2\2")
        buf.write("\u082e\u0830\7h\2\2\u082f\u0831\5\u017a\u00be\2\u0830")
        buf.write("\u082f\3\2\2\2\u0830\u0831\3\2\2\2\u0831\u0832\3\2\2\2")
        buf.write("\u0832\u0834\7;\2\2\u0833\u0835\5\u018e\u00c8\2\u0834")
        buf.write("\u0833\3\2\2\2\u0834\u0835\3\2\2\2\u0835\u0836\3\2\2\2")
        buf.write("\u0836\u0838\7<\2\2\u0837\u0839\5b\62\2\u0838\u0837\3")
        buf.write("\2\2\2\u0838\u0839\3\2\2\2\u0839\u083b\3\2\2\2\u083a\u07e7")
        buf.write("\3\2\2\2\u083a\u080a\3\2\2\2\u083a\u0822\3\2\2\2\u083b")
        buf.write("\u0175\3\2\2\2\u083c\u083d\7C\2\2\u083d\u083f\7!\2\2\u083e")
        buf.write("\u0840\5*\26\2\u083f\u083e\3\2\2\2\u083f\u0840\3\2\2\2")
        buf.write("\u0840\u0844\3\2\2\2\u0841\u0843\5\u00e6t\2\u0842\u0841")
        buf.write("\3\2\2\2\u0843\u0846\3\2\2\2\u0844\u0842\3\2\2\2\u0844")
        buf.write("\u0845\3\2\2\2\u0845\u0847\3\2\2\2\u0846\u0844\3\2\2\2")
        buf.write("\u0847\u0849\7h\2\2\u0848\u084a\5\u017a\u00be\2\u0849")
        buf.write("\u0848\3\2\2\2\u0849\u084a\3\2\2\2\u084a\u084b\3\2\2\2")
        buf.write("\u084b\u084d\7;\2\2\u084c\u084e\5\u018e\u00c8\2\u084d")
        buf.write("\u084c\3\2\2\2\u084d\u084e\3\2\2\2\u084e\u084f\3\2\2\2")
        buf.write("\u084f\u0851\7<\2\2\u0850\u0852\5b\62\2\u0851\u0850\3")
        buf.write("\2\2\2\u0851\u0852\3\2\2\2\u0852\u0177\3\2\2\2\u0853\u0855")
        buf.write("\7!\2\2\u0854\u0856\5*\26\2\u0855\u0854\3\2\2\2\u0855")
        buf.write("\u0856\3\2\2\2\u0856\u085a\3\2\2\2\u0857\u0859\5\u00e6")
        buf.write("t\2\u0858\u0857\3\2\2\2\u0859\u085c\3\2\2\2\u085a\u0858")
        buf.write("\3\2\2\2\u085a\u085b\3\2\2\2\u085b\u085d\3\2\2\2\u085c")
        buf.write("\u085a\3\2\2\2\u085d\u0868\7h\2\2\u085e\u0862\7C\2\2\u085f")
        buf.write("\u0861\5\u00e6t\2\u0860\u085f\3\2\2\2\u0861\u0864\3\2")
        buf.write("\2\2\u0862\u0860\3\2\2\2\u0862\u0863\3\2\2\2\u0863\u0865")
        buf.write("\3\2\2\2\u0864\u0862\3\2\2\2\u0865\u0867\7h\2\2\u0866")
        buf.write("\u085e\3\2\2\2\u0867\u086a\3\2\2\2\u0868\u0866\3\2\2\2")
        buf.write("\u0868\u0869\3\2\2\2\u0869\u086c\3\2\2\2\u086a\u0868\3")
        buf.write("\2\2\2\u086b\u086d\5\u017a\u00be\2\u086c\u086b\3\2\2\2")
        buf.write("\u086c\u086d\3\2\2\2\u086d\u086e\3\2\2\2\u086e\u0870\7")
        buf.write(";\2\2\u086f\u0871\5\u018e\u00c8\2\u0870\u086f\3\2\2\2")
        buf.write("\u0870\u0871\3\2\2\2\u0871\u0872\3\2\2\2\u0872\u0874\7")
        buf.write("<\2\2\u0873\u0875\5b\62\2\u0874\u0873\3\2\2\2\u0874\u0875")
        buf.write("\3\2\2\2\u0875\u088f\3\2\2\2\u0876\u0877\5:\36\2\u0877")
        buf.write("\u0878\7C\2\2\u0878\u087a\7!\2\2\u0879\u087b\5*\26\2\u087a")
        buf.write("\u0879\3\2\2\2\u087a\u087b\3\2\2\2\u087b\u087f\3\2\2\2")
        buf.write("\u087c\u087e\5\u00e6t\2\u087d\u087c\3\2\2\2\u087e\u0881")
        buf.write("\3\2\2\2\u087f\u087d\3\2\2\2\u087f\u0880\3\2\2\2\u0880")
        buf.write("\u0882\3\2\2\2\u0881\u087f\3\2\2\2\u0882\u0884\7h\2\2")
        buf.write("\u0883\u0885\5\u017a\u00be\2\u0884\u0883\3\2\2\2\u0884")
        buf.write("\u0885\3\2\2\2\u0885\u0886\3\2\2\2\u0886\u0888\7;\2\2")
        buf.write("\u0887\u0889\5\u018e\u00c8\2\u0888\u0887\3\2\2\2\u0888")
        buf.write("\u0889\3\2\2\2\u0889\u088a\3\2\2\2\u088a\u088c\7<\2\2")
        buf.write("\u088b\u088d\5b\62\2\u088c\u088b\3\2\2\2\u088c\u088d\3")
        buf.write("\2\2\2\u088d\u088f\3\2\2\2\u088e\u0853\3\2\2\2\u088e\u0876")
        buf.write("\3\2\2\2\u088f\u0179\3\2\2\2\u0890\u0894\5*\26\2\u0891")
        buf.write("\u0892\7F\2\2\u0892\u0894\7E\2\2\u0893\u0890\3\2\2\2\u0893")
        buf.write("\u0891\3\2\2\2\u0894\u017b\3\2\2\2\u0895\u0896\5\u0160")
        buf.write("\u00b1\2\u0896\u0897\7C\2\2\u0897\u0898\7h\2\2\u0898\u08a3")
        buf.write("\3\2\2\2\u0899\u089a\7*\2\2\u089a\u089b\7C\2\2\u089b\u08a3")
        buf.write("\7h\2\2\u089c\u089d\5\66\34\2\u089d\u089e\7C\2\2\u089e")
        buf.write("\u089f\7*\2\2\u089f\u08a0\7C\2\2\u08a0\u08a1\7h\2\2\u08a1")
        buf.write("\u08a3\3\2\2\2\u08a2\u0895\3\2\2\2\u08a2\u0899\3\2\2\2")
        buf.write("\u08a2\u089c\3\2\2\2\u08a3\u017d\3\2\2\2\u08a4\u08a5\7")
        buf.write("C\2\2\u08a5\u08a6\7h\2\2\u08a6\u017f\3\2\2\2\u08a7\u08a8")
        buf.write("\7*\2\2\u08a8\u08a9\7C\2\2\u08a9\u08b1\7h\2\2\u08aa\u08ab")
        buf.write("\5\66\34\2\u08ab\u08ac\7C\2\2\u08ac\u08ad\7*\2\2\u08ad")
        buf.write("\u08ae\7C\2\2\u08ae\u08af\7h\2\2\u08af\u08b1\3\2\2\2\u08b0")
        buf.write("\u08a7\3\2\2\2\u08b0\u08aa\3\2\2\2\u08b1\u0181\3\2\2\2")
        buf.write("\u08b2\u08b3\5:\36\2\u08b3\u08b4\7?\2\2\u08b4\u08b5\5")
        buf.write("\u019e\u00d0\2\u08b5\u08b6\7@\2\2\u08b6\u08bd\3\2\2\2")
        buf.write("\u08b7\u08b8\5\u0166\u00b4\2\u08b8\u08b9\7?\2\2\u08b9")
        buf.write("\u08ba\5\u019e\u00d0\2\u08ba\u08bb\7@\2\2\u08bb\u08bd")
        buf.write("\3\2\2\2\u08bc\u08b2\3\2\2\2\u08bc\u08b7\3\2\2\2\u08bd")
        buf.write("\u08c5\3\2\2\2\u08be\u08bf\5\u0164\u00b3\2\u08bf\u08c0")
        buf.write("\7?\2\2\u08c0\u08c1\5\u019e\u00d0\2\u08c1\u08c2\7@\2\2")
        buf.write("\u08c2\u08c4\3\2\2\2\u08c3\u08be\3\2\2\2\u08c4\u08c7\3")
        buf.write("\2\2\2\u08c5\u08c3\3\2\2\2\u08c5\u08c6\3\2\2\2\u08c6\u0183")
        buf.write("\3\2\2\2\u08c7\u08c5\3\2\2\2\u08c8\u08c9\5\u016c\u00b7")
        buf.write("\2\u08c9\u08ca\7?\2\2\u08ca\u08cb\5\u019e\u00d0\2\u08cb")
        buf.write("\u08cc\7@\2\2\u08cc\u08d4\3\2\2\2\u08cd\u08ce\5\u016a")
        buf.write("\u00b6\2\u08ce\u08cf\7?\2\2\u08cf\u08d0\5\u019e\u00d0")
        buf.write("\2\u08d0\u08d1\7@\2\2\u08d1\u08d3\3\2\2\2\u08d2\u08cd")
        buf.write("\3\2\2\2\u08d3\u08d6\3\2\2\2\u08d4\u08d2\3\2\2\2\u08d4")
        buf.write("\u08d5\3\2\2\2\u08d5\u0185\3\2\2\2\u08d6\u08d4\3\2\2\2")
        buf.write("\u08d7\u08d8\5:\36\2\u08d8\u08d9\7?\2\2\u08d9\u08da\5")
        buf.write("\u019e\u00d0\2\u08da\u08db\7@\2\2\u08db\u08e2\3\2\2\2")
        buf.write("\u08dc\u08dd\5\u0172\u00ba\2\u08dd\u08de\7?\2\2\u08de")
        buf.write("\u08df\5\u019e\u00d0\2\u08df\u08e0\7@\2\2\u08e0\u08e2")
        buf.write("\3\2\2\2\u08e1\u08d7\3\2\2\2\u08e1\u08dc\3\2\2\2\u08e2")
        buf.write("\u08ea\3\2\2\2\u08e3\u08e4\5\u0170\u00b9\2\u08e4\u08e5")
        buf.write("\7?\2\2\u08e5\u08e6\5\u019e\u00d0\2\u08e6\u08e7\7@\2\2")
        buf.write("\u08e7\u08e9\3\2\2\2\u08e8\u08e3\3\2\2\2\u08e9\u08ec\3")
        buf.write("\2\2\2\u08ea\u08e8\3\2\2\2\u08ea\u08eb\3\2\2\2\u08eb\u0187")
        buf.write("\3\2\2\2\u08ec\u08ea\3\2\2\2\u08ed\u08ee\5<\37\2\u08ee")
        buf.write("\u08f0\7;\2\2\u08ef\u08f1\5\u018e\u00c8\2\u08f0\u08ef")
        buf.write("\3\2\2\2\u08f0\u08f1\3\2\2\2\u08f1\u08f2\3\2\2\2\u08f2")
        buf.write("\u08f3\7<\2\2\u08f3\u0932\3\2\2\2\u08f4\u08f5\5\66\34")
        buf.write("\2\u08f5\u08f7\7C\2\2\u08f6\u08f8\5*\26\2\u08f7\u08f6")
        buf.write("\3\2\2\2\u08f7\u08f8\3\2\2\2\u08f8\u08f9\3\2\2\2\u08f9")
        buf.write("\u08fa\7h\2\2\u08fa\u08fc\7;\2\2\u08fb\u08fd\5\u018e\u00c8")
        buf.write("\2\u08fc\u08fb\3\2\2\2\u08fc\u08fd\3\2\2\2\u08fd\u08fe")
        buf.write("\3\2\2\2\u08fe\u08ff\7<\2\2\u08ff\u0932\3\2\2\2\u0900")
        buf.write("\u0901\5:\36\2\u0901\u0903\7C\2\2\u0902\u0904\5*\26\2")
        buf.write("\u0903\u0902\3\2\2\2\u0903\u0904\3\2\2\2\u0904\u0905\3")
        buf.write("\2\2\2\u0905\u0906\7h\2\2\u0906\u0908\7;\2\2\u0907\u0909")
        buf.write("\5\u018e\u00c8\2\u0908\u0907\3\2\2\2\u0908\u0909\3\2\2")
        buf.write("\2\u0909\u090a\3\2\2\2\u090a\u090b\7<\2\2\u090b\u0932")
        buf.write("\3\2\2\2\u090c\u090d\5\u0160\u00b1\2\u090d\u090f\7C\2")
        buf.write("\2\u090e\u0910\5*\26\2\u090f\u090e\3\2\2\2\u090f\u0910")
        buf.write("\3\2\2\2\u0910\u0911\3\2\2\2\u0911\u0912\7h\2\2\u0912")
        buf.write("\u0914\7;\2\2\u0913\u0915\5\u018e\u00c8\2\u0914\u0913")
        buf.write("\3\2\2\2\u0914\u0915\3\2\2\2\u0915\u0916\3\2\2\2\u0916")
        buf.write("\u0917\7<\2\2\u0917\u0932\3\2\2\2\u0918\u0919\7*\2\2\u0919")
        buf.write("\u091b\7C\2\2\u091a\u091c\5*\26\2\u091b\u091a\3\2\2\2")
        buf.write("\u091b\u091c\3\2\2\2\u091c\u091d\3\2\2\2\u091d\u091e\7")
        buf.write("h\2\2\u091e\u0920\7;\2\2\u091f\u0921\5\u018e\u00c8\2\u0920")
        buf.write("\u091f\3\2\2\2\u0920\u0921\3\2\2\2\u0921\u0922\3\2\2\2")
        buf.write("\u0922\u0932\7<\2\2\u0923\u0924\5\66\34\2\u0924\u0925")
        buf.write("\7C\2\2\u0925\u0926\7*\2\2\u0926\u0928\7C\2\2\u0927\u0929")
        buf.write("\5*\26\2\u0928\u0927\3\2\2\2\u0928\u0929\3\2\2\2\u0929")
        buf.write("\u092a\3\2\2\2\u092a\u092b\7h\2\2\u092b\u092d\7;\2\2\u092c")
        buf.write("\u092e\5\u018e\u00c8\2\u092d\u092c\3\2\2\2\u092d\u092e")
        buf.write("\3\2\2\2\u092e\u092f\3\2\2\2\u092f\u0930\7<\2\2\u0930")
        buf.write("\u0932\3\2\2\2\u0931\u08ed\3\2\2\2\u0931\u08f4\3\2\2\2")
        buf.write("\u0931\u0900\3\2\2\2\u0931\u090c\3\2\2\2\u0931\u0918\3")
        buf.write("\2\2\2\u0931\u0923\3\2\2\2\u0932\u0189\3\2\2\2\u0933\u0935")
        buf.write("\7C\2\2\u0934\u0936\5*\26\2\u0935\u0934\3\2\2\2\u0935")
        buf.write("\u0936\3\2\2\2\u0936\u0937\3\2\2\2\u0937\u0938\7h\2\2")
        buf.write("\u0938\u093a\7;\2\2\u0939\u093b\5\u018e\u00c8\2\u093a")
        buf.write("\u0939\3\2\2\2\u093a\u093b\3\2\2\2\u093b\u093c\3\2\2\2")
        buf.write("\u093c\u093d\7<\2\2\u093d\u018b\3\2\2\2\u093e\u093f\5")
        buf.write("<\37\2\u093f\u0941\7;\2\2\u0940\u0942\5\u018e\u00c8\2")
        buf.write("\u0941\u0940\3\2\2\2\u0941\u0942\3\2\2\2\u0942\u0943\3")
        buf.write("\2\2\2\u0943\u0944\7<\2\2\u0944\u0977\3\2\2\2\u0945\u0946")
        buf.write("\5\66\34\2\u0946\u0948\7C\2\2\u0947\u0949\5*\26\2\u0948")
        buf.write("\u0947\3\2\2\2\u0948\u0949\3\2\2\2\u0949\u094a\3\2\2\2")
        buf.write("\u094a\u094b\7h\2\2\u094b\u094d\7;\2\2\u094c\u094e\5\u018e")
        buf.write("\u00c8\2\u094d\u094c\3\2\2\2\u094d\u094e\3\2\2\2\u094e")
        buf.write("\u094f\3\2\2\2\u094f\u0950\7<\2\2\u0950\u0977\3\2\2\2")
        buf.write("\u0951\u0952\5:\36\2\u0952\u0954\7C\2\2\u0953\u0955\5")
        buf.write("*\26\2\u0954\u0953\3\2\2\2\u0954\u0955\3\2\2\2\u0955\u0956")
        buf.write("\3\2\2\2\u0956\u0957\7h\2\2\u0957\u0959\7;\2\2\u0958\u095a")
        buf.write("\5\u018e\u00c8\2\u0959\u0958\3\2\2\2\u0959\u095a\3\2\2")
        buf.write("\2\u095a\u095b\3\2\2\2\u095b\u095c\7<\2\2\u095c\u0977")
        buf.write("\3\2\2\2\u095d\u095e\7*\2\2\u095e\u0960\7C\2\2\u095f\u0961")
        buf.write("\5*\26\2\u0960\u095f\3\2\2\2\u0960\u0961\3\2\2\2\u0961")
        buf.write("\u0962\3\2\2\2\u0962\u0963\7h\2\2\u0963\u0965\7;\2\2\u0964")
        buf.write("\u0966\5\u018e\u00c8\2\u0965\u0964\3\2\2\2\u0965\u0966")
        buf.write("\3\2\2\2\u0966\u0967\3\2\2\2\u0967\u0977\7<\2\2\u0968")
        buf.write("\u0969\5\66\34\2\u0969\u096a\7C\2\2\u096a\u096b\7*\2\2")
        buf.write("\u096b\u096d\7C\2\2\u096c\u096e\5*\26\2\u096d\u096c\3")
        buf.write("\2\2\2\u096d\u096e\3\2\2\2\u096e\u096f\3\2\2\2\u096f\u0970")
        buf.write("\7h\2\2\u0970\u0972\7;\2\2\u0971\u0973\5\u018e\u00c8\2")
        buf.write("\u0972\u0971\3\2\2\2\u0972\u0973\3\2\2\2\u0973\u0974\3")
        buf.write("\2\2\2\u0974\u0975\7<\2\2\u0975\u0977\3\2\2\2\u0976\u093e")
        buf.write("\3\2\2\2\u0976\u0945\3\2\2\2\u0976\u0951\3\2\2\2\u0976")
        buf.write("\u095d\3\2\2\2\u0976\u0968\3\2\2\2\u0977\u018d\3\2\2\2")
        buf.write("\u0978\u097d\5\u019e\u00d0\2\u0979\u097a\7B\2\2\u097a")
        buf.write("\u097c\5\u019e\u00d0\2\u097b\u0979\3\2\2\2\u097c\u097f")
        buf.write("\3\2\2\2\u097d\u097b\3\2\2\2\u097d\u097e\3\2\2\2\u097e")
        buf.write("\u018f\3\2\2\2\u097f\u097d\3\2\2\2\u0980\u0981\5:\36\2")
        buf.write("\u0981\u0983\7\\\2\2\u0982\u0984\5*\26\2\u0983\u0982\3")
        buf.write("\2\2\2\u0983\u0984\3\2\2\2\u0984\u0985\3\2\2\2\u0985\u0986")
        buf.write("\7h\2\2\u0986\u09b0\3\2\2\2\u0987\u0988\5\f\7\2\u0988")
        buf.write("\u098a\7\\\2\2\u0989\u098b\5*\26\2\u098a\u0989\3\2\2\2")
        buf.write("\u098a\u098b\3\2\2\2\u098b\u098c\3\2\2\2\u098c\u098d\7")
        buf.write("h\2\2\u098d\u09b0\3\2\2\2\u098e\u098f\5\u0160\u00b1\2")
        buf.write("\u098f\u0991\7\\\2\2\u0990\u0992\5*\26\2\u0991\u0990\3")
        buf.write("\2\2\2\u0991\u0992\3\2\2\2\u0992\u0993\3\2\2\2\u0993\u0994")
        buf.write("\7h\2\2\u0994\u09b0\3\2\2\2\u0995\u0996\7*\2\2\u0996\u0998")
        buf.write("\7\\\2\2\u0997\u0999\5*\26\2\u0998\u0997\3\2\2\2\u0998")
        buf.write("\u0999\3\2\2\2\u0999\u099a\3\2\2\2\u099a\u09b0\7h\2\2")
        buf.write("\u099b\u099c\5\66\34\2\u099c\u099d\7C\2\2\u099d\u099e")
        buf.write("\7*\2\2\u099e\u09a0\7\\\2\2\u099f\u09a1\5*\26\2\u09a0")
        buf.write("\u099f\3\2\2\2\u09a0\u09a1\3\2\2\2\u09a1\u09a2\3\2\2\2")
        buf.write("\u09a2\u09a3\7h\2\2\u09a3\u09b0\3\2\2\2\u09a4\u09a5\5")
        buf.write("\20\t\2\u09a5\u09a7\7\\\2\2\u09a6\u09a8\5*\26\2\u09a7")
        buf.write("\u09a6\3\2\2\2\u09a7\u09a8\3\2\2\2\u09a8\u09a9\3\2\2\2")
        buf.write("\u09a9\u09aa\7!\2\2\u09aa\u09b0\3\2\2\2\u09ab\u09ac\5")
        buf.write("\36\20\2\u09ac\u09ad\7\\\2\2\u09ad\u09ae\7!\2\2\u09ae")
        buf.write("\u09b0\3\2\2\2\u09af\u0980\3\2\2\2\u09af\u0987\3\2\2\2")
        buf.write("\u09af\u098e\3\2\2\2\u09af\u0995\3\2\2\2\u09af\u099b\3")
        buf.write("\2\2\2\u09af\u09a4\3\2\2\2\u09af\u09ab\3\2\2\2\u09b0\u0191")
        buf.write("\3\2\2\2\u09b1\u09b3\7\\\2\2\u09b2\u09b4\5*\26\2\u09b3")
        buf.write("\u09b2\3\2\2\2\u09b3\u09b4\3\2\2\2\u09b4\u09b5\3\2\2\2")
        buf.write("\u09b5\u09b6\7h\2\2\u09b6\u0193\3\2\2\2\u09b7\u09b8\5")
        buf.write(":\36\2\u09b8\u09ba\7\\\2\2\u09b9\u09bb\5*\26\2\u09ba\u09b9")
        buf.write("\3\2\2\2\u09ba\u09bb\3\2\2\2\u09bb\u09bc\3\2\2\2\u09bc")
        buf.write("\u09bd\7h\2\2\u09bd\u09e0\3\2\2\2\u09be\u09bf\5\f\7\2")
        buf.write("\u09bf\u09c1\7\\\2\2\u09c0\u09c2\5*\26\2\u09c1\u09c0\3")
        buf.write("\2\2\2\u09c1\u09c2\3\2\2\2\u09c2\u09c3\3\2\2\2\u09c3\u09c4")
        buf.write("\7h\2\2\u09c4\u09e0\3\2\2\2\u09c5\u09c6\7*\2\2\u09c6\u09c8")
        buf.write("\7\\\2\2\u09c7\u09c9\5*\26\2\u09c8\u09c7\3\2\2\2\u09c8")
        buf.write("\u09c9\3\2\2\2\u09c9\u09ca\3\2\2\2\u09ca\u09e0\7h\2\2")
        buf.write("\u09cb\u09cc\5\66\34\2\u09cc\u09cd\7C\2\2\u09cd\u09ce")
        buf.write("\7*\2\2\u09ce\u09d0\7\\\2\2\u09cf\u09d1\5*\26\2\u09d0")
        buf.write("\u09cf\3\2\2\2\u09d0\u09d1\3\2\2\2\u09d1\u09d2\3\2\2\2")
        buf.write("\u09d2\u09d3\7h\2\2\u09d3\u09e0\3\2\2\2\u09d4\u09d5\5")
        buf.write("\20\t\2\u09d5\u09d7\7\\\2\2\u09d6\u09d8\5*\26\2\u09d7")
        buf.write("\u09d6\3\2\2\2\u09d7\u09d8\3\2\2\2\u09d8\u09d9\3\2\2\2")
        buf.write("\u09d9\u09da\7!\2\2\u09da\u09e0\3\2\2\2\u09db\u09dc\5")
        buf.write("\36\20\2\u09dc\u09dd\7\\\2\2\u09dd\u09de\7!\2\2\u09de")
        buf.write("\u09e0\3\2\2\2\u09df\u09b7\3\2\2\2\u09df\u09be\3\2\2\2")
        buf.write("\u09df\u09c5\3\2\2\2\u09df\u09cb\3\2\2\2\u09df\u09d4\3")
        buf.write("\2\2\2\u09df\u09db\3\2\2\2\u09e0\u0195\3\2\2\2\u09e1\u09e2")
        buf.write("\7!\2\2\u09e2\u09e3\5\4\3\2\u09e3\u09e5\5\u0198\u00cd")
        buf.write("\2\u09e4\u09e6\5 \21\2\u09e5\u09e4\3\2\2\2\u09e5\u09e6")
        buf.write("\3\2\2\2\u09e6\u09f8\3\2\2\2\u09e7\u09e8\7!\2\2\u09e8")
        buf.write("\u09e9\5\16\b\2\u09e9\u09eb\5\u0198\u00cd\2\u09ea\u09ec")
        buf.write("\5 \21\2\u09eb\u09ea\3\2\2\2\u09eb\u09ec\3\2\2\2\u09ec")
        buf.write("\u09f8\3\2\2\2\u09ed\u09ee\7!\2\2\u09ee\u09ef\5\4\3\2")
        buf.write("\u09ef\u09f0\5 \21\2\u09f0\u09f1\5\u00f8}\2\u09f1\u09f8")
        buf.write("\3\2\2\2\u09f2\u09f3\7!\2\2\u09f3\u09f4\5\16\b\2\u09f4")
        buf.write("\u09f5\5 \21\2\u09f5\u09f6\5\u00f8}\2\u09f6\u09f8\3\2")
        buf.write("\2\2\u09f7\u09e1\3\2\2\2\u09f7\u09e7\3\2\2\2\u09f7\u09ed")
        buf.write("\3\2\2\2\u09f7\u09f2\3\2\2\2\u09f8\u0197\3\2\2\2\u09f9")
        buf.write("\u09fd\5\u019a\u00ce\2\u09fa\u09fc\5\u019a\u00ce\2\u09fb")
        buf.write("\u09fa\3\2\2\2\u09fc\u09ff\3\2\2\2\u09fd\u09fb\3\2\2\2")
        buf.write("\u09fd\u09fe\3\2\2\2\u09fe\u0199\3\2\2\2\u09ff\u09fd\3")
        buf.write("\2\2\2\u0a00\u0a02\5\u00e6t\2\u0a01\u0a00\3\2\2\2\u0a02")
        buf.write("\u0a05\3\2\2\2\u0a03\u0a01\3\2\2\2\u0a03\u0a04\3\2\2\2")
        buf.write("\u0a04\u0a06\3\2\2\2\u0a05\u0a03\3\2\2\2\u0a06\u0a07\7")
        buf.write("?\2\2\u0a07\u0a08\5\u019e\u00d0\2\u0a08\u0a09\7@\2\2\u0a09")
        buf.write("\u019b\3\2\2\2\u0a0a\u0a0b\5\u019e\u00d0\2\u0a0b\u019d")
        buf.write("\3\2\2\2\u0a0c\u0a0f\5\u01a0\u00d1\2\u0a0d\u0a0f\5\u01a8")
        buf.write("\u00d5\2\u0a0e\u0a0c\3\2\2\2\u0a0e\u0a0d\3\2\2\2\u0a0f")
        buf.write("\u019f\3\2\2\2\u0a10\u0a11\5\u01a2\u00d2\2\u0a11\u0a12")
        buf.write("\7[\2\2\u0a12\u0a13\5\u01a6\u00d4\2\u0a13\u01a1\3\2\2")
        buf.write("\2\u0a14\u0a1f\7h\2\2\u0a15\u0a17\7;\2\2\u0a16\u0a18\5")
        buf.write("\u0096L\2\u0a17\u0a16\3\2\2\2\u0a17\u0a18\3\2\2\2\u0a18")
        buf.write("\u0a19\3\2\2\2\u0a19\u0a1f\7<\2\2\u0a1a\u0a1b\7;\2\2\u0a1b")
        buf.write("\u0a1c\5\u01a4\u00d3\2\u0a1c\u0a1d\7<\2\2\u0a1d\u0a1f")
        buf.write("\3\2\2\2\u0a1e\u0a14\3\2\2\2\u0a1e\u0a15\3\2\2\2\u0a1e")
        buf.write("\u0a1a\3\2\2\2\u0a1f\u01a3\3\2\2\2\u0a20\u0a25\7h\2\2")
        buf.write("\u0a21\u0a22\7B\2\2\u0a22\u0a24\7h\2\2\u0a23\u0a21\3\2")
        buf.write("\2\2\u0a24\u0a27\3\2\2\2\u0a25\u0a23\3\2\2\2\u0a25\u0a26")
        buf.write("\3\2\2\2\u0a26\u01a5\3\2\2\2\u0a27\u0a25\3\2\2\2\u0a28")
        buf.write("\u0a2b\5\u019e\u00d0\2\u0a29\u0a2b\5\u00fc\177\2\u0a2a")
        buf.write("\u0a28\3\2\2\2\u0a2a\u0a29\3\2\2\2\u0a2b\u01a7\3\2\2\2")
        buf.write("\u0a2c\u0a2f\5\u01b0\u00d9\2\u0a2d\u0a2f\5\u01aa\u00d6")
        buf.write("\2\u0a2e\u0a2c\3\2\2\2\u0a2e\u0a2d\3\2\2\2\u0a2f\u01a9")
        buf.write("\3\2\2\2\u0a30\u0a31\5\u01ac\u00d7\2\u0a31\u0a32\5\u01ae")
        buf.write("\u00d8\2\u0a32\u0a33\5\u019e\u00d0\2\u0a33\u01ab\3\2\2")
        buf.write("\2\u0a34\u0a38\5:\36\2\u0a35\u0a38\5\u017c\u00bf\2\u0a36")
        buf.write("\u0a38\5\u0182\u00c2\2\u0a37\u0a34\3\2\2\2\u0a37\u0a35")
        buf.write("\3\2\2\2\u0a37\u0a36\3\2\2\2\u0a38\u01ad\3\2\2\2\u0a39")
        buf.write("\u0a3a\t\5\2\2\u0a3a\u01af\3\2\2\2\u0a3b\u0a43\5\u01b2")
        buf.write("\u00da\2\u0a3c\u0a3d\5\u01b2\u00da\2\u0a3d\u0a3e\7I\2")
        buf.write("\2\u0a3e\u0a3f\5\u019e\u00d0\2\u0a3f\u0a40\7J\2\2\u0a40")
        buf.write("\u0a41\5\u01b0\u00d9\2\u0a41\u0a43\3\2\2\2\u0a42\u0a3b")
        buf.write("\3\2\2\2\u0a42\u0a3c\3\2\2\2\u0a43\u01b1\3\2\2\2\u0a44")
        buf.write("\u0a45\b\u00da\1\2\u0a45\u0a46\5\u01b4\u00db\2\u0a46\u0a4c")
        buf.write("\3\2\2\2\u0a47\u0a48\f\3\2\2\u0a48\u0a49\7P\2\2\u0a49")
        buf.write("\u0a4b\5\u01b4\u00db\2\u0a4a\u0a47\3\2\2\2\u0a4b\u0a4e")
        buf.write("\3\2\2\2\u0a4c\u0a4a\3\2\2\2\u0a4c\u0a4d\3\2\2\2\u0a4d")
        buf.write("\u01b3\3\2\2\2\u0a4e\u0a4c\3\2\2\2\u0a4f\u0a50\b\u00db")
        buf.write("\1\2\u0a50\u0a51\5\u01b6\u00dc\2\u0a51\u0a57\3\2\2\2\u0a52")
        buf.write("\u0a53\f\3\2\2\u0a53\u0a54\7O\2\2\u0a54\u0a56\5\u01b6")
        buf.write("\u00dc\2\u0a55\u0a52\3\2\2\2\u0a56\u0a59\3\2\2\2\u0a57")
        buf.write("\u0a55\3\2\2\2\u0a57\u0a58\3\2\2\2\u0a58\u01b5\3\2\2\2")
        buf.write("\u0a59\u0a57\3\2\2\2\u0a5a\u0a5b\b\u00dc\1\2\u0a5b\u0a5c")
        buf.write("\5\u01b8\u00dd\2\u0a5c\u0a62\3\2\2\2\u0a5d\u0a5e\f\3\2")
        buf.write("\2\u0a5e\u0a5f\7X\2\2\u0a5f\u0a61\5\u01b8\u00dd\2\u0a60")
        buf.write("\u0a5d\3\2\2\2\u0a61\u0a64\3\2\2\2\u0a62\u0a60\3\2\2\2")
        buf.write("\u0a62\u0a63\3\2\2\2\u0a63\u01b7\3\2\2\2\u0a64\u0a62\3")
        buf.write("\2\2\2\u0a65\u0a66\b\u00dd\1\2\u0a66\u0a67\5\u01ba\u00de")
        buf.write("\2\u0a67\u0a6d\3\2\2\2\u0a68\u0a69\f\3\2\2\u0a69\u0a6a")
        buf.write("\7Y\2\2\u0a6a\u0a6c\5\u01ba\u00de\2\u0a6b\u0a68\3\2\2")
        buf.write("\2\u0a6c\u0a6f\3\2\2\2\u0a6d\u0a6b\3\2\2\2\u0a6d\u0a6e")
        buf.write("\3\2\2\2\u0a6e\u01b9\3\2\2\2\u0a6f\u0a6d\3\2\2\2\u0a70")
        buf.write("\u0a71\b\u00de\1\2\u0a71\u0a72\5\u01bc\u00df\2\u0a72\u0a78")
        buf.write("\3\2\2\2\u0a73\u0a74\f\3\2\2\u0a74\u0a75\7W\2\2\u0a75")
        buf.write("\u0a77\5\u01bc\u00df\2\u0a76\u0a73\3\2\2\2\u0a77\u0a7a")
        buf.write("\3\2\2\2\u0a78\u0a76\3\2\2\2\u0a78\u0a79\3\2\2\2\u0a79")
        buf.write("\u01bb\3\2\2\2\u0a7a\u0a78\3\2\2\2\u0a7b\u0a7c\b\u00df")
        buf.write("\1\2\u0a7c\u0a7d\5\u01be\u00e0\2\u0a7d\u0a86\3\2\2\2\u0a7e")
        buf.write("\u0a7f\f\4\2\2\u0a7f\u0a80\7K\2\2\u0a80\u0a85\5\u01be")
        buf.write("\u00e0\2\u0a81\u0a82\f\3\2\2\u0a82\u0a83\7N\2\2\u0a83")
        buf.write("\u0a85\5\u01be\u00e0\2\u0a84\u0a7e\3\2\2\2\u0a84\u0a81")
        buf.write("\3\2\2\2\u0a85\u0a88\3\2\2\2\u0a86\u0a84\3\2\2\2\u0a86")
        buf.write("\u0a87\3\2\2\2\u0a87\u01bd\3\2\2\2\u0a88\u0a86\3\2\2\2")
        buf.write("\u0a89\u0a8a\b\u00e0\1\2\u0a8a\u0a8b\5\u01c0\u00e1\2\u0a8b")
        buf.write("\u0a9d\3\2\2\2\u0a8c\u0a8d\f\7\2\2\u0a8d\u0a8e\7F\2\2")
        buf.write("\u0a8e\u0a9c\5\u01c0\u00e1\2\u0a8f\u0a90\f\6\2\2\u0a90")
        buf.write("\u0a91\7E\2\2\u0a91\u0a9c\5\u01c0\u00e1\2\u0a92\u0a93")
        buf.write("\f\5\2\2\u0a93\u0a94\7L\2\2\u0a94\u0a9c\5\u01c0\u00e1")
        buf.write("\2\u0a95\u0a96\f\4\2\2\u0a96\u0a97\7M\2\2\u0a97\u0a9c")
        buf.write("\5\u01c0\u00e1\2\u0a98\u0a99\f\3\2\2\u0a99\u0a9a\7\34")
        buf.write("\2\2\u0a9a\u0a9c\5\f\7\2\u0a9b\u0a8c\3\2\2\2\u0a9b\u0a8f")
        buf.write("\3\2\2\2\u0a9b\u0a92\3\2\2\2\u0a9b\u0a95\3\2\2\2\u0a9b")
        buf.write("\u0a98\3\2\2\2\u0a9c\u0a9f\3\2\2\2\u0a9d\u0a9b\3\2\2\2")
        buf.write("\u0a9d\u0a9e\3\2\2\2\u0a9e\u01bf\3\2\2\2\u0a9f\u0a9d\3")
        buf.write("\2\2\2\u0aa0\u0aa1\b\u00e1\1\2\u0aa1\u0aa2\5\u01c2\u00e2")
        buf.write("\2\u0aa2\u0ab2\3\2\2\2\u0aa3\u0aa4\f\5\2\2\u0aa4\u0aa5")
        buf.write("\7F\2\2\u0aa5\u0aa6\7F\2\2\u0aa6\u0ab1\5\u01c2\u00e2\2")
        buf.write("\u0aa7\u0aa8\f\4\2\2\u0aa8\u0aa9\7E\2\2\u0aa9\u0aaa\7")
        buf.write("E\2\2\u0aaa\u0ab1\5\u01c2\u00e2\2\u0aab\u0aac\f\3\2\2")
        buf.write("\u0aac\u0aad\7E\2\2\u0aad\u0aae\7E\2\2\u0aae\u0aaf\7E")
        buf.write("\2\2\u0aaf\u0ab1\5\u01c2\u00e2\2\u0ab0\u0aa3\3\2\2\2\u0ab0")
        buf.write("\u0aa7\3\2\2\2\u0ab0\u0aab\3\2\2\2\u0ab1\u0ab4\3\2\2\2")
        buf.write("\u0ab2\u0ab0\3\2\2\2\u0ab2\u0ab3\3\2\2\2\u0ab3\u01c1\3")
        buf.write("\2\2\2\u0ab4\u0ab2\3\2\2\2\u0ab5\u0ab6\b\u00e2\1\2\u0ab6")
        buf.write("\u0ab7\5\u01c4\u00e3\2\u0ab7\u0ac0\3\2\2\2\u0ab8\u0ab9")
        buf.write("\f\4\2\2\u0ab9\u0aba\7S\2\2\u0aba\u0abf\5\u01c4\u00e3")
        buf.write("\2\u0abb\u0abc\f\3\2\2\u0abc\u0abd\7T\2\2\u0abd\u0abf")
        buf.write("\5\u01c4\u00e3\2\u0abe\u0ab8\3\2\2\2\u0abe\u0abb\3\2\2")
        buf.write("\2\u0abf\u0ac2\3\2\2\2\u0ac0\u0abe\3\2\2\2\u0ac0\u0ac1")
        buf.write("\3\2\2\2\u0ac1\u01c3\3\2\2\2\u0ac2\u0ac0\3\2\2\2\u0ac3")
        buf.write("\u0ac4\b\u00e3\1\2\u0ac4\u0ac5\5\u01c6\u00e4\2\u0ac5\u0ad1")
        buf.write("\3\2\2\2\u0ac6\u0ac7\f\5\2\2\u0ac7\u0ac8\7U\2\2\u0ac8")
        buf.write("\u0ad0\5\u01c6\u00e4\2\u0ac9\u0aca\f\4\2\2\u0aca\u0acb")
        buf.write("\7V\2\2\u0acb\u0ad0\5\u01c6\u00e4\2\u0acc\u0acd\f\3\2")
        buf.write("\2\u0acd\u0ace\7Z\2\2\u0ace\u0ad0\5\u01c6\u00e4\2\u0acf")
        buf.write("\u0ac6\3\2\2\2\u0acf\u0ac9\3\2\2\2\u0acf\u0acc\3\2\2\2")
        buf.write("\u0ad0\u0ad3\3\2\2\2\u0ad1\u0acf\3\2\2\2\u0ad1\u0ad2\3")
        buf.write("\2\2\2\u0ad2\u01c5\3\2\2\2\u0ad3\u0ad1\3\2\2\2\u0ad4\u0adc")
        buf.write("\5\u01c8\u00e5\2\u0ad5\u0adc\5\u01ca\u00e6\2\u0ad6\u0ad7")
        buf.write("\7S\2\2\u0ad7\u0adc\5\u01c6\u00e4\2\u0ad8\u0ad9\7T\2\2")
        buf.write("\u0ad9\u0adc\5\u01c6\u00e4\2\u0ada\u0adc\5\u01cc\u00e7")
        buf.write("\2\u0adb\u0ad4\3\2\2\2\u0adb\u0ad5\3\2\2\2\u0adb\u0ad6")
        buf.write("\3\2\2\2\u0adb\u0ad8\3\2\2\2\u0adb\u0ada\3\2\2\2\u0adc")
        buf.write("\u01c7\3\2\2\2\u0add\u0ade\7Q\2\2\u0ade\u0adf\5\u01c6")
        buf.write("\u00e4\2\u0adf\u01c9\3\2\2\2\u0ae0\u0ae1\7R\2\2\u0ae1")
        buf.write("\u0ae2\5\u01c6\u00e4\2\u0ae2\u01cb\3\2\2\2\u0ae3\u0aea")
        buf.write("\5\u01ce\u00e8\2\u0ae4\u0ae5\7H\2\2\u0ae5\u0aea\5\u01c6")
        buf.write("\u00e4\2\u0ae6\u0ae7\7G\2\2\u0ae7\u0aea\5\u01c6\u00e4")
        buf.write("\2\u0ae8\u0aea\5\u01d8\u00ed\2\u0ae9\u0ae3\3\2\2\2\u0ae9")
        buf.write("\u0ae4\3\2\2\2\u0ae9\u0ae6\3\2\2\2\u0ae9\u0ae8\3\2\2\2")
        buf.write("\u0aea\u01cd\3\2\2\2\u0aeb\u0aee\5\u0160\u00b1\2\u0aec")
        buf.write("\u0aee\5:\36\2\u0aed\u0aeb\3\2\2\2\u0aed\u0aec\3\2\2\2")
        buf.write("\u0aee\u0af3\3\2\2\2\u0aef\u0af2\5\u01d2\u00ea\2\u0af0")
        buf.write("\u0af2\5\u01d6\u00ec\2\u0af1\u0aef\3\2\2\2\u0af1\u0af0")
        buf.write("\3\2\2\2\u0af2\u0af5\3\2\2\2\u0af3\u0af1\3\2\2\2\u0af3")
        buf.write("\u0af4\3\2\2\2\u0af4\u01cf\3\2\2\2\u0af5\u0af3\3\2\2\2")
        buf.write("\u0af6\u0af7\5\u01ce\u00e8\2\u0af7\u0af8\7Q\2\2\u0af8")
        buf.write("\u01d1\3\2\2\2\u0af9\u0afa\7Q\2\2\u0afa\u01d3\3\2\2\2")
        buf.write("\u0afb\u0afc\5\u01ce\u00e8\2\u0afc\u0afd\7R\2\2\u0afd")
        buf.write("\u01d5\3\2\2\2\u0afe\u0aff\7R\2\2\u0aff\u01d7\3\2\2\2")
        buf.write("\u0b00\u0b01\7;\2\2\u0b01\u0b02\5\4\3\2\u0b02\u0b03\7")
        buf.write("<\2\2\u0b03\u0b04\5\u01c6\u00e4\2\u0b04\u0b1c\3\2\2\2")
        buf.write("\u0b05\u0b06\7;\2\2\u0b06\u0b0a\5\f\7\2\u0b07\u0b09\5")
        buf.write("(\25\2\u0b08\u0b07\3\2\2\2\u0b09\u0b0c\3\2\2\2\u0b0a\u0b08")
        buf.write("\3\2\2\2\u0b0a\u0b0b\3\2\2\2\u0b0b\u0b0d\3\2\2\2\u0b0c")
        buf.write("\u0b0a\3\2\2\2\u0b0d\u0b0e\7<\2\2\u0b0e\u0b0f\5\u01cc")
        buf.write("\u00e7\2\u0b0f\u0b1c\3\2\2\2\u0b10\u0b11\7;\2\2\u0b11")
        buf.write("\u0b15\5\f\7\2\u0b12\u0b14\5(\25\2\u0b13\u0b12\3\2\2\2")
        buf.write("\u0b14\u0b17\3\2\2\2\u0b15\u0b13\3\2\2\2\u0b15\u0b16\3")
        buf.write("\2\2\2\u0b16\u0b18\3\2\2\2\u0b17\u0b15\3\2\2\2\u0b18\u0b19")
        buf.write("\7<\2\2\u0b19\u0b1a\5\u01a0\u00d1\2\u0b1a\u0b1c\3\2\2")
        buf.write("\2\u0b1b\u0b00\3\2\2\2\u0b1b\u0b05\3\2\2\2\u0b1b\u0b10")
        buf.write("\3\2\2\2\u0b1c\u01d9\3\2\2\2\u0144\u01df\u01e6\u01ea\u01ee")
        buf.write("\u01f7\u01fb\u01ff\u0201\u0207\u020c\u0213\u0218\u021a")
        buf.write("\u0220\u0225\u022a\u022f\u023a\u0248\u024d\u0255\u025c")
        buf.write("\u0262\u0267\u0272\u0275\u0283\u0288\u028d\u0292\u0298")
        buf.write("\u02a2\u02aa\u02b4\u02bc\u02c8\u02cc\u02d1\u02d7\u02df")
        buf.write("\u02ec\u0309\u030d\u0312\u0318\u031b\u031e\u032a\u0335")
        buf.write("\u0343\u034a\u0353\u035a\u035f\u036e\u0375\u037b\u037f")
        buf.write("\u0383\u0387\u038b\u0390\u0394\u0398\u039a\u039f\u03a6")
        buf.write("\u03ab\u03ad\u03b3\u03b8\u03bc\u03cf\u03d4\u03e4\u03e9")
        buf.write("\u03ef\u03f5\u03f7\u03fb\u0400\u0404\u040c\u0413\u041b")
        buf.write("\u041e\u0423\u042b\u0430\u0437\u043e\u0443\u0449\u0455")
        buf.write("\u045a\u045e\u0468\u046d\u0475\u0478\u047d\u0485\u0488")
        buf.write("\u048d\u0492\u0497\u049c\u04a3\u04a8\u04b0\u04b5\u04ba")
        buf.write("\u04bf\u04c5\u04cb\u04ce\u04d1\u04da\u04e0\u04e6\u04e9")
        buf.write("\u04ec\u04f4\u04f9\u04fe\u0504\u0507\u0512\u051b\u0525")
        buf.write("\u052a\u0535\u053a\u0546\u054b\u0557\u0561\u0566\u056e")
        buf.write("\u0571\u0578\u0580\u0586\u058f\u0599\u059d\u05a0\u05a9")
        buf.write("\u05b7\u05ba\u05c3\u05c8\u05cf\u05d4\u05dc\u05e8\u05ef")
        buf.write("\u05fd\u0613\u0635\u0641\u0647\u0653\u0660\u067a\u067e")
        buf.write("\u0683\u0687\u068b\u0693\u0697\u069b\u06a2\u06ab\u06b3")
        buf.write("\u06c2\u06ce\u06d4\u06da\u06ef\u06f4\u06fa\u0706\u0711")
        buf.write("\u071b\u071e\u0723\u072c\u0732\u073c\u0741\u074a\u0761")
        buf.write("\u076b\u0781\u0788\u0790\u0798\u07a3\u07ba\u07c4\u07cf")
        buf.write("\u07e5\u07e9\u07ee\u07f6\u07fc\u0800\u0804\u0808\u080e")
        buf.write("\u0813\u0818\u081c\u0820\u0826\u082b\u0830\u0834\u0838")
        buf.write("\u083a\u083f\u0844\u0849\u084d\u0851\u0855\u085a\u0862")
        buf.write("\u0868\u086c\u0870\u0874\u087a\u087f\u0884\u0888\u088c")
        buf.write("\u088e\u0893\u08a2\u08b0\u08bc\u08c5\u08d4\u08e1\u08ea")
        buf.write("\u08f0\u08f7\u08fc\u0903\u0908\u090f\u0914\u091b\u0920")
        buf.write("\u0928\u092d\u0931\u0935\u093a\u0941\u0948\u094d\u0954")
        buf.write("\u0959\u0960\u0965\u096d\u0972\u0976\u097d\u0983\u098a")
        buf.write("\u0991\u0998\u09a0\u09a7\u09af\u09b3\u09ba\u09c1\u09c8")
        buf.write("\u09d0\u09d7\u09df\u09e5\u09eb\u09f7\u09fd\u0a03\u0a0e")
        buf.write("\u0a17\u0a1e\u0a25\u0a2a\u0a2e\u0a37\u0a42\u0a4c\u0a57")
        buf.write("\u0a62\u0a6d\u0a78\u0a84\u0a86\u0a9b\u0a9d\u0ab0\u0ab2")
        buf.write("\u0abe\u0ac0\u0acf\u0ad1\u0adb\u0ae9\u0aed\u0af1\u0af3")
        buf.write("\u0b0a\u0b15\u0b1b")
        return buf.getvalue()


class Java8Parser ( Parser ):

    grammarFileName = "Java8Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'abstract'", "'assert'", "'boolean'", 
                     "'break'", "'byte'", "'case'", "'catch'", "'char'", 
                     "'class'", "'const'", "'continue'", "'default'", "'do'", 
                     "'double'", "'else'", "'enum'", "'extends'", "'final'", 
                     "'finally'", "'float'", "'for'", "'if'", "'goto'", 
                     "'implements'", "'import'", "'instanceof'", "'int'", 
                     "'interface'", "'long'", "'native'", "'new'", "'package'", 
                     "'private'", "'protected'", "'public'", "'return'", 
                     "'short'", "'static'", "'strictfp'", "'super'", "'switch'", 
                     "'synchronized'", "'this'", "'throw'", "'throws'", 
                     "'transient'", "'try'", "'void'", "'volatile'", "'while'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'null'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "';'", "','", "'.'", "'='", "'>'", "'<'", 
                     "'!'", "'~'", "'?'", "':'", "'=='", "'<='", "'>='", 
                     "'!='", "'&&'", "'||'", "'++'", "'--'", "'+'", "'-'", 
                     "'*'", "'/'", "'&'", "'|'", "'^'", "'%'", "'->'", "'::'", 
                     "'+='", "'-='", "'*='", "'/='", "'&='", "'|='", "'^='", 
                     "'%='", "'<<='", "'>>='", "'>>>='", "<INVALID>", "'@'", 
                     "'...'" ]

    symbolicNames = [ "<INVALID>", "ABSTRACT", "ASSERT", "BOOLEAN", "BREAK", 
                      "BYTE", "CASE", "CATCH", "CHAR", "CLASS", "CONST", 
                      "CONTINUE", "DEFAULT", "DO", "DOUBLE", "ELSE", "ENUM", 
                      "EXTENDS", "FINAL", "FINALLY", "FLOAT", "FOR", "IF", 
                      "GOTO", "IMPLEMENTS", "IMPORT", "INSTANCEOF", "INT", 
                      "INTERFACE", "LONG", "NATIVE", "NEW", "PACKAGE", "PRIVATE", 
                      "PROTECTED", "PUBLIC", "RETURN", "SHORT", "STATIC", 
                      "STRICTFP", "SUPER", "SWITCH", "SYNCHRONIZED", "THIS", 
                      "THROW", "THROWS", "TRANSIENT", "TRY", "VOID", "VOLATILE", 
                      "WHILE", "IntegerLiteral", "FloatingPointLiteral", 
                      "BooleanLiteral", "CharacterLiteral", "StringLiteral", 
                      "NullLiteral", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", "ASSIGN", 
                      "GT", "LT", "BANG", "TILDE", "QUESTION", "COLON", 
                      "EQUAL", "LE", "GE", "NOTEQUAL", "AND", "OR", "INC", 
                      "DEC", "ADD", "SUB", "MUL", "DIV", "BITAND", "BITOR", 
                      "CARET", "MOD", "ARROW", "COLONCOLON", "ADD_ASSIGN", 
                      "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "AND_ASSIGN", 
                      "OR_ASSIGN", "XOR_ASSIGN", "MOD_ASSIGN", "LSHIFT_ASSIGN", 
                      "RSHIFT_ASSIGN", "URSHIFT_ASSIGN", "Identifier", "AT", 
                      "ELLIPSIS", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_literal = 0
    RULE_primitiveType = 1
    RULE_numericType = 2
    RULE_integralType = 3
    RULE_floatingPointType = 4
    RULE_referenceType = 5
    RULE_classOrInterfaceType = 6
    RULE_classType = 7
    RULE_classType_lf_classOrInterfaceType = 8
    RULE_classType_lfno_classOrInterfaceType = 9
    RULE_interfaceType = 10
    RULE_interfaceType_lf_classOrInterfaceType = 11
    RULE_interfaceType_lfno_classOrInterfaceType = 12
    RULE_typeVariable = 13
    RULE_arrayType = 14
    RULE_dims = 15
    RULE_typeParameter = 16
    RULE_typeParameterModifier = 17
    RULE_typeBound = 18
    RULE_additionalBound = 19
    RULE_typeArguments = 20
    RULE_typeArgumentList = 21
    RULE_typeArgument = 22
    RULE_wildcard = 23
    RULE_wildcardBounds = 24
    RULE_packageName = 25
    RULE_typeName = 26
    RULE_packageOrTypeName = 27
    RULE_expressionName = 28
    RULE_methodName = 29
    RULE_ambiguousName = 30
    RULE_compilationUnit = 31
    RULE_packageDeclaration = 32
    RULE_packageModifier = 33
    RULE_importDeclaration = 34
    RULE_singleTypeImportDeclaration = 35
    RULE_typeImportOnDemandDeclaration = 36
    RULE_singleStaticImportDeclaration = 37
    RULE_staticImportOnDemandDeclaration = 38
    RULE_typeDeclaration = 39
    RULE_classDeclaration = 40
    RULE_normalClassDeclaration = 41
    RULE_classModifier = 42
    RULE_typeParameters = 43
    RULE_typeParameterList = 44
    RULE_superclass = 45
    RULE_superinterfaces = 46
    RULE_interfaceTypeList = 47
    RULE_classBody = 48
    RULE_classBodyDeclaration = 49
    RULE_classMemberDeclaration = 50
    RULE_fieldDeclaration = 51
    RULE_fieldModifier = 52
    RULE_variableDeclaratorList = 53
    RULE_variableDeclarator = 54
    RULE_variableDeclaratorId = 55
    RULE_variableInitializer = 56
    RULE_unannType = 57
    RULE_unannPrimitiveType = 58
    RULE_unannReferenceType = 59
    RULE_unannClassOrInterfaceType = 60
    RULE_unannClassType = 61
    RULE_unannClassType_lf_unannClassOrInterfaceType = 62
    RULE_unannClassType_lfno_unannClassOrInterfaceType = 63
    RULE_unannInterfaceType = 64
    RULE_unannInterfaceType_lf_unannClassOrInterfaceType = 65
    RULE_unannInterfaceType_lfno_unannClassOrInterfaceType = 66
    RULE_unannTypeVariable = 67
    RULE_unannArrayType = 68
    RULE_methodDeclaration = 69
    RULE_methodModifier = 70
    RULE_methodHeader = 71
    RULE_result = 72
    RULE_methodDeclarator = 73
    RULE_formalParameterList = 74
    RULE_formalParameters = 75
    RULE_formalParameter = 76
    RULE_variableModifier = 77
    RULE_lastFormalParameter = 78
    RULE_receiverParameter = 79
    RULE_throws_ = 80
    RULE_exceptionTypeList = 81
    RULE_exceptionType = 82
    RULE_methodBody = 83
    RULE_instanceInitializer = 84
    RULE_staticInitializer = 85
    RULE_constructorDeclaration = 86
    RULE_constructorModifier = 87
    RULE_constructorDeclarator = 88
    RULE_simpleTypeName = 89
    RULE_constructorBody = 90
    RULE_explicitConstructorInvocation = 91
    RULE_enumDeclaration = 92
    RULE_enumBody = 93
    RULE_enumConstantList = 94
    RULE_enumConstant = 95
    RULE_enumConstantModifier = 96
    RULE_enumBodyDeclarations = 97
    RULE_interfaceDeclaration = 98
    RULE_normalInterfaceDeclaration = 99
    RULE_interfaceModifier = 100
    RULE_extendsInterfaces = 101
    RULE_interfaceBody = 102
    RULE_interfaceMemberDeclaration = 103
    RULE_constantDeclaration = 104
    RULE_constantModifier = 105
    RULE_interfaceMethodDeclaration = 106
    RULE_interfaceMethodModifier = 107
    RULE_annotationTypeDeclaration = 108
    RULE_annotationTypeBody = 109
    RULE_annotationTypeMemberDeclaration = 110
    RULE_annotationTypeElementDeclaration = 111
    RULE_annotationTypeElementModifier = 112
    RULE_defaultValue = 113
    RULE_annotation = 114
    RULE_normalAnnotation = 115
    RULE_elementValuePairList = 116
    RULE_elementValuePair = 117
    RULE_elementValue = 118
    RULE_elementValueArrayInitializer = 119
    RULE_elementValueList = 120
    RULE_markerAnnotation = 121
    RULE_singleElementAnnotation = 122
    RULE_arrayInitializer = 123
    RULE_variableInitializerList = 124
    RULE_block = 125
    RULE_blockStatements = 126
    RULE_blockStatement = 127
    RULE_localVariableDeclarationStatement = 128
    RULE_localVariableDeclaration = 129
    RULE_statement = 130
    RULE_statementNoShortIf = 131
    RULE_statementWithoutTrailingSubstatement = 132
    RULE_emptyStatement = 133
    RULE_labeledStatement = 134
    RULE_labeledStatementNoShortIf = 135
    RULE_expressionStatement = 136
    RULE_statementExpression = 137
    RULE_ifThenStatement = 138
    RULE_ifThenElseStatement = 139
    RULE_ifThenElseStatementNoShortIf = 140
    RULE_assertStatement = 141
    RULE_switchStatement = 142
    RULE_switchBlock = 143
    RULE_switchBlockStatementGroup = 144
    RULE_switchLabels = 145
    RULE_switchLabel = 146
    RULE_enumConstantName = 147
    RULE_whileStatement = 148
    RULE_whileStatementNoShortIf = 149
    RULE_doStatement = 150
    RULE_forStatement = 151
    RULE_forStatementNoShortIf = 152
    RULE_basicForStatement = 153
    RULE_basicForStatementNoShortIf = 154
    RULE_forInit = 155
    RULE_forUpdate = 156
    RULE_statementExpressionList = 157
    RULE_enhancedForStatement = 158
    RULE_enhancedForStatementNoShortIf = 159
    RULE_breakStatement = 160
    RULE_continueStatement = 161
    RULE_returnStatement = 162
    RULE_throwStatement = 163
    RULE_synchronizedStatement = 164
    RULE_tryStatement = 165
    RULE_catches = 166
    RULE_catchClause = 167
    RULE_catchFormalParameter = 168
    RULE_catchType = 169
    RULE_finally_ = 170
    RULE_tryWithResourcesStatement = 171
    RULE_resourceSpecification = 172
    RULE_resourceList = 173
    RULE_resource = 174
    RULE_primary = 175
    RULE_primaryNoNewArray = 176
    RULE_primaryNoNewArray_lf_arrayAccess = 177
    RULE_primaryNoNewArray_lfno_arrayAccess = 178
    RULE_primaryNoNewArray_lf_primary = 179
    RULE_primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary = 180
    RULE_primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary = 181
    RULE_primaryNoNewArray_lfno_primary = 182
    RULE_primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary = 183
    RULE_primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary = 184
    RULE_classInstanceCreationExpression = 185
    RULE_classInstanceCreationExpression_lf_primary = 186
    RULE_classInstanceCreationExpression_lfno_primary = 187
    RULE_typeArgumentsOrDiamond = 188
    RULE_fieldAccess = 189
    RULE_fieldAccess_lf_primary = 190
    RULE_fieldAccess_lfno_primary = 191
    RULE_arrayAccess = 192
    RULE_arrayAccess_lf_primary = 193
    RULE_arrayAccess_lfno_primary = 194
    RULE_methodInvocation = 195
    RULE_methodInvocation_lf_primary = 196
    RULE_methodInvocation_lfno_primary = 197
    RULE_argumentList = 198
    RULE_methodReference = 199
    RULE_methodReference_lf_primary = 200
    RULE_methodReference_lfno_primary = 201
    RULE_arrayCreationExpression = 202
    RULE_dimExprs = 203
    RULE_dimExpr = 204
    RULE_constantExpression = 205
    RULE_expression = 206
    RULE_lambdaExpression = 207
    RULE_lambdaParameters = 208
    RULE_inferredFormalParameterList = 209
    RULE_lambdaBody = 210
    RULE_assignmentExpression = 211
    RULE_assignment = 212
    RULE_leftHandSide = 213
    RULE_assignmentOperator = 214
    RULE_conditionalExpression = 215
    RULE_conditionalOrExpression = 216
    RULE_conditionalAndExpression = 217
    RULE_inclusiveOrExpression = 218
    RULE_exclusiveOrExpression = 219
    RULE_andExpression = 220
    RULE_equalityExpression = 221
    RULE_relationalExpression = 222
    RULE_shiftExpression = 223
    RULE_additiveExpression = 224
    RULE_multiplicativeExpression = 225
    RULE_unaryExpression = 226
    RULE_preIncrementExpression = 227
    RULE_preDecrementExpression = 228
    RULE_unaryExpressionNotPlusMinus = 229
    RULE_postfixExpression = 230
    RULE_postIncrementExpression = 231
    RULE_postIncrementExpression_lf_postfixExpression = 232
    RULE_postDecrementExpression = 233
    RULE_postDecrementExpression_lf_postfixExpression = 234
    RULE_castExpression = 235

    ruleNames =  [ "literal", "primitiveType", "numericType", "integralType", 
                   "floatingPointType", "referenceType", "classOrInterfaceType", 
                   "classType", "classType_lf_classOrInterfaceType", "classType_lfno_classOrInterfaceType", 
                   "interfaceType", "interfaceType_lf_classOrInterfaceType", 
                   "interfaceType_lfno_classOrInterfaceType", "typeVariable", 
                   "arrayType", "dims", "typeParameter", "typeParameterModifier", 
                   "typeBound", "additionalBound", "typeArguments", "typeArgumentList", 
                   "typeArgument", "wildcard", "wildcardBounds", "packageName", 
                   "typeName", "packageOrTypeName", "expressionName", "methodName", 
                   "ambiguousName", "compilationUnit", "packageDeclaration", 
                   "packageModifier", "importDeclaration", "singleTypeImportDeclaration", 
                   "typeImportOnDemandDeclaration", "singleStaticImportDeclaration", 
                   "staticImportOnDemandDeclaration", "typeDeclaration", 
                   "classDeclaration", "normalClassDeclaration", "classModifier", 
                   "typeParameters", "typeParameterList", "superclass", 
                   "superinterfaces", "interfaceTypeList", "classBody", 
                   "classBodyDeclaration", "classMemberDeclaration", "fieldDeclaration", 
                   "fieldModifier", "variableDeclaratorList", "variableDeclarator", 
                   "variableDeclaratorId", "variableInitializer", "unannType", 
                   "unannPrimitiveType", "unannReferenceType", "unannClassOrInterfaceType", 
                   "unannClassType", "unannClassType_lf_unannClassOrInterfaceType", 
                   "unannClassType_lfno_unannClassOrInterfaceType", "unannInterfaceType", 
                   "unannInterfaceType_lf_unannClassOrInterfaceType", "unannInterfaceType_lfno_unannClassOrInterfaceType", 
                   "unannTypeVariable", "unannArrayType", "methodDeclaration", 
                   "methodModifier", "methodHeader", "result", "methodDeclarator", 
                   "formalParameterList", "formalParameters", "formalParameter", 
                   "variableModifier", "lastFormalParameter", "receiverParameter", 
                   "throws_", "exceptionTypeList", "exceptionType", "methodBody", 
                   "instanceInitializer", "staticInitializer", "constructorDeclaration", 
                   "constructorModifier", "constructorDeclarator", "simpleTypeName", 
                   "constructorBody", "explicitConstructorInvocation", "enumDeclaration", 
                   "enumBody", "enumConstantList", "enumConstant", "enumConstantModifier", 
                   "enumBodyDeclarations", "interfaceDeclaration", "normalInterfaceDeclaration", 
                   "interfaceModifier", "extendsInterfaces", "interfaceBody", 
                   "interfaceMemberDeclaration", "constantDeclaration", 
                   "constantModifier", "interfaceMethodDeclaration", "interfaceMethodModifier", 
                   "annotationTypeDeclaration", "annotationTypeBody", "annotationTypeMemberDeclaration", 
                   "annotationTypeElementDeclaration", "annotationTypeElementModifier", 
                   "defaultValue", "annotation", "normalAnnotation", "elementValuePairList", 
                   "elementValuePair", "elementValue", "elementValueArrayInitializer", 
                   "elementValueList", "markerAnnotation", "singleElementAnnotation", 
                   "arrayInitializer", "variableInitializerList", "block", 
                   "blockStatements", "blockStatement", "localVariableDeclarationStatement", 
                   "localVariableDeclaration", "statement", "statementNoShortIf", 
                   "statementWithoutTrailingSubstatement", "emptyStatement", 
                   "labeledStatement", "labeledStatementNoShortIf", "expressionStatement", 
                   "statementExpression", "ifThenStatement", "ifThenElseStatement", 
                   "ifThenElseStatementNoShortIf", "assertStatement", "switchStatement", 
                   "switchBlock", "switchBlockStatementGroup", "switchLabels", 
                   "switchLabel", "enumConstantName", "whileStatement", 
                   "whileStatementNoShortIf", "doStatement", "forStatement", 
                   "forStatementNoShortIf", "basicForStatement", "basicForStatementNoShortIf", 
                   "forInit", "forUpdate", "statementExpressionList", "enhancedForStatement", 
                   "enhancedForStatementNoShortIf", "breakStatement", "continueStatement", 
                   "returnStatement", "throwStatement", "synchronizedStatement", 
                   "tryStatement", "catches", "catchClause", "catchFormalParameter", 
                   "catchType", "finally_", "tryWithResourcesStatement", 
                   "resourceSpecification", "resourceList", "resource", 
                   "primary", "primaryNoNewArray", "primaryNoNewArray_lf_arrayAccess", 
                   "primaryNoNewArray_lfno_arrayAccess", "primaryNoNewArray_lf_primary", 
                   "primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary", 
                   "primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary", 
                   "primaryNoNewArray_lfno_primary", "primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary", 
                   "primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary", 
                   "classInstanceCreationExpression", "classInstanceCreationExpression_lf_primary", 
                   "classInstanceCreationExpression_lfno_primary", "typeArgumentsOrDiamond", 
                   "fieldAccess", "fieldAccess_lf_primary", "fieldAccess_lfno_primary", 
                   "arrayAccess", "arrayAccess_lf_primary", "arrayAccess_lfno_primary", 
                   "methodInvocation", "methodInvocation_lf_primary", "methodInvocation_lfno_primary", 
                   "argumentList", "methodReference", "methodReference_lf_primary", 
                   "methodReference_lfno_primary", "arrayCreationExpression", 
                   "dimExprs", "dimExpr", "constantExpression", "expression", 
                   "lambdaExpression", "lambdaParameters", "inferredFormalParameterList", 
                   "lambdaBody", "assignmentExpression", "assignment", "leftHandSide", 
                   "assignmentOperator", "conditionalExpression", "conditionalOrExpression", 
                   "conditionalAndExpression", "inclusiveOrExpression", 
                   "exclusiveOrExpression", "andExpression", "equalityExpression", 
                   "relationalExpression", "shiftExpression", "additiveExpression", 
                   "multiplicativeExpression", "unaryExpression", "preIncrementExpression", 
                   "preDecrementExpression", "unaryExpressionNotPlusMinus", 
                   "postfixExpression", "postIncrementExpression", "postIncrementExpression_lf_postfixExpression", 
                   "postDecrementExpression", "postDecrementExpression_lf_postfixExpression", 
                   "castExpression" ]

    EOF = Token.EOF
    ABSTRACT=1
    ASSERT=2
    BOOLEAN=3
    BREAK=4
    BYTE=5
    CASE=6
    CATCH=7
    CHAR=8
    CLASS=9
    CONST=10
    CONTINUE=11
    DEFAULT=12
    DO=13
    DOUBLE=14
    ELSE=15
    ENUM=16
    EXTENDS=17
    FINAL=18
    FINALLY=19
    FLOAT=20
    FOR=21
    IF=22
    GOTO=23
    IMPLEMENTS=24
    IMPORT=25
    INSTANCEOF=26
    INT=27
    INTERFACE=28
    LONG=29
    NATIVE=30
    NEW=31
    PACKAGE=32
    PRIVATE=33
    PROTECTED=34
    PUBLIC=35
    RETURN=36
    SHORT=37
    STATIC=38
    STRICTFP=39
    SUPER=40
    SWITCH=41
    SYNCHRONIZED=42
    THIS=43
    THROW=44
    THROWS=45
    TRANSIENT=46
    TRY=47
    VOID=48
    VOLATILE=49
    WHILE=50
    IntegerLiteral=51
    FloatingPointLiteral=52
    BooleanLiteral=53
    CharacterLiteral=54
    StringLiteral=55
    NullLiteral=56
    LPAREN=57
    RPAREN=58
    LBRACE=59
    RBRACE=60
    LBRACK=61
    RBRACK=62
    SEMI=63
    COMMA=64
    DOT=65
    ASSIGN=66
    GT=67
    LT=68
    BANG=69
    TILDE=70
    QUESTION=71
    COLON=72
    EQUAL=73
    LE=74
    GE=75
    NOTEQUAL=76
    AND=77
    OR=78
    INC=79
    DEC=80
    ADD=81
    SUB=82
    MUL=83
    DIV=84
    BITAND=85
    BITOR=86
    CARET=87
    MOD=88
    ARROW=89
    COLONCOLON=90
    ADD_ASSIGN=91
    SUB_ASSIGN=92
    MUL_ASSIGN=93
    DIV_ASSIGN=94
    AND_ASSIGN=95
    OR_ASSIGN=96
    XOR_ASSIGN=97
    MOD_ASSIGN=98
    LSHIFT_ASSIGN=99
    RSHIFT_ASSIGN=100
    URSHIFT_ASSIGN=101
    Identifier=102
    AT=103
    ELLIPSIS=104
    WS=105
    COMMENT=106
    LINE_COMMENT=107

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(Java8Parser.IntegerLiteral, 0)

        def FloatingPointLiteral(self):
            return self.getToken(Java8Parser.FloatingPointLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(Java8Parser.BooleanLiteral, 0)

        def CharacterLiteral(self):
            return self.getToken(Java8Parser.CharacterLiteral, 0)

        def StringLiteral(self):
            return self.getToken(Java8Parser.StringLiteral, 0)

        def NullLiteral(self):
            return self.getToken(Java8Parser.NullLiteral, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = Java8Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericType(self):
            return self.getTypedRuleContext(Java8Parser.NumericTypeContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def BOOLEAN(self):
            return self.getToken(Java8Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)




    def primitiveType(self):

        localctx = Java8Parser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 474
                    self.annotation()
                    self.state = 479
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 480
                self.numericType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 481
                    self.annotation()
                    self.state = 486
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 487
                self.match(Java8Parser.BOOLEAN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integralType(self):
            return self.getTypedRuleContext(Java8Parser.IntegralTypeContext,0)


        def floatingPointType(self):
            return self.getTypedRuleContext(Java8Parser.FloatingPointTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_numericType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericType" ):
                listener.enterNumericType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericType" ):
                listener.exitNumericType(self)




    def numericType(self):

        localctx = Java8Parser.NumericTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_numericType)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.BYTE, Java8Parser.CHAR, Java8Parser.INT, Java8Parser.LONG, Java8Parser.SHORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.integralType()
                pass
            elif token in [Java8Parser.DOUBLE, Java8Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.floatingPointType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegralTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BYTE(self):
            return self.getToken(Java8Parser.BYTE, 0)

        def SHORT(self):
            return self.getToken(Java8Parser.SHORT, 0)

        def INT(self):
            return self.getToken(Java8Parser.INT, 0)

        def LONG(self):
            return self.getToken(Java8Parser.LONG, 0)

        def CHAR(self):
            return self.getToken(Java8Parser.CHAR, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_integralType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegralType" ):
                listener.enterIntegralType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegralType" ):
                listener.exitIntegralType(self)




    def integralType(self):

        localctx = Java8Parser.IntegralTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_integralType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.SHORT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatingPointTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(Java8Parser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(Java8Parser.DOUBLE, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_floatingPointType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatingPointType" ):
                listener.enterFloatingPointType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatingPointType" ):
                listener.exitFloatingPointType(self)




    def floatingPointType(self):

        localctx = Java8Parser.FloatingPointTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_floatingPointType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            _la = self._input.LA(1)
            if not(_la==Java8Parser.DOUBLE or _la==Java8Parser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.ClassOrInterfaceTypeContext,0)


        def typeVariable(self):
            return self.getTypedRuleContext(Java8Parser.TypeVariableContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(Java8Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_referenceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReferenceType" ):
                listener.enterReferenceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReferenceType" ):
                listener.exitReferenceType(self)




    def referenceType(self):

        localctx = Java8Parser.ReferenceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_referenceType)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.classOrInterfaceType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 499
                self.typeVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 500
                self.arrayType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classType_lfno_classOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.ClassType_lfno_classOrInterfaceTypeContext,0)


        def interfaceType_lfno_classOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.InterfaceType_lfno_classOrInterfaceTypeContext,0)


        def classType_lf_classOrInterfaceType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ClassType_lf_classOrInterfaceTypeContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ClassType_lf_classOrInterfaceTypeContext,i)


        def interfaceType_lf_classOrInterfaceType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.InterfaceType_lf_classOrInterfaceTypeContext)
            else:
                return self.getTypedRuleContext(Java8Parser.InterfaceType_lf_classOrInterfaceTypeContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_classOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassOrInterfaceType" ):
                listener.enterClassOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassOrInterfaceType" ):
                listener.exitClassOrInterfaceType(self)




    def classOrInterfaceType(self):

        localctx = Java8Parser.ClassOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_classOrInterfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 503
                self.classType_lfno_classOrInterfaceType()
                pass

            elif la_ == 2:
                self.state = 504
                self.interfaceType_lfno_classOrInterfaceType()
                pass


            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 509
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        self.state = 507
                        self.classType_lf_classOrInterfaceType()
                        pass

                    elif la_ == 2:
                        self.state = 508
                        self.interfaceType_lf_classOrInterfaceType()
                        pass

             
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def classOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.ClassOrInterfaceTypeContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_classType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassType" ):
                listener.enterClassType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassType" ):
                listener.exitClassType(self)




    def classType(self):

        localctx = Java8Parser.ClassTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_classType)
        self._la = 0 # Token type
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 517
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 514
                    self.annotation()
                    self.state = 519
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 520
                self.match(Java8Parser.Identifier)
                self.state = 522
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 521
                    self.typeArguments()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
                self.classOrInterfaceType()
                self.state = 525
                self.match(Java8Parser.DOT)
                self.state = 529
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 526
                    self.annotation()
                    self.state = 531
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 532
                self.match(Java8Parser.Identifier)
                self.state = 534
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 533
                    self.typeArguments()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassType_lf_classOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_classType_lf_classOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassType_lf_classOrInterfaceType" ):
                listener.enterClassType_lf_classOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassType_lf_classOrInterfaceType" ):
                listener.exitClassType_lf_classOrInterfaceType(self)




    def classType_lf_classOrInterfaceType(self):

        localctx = Java8Parser.ClassType_lf_classOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_classType_lf_classOrInterfaceType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(Java8Parser.DOT)
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 539
                self.annotation()
                self.state = 544
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 545
            self.match(Java8Parser.Identifier)
            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 546
                self.typeArguments()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassType_lfno_classOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_classType_lfno_classOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassType_lfno_classOrInterfaceType" ):
                listener.enterClassType_lfno_classOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassType_lfno_classOrInterfaceType" ):
                listener.exitClassType_lfno_classOrInterfaceType(self)




    def classType_lfno_classOrInterfaceType(self):

        localctx = Java8Parser.ClassType_lfno_classOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_classType_lfno_classOrInterfaceType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 549
                self.annotation()
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 555
            self.match(Java8Parser.Identifier)
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 556
                self.typeArguments()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classType(self):
            return self.getTypedRuleContext(Java8Parser.ClassTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_interfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceType" ):
                listener.enterInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceType" ):
                listener.exitInterfaceType(self)




    def interfaceType(self):

        localctx = Java8Parser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_interfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.classType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceType_lf_classOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classType_lf_classOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.ClassType_lf_classOrInterfaceTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_interfaceType_lf_classOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceType_lf_classOrInterfaceType" ):
                listener.enterInterfaceType_lf_classOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceType_lf_classOrInterfaceType" ):
                listener.exitInterfaceType_lf_classOrInterfaceType(self)




    def interfaceType_lf_classOrInterfaceType(self):

        localctx = Java8Parser.InterfaceType_lf_classOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_interfaceType_lf_classOrInterfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.classType_lf_classOrInterfaceType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceType_lfno_classOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classType_lfno_classOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.ClassType_lfno_classOrInterfaceTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_interfaceType_lfno_classOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceType_lfno_classOrInterfaceType" ):
                listener.enterInterfaceType_lfno_classOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceType_lfno_classOrInterfaceType" ):
                listener.exitInterfaceType_lfno_classOrInterfaceType(self)




    def interfaceType_lfno_classOrInterfaceType(self):

        localctx = Java8Parser.InterfaceType_lfno_classOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_interfaceType_lfno_classOrInterfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.classType_lfno_classOrInterfaceType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_typeVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeVariable" ):
                listener.enterTypeVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeVariable" ):
                listener.exitTypeVariable(self)




    def typeVariable(self):

        localctx = Java8Parser.TypeVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_typeVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 565
                self.annotation()
                self.state = 570
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 571
            self.match(Java8Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(Java8Parser.PrimitiveTypeContext,0)


        def dims(self):
            return self.getTypedRuleContext(Java8Parser.DimsContext,0)


        def classOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.ClassOrInterfaceTypeContext,0)


        def typeVariable(self):
            return self.getTypedRuleContext(Java8Parser.TypeVariableContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_arrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)




    def arrayType(self):

        localctx = Java8Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arrayType)
        try:
            self.state = 582
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 573
                self.primitiveType()
                self.state = 574
                self.dims()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 576
                self.classOrInterfaceType()
                self.state = 577
                self.dims()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 579
                self.typeVariable()
                self.state = 580
                self.dims()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.LBRACK)
            else:
                return self.getToken(Java8Parser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.RBRACK)
            else:
                return self.getToken(Java8Parser.RBRACK, i)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_dims

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDims" ):
                listener.enterDims(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDims" ):
                listener.exitDims(self)




    def dims(self):

        localctx = Java8Parser.DimsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dims)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 584
                self.annotation()
                self.state = 589
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 590
            self.match(Java8Parser.LBRACK)
            self.state = 591
            self.match(Java8Parser.RBRACK)
            self.state = 602
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 595
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==Java8Parser.AT:
                        self.state = 592
                        self.annotation()
                        self.state = 597
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 598
                    self.match(Java8Parser.LBRACK)
                    self.state = 599
                    self.match(Java8Parser.RBRACK) 
                self.state = 604
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def typeParameterModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.TypeParameterModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.TypeParameterModifierContext,i)


        def typeBound(self):
            return self.getTypedRuleContext(Java8Parser.TypeBoundContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_typeParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParameter" ):
                listener.enterTypeParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParameter" ):
                listener.exitTypeParameter(self)




    def typeParameter(self):

        localctx = Java8Parser.TypeParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_typeParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 605
                self.typeParameterModifier()
                self.state = 610
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 611
            self.match(Java8Parser.Identifier)
            self.state = 613
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.EXTENDS:
                self.state = 612
                self.typeBound()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeParameterModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_typeParameterModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParameterModifier" ):
                listener.enterTypeParameterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParameterModifier" ):
                listener.exitTypeParameterModifier(self)




    def typeParameterModifier(self):

        localctx = Java8Parser.TypeParameterModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_typeParameterModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.annotation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeBoundContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(Java8Parser.EXTENDS, 0)

        def typeVariable(self):
            return self.getTypedRuleContext(Java8Parser.TypeVariableContext,0)


        def classOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.ClassOrInterfaceTypeContext,0)


        def additionalBound(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AdditionalBoundContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AdditionalBoundContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_typeBound

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeBound" ):
                listener.enterTypeBound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeBound" ):
                listener.exitTypeBound(self)




    def typeBound(self):

        localctx = Java8Parser.TypeBoundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_typeBound)
        self._la = 0 # Token type
        try:
            self.state = 627
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 617
                self.match(Java8Parser.EXTENDS)
                self.state = 618
                self.typeVariable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 619
                self.match(Java8Parser.EXTENDS)
                self.state = 620
                self.classOrInterfaceType()
                self.state = 624
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.BITAND:
                    self.state = 621
                    self.additionalBound()
                    self.state = 626
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionalBoundContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BITAND(self):
            return self.getToken(Java8Parser.BITAND, 0)

        def interfaceType(self):
            return self.getTypedRuleContext(Java8Parser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_additionalBound

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionalBound" ):
                listener.enterAdditionalBound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionalBound" ):
                listener.exitAdditionalBound(self)




    def additionalBound(self):

        localctx = Java8Parser.AdditionalBoundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_additionalBound)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(Java8Parser.BITAND)
            self.state = 630
            self.interfaceType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(Java8Parser.LT, 0)

        def typeArgumentList(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentListContext,0)


        def GT(self):
            return self.getToken(Java8Parser.GT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_typeArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeArguments" ):
                listener.enterTypeArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeArguments" ):
                listener.exitTypeArguments(self)




    def typeArguments(self):

        localctx = Java8Parser.TypeArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_typeArguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.match(Java8Parser.LT)
            self.state = 633
            self.typeArgumentList()
            self.state = 634
            self.match(Java8Parser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.TypeArgumentContext)
            else:
                return self.getTypedRuleContext(Java8Parser.TypeArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_typeArgumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeArgumentList" ):
                listener.enterTypeArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeArgumentList" ):
                listener.exitTypeArgumentList(self)




    def typeArgumentList(self):

        localctx = Java8Parser.TypeArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_typeArgumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
            self.typeArgument()
            self.state = 641
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.COMMA:
                self.state = 637
                self.match(Java8Parser.COMMA)
                self.state = 638
                self.typeArgument()
                self.state = 643
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def referenceType(self):
            return self.getTypedRuleContext(Java8Parser.ReferenceTypeContext,0)


        def wildcard(self):
            return self.getTypedRuleContext(Java8Parser.WildcardContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_typeArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeArgument" ):
                listener.enterTypeArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeArgument" ):
                listener.exitTypeArgument(self)




    def typeArgument(self):

        localctx = Java8Parser.TypeArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_typeArgument)
        try:
            self.state = 646
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 644
                self.referenceType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 645
                self.wildcard()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WildcardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION(self):
            return self.getToken(Java8Parser.QUESTION, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def wildcardBounds(self):
            return self.getTypedRuleContext(Java8Parser.WildcardBoundsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_wildcard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWildcard" ):
                listener.enterWildcard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWildcard" ):
                listener.exitWildcard(self)




    def wildcard(self):

        localctx = Java8Parser.WildcardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_wildcard)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 648
                self.annotation()
                self.state = 653
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 654
            self.match(Java8Parser.QUESTION)
            self.state = 656
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.EXTENDS or _la==Java8Parser.SUPER:
                self.state = 655
                self.wildcardBounds()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WildcardBoundsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(Java8Parser.EXTENDS, 0)

        def referenceType(self):
            return self.getTypedRuleContext(Java8Parser.ReferenceTypeContext,0)


        def SUPER(self):
            return self.getToken(Java8Parser.SUPER, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_wildcardBounds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWildcardBounds" ):
                listener.enterWildcardBounds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWildcardBounds" ):
                listener.exitWildcardBounds(self)




    def wildcardBounds(self):

        localctx = Java8Parser.WildcardBoundsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_wildcardBounds)
        try:
            self.state = 662
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.EXTENDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 658
                self.match(Java8Parser.EXTENDS)
                self.state = 659
                self.referenceType()
                pass
            elif token in [Java8Parser.SUPER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 660
                self.match(Java8Parser.SUPER)
                self.state = 661
                self.referenceType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def packageName(self):
            return self.getTypedRuleContext(Java8Parser.PackageNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_packageName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageName" ):
                listener.enterPackageName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageName" ):
                listener.exitPackageName(self)



    def packageName(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.PackageNameContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_packageName, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.match(Java8Parser.Identifier)
            self._ctx.stop = self._input.LT(-1)
            self.state = 672
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java8Parser.PackageNameContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_packageName)
                    self.state = 667
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 668
                    self.match(Java8Parser.DOT)
                    self.state = 669
                    self.match(Java8Parser.Identifier) 
                self.state = 674
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def packageOrTypeName(self):
            return self.getTypedRuleContext(Java8Parser.PackageOrTypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)




    def typeName(self):

        localctx = Java8Parser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_typeName)
        try:
            self.state = 680
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 675
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 676
                self.packageOrTypeName(0)
                self.state = 677
                self.match(Java8Parser.DOT)
                self.state = 678
                self.match(Java8Parser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageOrTypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def packageOrTypeName(self):
            return self.getTypedRuleContext(Java8Parser.PackageOrTypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_packageOrTypeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageOrTypeName" ):
                listener.enterPackageOrTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageOrTypeName" ):
                listener.exitPackageOrTypeName(self)



    def packageOrTypeName(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.PackageOrTypeNameContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_packageOrTypeName, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 683
            self.match(Java8Parser.Identifier)
            self._ctx.stop = self._input.LT(-1)
            self.state = 690
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java8Parser.PackageOrTypeNameContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_packageOrTypeName)
                    self.state = 685
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 686
                    self.match(Java8Parser.DOT)
                    self.state = 687
                    self.match(Java8Parser.Identifier) 
                self.state = 692
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def ambiguousName(self):
            return self.getTypedRuleContext(Java8Parser.AmbiguousNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_expressionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionName" ):
                listener.enterExpressionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionName" ):
                listener.exitExpressionName(self)




    def expressionName(self):

        localctx = Java8Parser.ExpressionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expressionName)
        try:
            self.state = 698
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 693
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 694
                self.ambiguousName(0)
                self.state = 695
                self.match(Java8Parser.DOT)
                self.state = 696
                self.match(Java8Parser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_methodName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodName" ):
                listener.enterMethodName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodName" ):
                listener.exitMethodName(self)




    def methodName(self):

        localctx = Java8Parser.MethodNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_methodName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 700
            self.match(Java8Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AmbiguousNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def ambiguousName(self):
            return self.getTypedRuleContext(Java8Parser.AmbiguousNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_ambiguousName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAmbiguousName" ):
                listener.enterAmbiguousName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAmbiguousName" ):
                listener.exitAmbiguousName(self)



    def ambiguousName(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.AmbiguousNameContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_ambiguousName, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 703
            self.match(Java8Parser.Identifier)
            self._ctx.stop = self._input.LT(-1)
            self.state = 710
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java8Parser.AmbiguousNameContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_ambiguousName)
                    self.state = 705
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 706
                    self.match(Java8Parser.DOT)
                    self.state = 707
                    self.match(Java8Parser.Identifier) 
                self.state = 712
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Java8Parser.EOF, 0)

        def packageDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.PackageDeclarationContext,0)


        def importDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ImportDeclarationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ImportDeclarationContext,i)


        def typeDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.TypeDeclarationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.TypeDeclarationContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)




    def compilationUnit(self):

        localctx = Java8Parser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 713
                self.packageDeclaration()


            self.state = 719
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.IMPORT:
                self.state = 716
                self.importDeclaration()
                self.state = 721
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 725
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.CLASS) | (1 << Java8Parser.ENUM) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.INTERFACE) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP) | (1 << Java8Parser.SEMI))) != 0) or _la==Java8Parser.AT:
                self.state = 722
                self.typeDeclaration()
                self.state = 727
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 728
            self.match(Java8Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE(self):
            return self.getToken(Java8Parser.PACKAGE, 0)

        def packageName(self):
            return self.getTypedRuleContext(Java8Parser.PackageNameContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def packageModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.PackageModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.PackageModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_packageDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageDeclaration" ):
                listener.enterPackageDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageDeclaration" ):
                listener.exitPackageDeclaration(self)




    def packageDeclaration(self):

        localctx = Java8Parser.PackageDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_packageDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 733
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 730
                self.packageModifier()
                self.state = 735
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 736
            self.match(Java8Parser.PACKAGE)
            self.state = 737
            self.packageName(0)
            self.state = 738
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_packageModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageModifier" ):
                listener.enterPackageModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageModifier" ):
                listener.exitPackageModifier(self)




    def packageModifier(self):

        localctx = Java8Parser.PackageModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_packageModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 740
            self.annotation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleTypeImportDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.SingleTypeImportDeclarationContext,0)


        def typeImportOnDemandDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.TypeImportOnDemandDeclarationContext,0)


        def singleStaticImportDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.SingleStaticImportDeclarationContext,0)


        def staticImportOnDemandDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.StaticImportOnDemandDeclarationContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_importDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDeclaration" ):
                listener.enterImportDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDeclaration" ):
                listener.exitImportDeclaration(self)




    def importDeclaration(self):

        localctx = Java8Parser.ImportDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_importDeclaration)
        try:
            self.state = 746
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 742
                self.singleTypeImportDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 743
                self.typeImportOnDemandDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 744
                self.singleStaticImportDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 745
                self.staticImportOnDemandDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleTypeImportDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(Java8Parser.IMPORT, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_singleTypeImportDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleTypeImportDeclaration" ):
                listener.enterSingleTypeImportDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleTypeImportDeclaration" ):
                listener.exitSingleTypeImportDeclaration(self)




    def singleTypeImportDeclaration(self):

        localctx = Java8Parser.SingleTypeImportDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_singleTypeImportDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 748
            self.match(Java8Parser.IMPORT)
            self.state = 749
            self.typeName()
            self.state = 750
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeImportOnDemandDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(Java8Parser.IMPORT, 0)

        def packageOrTypeName(self):
            return self.getTypedRuleContext(Java8Parser.PackageOrTypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def MUL(self):
            return self.getToken(Java8Parser.MUL, 0)

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_typeImportOnDemandDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeImportOnDemandDeclaration" ):
                listener.enterTypeImportOnDemandDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeImportOnDemandDeclaration" ):
                listener.exitTypeImportOnDemandDeclaration(self)




    def typeImportOnDemandDeclaration(self):

        localctx = Java8Parser.TypeImportOnDemandDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_typeImportOnDemandDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 752
            self.match(Java8Parser.IMPORT)
            self.state = 753
            self.packageOrTypeName(0)
            self.state = 754
            self.match(Java8Parser.DOT)
            self.state = 755
            self.match(Java8Parser.MUL)
            self.state = 756
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleStaticImportDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(Java8Parser.IMPORT, 0)

        def STATIC(self):
            return self.getToken(Java8Parser.STATIC, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_singleStaticImportDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleStaticImportDeclaration" ):
                listener.enterSingleStaticImportDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleStaticImportDeclaration" ):
                listener.exitSingleStaticImportDeclaration(self)




    def singleStaticImportDeclaration(self):

        localctx = Java8Parser.SingleStaticImportDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_singleStaticImportDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 758
            self.match(Java8Parser.IMPORT)
            self.state = 759
            self.match(Java8Parser.STATIC)
            self.state = 760
            self.typeName()
            self.state = 761
            self.match(Java8Parser.DOT)
            self.state = 762
            self.match(Java8Parser.Identifier)
            self.state = 763
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticImportOnDemandDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(Java8Parser.IMPORT, 0)

        def STATIC(self):
            return self.getToken(Java8Parser.STATIC, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def MUL(self):
            return self.getToken(Java8Parser.MUL, 0)

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_staticImportOnDemandDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaticImportOnDemandDeclaration" ):
                listener.enterStaticImportOnDemandDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaticImportOnDemandDeclaration" ):
                listener.exitStaticImportOnDemandDeclaration(self)




    def staticImportOnDemandDeclaration(self):

        localctx = Java8Parser.StaticImportOnDemandDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_staticImportOnDemandDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 765
            self.match(Java8Parser.IMPORT)
            self.state = 766
            self.match(Java8Parser.STATIC)
            self.state = 767
            self.typeName()
            self.state = 768
            self.match(Java8Parser.DOT)
            self.state = 769
            self.match(Java8Parser.MUL)
            self.state = 770
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.InterfaceDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_typeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDeclaration" ):
                listener.enterTypeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDeclaration" ):
                listener.exitTypeDeclaration(self)




    def typeDeclaration(self):

        localctx = Java8Parser.TypeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_typeDeclaration)
        try:
            self.state = 775
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 772
                self.classDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 773
                self.interfaceDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 774
                self.match(Java8Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalClassDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.NormalClassDeclarationContext,0)


        def enumDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.EnumDeclarationContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)




    def classDeclaration(self):

        localctx = Java8Parser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_classDeclaration)
        try:
            self.state = 779
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 777
                self.normalClassDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 778
                self.enumDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(Java8Parser.CLASS, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def classBody(self):
            return self.getTypedRuleContext(Java8Parser.ClassBodyContext,0)


        def classModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ClassModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ClassModifierContext,i)


        def typeParameters(self):
            return self.getTypedRuleContext(Java8Parser.TypeParametersContext,0)


        def superclass(self):
            return self.getTypedRuleContext(Java8Parser.SuperclassContext,0)


        def superinterfaces(self):
            return self.getTypedRuleContext(Java8Parser.SuperinterfacesContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_normalClassDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalClassDeclaration" ):
                listener.enterNormalClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalClassDeclaration" ):
                listener.exitNormalClassDeclaration(self)




    def normalClassDeclaration(self):

        localctx = Java8Parser.NormalClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_normalClassDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 784
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP))) != 0) or _la==Java8Parser.AT:
                self.state = 781
                self.classModifier()
                self.state = 786
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 787
            self.match(Java8Parser.CLASS)
            self.state = 788
            self.match(Java8Parser.Identifier)
            self.state = 790
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LT:
                self.state = 789
                self.typeParameters()


            self.state = 793
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.EXTENDS:
                self.state = 792
                self.superclass()


            self.state = 796
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.IMPLEMENTS:
                self.state = 795
                self.superinterfaces()


            self.state = 798
            self.classBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java8Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(Java8Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(Java8Parser.PRIVATE, 0)

        def ABSTRACT(self):
            return self.getToken(Java8Parser.ABSTRACT, 0)

        def STATIC(self):
            return self.getToken(Java8Parser.STATIC, 0)

        def FINAL(self):
            return self.getToken(Java8Parser.FINAL, 0)

        def STRICTFP(self):
            return self.getToken(Java8Parser.STRICTFP, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_classModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassModifier" ):
                listener.enterClassModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassModifier" ):
                listener.exitClassModifier(self)




    def classModifier(self):

        localctx = Java8Parser.ClassModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_classModifier)
        try:
            self.state = 808
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 800
                self.annotation()
                pass
            elif token in [Java8Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 801
                self.match(Java8Parser.PUBLIC)
                pass
            elif token in [Java8Parser.PROTECTED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 802
                self.match(Java8Parser.PROTECTED)
                pass
            elif token in [Java8Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 803
                self.match(Java8Parser.PRIVATE)
                pass
            elif token in [Java8Parser.ABSTRACT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 804
                self.match(Java8Parser.ABSTRACT)
                pass
            elif token in [Java8Parser.STATIC]:
                self.enterOuterAlt(localctx, 6)
                self.state = 805
                self.match(Java8Parser.STATIC)
                pass
            elif token in [Java8Parser.FINAL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 806
                self.match(Java8Parser.FINAL)
                pass
            elif token in [Java8Parser.STRICTFP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 807
                self.match(Java8Parser.STRICTFP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(Java8Parser.LT, 0)

        def typeParameterList(self):
            return self.getTypedRuleContext(Java8Parser.TypeParameterListContext,0)


        def GT(self):
            return self.getToken(Java8Parser.GT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_typeParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParameters" ):
                listener.enterTypeParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParameters" ):
                listener.exitTypeParameters(self)




    def typeParameters(self):

        localctx = Java8Parser.TypeParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_typeParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 810
            self.match(Java8Parser.LT)
            self.state = 811
            self.typeParameterList()
            self.state = 812
            self.match(Java8Parser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.TypeParameterContext)
            else:
                return self.getTypedRuleContext(Java8Parser.TypeParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_typeParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParameterList" ):
                listener.enterTypeParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParameterList" ):
                listener.exitTypeParameterList(self)




    def typeParameterList(self):

        localctx = Java8Parser.TypeParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_typeParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 814
            self.typeParameter()
            self.state = 819
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.COMMA:
                self.state = 815
                self.match(Java8Parser.COMMA)
                self.state = 816
                self.typeParameter()
                self.state = 821
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperclassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(Java8Parser.EXTENDS, 0)

        def classType(self):
            return self.getTypedRuleContext(Java8Parser.ClassTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_superclass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperclass" ):
                listener.enterSuperclass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperclass" ):
                listener.exitSuperclass(self)




    def superclass(self):

        localctx = Java8Parser.SuperclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_superclass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 822
            self.match(Java8Parser.EXTENDS)
            self.state = 823
            self.classType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperinterfacesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPLEMENTS(self):
            return self.getToken(Java8Parser.IMPLEMENTS, 0)

        def interfaceTypeList(self):
            return self.getTypedRuleContext(Java8Parser.InterfaceTypeListContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_superinterfaces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperinterfaces" ):
                listener.enterSuperinterfaces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperinterfaces" ):
                listener.exitSuperinterfaces(self)




    def superinterfaces(self):

        localctx = Java8Parser.SuperinterfacesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_superinterfaces)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 825
            self.match(Java8Parser.IMPLEMENTS)
            self.state = 826
            self.interfaceTypeList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfaceType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.InterfaceTypeContext)
            else:
                return self.getTypedRuleContext(Java8Parser.InterfaceTypeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_interfaceTypeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceTypeList" ):
                listener.enterInterfaceTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceTypeList" ):
                listener.exitInterfaceTypeList(self)




    def interfaceTypeList(self):

        localctx = Java8Parser.InterfaceTypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_interfaceTypeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 828
            self.interfaceType()
            self.state = 833
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.COMMA:
                self.state = 829
                self.match(Java8Parser.COMMA)
                self.state = 830
                self.interfaceType()
                self.state = 835
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java8Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java8Parser.RBRACE, 0)

        def classBodyDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ClassBodyDeclarationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ClassBodyDeclarationContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)




    def classBody(self):

        localctx = Java8Parser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 836
            self.match(Java8Parser.LBRACE)
            self.state = 840
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.CLASS) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.ENUM) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.INTERFACE) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NATIVE) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP) | (1 << Java8Parser.SYNCHRONIZED) | (1 << Java8Parser.TRANSIENT) | (1 << Java8Parser.VOID) | (1 << Java8Parser.VOLATILE) | (1 << Java8Parser.LBRACE) | (1 << Java8Parser.SEMI))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (Java8Parser.LT - 68)) | (1 << (Java8Parser.Identifier - 68)) | (1 << (Java8Parser.AT - 68)))) != 0):
                self.state = 837
                self.classBodyDeclaration()
                self.state = 842
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 843
            self.match(Java8Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classMemberDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.ClassMemberDeclarationContext,0)


        def instanceInitializer(self):
            return self.getTypedRuleContext(Java8Parser.InstanceInitializerContext,0)


        def staticInitializer(self):
            return self.getTypedRuleContext(Java8Parser.StaticInitializerContext,0)


        def constructorDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.ConstructorDeclarationContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_classBodyDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBodyDeclaration" ):
                listener.enterClassBodyDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBodyDeclaration" ):
                listener.exitClassBodyDeclaration(self)




    def classBodyDeclaration(self):

        localctx = Java8Parser.ClassBodyDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_classBodyDeclaration)
        try:
            self.state = 849
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 845
                self.classMemberDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 846
                self.instanceInitializer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 847
                self.staticInitializer()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 848
                self.constructorDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.FieldDeclarationContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.MethodDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.InterfaceDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_classMemberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassMemberDeclaration" ):
                listener.enterClassMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassMemberDeclaration" ):
                listener.exitClassMemberDeclaration(self)




    def classMemberDeclaration(self):

        localctx = Java8Parser.ClassMemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_classMemberDeclaration)
        try:
            self.state = 856
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 851
                self.fieldDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 852
                self.methodDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 853
                self.classDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 854
                self.interfaceDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 855
                self.match(Java8Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def variableDeclaratorList(self):
            return self.getTypedRuleContext(Java8Parser.VariableDeclaratorListContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def fieldModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.FieldModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.FieldModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_fieldDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDeclaration" ):
                listener.enterFieldDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDeclaration" ):
                listener.exitFieldDeclaration(self)




    def fieldDeclaration(self):

        localctx = Java8Parser.FieldDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_fieldDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 861
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.FINAL) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.TRANSIENT) | (1 << Java8Parser.VOLATILE))) != 0) or _la==Java8Parser.AT:
                self.state = 858
                self.fieldModifier()
                self.state = 863
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 864
            self.unannType()
            self.state = 865
            self.variableDeclaratorList()
            self.state = 866
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java8Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(Java8Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(Java8Parser.PRIVATE, 0)

        def STATIC(self):
            return self.getToken(Java8Parser.STATIC, 0)

        def FINAL(self):
            return self.getToken(Java8Parser.FINAL, 0)

        def TRANSIENT(self):
            return self.getToken(Java8Parser.TRANSIENT, 0)

        def VOLATILE(self):
            return self.getToken(Java8Parser.VOLATILE, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_fieldModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldModifier" ):
                listener.enterFieldModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldModifier" ):
                listener.exitFieldModifier(self)




    def fieldModifier(self):

        localctx = Java8Parser.FieldModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_fieldModifier)
        try:
            self.state = 876
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 868
                self.annotation()
                pass
            elif token in [Java8Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 869
                self.match(Java8Parser.PUBLIC)
                pass
            elif token in [Java8Parser.PROTECTED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 870
                self.match(Java8Parser.PROTECTED)
                pass
            elif token in [Java8Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 871
                self.match(Java8Parser.PRIVATE)
                pass
            elif token in [Java8Parser.STATIC]:
                self.enterOuterAlt(localctx, 5)
                self.state = 872
                self.match(Java8Parser.STATIC)
                pass
            elif token in [Java8Parser.FINAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 873
                self.match(Java8Parser.FINAL)
                pass
            elif token in [Java8Parser.TRANSIENT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 874
                self.match(Java8Parser.TRANSIENT)
                pass
            elif token in [Java8Parser.VOLATILE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 875
                self.match(Java8Parser.VOLATILE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.VariableDeclaratorContext)
            else:
                return self.getTypedRuleContext(Java8Parser.VariableDeclaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_variableDeclaratorList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaratorList" ):
                listener.enterVariableDeclaratorList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaratorList" ):
                listener.exitVariableDeclaratorList(self)




    def variableDeclaratorList(self):

        localctx = Java8Parser.VariableDeclaratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_variableDeclaratorList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 878
            self.variableDeclarator()
            self.state = 883
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.COMMA:
                self.state = 879
                self.match(Java8Parser.COMMA)
                self.state = 880
                self.variableDeclarator()
                self.state = 885
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java8Parser.VariableDeclaratorIdContext,0)


        def ASSIGN(self):
            return self.getToken(Java8Parser.ASSIGN, 0)

        def variableInitializer(self):
            return self.getTypedRuleContext(Java8Parser.VariableInitializerContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_variableDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarator" ):
                listener.enterVariableDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarator" ):
                listener.exitVariableDeclarator(self)




    def variableDeclarator(self):

        localctx = Java8Parser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_variableDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 886
            self.variableDeclaratorId()
            self.state = 889
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.ASSIGN:
                self.state = 887
                self.match(Java8Parser.ASSIGN)
                self.state = 888
                self.variableInitializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def dims(self):
            return self.getTypedRuleContext(Java8Parser.DimsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_variableDeclaratorId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaratorId" ):
                listener.enterVariableDeclaratorId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaratorId" ):
                listener.exitVariableDeclaratorId(self)




    def variableDeclaratorId(self):

        localctx = Java8Parser.VariableDeclaratorIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_variableDeclaratorId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 891
            self.match(Java8Parser.Identifier)
            self.state = 893
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LBRACK or _la==Java8Parser.AT:
                self.state = 892
                self.dims()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def arrayInitializer(self):
            return self.getTypedRuleContext(Java8Parser.ArrayInitializerContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_variableInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableInitializer" ):
                listener.enterVariableInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableInitializer" ):
                listener.exitVariableInitializer(self)




    def variableInitializer(self):

        localctx = Java8Parser.VariableInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_variableInitializer)
        try:
            self.state = 897
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.BOOLEAN, Java8Parser.BYTE, Java8Parser.CHAR, Java8Parser.DOUBLE, Java8Parser.FLOAT, Java8Parser.INT, Java8Parser.LONG, Java8Parser.NEW, Java8Parser.SHORT, Java8Parser.SUPER, Java8Parser.THIS, Java8Parser.VOID, Java8Parser.IntegerLiteral, Java8Parser.FloatingPointLiteral, Java8Parser.BooleanLiteral, Java8Parser.CharacterLiteral, Java8Parser.StringLiteral, Java8Parser.NullLiteral, Java8Parser.LPAREN, Java8Parser.BANG, Java8Parser.TILDE, Java8Parser.INC, Java8Parser.DEC, Java8Parser.ADD, Java8Parser.SUB, Java8Parser.Identifier, Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 895
                self.expression()
                pass
            elif token in [Java8Parser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 896
                self.arrayInitializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannPrimitiveType(self):
            return self.getTypedRuleContext(Java8Parser.UnannPrimitiveTypeContext,0)


        def unannReferenceType(self):
            return self.getTypedRuleContext(Java8Parser.UnannReferenceTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_unannType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannType" ):
                listener.enterUnannType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannType" ):
                listener.exitUnannType(self)




    def unannType(self):

        localctx = Java8Parser.UnannTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_unannType)
        try:
            self.state = 901
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 899
                self.unannPrimitiveType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 900
                self.unannReferenceType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannPrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericType(self):
            return self.getTypedRuleContext(Java8Parser.NumericTypeContext,0)


        def BOOLEAN(self):
            return self.getToken(Java8Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_unannPrimitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannPrimitiveType" ):
                listener.enterUnannPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannPrimitiveType" ):
                listener.exitUnannPrimitiveType(self)




    def unannPrimitiveType(self):

        localctx = Java8Parser.UnannPrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_unannPrimitiveType)
        try:
            self.state = 905
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.BYTE, Java8Parser.CHAR, Java8Parser.DOUBLE, Java8Parser.FLOAT, Java8Parser.INT, Java8Parser.LONG, Java8Parser.SHORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 903
                self.numericType()
                pass
            elif token in [Java8Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 904
                self.match(Java8Parser.BOOLEAN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannReferenceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannClassOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.UnannClassOrInterfaceTypeContext,0)


        def unannTypeVariable(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeVariableContext,0)


        def unannArrayType(self):
            return self.getTypedRuleContext(Java8Parser.UnannArrayTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_unannReferenceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannReferenceType" ):
                listener.enterUnannReferenceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannReferenceType" ):
                listener.exitUnannReferenceType(self)




    def unannReferenceType(self):

        localctx = Java8Parser.UnannReferenceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_unannReferenceType)
        try:
            self.state = 910
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 907
                self.unannClassOrInterfaceType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 908
                self.unannTypeVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 909
                self.unannArrayType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannClassOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannClassType_lfno_unannClassOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext,0)


        def unannInterfaceType_lfno_unannClassOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.UnannInterfaceType_lfno_unannClassOrInterfaceTypeContext,0)


        def unannClassType_lf_unannClassOrInterfaceType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.UnannClassType_lf_unannClassOrInterfaceTypeContext)
            else:
                return self.getTypedRuleContext(Java8Parser.UnannClassType_lf_unannClassOrInterfaceTypeContext,i)


        def unannInterfaceType_lf_unannClassOrInterfaceType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.UnannInterfaceType_lf_unannClassOrInterfaceTypeContext)
            else:
                return self.getTypedRuleContext(Java8Parser.UnannInterfaceType_lf_unannClassOrInterfaceTypeContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_unannClassOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannClassOrInterfaceType" ):
                listener.enterUnannClassOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannClassOrInterfaceType" ):
                listener.exitUnannClassOrInterfaceType(self)




    def unannClassOrInterfaceType(self):

        localctx = Java8Parser.UnannClassOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_unannClassOrInterfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 914
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.state = 912
                self.unannClassType_lfno_unannClassOrInterfaceType()
                pass

            elif la_ == 2:
                self.state = 913
                self.unannInterfaceType_lfno_unannClassOrInterfaceType()
                pass


            self.state = 920
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 918
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                    if la_ == 1:
                        self.state = 916
                        self.unannClassType_lf_unannClassOrInterfaceType()
                        pass

                    elif la_ == 2:
                        self.state = 917
                        self.unannInterfaceType_lf_unannClassOrInterfaceType()
                        pass

             
                self.state = 922
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannClassTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def unannClassOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.UnannClassOrInterfaceTypeContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_unannClassType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannClassType" ):
                listener.enterUnannClassType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannClassType" ):
                listener.exitUnannClassType(self)




    def unannClassType(self):

        localctx = Java8Parser.UnannClassTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_unannClassType)
        self._la = 0 # Token type
        try:
            self.state = 939
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 923
                self.match(Java8Parser.Identifier)
                self.state = 925
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 924
                    self.typeArguments()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 927
                self.unannClassOrInterfaceType()
                self.state = 928
                self.match(Java8Parser.DOT)
                self.state = 932
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 929
                    self.annotation()
                    self.state = 934
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 935
                self.match(Java8Parser.Identifier)
                self.state = 937
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 936
                    self.typeArguments()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannClassType_lf_unannClassOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_unannClassType_lf_unannClassOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannClassType_lf_unannClassOrInterfaceType" ):
                listener.enterUnannClassType_lf_unannClassOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannClassType_lf_unannClassOrInterfaceType" ):
                listener.exitUnannClassType_lf_unannClassOrInterfaceType(self)




    def unannClassType_lf_unannClassOrInterfaceType(self):

        localctx = Java8Parser.UnannClassType_lf_unannClassOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_unannClassType_lf_unannClassOrInterfaceType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 941
            self.match(Java8Parser.DOT)
            self.state = 945
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 942
                self.annotation()
                self.state = 947
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 948
            self.match(Java8Parser.Identifier)
            self.state = 950
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LT:
                self.state = 949
                self.typeArguments()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannClassType_lfno_unannClassOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_unannClassType_lfno_unannClassOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannClassType_lfno_unannClassOrInterfaceType" ):
                listener.enterUnannClassType_lfno_unannClassOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannClassType_lfno_unannClassOrInterfaceType" ):
                listener.exitUnannClassType_lfno_unannClassOrInterfaceType(self)




    def unannClassType_lfno_unannClassOrInterfaceType(self):

        localctx = Java8Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_unannClassType_lfno_unannClassOrInterfaceType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 952
            self.match(Java8Parser.Identifier)
            self.state = 954
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LT:
                self.state = 953
                self.typeArguments()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannClassType(self):
            return self.getTypedRuleContext(Java8Parser.UnannClassTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_unannInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannInterfaceType" ):
                listener.enterUnannInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannInterfaceType" ):
                listener.exitUnannInterfaceType(self)




    def unannInterfaceType(self):

        localctx = Java8Parser.UnannInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_unannInterfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 956
            self.unannClassType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannInterfaceType_lf_unannClassOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannClassType_lf_unannClassOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.UnannClassType_lf_unannClassOrInterfaceTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_unannInterfaceType_lf_unannClassOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannInterfaceType_lf_unannClassOrInterfaceType" ):
                listener.enterUnannInterfaceType_lf_unannClassOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannInterfaceType_lf_unannClassOrInterfaceType" ):
                listener.exitUnannInterfaceType_lf_unannClassOrInterfaceType(self)




    def unannInterfaceType_lf_unannClassOrInterfaceType(self):

        localctx = Java8Parser.UnannInterfaceType_lf_unannClassOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_unannInterfaceType_lf_unannClassOrInterfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 958
            self.unannClassType_lf_unannClassOrInterfaceType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannInterfaceType_lfno_unannClassOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannClassType_lfno_unannClassOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_unannInterfaceType_lfno_unannClassOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannInterfaceType_lfno_unannClassOrInterfaceType" ):
                listener.enterUnannInterfaceType_lfno_unannClassOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannInterfaceType_lfno_unannClassOrInterfaceType" ):
                listener.exitUnannInterfaceType_lfno_unannClassOrInterfaceType(self)




    def unannInterfaceType_lfno_unannClassOrInterfaceType(self):

        localctx = Java8Parser.UnannInterfaceType_lfno_unannClassOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_unannInterfaceType_lfno_unannClassOrInterfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 960
            self.unannClassType_lfno_unannClassOrInterfaceType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannTypeVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_unannTypeVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannTypeVariable" ):
                listener.enterUnannTypeVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannTypeVariable" ):
                listener.exitUnannTypeVariable(self)




    def unannTypeVariable(self):

        localctx = Java8Parser.UnannTypeVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_unannTypeVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 962
            self.match(Java8Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannPrimitiveType(self):
            return self.getTypedRuleContext(Java8Parser.UnannPrimitiveTypeContext,0)


        def dims(self):
            return self.getTypedRuleContext(Java8Parser.DimsContext,0)


        def unannClassOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.UnannClassOrInterfaceTypeContext,0)


        def unannTypeVariable(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeVariableContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_unannArrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannArrayType" ):
                listener.enterUnannArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannArrayType" ):
                listener.exitUnannArrayType(self)




    def unannArrayType(self):

        localctx = Java8Parser.UnannArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_unannArrayType)
        try:
            self.state = 973
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 964
                self.unannPrimitiveType()
                self.state = 965
                self.dims()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 967
                self.unannClassOrInterfaceType()
                self.state = 968
                self.dims()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 970
                self.unannTypeVariable()
                self.state = 971
                self.dims()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodHeader(self):
            return self.getTypedRuleContext(Java8Parser.MethodHeaderContext,0)


        def methodBody(self):
            return self.getTypedRuleContext(Java8Parser.MethodBodyContext,0)


        def methodModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.MethodModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.MethodModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)




    def methodDeclaration(self):

        localctx = Java8Parser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 978
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.NATIVE) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP) | (1 << Java8Parser.SYNCHRONIZED))) != 0) or _la==Java8Parser.AT:
                self.state = 975
                self.methodModifier()
                self.state = 980
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 981
            self.methodHeader()
            self.state = 982
            self.methodBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java8Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(Java8Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(Java8Parser.PRIVATE, 0)

        def ABSTRACT(self):
            return self.getToken(Java8Parser.ABSTRACT, 0)

        def STATIC(self):
            return self.getToken(Java8Parser.STATIC, 0)

        def FINAL(self):
            return self.getToken(Java8Parser.FINAL, 0)

        def SYNCHRONIZED(self):
            return self.getToken(Java8Parser.SYNCHRONIZED, 0)

        def NATIVE(self):
            return self.getToken(Java8Parser.NATIVE, 0)

        def STRICTFP(self):
            return self.getToken(Java8Parser.STRICTFP, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_methodModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodModifier" ):
                listener.enterMethodModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodModifier" ):
                listener.exitMethodModifier(self)




    def methodModifier(self):

        localctx = Java8Parser.MethodModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_methodModifier)
        try:
            self.state = 994
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 984
                self.annotation()
                pass
            elif token in [Java8Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 985
                self.match(Java8Parser.PUBLIC)
                pass
            elif token in [Java8Parser.PROTECTED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 986
                self.match(Java8Parser.PROTECTED)
                pass
            elif token in [Java8Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 987
                self.match(Java8Parser.PRIVATE)
                pass
            elif token in [Java8Parser.ABSTRACT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 988
                self.match(Java8Parser.ABSTRACT)
                pass
            elif token in [Java8Parser.STATIC]:
                self.enterOuterAlt(localctx, 6)
                self.state = 989
                self.match(Java8Parser.STATIC)
                pass
            elif token in [Java8Parser.FINAL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 990
                self.match(Java8Parser.FINAL)
                pass
            elif token in [Java8Parser.SYNCHRONIZED]:
                self.enterOuterAlt(localctx, 8)
                self.state = 991
                self.match(Java8Parser.SYNCHRONIZED)
                pass
            elif token in [Java8Parser.NATIVE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 992
                self.match(Java8Parser.NATIVE)
                pass
            elif token in [Java8Parser.STRICTFP]:
                self.enterOuterAlt(localctx, 10)
                self.state = 993
                self.match(Java8Parser.STRICTFP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodHeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def result(self):
            return self.getTypedRuleContext(Java8Parser.ResultContext,0)


        def methodDeclarator(self):
            return self.getTypedRuleContext(Java8Parser.MethodDeclaratorContext,0)


        def throws_(self):
            return self.getTypedRuleContext(Java8Parser.Throws_Context,0)


        def typeParameters(self):
            return self.getTypedRuleContext(Java8Parser.TypeParametersContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_methodHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodHeader" ):
                listener.enterMethodHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodHeader" ):
                listener.exitMethodHeader(self)




    def methodHeader(self):

        localctx = Java8Parser.MethodHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_methodHeader)
        self._la = 0 # Token type
        try:
            self.state = 1013
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.BOOLEAN, Java8Parser.BYTE, Java8Parser.CHAR, Java8Parser.DOUBLE, Java8Parser.FLOAT, Java8Parser.INT, Java8Parser.LONG, Java8Parser.SHORT, Java8Parser.VOID, Java8Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 996
                self.result()
                self.state = 997
                self.methodDeclarator()
                self.state = 999
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.THROWS:
                    self.state = 998
                    self.throws_()


                pass
            elif token in [Java8Parser.LT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1001
                self.typeParameters()
                self.state = 1005
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 1002
                    self.annotation()
                    self.state = 1007
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1008
                self.result()
                self.state = 1009
                self.methodDeclarator()
                self.state = 1011
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.THROWS:
                    self.state = 1010
                    self.throws_()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def VOID(self):
            return self.getToken(Java8Parser.VOID, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResult" ):
                listener.enterResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResult" ):
                listener.exitResult(self)




    def result(self):

        localctx = Java8Parser.ResultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_result)
        try:
            self.state = 1017
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.BOOLEAN, Java8Parser.BYTE, Java8Parser.CHAR, Java8Parser.DOUBLE, Java8Parser.FLOAT, Java8Parser.INT, Java8Parser.LONG, Java8Parser.SHORT, Java8Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1015
                self.unannType()
                pass
            elif token in [Java8Parser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1016
                self.match(Java8Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(Java8Parser.FormalParameterListContext,0)


        def dims(self):
            return self.getTypedRuleContext(Java8Parser.DimsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_methodDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclarator" ):
                listener.enterMethodDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclarator" ):
                listener.exitMethodDeclarator(self)




    def methodDeclarator(self):

        localctx = Java8Parser.MethodDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_methodDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1019
            self.match(Java8Parser.Identifier)
            self.state = 1020
            self.match(Java8Parser.LPAREN)
            self.state = 1022
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.SHORT))) != 0) or _la==Java8Parser.Identifier or _la==Java8Parser.AT:
                self.state = 1021
                self.formalParameterList()


            self.state = 1024
            self.match(Java8Parser.RPAREN)
            self.state = 1026
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LBRACK or _la==Java8Parser.AT:
                self.state = 1025
                self.dims()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def receiverParameter(self):
            return self.getTypedRuleContext(Java8Parser.ReceiverParameterContext,0)


        def formalParameters(self):
            return self.getTypedRuleContext(Java8Parser.FormalParametersContext,0)


        def COMMA(self):
            return self.getToken(Java8Parser.COMMA, 0)

        def lastFormalParameter(self):
            return self.getTypedRuleContext(Java8Parser.LastFormalParameterContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_formalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterList" ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterList" ):
                listener.exitFormalParameterList(self)




    def formalParameterList(self):

        localctx = Java8Parser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_formalParameterList)
        try:
            self.state = 1034
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1028
                self.receiverParameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1029
                self.formalParameters()
                self.state = 1030
                self.match(Java8Parser.COMMA)
                self.state = 1031
                self.lastFormalParameter()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1033
                self.lastFormalParameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formalParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.FormalParameterContext)
            else:
                return self.getTypedRuleContext(Java8Parser.FormalParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def receiverParameter(self):
            return self.getTypedRuleContext(Java8Parser.ReceiverParameterContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_formalParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameters" ):
                listener.enterFormalParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameters" ):
                listener.exitFormalParameters(self)




    def formalParameters(self):

        localctx = Java8Parser.FormalParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_formalParameters)
        try:
            self.state = 1052
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1036
                self.formalParameter()
                self.state = 1041
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 1037
                        self.match(Java8Parser.COMMA)
                        self.state = 1038
                        self.formalParameter() 
                    self.state = 1043
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1044
                self.receiverParameter()
                self.state = 1049
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 1045
                        self.match(Java8Parser.COMMA)
                        self.state = 1046
                        self.formalParameter() 
                    self.state = 1051
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java8Parser.VariableDeclaratorIdContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.VariableModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_formalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameter" ):
                listener.enterFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameter" ):
                listener.exitFormalParameter(self)




    def formalParameter(self):

        localctx = Java8Parser.FormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_formalParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1057
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.FINAL or _la==Java8Parser.AT:
                self.state = 1054
                self.variableModifier()
                self.state = 1059
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1060
            self.unannType()
            self.state = 1061
            self.variableDeclaratorId()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def FINAL(self):
            return self.getToken(Java8Parser.FINAL, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_variableModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableModifier" ):
                listener.enterVariableModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableModifier" ):
                listener.exitVariableModifier(self)




    def variableModifier(self):

        localctx = Java8Parser.VariableModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_variableModifier)
        try:
            self.state = 1065
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1063
                self.annotation()
                pass
            elif token in [Java8Parser.FINAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1064
                self.match(Java8Parser.FINAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LastFormalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def ELLIPSIS(self):
            return self.getToken(Java8Parser.ELLIPSIS, 0)

        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java8Parser.VariableDeclaratorIdContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.VariableModifierContext,i)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def formalParameter(self):
            return self.getTypedRuleContext(Java8Parser.FormalParameterContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_lastFormalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLastFormalParameter" ):
                listener.enterLastFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLastFormalParameter" ):
                listener.exitLastFormalParameter(self)




    def lastFormalParameter(self):

        localctx = Java8Parser.LastFormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_lastFormalParameter)
        self._la = 0 # Token type
        try:
            self.state = 1084
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1070
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.FINAL or _la==Java8Parser.AT:
                    self.state = 1067
                    self.variableModifier()
                    self.state = 1072
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1073
                self.unannType()
                self.state = 1077
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 1074
                    self.annotation()
                    self.state = 1079
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1080
                self.match(Java8Parser.ELLIPSIS)
                self.state = 1081
                self.variableDeclaratorId()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1083
                self.formalParameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def THIS(self):
            return self.getToken(Java8Parser.THIS, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_receiverParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceiverParameter" ):
                listener.enterReceiverParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceiverParameter" ):
                listener.exitReceiverParameter(self)




    def receiverParameter(self):

        localctx = Java8Parser.ReceiverParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_receiverParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1089
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 1086
                self.annotation()
                self.state = 1091
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1092
            self.unannType()
            self.state = 1095
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.Identifier:
                self.state = 1093
                self.match(Java8Parser.Identifier)
                self.state = 1094
                self.match(Java8Parser.DOT)


            self.state = 1097
            self.match(Java8Parser.THIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Throws_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROWS(self):
            return self.getToken(Java8Parser.THROWS, 0)

        def exceptionTypeList(self):
            return self.getTypedRuleContext(Java8Parser.ExceptionTypeListContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_throws_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrows_" ):
                listener.enterThrows_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrows_" ):
                listener.exitThrows_(self)




    def throws_(self):

        localctx = Java8Parser.Throws_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_throws_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1099
            self.match(Java8Parser.THROWS)
            self.state = 1100
            self.exceptionTypeList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExceptionTypeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exceptionType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ExceptionTypeContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ExceptionTypeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_exceptionTypeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExceptionTypeList" ):
                listener.enterExceptionTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExceptionTypeList" ):
                listener.exitExceptionTypeList(self)




    def exceptionTypeList(self):

        localctx = Java8Parser.ExceptionTypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_exceptionTypeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1102
            self.exceptionType()
            self.state = 1107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.COMMA:
                self.state = 1103
                self.match(Java8Parser.COMMA)
                self.state = 1104
                self.exceptionType()
                self.state = 1109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExceptionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classType(self):
            return self.getTypedRuleContext(Java8Parser.ClassTypeContext,0)


        def typeVariable(self):
            return self.getTypedRuleContext(Java8Parser.TypeVariableContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_exceptionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExceptionType" ):
                listener.enterExceptionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExceptionType" ):
                listener.exitExceptionType(self)




    def exceptionType(self):

        localctx = Java8Parser.ExceptionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_exceptionType)
        try:
            self.state = 1112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1110
                self.classType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1111
                self.typeVariable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(Java8Parser.BlockContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_methodBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodBody" ):
                listener.enterMethodBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodBody" ):
                listener.exitMethodBody(self)




    def methodBody(self):

        localctx = Java8Parser.MethodBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_methodBody)
        try:
            self.state = 1116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1114
                self.block()
                pass
            elif token in [Java8Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1115
                self.match(Java8Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(Java8Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_instanceInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceInitializer" ):
                listener.enterInstanceInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceInitializer" ):
                listener.exitInstanceInitializer(self)




    def instanceInitializer(self):

        localctx = Java8Parser.InstanceInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_instanceInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1118
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(Java8Parser.STATIC, 0)

        def block(self):
            return self.getTypedRuleContext(Java8Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_staticInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaticInitializer" ):
                listener.enterStaticInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaticInitializer" ):
                listener.exitStaticInitializer(self)




    def staticInitializer(self):

        localctx = Java8Parser.StaticInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_staticInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1120
            self.match(Java8Parser.STATIC)
            self.state = 1121
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructorDeclarator(self):
            return self.getTypedRuleContext(Java8Parser.ConstructorDeclaratorContext,0)


        def constructorBody(self):
            return self.getTypedRuleContext(Java8Parser.ConstructorBodyContext,0)


        def constructorModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ConstructorModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ConstructorModifierContext,i)


        def throws_(self):
            return self.getTypedRuleContext(Java8Parser.Throws_Context,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_constructorDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDeclaration" ):
                listener.enterConstructorDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDeclaration" ):
                listener.exitConstructorDeclaration(self)




    def constructorDeclaration(self):

        localctx = Java8Parser.ConstructorDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_constructorDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC))) != 0) or _la==Java8Parser.AT:
                self.state = 1123
                self.constructorModifier()
                self.state = 1128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1129
            self.constructorDeclarator()
            self.state = 1131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.THROWS:
                self.state = 1130
                self.throws_()


            self.state = 1133
            self.constructorBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java8Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(Java8Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(Java8Parser.PRIVATE, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_constructorModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorModifier" ):
                listener.enterConstructorModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorModifier" ):
                listener.exitConstructorModifier(self)




    def constructorModifier(self):

        localctx = Java8Parser.ConstructorModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_constructorModifier)
        try:
            self.state = 1139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1135
                self.annotation()
                pass
            elif token in [Java8Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1136
                self.match(Java8Parser.PUBLIC)
                pass
            elif token in [Java8Parser.PROTECTED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1137
                self.match(Java8Parser.PROTECTED)
                pass
            elif token in [Java8Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1138
                self.match(Java8Parser.PRIVATE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleTypeName(self):
            return self.getTypedRuleContext(Java8Parser.SimpleTypeNameContext,0)


        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def typeParameters(self):
            return self.getTypedRuleContext(Java8Parser.TypeParametersContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(Java8Parser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_constructorDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDeclarator" ):
                listener.enterConstructorDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDeclarator" ):
                listener.exitConstructorDeclarator(self)




    def constructorDeclarator(self):

        localctx = Java8Parser.ConstructorDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_constructorDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LT:
                self.state = 1141
                self.typeParameters()


            self.state = 1144
            self.simpleTypeName()
            self.state = 1145
            self.match(Java8Parser.LPAREN)
            self.state = 1147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.SHORT))) != 0) or _la==Java8Parser.Identifier or _la==Java8Parser.AT:
                self.state = 1146
                self.formalParameterList()


            self.state = 1149
            self.match(Java8Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleTypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_simpleTypeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleTypeName" ):
                listener.enterSimpleTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleTypeName" ):
                listener.exitSimpleTypeName(self)




    def simpleTypeName(self):

        localctx = Java8Parser.SimpleTypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_simpleTypeName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1151
            self.match(Java8Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java8Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java8Parser.RBRACE, 0)

        def explicitConstructorInvocation(self):
            return self.getTypedRuleContext(Java8Parser.ExplicitConstructorInvocationContext,0)


        def blockStatements(self):
            return self.getTypedRuleContext(Java8Parser.BlockStatementsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_constructorBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorBody" ):
                listener.enterConstructorBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorBody" ):
                listener.exitConstructorBody(self)




    def constructorBody(self):

        localctx = Java8Parser.ConstructorBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_constructorBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1153
            self.match(Java8Parser.LBRACE)
            self.state = 1155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,101,self._ctx)
            if la_ == 1:
                self.state = 1154
                self.explicitConstructorInvocation()


            self.state = 1158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.ASSERT) | (1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BREAK) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.CLASS) | (1 << Java8Parser.CONTINUE) | (1 << Java8Parser.DO) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.ENUM) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.FOR) | (1 << Java8Parser.IF) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.RETURN) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.SWITCH) | (1 << Java8Parser.SYNCHRONIZED) | (1 << Java8Parser.THIS) | (1 << Java8Parser.THROW) | (1 << Java8Parser.TRY) | (1 << Java8Parser.VOID) | (1 << Java8Parser.WHILE) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN) | (1 << Java8Parser.LBRACE) | (1 << Java8Parser.SEMI))) != 0) or ((((_la - 79)) & ~0x3f) == 0 and ((1 << (_la - 79)) & ((1 << (Java8Parser.INC - 79)) | (1 << (Java8Parser.DEC - 79)) | (1 << (Java8Parser.Identifier - 79)) | (1 << (Java8Parser.AT - 79)))) != 0):
                self.state = 1157
                self.blockStatements()


            self.state = 1160
            self.match(Java8Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplicitConstructorInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(Java8Parser.THIS, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java8Parser.ArgumentListContext,0)


        def SUPER(self):
            return self.getToken(Java8Parser.SUPER, 0)

        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def primary(self):
            return self.getTypedRuleContext(Java8Parser.PrimaryContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_explicitConstructorInvocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicitConstructorInvocation" ):
                listener.enterExplicitConstructorInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicitConstructorInvocation" ):
                listener.exitExplicitConstructorInvocation(self)




    def explicitConstructorInvocation(self):

        localctx = Java8Parser.ExplicitConstructorInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_explicitConstructorInvocation)
        self._la = 0 # Token type
        try:
            self.state = 1208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 1162
                    self.typeArguments()


                self.state = 1165
                self.match(Java8Parser.THIS)
                self.state = 1166
                self.match(Java8Parser.LPAREN)
                self.state = 1168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 1167
                    self.argumentList()


                self.state = 1170
                self.match(Java8Parser.RPAREN)
                self.state = 1171
                self.match(Java8Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 1172
                    self.typeArguments()


                self.state = 1175
                self.match(Java8Parser.SUPER)
                self.state = 1176
                self.match(Java8Parser.LPAREN)
                self.state = 1178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 1177
                    self.argumentList()


                self.state = 1180
                self.match(Java8Parser.RPAREN)
                self.state = 1181
                self.match(Java8Parser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1182
                self.expressionName()
                self.state = 1183
                self.match(Java8Parser.DOT)
                self.state = 1185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 1184
                    self.typeArguments()


                self.state = 1187
                self.match(Java8Parser.SUPER)
                self.state = 1188
                self.match(Java8Parser.LPAREN)
                self.state = 1190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 1189
                    self.argumentList()


                self.state = 1192
                self.match(Java8Parser.RPAREN)
                self.state = 1193
                self.match(Java8Parser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1195
                self.primary()
                self.state = 1196
                self.match(Java8Parser.DOT)
                self.state = 1198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 1197
                    self.typeArguments()


                self.state = 1200
                self.match(Java8Parser.SUPER)
                self.state = 1201
                self.match(Java8Parser.LPAREN)
                self.state = 1203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 1202
                    self.argumentList()


                self.state = 1205
                self.match(Java8Parser.RPAREN)
                self.state = 1206
                self.match(Java8Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(Java8Parser.ENUM, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def enumBody(self):
            return self.getTypedRuleContext(Java8Parser.EnumBodyContext,0)


        def classModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ClassModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ClassModifierContext,i)


        def superinterfaces(self):
            return self.getTypedRuleContext(Java8Parser.SuperinterfacesContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_enumDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDeclaration" ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDeclaration" ):
                listener.exitEnumDeclaration(self)




    def enumDeclaration(self):

        localctx = Java8Parser.EnumDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP))) != 0) or _la==Java8Parser.AT:
                self.state = 1210
                self.classModifier()
                self.state = 1215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1216
            self.match(Java8Parser.ENUM)
            self.state = 1217
            self.match(Java8Parser.Identifier)
            self.state = 1219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.IMPLEMENTS:
                self.state = 1218
                self.superinterfaces()


            self.state = 1221
            self.enumBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java8Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java8Parser.RBRACE, 0)

        def enumConstantList(self):
            return self.getTypedRuleContext(Java8Parser.EnumConstantListContext,0)


        def COMMA(self):
            return self.getToken(Java8Parser.COMMA, 0)

        def enumBodyDeclarations(self):
            return self.getTypedRuleContext(Java8Parser.EnumBodyDeclarationsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_enumBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumBody" ):
                listener.enterEnumBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumBody" ):
                listener.exitEnumBody(self)




    def enumBody(self):

        localctx = Java8Parser.EnumBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1223
            self.match(Java8Parser.LBRACE)
            self.state = 1225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.Identifier or _la==Java8Parser.AT:
                self.state = 1224
                self.enumConstantList()


            self.state = 1228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.COMMA:
                self.state = 1227
                self.match(Java8Parser.COMMA)


            self.state = 1231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.SEMI:
                self.state = 1230
                self.enumBodyDeclarations()


            self.state = 1233
            self.match(Java8Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumConstantListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumConstant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.EnumConstantContext)
            else:
                return self.getTypedRuleContext(Java8Parser.EnumConstantContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_enumConstantList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumConstantList" ):
                listener.enterEnumConstantList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumConstantList" ):
                listener.exitEnumConstantList(self)




    def enumConstantList(self):

        localctx = Java8Parser.EnumConstantListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_enumConstantList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1235
            self.enumConstant()
            self.state = 1240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,117,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1236
                    self.match(Java8Parser.COMMA)
                    self.state = 1237
                    self.enumConstant() 
                self.state = 1242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,117,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def enumConstantModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.EnumConstantModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.EnumConstantModifierContext,i)


        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def classBody(self):
            return self.getTypedRuleContext(Java8Parser.ClassBodyContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java8Parser.ArgumentListContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_enumConstant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumConstant" ):
                listener.enterEnumConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumConstant" ):
                listener.exitEnumConstant(self)




    def enumConstant(self):

        localctx = Java8Parser.EnumConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_enumConstant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 1243
                self.enumConstantModifier()
                self.state = 1248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1249
            self.match(Java8Parser.Identifier)
            self.state = 1255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LPAREN:
                self.state = 1250
                self.match(Java8Parser.LPAREN)
                self.state = 1252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 1251
                    self.argumentList()


                self.state = 1254
                self.match(Java8Parser.RPAREN)


            self.state = 1258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LBRACE:
                self.state = 1257
                self.classBody()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumConstantModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_enumConstantModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumConstantModifier" ):
                listener.enterEnumConstantModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumConstantModifier" ):
                listener.exitEnumConstantModifier(self)




    def enumConstantModifier(self):

        localctx = Java8Parser.EnumConstantModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_enumConstantModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1260
            self.annotation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumBodyDeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def classBodyDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ClassBodyDeclarationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ClassBodyDeclarationContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_enumBodyDeclarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumBodyDeclarations" ):
                listener.enterEnumBodyDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumBodyDeclarations" ):
                listener.exitEnumBodyDeclarations(self)




    def enumBodyDeclarations(self):

        localctx = Java8Parser.EnumBodyDeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_enumBodyDeclarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1262
            self.match(Java8Parser.SEMI)
            self.state = 1266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.CLASS) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.ENUM) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.INTERFACE) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NATIVE) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP) | (1 << Java8Parser.SYNCHRONIZED) | (1 << Java8Parser.TRANSIENT) | (1 << Java8Parser.VOID) | (1 << Java8Parser.VOLATILE) | (1 << Java8Parser.LBRACE) | (1 << Java8Parser.SEMI))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (Java8Parser.LT - 68)) | (1 << (Java8Parser.Identifier - 68)) | (1 << (Java8Parser.AT - 68)))) != 0):
                self.state = 1263
                self.classBodyDeclaration()
                self.state = 1268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalInterfaceDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.NormalInterfaceDeclarationContext,0)


        def annotationTypeDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationTypeDeclarationContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_interfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceDeclaration" ):
                listener.enterInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceDeclaration" ):
                listener.exitInterfaceDeclaration(self)




    def interfaceDeclaration(self):

        localctx = Java8Parser.InterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_interfaceDeclaration)
        try:
            self.state = 1271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,123,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1269
                self.normalInterfaceDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1270
                self.annotationTypeDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalInterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(Java8Parser.INTERFACE, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def interfaceBody(self):
            return self.getTypedRuleContext(Java8Parser.InterfaceBodyContext,0)


        def interfaceModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.InterfaceModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.InterfaceModifierContext,i)


        def typeParameters(self):
            return self.getTypedRuleContext(Java8Parser.TypeParametersContext,0)


        def extendsInterfaces(self):
            return self.getTypedRuleContext(Java8Parser.ExtendsInterfacesContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_normalInterfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalInterfaceDeclaration" ):
                listener.enterNormalInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalInterfaceDeclaration" ):
                listener.exitNormalInterfaceDeclaration(self)




    def normalInterfaceDeclaration(self):

        localctx = Java8Parser.NormalInterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_normalInterfaceDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP))) != 0) or _la==Java8Parser.AT:
                self.state = 1273
                self.interfaceModifier()
                self.state = 1278
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1279
            self.match(Java8Parser.INTERFACE)
            self.state = 1280
            self.match(Java8Parser.Identifier)
            self.state = 1282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LT:
                self.state = 1281
                self.typeParameters()


            self.state = 1285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.EXTENDS:
                self.state = 1284
                self.extendsInterfaces()


            self.state = 1287
            self.interfaceBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java8Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(Java8Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(Java8Parser.PRIVATE, 0)

        def ABSTRACT(self):
            return self.getToken(Java8Parser.ABSTRACT, 0)

        def STATIC(self):
            return self.getToken(Java8Parser.STATIC, 0)

        def STRICTFP(self):
            return self.getToken(Java8Parser.STRICTFP, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_interfaceModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceModifier" ):
                listener.enterInterfaceModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceModifier" ):
                listener.exitInterfaceModifier(self)




    def interfaceModifier(self):

        localctx = Java8Parser.InterfaceModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_interfaceModifier)
        try:
            self.state = 1296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1289
                self.annotation()
                pass
            elif token in [Java8Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1290
                self.match(Java8Parser.PUBLIC)
                pass
            elif token in [Java8Parser.PROTECTED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1291
                self.match(Java8Parser.PROTECTED)
                pass
            elif token in [Java8Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1292
                self.match(Java8Parser.PRIVATE)
                pass
            elif token in [Java8Parser.ABSTRACT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1293
                self.match(Java8Parser.ABSTRACT)
                pass
            elif token in [Java8Parser.STATIC]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1294
                self.match(Java8Parser.STATIC)
                pass
            elif token in [Java8Parser.STRICTFP]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1295
                self.match(Java8Parser.STRICTFP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtendsInterfacesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(Java8Parser.EXTENDS, 0)

        def interfaceTypeList(self):
            return self.getTypedRuleContext(Java8Parser.InterfaceTypeListContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_extendsInterfaces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtendsInterfaces" ):
                listener.enterExtendsInterfaces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtendsInterfaces" ):
                listener.exitExtendsInterfaces(self)




    def extendsInterfaces(self):

        localctx = Java8Parser.ExtendsInterfacesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_extendsInterfaces)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1298
            self.match(Java8Parser.EXTENDS)
            self.state = 1299
            self.interfaceTypeList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java8Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java8Parser.RBRACE, 0)

        def interfaceMemberDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.InterfaceMemberDeclarationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.InterfaceMemberDeclarationContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_interfaceBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceBody" ):
                listener.enterInterfaceBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceBody" ):
                listener.exitInterfaceBody(self)




    def interfaceBody(self):

        localctx = Java8Parser.InterfaceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_interfaceBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1301
            self.match(Java8Parser.LBRACE)
            self.state = 1305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.CLASS) | (1 << Java8Parser.DEFAULT) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.ENUM) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.INTERFACE) | (1 << Java8Parser.LONG) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP) | (1 << Java8Parser.VOID) | (1 << Java8Parser.SEMI))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (Java8Parser.LT - 68)) | (1 << (Java8Parser.Identifier - 68)) | (1 << (Java8Parser.AT - 68)))) != 0):
                self.state = 1302
                self.interfaceMemberDeclaration()
                self.state = 1307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1308
            self.match(Java8Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constantDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.ConstantDeclarationContext,0)


        def interfaceMethodDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.InterfaceMethodDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.InterfaceDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_interfaceMemberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceMemberDeclaration" ):
                listener.enterInterfaceMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceMemberDeclaration" ):
                listener.exitInterfaceMemberDeclaration(self)




    def interfaceMemberDeclaration(self):

        localctx = Java8Parser.InterfaceMemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_interfaceMemberDeclaration)
        try:
            self.state = 1315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,129,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1310
                self.constantDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1311
                self.interfaceMethodDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1312
                self.classDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1313
                self.interfaceDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1314
                self.match(Java8Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def variableDeclaratorList(self):
            return self.getTypedRuleContext(Java8Parser.VariableDeclaratorListContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def constantModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ConstantModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ConstantModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_constantDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantDeclaration" ):
                listener.enterConstantDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantDeclaration" ):
                listener.exitConstantDeclaration(self)




    def constantDeclaration(self):

        localctx = Java8Parser.ConstantDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_constantDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.FINAL) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.STATIC))) != 0) or _la==Java8Parser.AT:
                self.state = 1317
                self.constantModifier()
                self.state = 1322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1323
            self.unannType()
            self.state = 1324
            self.variableDeclaratorList()
            self.state = 1325
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java8Parser.PUBLIC, 0)

        def STATIC(self):
            return self.getToken(Java8Parser.STATIC, 0)

        def FINAL(self):
            return self.getToken(Java8Parser.FINAL, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_constantModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantModifier" ):
                listener.enterConstantModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantModifier" ):
                listener.exitConstantModifier(self)




    def constantModifier(self):

        localctx = Java8Parser.ConstantModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_constantModifier)
        try:
            self.state = 1331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1327
                self.annotation()
                pass
            elif token in [Java8Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1328
                self.match(Java8Parser.PUBLIC)
                pass
            elif token in [Java8Parser.STATIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1329
                self.match(Java8Parser.STATIC)
                pass
            elif token in [Java8Parser.FINAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1330
                self.match(Java8Parser.FINAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodHeader(self):
            return self.getTypedRuleContext(Java8Parser.MethodHeaderContext,0)


        def methodBody(self):
            return self.getTypedRuleContext(Java8Parser.MethodBodyContext,0)


        def interfaceMethodModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.InterfaceMethodModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.InterfaceMethodModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_interfaceMethodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceMethodDeclaration" ):
                listener.enterInterfaceMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceMethodDeclaration" ):
                listener.exitInterfaceMethodDeclaration(self)




    def interfaceMethodDeclaration(self):

        localctx = Java8Parser.InterfaceMethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_interfaceMethodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.DEFAULT) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP))) != 0) or _la==Java8Parser.AT:
                self.state = 1333
                self.interfaceMethodModifier()
                self.state = 1338
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1339
            self.methodHeader()
            self.state = 1340
            self.methodBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMethodModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java8Parser.PUBLIC, 0)

        def ABSTRACT(self):
            return self.getToken(Java8Parser.ABSTRACT, 0)

        def DEFAULT(self):
            return self.getToken(Java8Parser.DEFAULT, 0)

        def STATIC(self):
            return self.getToken(Java8Parser.STATIC, 0)

        def STRICTFP(self):
            return self.getToken(Java8Parser.STRICTFP, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_interfaceMethodModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceMethodModifier" ):
                listener.enterInterfaceMethodModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceMethodModifier" ):
                listener.exitInterfaceMethodModifier(self)




    def interfaceMethodModifier(self):

        localctx = Java8Parser.InterfaceMethodModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_interfaceMethodModifier)
        try:
            self.state = 1348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1342
                self.annotation()
                pass
            elif token in [Java8Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1343
                self.match(Java8Parser.PUBLIC)
                pass
            elif token in [Java8Parser.ABSTRACT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1344
                self.match(Java8Parser.ABSTRACT)
                pass
            elif token in [Java8Parser.DEFAULT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1345
                self.match(Java8Parser.DEFAULT)
                pass
            elif token in [Java8Parser.STATIC]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1346
                self.match(Java8Parser.STATIC)
                pass
            elif token in [Java8Parser.STRICTFP]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1347
                self.match(Java8Parser.STRICTFP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationTypeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(Java8Parser.AT, 0)

        def INTERFACE(self):
            return self.getToken(Java8Parser.INTERFACE, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def annotationTypeBody(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationTypeBodyContext,0)


        def interfaceModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.InterfaceModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.InterfaceModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_annotationTypeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationTypeDeclaration" ):
                listener.enterAnnotationTypeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationTypeDeclaration" ):
                listener.exitAnnotationTypeDeclaration(self)




    def annotationTypeDeclaration(self):

        localctx = Java8Parser.AnnotationTypeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_annotationTypeDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1353
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,134,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1350
                    self.interfaceModifier() 
                self.state = 1355
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,134,self._ctx)

            self.state = 1356
            self.match(Java8Parser.AT)
            self.state = 1357
            self.match(Java8Parser.INTERFACE)
            self.state = 1358
            self.match(Java8Parser.Identifier)
            self.state = 1359
            self.annotationTypeBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationTypeBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java8Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java8Parser.RBRACE, 0)

        def annotationTypeMemberDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationTypeMemberDeclarationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationTypeMemberDeclarationContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_annotationTypeBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationTypeBody" ):
                listener.enterAnnotationTypeBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationTypeBody" ):
                listener.exitAnnotationTypeBody(self)




    def annotationTypeBody(self):

        localctx = Java8Parser.AnnotationTypeBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_annotationTypeBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1361
            self.match(Java8Parser.LBRACE)
            self.state = 1365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.CLASS) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.ENUM) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.INTERFACE) | (1 << Java8Parser.LONG) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP) | (1 << Java8Parser.SEMI))) != 0) or _la==Java8Parser.Identifier or _la==Java8Parser.AT:
                self.state = 1362
                self.annotationTypeMemberDeclaration()
                self.state = 1367
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1368
            self.match(Java8Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationTypeMemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotationTypeElementDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationTypeElementDeclarationContext,0)


        def constantDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.ConstantDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.InterfaceDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_annotationTypeMemberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationTypeMemberDeclaration" ):
                listener.enterAnnotationTypeMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationTypeMemberDeclaration" ):
                listener.exitAnnotationTypeMemberDeclaration(self)




    def annotationTypeMemberDeclaration(self):

        localctx = Java8Parser.AnnotationTypeMemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_annotationTypeMemberDeclaration)
        try:
            self.state = 1375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,136,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1370
                self.annotationTypeElementDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1371
                self.constantDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1372
                self.classDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1373
                self.interfaceDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1374
                self.match(Java8Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationTypeElementDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def annotationTypeElementModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationTypeElementModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationTypeElementModifierContext,i)


        def dims(self):
            return self.getTypedRuleContext(Java8Parser.DimsContext,0)


        def defaultValue(self):
            return self.getTypedRuleContext(Java8Parser.DefaultValueContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_annotationTypeElementDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationTypeElementDeclaration" ):
                listener.enterAnnotationTypeElementDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationTypeElementDeclaration" ):
                listener.exitAnnotationTypeElementDeclaration(self)




    def annotationTypeElementDeclaration(self):

        localctx = Java8Parser.AnnotationTypeElementDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_annotationTypeElementDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.ABSTRACT or _la==Java8Parser.PUBLIC or _la==Java8Parser.AT:
                self.state = 1377
                self.annotationTypeElementModifier()
                self.state = 1382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1383
            self.unannType()
            self.state = 1384
            self.match(Java8Parser.Identifier)
            self.state = 1385
            self.match(Java8Parser.LPAREN)
            self.state = 1386
            self.match(Java8Parser.RPAREN)
            self.state = 1388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LBRACK or _la==Java8Parser.AT:
                self.state = 1387
                self.dims()


            self.state = 1391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.DEFAULT:
                self.state = 1390
                self.defaultValue()


            self.state = 1393
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationTypeElementModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java8Parser.PUBLIC, 0)

        def ABSTRACT(self):
            return self.getToken(Java8Parser.ABSTRACT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_annotationTypeElementModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationTypeElementModifier" ):
                listener.enterAnnotationTypeElementModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationTypeElementModifier" ):
                listener.exitAnnotationTypeElementModifier(self)




    def annotationTypeElementModifier(self):

        localctx = Java8Parser.AnnotationTypeElementModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_annotationTypeElementModifier)
        try:
            self.state = 1398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1395
                self.annotation()
                pass
            elif token in [Java8Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1396
                self.match(Java8Parser.PUBLIC)
                pass
            elif token in [Java8Parser.ABSTRACT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1397
                self.match(Java8Parser.ABSTRACT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(Java8Parser.DEFAULT, 0)

        def elementValue(self):
            return self.getTypedRuleContext(Java8Parser.ElementValueContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_defaultValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultValue" ):
                listener.enterDefaultValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultValue" ):
                listener.exitDefaultValue(self)




    def defaultValue(self):

        localctx = Java8Parser.DefaultValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_defaultValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1400
            self.match(Java8Parser.DEFAULT)
            self.state = 1401
            self.elementValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalAnnotation(self):
            return self.getTypedRuleContext(Java8Parser.NormalAnnotationContext,0)


        def markerAnnotation(self):
            return self.getTypedRuleContext(Java8Parser.MarkerAnnotationContext,0)


        def singleElementAnnotation(self):
            return self.getTypedRuleContext(Java8Parser.SingleElementAnnotationContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotation" ):
                listener.enterAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotation" ):
                listener.exitAnnotation(self)




    def annotation(self):

        localctx = Java8Parser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_annotation)
        try:
            self.state = 1406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,141,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1403
                self.normalAnnotation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1404
                self.markerAnnotation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1405
                self.singleElementAnnotation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalAnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(Java8Parser.AT, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def elementValuePairList(self):
            return self.getTypedRuleContext(Java8Parser.ElementValuePairListContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_normalAnnotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalAnnotation" ):
                listener.enterNormalAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalAnnotation" ):
                listener.exitNormalAnnotation(self)




    def normalAnnotation(self):

        localctx = Java8Parser.NormalAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_normalAnnotation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1408
            self.match(Java8Parser.AT)
            self.state = 1409
            self.typeName()
            self.state = 1410
            self.match(Java8Parser.LPAREN)
            self.state = 1412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.Identifier:
                self.state = 1411
                self.elementValuePairList()


            self.state = 1414
            self.match(Java8Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementValuePairListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ElementValuePairContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ElementValuePairContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_elementValuePairList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementValuePairList" ):
                listener.enterElementValuePairList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementValuePairList" ):
                listener.exitElementValuePairList(self)




    def elementValuePairList(self):

        localctx = Java8Parser.ElementValuePairListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_elementValuePairList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1416
            self.elementValuePair()
            self.state = 1421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.COMMA:
                self.state = 1417
                self.match(Java8Parser.COMMA)
                self.state = 1418
                self.elementValuePair()
                self.state = 1423
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementValuePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def ASSIGN(self):
            return self.getToken(Java8Parser.ASSIGN, 0)

        def elementValue(self):
            return self.getTypedRuleContext(Java8Parser.ElementValueContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_elementValuePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementValuePair" ):
                listener.enterElementValuePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementValuePair" ):
                listener.exitElementValuePair(self)




    def elementValuePair(self):

        localctx = Java8Parser.ElementValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_elementValuePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1424
            self.match(Java8Parser.Identifier)
            self.state = 1425
            self.match(Java8Parser.ASSIGN)
            self.state = 1426
            self.elementValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(Java8Parser.ConditionalExpressionContext,0)


        def elementValueArrayInitializer(self):
            return self.getTypedRuleContext(Java8Parser.ElementValueArrayInitializerContext,0)


        def annotation(self):
            return self.getTypedRuleContext(Java8Parser.AnnotationContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_elementValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementValue" ):
                listener.enterElementValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementValue" ):
                listener.exitElementValue(self)




    def elementValue(self):

        localctx = Java8Parser.ElementValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_elementValue)
        try:
            self.state = 1431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,144,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1428
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1429
                self.elementValueArrayInitializer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1430
                self.annotation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementValueArrayInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java8Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java8Parser.RBRACE, 0)

        def elementValueList(self):
            return self.getTypedRuleContext(Java8Parser.ElementValueListContext,0)


        def COMMA(self):
            return self.getToken(Java8Parser.COMMA, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_elementValueArrayInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementValueArrayInitializer" ):
                listener.enterElementValueArrayInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementValueArrayInitializer" ):
                listener.exitElementValueArrayInitializer(self)




    def elementValueArrayInitializer(self):

        localctx = Java8Parser.ElementValueArrayInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_elementValueArrayInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1433
            self.match(Java8Parser.LBRACE)
            self.state = 1435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN) | (1 << Java8Parser.LBRACE))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                self.state = 1434
                self.elementValueList()


            self.state = 1438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.COMMA:
                self.state = 1437
                self.match(Java8Parser.COMMA)


            self.state = 1440
            self.match(Java8Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementValueListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ElementValueContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ElementValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_elementValueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementValueList" ):
                listener.enterElementValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementValueList" ):
                listener.exitElementValueList(self)




    def elementValueList(self):

        localctx = Java8Parser.ElementValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_elementValueList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1442
            self.elementValue()
            self.state = 1447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,147,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1443
                    self.match(Java8Parser.COMMA)
                    self.state = 1444
                    self.elementValue() 
                self.state = 1449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,147,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MarkerAnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(Java8Parser.AT, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_markerAnnotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMarkerAnnotation" ):
                listener.enterMarkerAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMarkerAnnotation" ):
                listener.exitMarkerAnnotation(self)




    def markerAnnotation(self):

        localctx = Java8Parser.MarkerAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_markerAnnotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1450
            self.match(Java8Parser.AT)
            self.state = 1451
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleElementAnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(Java8Parser.AT, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def elementValue(self):
            return self.getTypedRuleContext(Java8Parser.ElementValueContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_singleElementAnnotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleElementAnnotation" ):
                listener.enterSingleElementAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleElementAnnotation" ):
                listener.exitSingleElementAnnotation(self)




    def singleElementAnnotation(self):

        localctx = Java8Parser.SingleElementAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_singleElementAnnotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1453
            self.match(Java8Parser.AT)
            self.state = 1454
            self.typeName()
            self.state = 1455
            self.match(Java8Parser.LPAREN)
            self.state = 1456
            self.elementValue()
            self.state = 1457
            self.match(Java8Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java8Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java8Parser.RBRACE, 0)

        def variableInitializerList(self):
            return self.getTypedRuleContext(Java8Parser.VariableInitializerListContext,0)


        def COMMA(self):
            return self.getToken(Java8Parser.COMMA, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_arrayInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayInitializer" ):
                listener.enterArrayInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayInitializer" ):
                listener.exitArrayInitializer(self)




    def arrayInitializer(self):

        localctx = Java8Parser.ArrayInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_arrayInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1459
            self.match(Java8Parser.LBRACE)
            self.state = 1461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN) | (1 << Java8Parser.LBRACE))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                self.state = 1460
                self.variableInitializerList()


            self.state = 1464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.COMMA:
                self.state = 1463
                self.match(Java8Parser.COMMA)


            self.state = 1466
            self.match(Java8Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableInitializerListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableInitializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.VariableInitializerContext)
            else:
                return self.getTypedRuleContext(Java8Parser.VariableInitializerContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_variableInitializerList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableInitializerList" ):
                listener.enterVariableInitializerList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableInitializerList" ):
                listener.exitVariableInitializerList(self)




    def variableInitializerList(self):

        localctx = Java8Parser.VariableInitializerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_variableInitializerList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1468
            self.variableInitializer()
            self.state = 1473
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,150,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1469
                    self.match(Java8Parser.COMMA)
                    self.state = 1470
                    self.variableInitializer() 
                self.state = 1475
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,150,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java8Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java8Parser.RBRACE, 0)

        def blockStatements(self):
            return self.getTypedRuleContext(Java8Parser.BlockStatementsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = Java8Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1476
            self.match(Java8Parser.LBRACE)
            self.state = 1478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.ASSERT) | (1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BREAK) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.CLASS) | (1 << Java8Parser.CONTINUE) | (1 << Java8Parser.DO) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.ENUM) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.FOR) | (1 << Java8Parser.IF) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.RETURN) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.SWITCH) | (1 << Java8Parser.SYNCHRONIZED) | (1 << Java8Parser.THIS) | (1 << Java8Parser.THROW) | (1 << Java8Parser.TRY) | (1 << Java8Parser.VOID) | (1 << Java8Parser.WHILE) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN) | (1 << Java8Parser.LBRACE) | (1 << Java8Parser.SEMI))) != 0) or ((((_la - 79)) & ~0x3f) == 0 and ((1 << (_la - 79)) & ((1 << (Java8Parser.INC - 79)) | (1 << (Java8Parser.DEC - 79)) | (1 << (Java8Parser.Identifier - 79)) | (1 << (Java8Parser.AT - 79)))) != 0):
                self.state = 1477
                self.blockStatements()


            self.state = 1480
            self.match(Java8Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(Java8Parser.BlockStatementContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_blockStatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatements" ):
                listener.enterBlockStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatements" ):
                listener.exitBlockStatements(self)




    def blockStatements(self):

        localctx = Java8Parser.BlockStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_blockStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1483 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1482
                self.blockStatement()
                self.state = 1485 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.ABSTRACT) | (1 << Java8Parser.ASSERT) | (1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BREAK) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.CLASS) | (1 << Java8Parser.CONTINUE) | (1 << Java8Parser.DO) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.ENUM) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.FOR) | (1 << Java8Parser.IF) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.PRIVATE) | (1 << Java8Parser.PROTECTED) | (1 << Java8Parser.PUBLIC) | (1 << Java8Parser.RETURN) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.STATIC) | (1 << Java8Parser.STRICTFP) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.SWITCH) | (1 << Java8Parser.SYNCHRONIZED) | (1 << Java8Parser.THIS) | (1 << Java8Parser.THROW) | (1 << Java8Parser.TRY) | (1 << Java8Parser.VOID) | (1 << Java8Parser.WHILE) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN) | (1 << Java8Parser.LBRACE) | (1 << Java8Parser.SEMI))) != 0) or ((((_la - 79)) & ~0x3f) == 0 and ((1 << (_la - 79)) & ((1 << (Java8Parser.INC - 79)) | (1 << (Java8Parser.DEC - 79)) | (1 << (Java8Parser.Identifier - 79)) | (1 << (Java8Parser.AT - 79)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localVariableDeclarationStatement(self):
            return self.getTypedRuleContext(Java8Parser.LocalVariableDeclarationStatementContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.ClassDeclarationContext,0)


        def statement(self):
            return self.getTypedRuleContext(Java8Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)




    def blockStatement(self):

        localctx = Java8Parser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_blockStatement)
        try:
            self.state = 1490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,153,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1487
                self.localVariableDeclarationStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1488
                self.classDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1489
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalVariableDeclarationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localVariableDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.LocalVariableDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_localVariableDeclarationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalVariableDeclarationStatement" ):
                listener.enterLocalVariableDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalVariableDeclarationStatement" ):
                listener.exitLocalVariableDeclarationStatement(self)




    def localVariableDeclarationStatement(self):

        localctx = Java8Parser.LocalVariableDeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_localVariableDeclarationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1492
            self.localVariableDeclaration()
            self.state = 1493
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalVariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def variableDeclaratorList(self):
            return self.getTypedRuleContext(Java8Parser.VariableDeclaratorListContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.VariableModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_localVariableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalVariableDeclaration" ):
                listener.enterLocalVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalVariableDeclaration" ):
                listener.exitLocalVariableDeclaration(self)




    def localVariableDeclaration(self):

        localctx = Java8Parser.LocalVariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_localVariableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.FINAL or _la==Java8Parser.AT:
                self.state = 1495
                self.variableModifier()
                self.state = 1500
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1501
            self.unannType()
            self.state = 1502
            self.variableDeclaratorList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementWithoutTrailingSubstatement(self):
            return self.getTypedRuleContext(Java8Parser.StatementWithoutTrailingSubstatementContext,0)


        def labeledStatement(self):
            return self.getTypedRuleContext(Java8Parser.LabeledStatementContext,0)


        def ifThenStatement(self):
            return self.getTypedRuleContext(Java8Parser.IfThenStatementContext,0)


        def ifThenElseStatement(self):
            return self.getTypedRuleContext(Java8Parser.IfThenElseStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(Java8Parser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(Java8Parser.ForStatementContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = Java8Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_statement)
        try:
            self.state = 1510
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,155,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1504
                self.statementWithoutTrailingSubstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1505
                self.labeledStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1506
                self.ifThenStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1507
                self.ifThenElseStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1508
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1509
                self.forStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementWithoutTrailingSubstatement(self):
            return self.getTypedRuleContext(Java8Parser.StatementWithoutTrailingSubstatementContext,0)


        def labeledStatementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.LabeledStatementNoShortIfContext,0)


        def ifThenElseStatementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.IfThenElseStatementNoShortIfContext,0)


        def whileStatementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.WhileStatementNoShortIfContext,0)


        def forStatementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.ForStatementNoShortIfContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_statementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementNoShortIf" ):
                listener.enterStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementNoShortIf" ):
                listener.exitStatementNoShortIf(self)




    def statementNoShortIf(self):

        localctx = Java8Parser.StatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_statementNoShortIf)
        try:
            self.state = 1517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,156,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1512
                self.statementWithoutTrailingSubstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1513
                self.labeledStatementNoShortIf()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1514
                self.ifThenElseStatementNoShortIf()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1515
                self.whileStatementNoShortIf()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1516
                self.forStatementNoShortIf()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementWithoutTrailingSubstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(Java8Parser.BlockContext,0)


        def emptyStatement(self):
            return self.getTypedRuleContext(Java8Parser.EmptyStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionStatementContext,0)


        def assertStatement(self):
            return self.getTypedRuleContext(Java8Parser.AssertStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(Java8Parser.SwitchStatementContext,0)


        def doStatement(self):
            return self.getTypedRuleContext(Java8Parser.DoStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(Java8Parser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(Java8Parser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(Java8Parser.ReturnStatementContext,0)


        def synchronizedStatement(self):
            return self.getTypedRuleContext(Java8Parser.SynchronizedStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(Java8Parser.ThrowStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(Java8Parser.TryStatementContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_statementWithoutTrailingSubstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementWithoutTrailingSubstatement" ):
                listener.enterStatementWithoutTrailingSubstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementWithoutTrailingSubstatement" ):
                listener.exitStatementWithoutTrailingSubstatement(self)




    def statementWithoutTrailingSubstatement(self):

        localctx = Java8Parser.StatementWithoutTrailingSubstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_statementWithoutTrailingSubstatement)
        try:
            self.state = 1531
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1519
                self.block()
                pass
            elif token in [Java8Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1520
                self.emptyStatement()
                pass
            elif token in [Java8Parser.BOOLEAN, Java8Parser.BYTE, Java8Parser.CHAR, Java8Parser.DOUBLE, Java8Parser.FLOAT, Java8Parser.INT, Java8Parser.LONG, Java8Parser.NEW, Java8Parser.SHORT, Java8Parser.SUPER, Java8Parser.THIS, Java8Parser.VOID, Java8Parser.IntegerLiteral, Java8Parser.FloatingPointLiteral, Java8Parser.BooleanLiteral, Java8Parser.CharacterLiteral, Java8Parser.StringLiteral, Java8Parser.NullLiteral, Java8Parser.LPAREN, Java8Parser.INC, Java8Parser.DEC, Java8Parser.Identifier, Java8Parser.AT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1521
                self.expressionStatement()
                pass
            elif token in [Java8Parser.ASSERT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1522
                self.assertStatement()
                pass
            elif token in [Java8Parser.SWITCH]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1523
                self.switchStatement()
                pass
            elif token in [Java8Parser.DO]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1524
                self.doStatement()
                pass
            elif token in [Java8Parser.BREAK]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1525
                self.breakStatement()
                pass
            elif token in [Java8Parser.CONTINUE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1526
                self.continueStatement()
                pass
            elif token in [Java8Parser.RETURN]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1527
                self.returnStatement()
                pass
            elif token in [Java8Parser.SYNCHRONIZED]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1528
                self.synchronizedStatement()
                pass
            elif token in [Java8Parser.THROW]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1529
                self.throwStatement()
                pass
            elif token in [Java8Parser.TRY]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1530
                self.tryStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_emptyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)




    def emptyStatement(self):

        localctx = Java8Parser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1533
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def COLON(self):
            return self.getToken(Java8Parser.COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(Java8Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_labeledStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledStatement" ):
                listener.enterLabeledStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledStatement" ):
                listener.exitLabeledStatement(self)




    def labeledStatement(self):

        localctx = Java8Parser.LabeledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_labeledStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1535
            self.match(Java8Parser.Identifier)
            self.state = 1536
            self.match(Java8Parser.COLON)
            self.state = 1537
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def COLON(self):
            return self.getToken(Java8Parser.COLON, 0)

        def statementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.StatementNoShortIfContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_labeledStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledStatementNoShortIf" ):
                listener.enterLabeledStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledStatementNoShortIf" ):
                listener.exitLabeledStatementNoShortIf(self)




    def labeledStatementNoShortIf(self):

        localctx = Java8Parser.LabeledStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_labeledStatementNoShortIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1539
            self.match(Java8Parser.Identifier)
            self.state = 1540
            self.match(Java8Parser.COLON)
            self.state = 1541
            self.statementNoShortIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementExpression(self):
            return self.getTypedRuleContext(Java8Parser.StatementExpressionContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = Java8Parser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1543
            self.statementExpression()
            self.state = 1544
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(Java8Parser.AssignmentContext,0)


        def preIncrementExpression(self):
            return self.getTypedRuleContext(Java8Parser.PreIncrementExpressionContext,0)


        def preDecrementExpression(self):
            return self.getTypedRuleContext(Java8Parser.PreDecrementExpressionContext,0)


        def postIncrementExpression(self):
            return self.getTypedRuleContext(Java8Parser.PostIncrementExpressionContext,0)


        def postDecrementExpression(self):
            return self.getTypedRuleContext(Java8Parser.PostDecrementExpressionContext,0)


        def methodInvocation(self):
            return self.getTypedRuleContext(Java8Parser.MethodInvocationContext,0)


        def classInstanceCreationExpression(self):
            return self.getTypedRuleContext(Java8Parser.ClassInstanceCreationExpressionContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_statementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementExpression" ):
                listener.enterStatementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementExpression" ):
                listener.exitStatementExpression(self)




    def statementExpression(self):

        localctx = Java8Parser.StatementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_statementExpression)
        try:
            self.state = 1553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,158,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1546
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1547
                self.preIncrementExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1548
                self.preDecrementExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1549
                self.postIncrementExpression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1550
                self.postDecrementExpression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1551
                self.methodInvocation()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1552
                self.classInstanceCreationExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfThenStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Java8Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(Java8Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_ifThenStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfThenStatement" ):
                listener.enterIfThenStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfThenStatement" ):
                listener.exitIfThenStatement(self)




    def ifThenStatement(self):

        localctx = Java8Parser.IfThenStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_ifThenStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1555
            self.match(Java8Parser.IF)
            self.state = 1556
            self.match(Java8Parser.LPAREN)
            self.state = 1557
            self.expression()
            self.state = 1558
            self.match(Java8Parser.RPAREN)
            self.state = 1559
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfThenElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Java8Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def statementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.StatementNoShortIfContext,0)


        def ELSE(self):
            return self.getToken(Java8Parser.ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(Java8Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_ifThenElseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfThenElseStatement" ):
                listener.enterIfThenElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfThenElseStatement" ):
                listener.exitIfThenElseStatement(self)




    def ifThenElseStatement(self):

        localctx = Java8Parser.IfThenElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_ifThenElseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1561
            self.match(Java8Parser.IF)
            self.state = 1562
            self.match(Java8Parser.LPAREN)
            self.state = 1563
            self.expression()
            self.state = 1564
            self.match(Java8Parser.RPAREN)
            self.state = 1565
            self.statementNoShortIf()
            self.state = 1566
            self.match(Java8Parser.ELSE)
            self.state = 1567
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfThenElseStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Java8Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def statementNoShortIf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.StatementNoShortIfContext)
            else:
                return self.getTypedRuleContext(Java8Parser.StatementNoShortIfContext,i)


        def ELSE(self):
            return self.getToken(Java8Parser.ELSE, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_ifThenElseStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfThenElseStatementNoShortIf" ):
                listener.enterIfThenElseStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfThenElseStatementNoShortIf" ):
                listener.exitIfThenElseStatementNoShortIf(self)




    def ifThenElseStatementNoShortIf(self):

        localctx = Java8Parser.IfThenElseStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_ifThenElseStatementNoShortIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1569
            self.match(Java8Parser.IF)
            self.state = 1570
            self.match(Java8Parser.LPAREN)
            self.state = 1571
            self.expression()
            self.state = 1572
            self.match(Java8Parser.RPAREN)
            self.state = 1573
            self.statementNoShortIf()
            self.state = 1574
            self.match(Java8Parser.ELSE)
            self.state = 1575
            self.statementNoShortIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssertStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSERT(self):
            return self.getToken(Java8Parser.ASSERT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ExpressionContext,i)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def COLON(self):
            return self.getToken(Java8Parser.COLON, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_assertStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssertStatement" ):
                listener.enterAssertStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssertStatement" ):
                listener.exitAssertStatement(self)




    def assertStatement(self):

        localctx = Java8Parser.AssertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_assertStatement)
        try:
            self.state = 1587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,159,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1577
                self.match(Java8Parser.ASSERT)
                self.state = 1578
                self.expression()
                self.state = 1579
                self.match(Java8Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1581
                self.match(Java8Parser.ASSERT)
                self.state = 1582
                self.expression()
                self.state = 1583
                self.match(Java8Parser.COLON)
                self.state = 1584
                self.expression()
                self.state = 1585
                self.match(Java8Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(Java8Parser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def switchBlock(self):
            return self.getTypedRuleContext(Java8Parser.SwitchBlockContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = Java8Parser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1589
            self.match(Java8Parser.SWITCH)
            self.state = 1590
            self.match(Java8Parser.LPAREN)
            self.state = 1591
            self.expression()
            self.state = 1592
            self.match(Java8Parser.RPAREN)
            self.state = 1593
            self.switchBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java8Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java8Parser.RBRACE, 0)

        def switchBlockStatementGroup(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.SwitchBlockStatementGroupContext)
            else:
                return self.getTypedRuleContext(Java8Parser.SwitchBlockStatementGroupContext,i)


        def switchLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.SwitchLabelContext)
            else:
                return self.getTypedRuleContext(Java8Parser.SwitchLabelContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_switchBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBlock" ):
                listener.enterSwitchBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBlock" ):
                listener.exitSwitchBlock(self)




    def switchBlock(self):

        localctx = Java8Parser.SwitchBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_switchBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1595
            self.match(Java8Parser.LBRACE)
            self.state = 1599
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,160,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1596
                    self.switchBlockStatementGroup() 
                self.state = 1601
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,160,self._ctx)

            self.state = 1605
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.CASE or _la==Java8Parser.DEFAULT:
                self.state = 1602
                self.switchLabel()
                self.state = 1607
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1608
            self.match(Java8Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBlockStatementGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switchLabels(self):
            return self.getTypedRuleContext(Java8Parser.SwitchLabelsContext,0)


        def blockStatements(self):
            return self.getTypedRuleContext(Java8Parser.BlockStatementsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_switchBlockStatementGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBlockStatementGroup" ):
                listener.enterSwitchBlockStatementGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBlockStatementGroup" ):
                listener.exitSwitchBlockStatementGroup(self)




    def switchBlockStatementGroup(self):

        localctx = Java8Parser.SwitchBlockStatementGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_switchBlockStatementGroup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1610
            self.switchLabels()
            self.state = 1611
            self.blockStatements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchLabelsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switchLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.SwitchLabelContext)
            else:
                return self.getTypedRuleContext(Java8Parser.SwitchLabelContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_switchLabels

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchLabels" ):
                listener.enterSwitchLabels(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchLabels" ):
                listener.exitSwitchLabels(self)




    def switchLabels(self):

        localctx = Java8Parser.SwitchLabelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_switchLabels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1613
            self.switchLabel()
            self.state = 1617
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.CASE or _la==Java8Parser.DEFAULT:
                self.state = 1614
                self.switchLabel()
                self.state = 1619
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(Java8Parser.CASE, 0)

        def constantExpression(self):
            return self.getTypedRuleContext(Java8Parser.ConstantExpressionContext,0)


        def COLON(self):
            return self.getToken(Java8Parser.COLON, 0)

        def enumConstantName(self):
            return self.getTypedRuleContext(Java8Parser.EnumConstantNameContext,0)


        def DEFAULT(self):
            return self.getToken(Java8Parser.DEFAULT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_switchLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchLabel" ):
                listener.enterSwitchLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchLabel" ):
                listener.exitSwitchLabel(self)




    def switchLabel(self):

        localctx = Java8Parser.SwitchLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_switchLabel)
        try:
            self.state = 1630
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,163,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1620
                self.match(Java8Parser.CASE)
                self.state = 1621
                self.constantExpression()
                self.state = 1622
                self.match(Java8Parser.COLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1624
                self.match(Java8Parser.CASE)
                self.state = 1625
                self.enumConstantName()
                self.state = 1626
                self.match(Java8Parser.COLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1628
                self.match(Java8Parser.DEFAULT)
                self.state = 1629
                self.match(Java8Parser.COLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumConstantNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_enumConstantName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumConstantName" ):
                listener.enterEnumConstantName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumConstantName" ):
                listener.exitEnumConstantName(self)




    def enumConstantName(self):

        localctx = Java8Parser.EnumConstantNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_enumConstantName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1632
            self.match(Java8Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(Java8Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(Java8Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = Java8Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1634
            self.match(Java8Parser.WHILE)
            self.state = 1635
            self.match(Java8Parser.LPAREN)
            self.state = 1636
            self.expression()
            self.state = 1637
            self.match(Java8Parser.RPAREN)
            self.state = 1638
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(Java8Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def statementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.StatementNoShortIfContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_whileStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatementNoShortIf" ):
                listener.enterWhileStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatementNoShortIf" ):
                listener.exitWhileStatementNoShortIf(self)




    def whileStatementNoShortIf(self):

        localctx = Java8Parser.WhileStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_whileStatementNoShortIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1640
            self.match(Java8Parser.WHILE)
            self.state = 1641
            self.match(Java8Parser.LPAREN)
            self.state = 1642
            self.expression()
            self.state = 1643
            self.match(Java8Parser.RPAREN)
            self.state = 1644
            self.statementNoShortIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(Java8Parser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(Java8Parser.StatementContext,0)


        def WHILE(self):
            return self.getToken(Java8Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_doStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoStatement" ):
                listener.enterDoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoStatement" ):
                listener.exitDoStatement(self)




    def doStatement(self):

        localctx = Java8Parser.DoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_doStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1646
            self.match(Java8Parser.DO)
            self.state = 1647
            self.statement()
            self.state = 1648
            self.match(Java8Parser.WHILE)
            self.state = 1649
            self.match(Java8Parser.LPAREN)
            self.state = 1650
            self.expression()
            self.state = 1651
            self.match(Java8Parser.RPAREN)
            self.state = 1652
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicForStatement(self):
            return self.getTypedRuleContext(Java8Parser.BasicForStatementContext,0)


        def enhancedForStatement(self):
            return self.getTypedRuleContext(Java8Parser.EnhancedForStatementContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = Java8Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_forStatement)
        try:
            self.state = 1656
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,164,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1654
                self.basicForStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1655
                self.enhancedForStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicForStatementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.BasicForStatementNoShortIfContext,0)


        def enhancedForStatementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.EnhancedForStatementNoShortIfContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_forStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatementNoShortIf" ):
                listener.enterForStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatementNoShortIf" ):
                listener.exitForStatementNoShortIf(self)




    def forStatementNoShortIf(self):

        localctx = Java8Parser.ForStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_forStatementNoShortIf)
        try:
            self.state = 1660
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,165,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1658
                self.basicForStatementNoShortIf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1659
                self.enhancedForStatementNoShortIf()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Java8Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.SEMI)
            else:
                return self.getToken(Java8Parser.SEMI, i)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(Java8Parser.StatementContext,0)


        def forInit(self):
            return self.getTypedRuleContext(Java8Parser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(Java8Parser.ForUpdateContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_basicForStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicForStatement" ):
                listener.enterBasicForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicForStatement" ):
                listener.exitBasicForStatement(self)




    def basicForStatement(self):

        localctx = Java8Parser.BasicForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_basicForStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1662
            self.match(Java8Parser.FOR)
            self.state = 1663
            self.match(Java8Parser.LPAREN)
            self.state = 1665
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 79)) & ~0x3f) == 0 and ((1 << (_la - 79)) & ((1 << (Java8Parser.INC - 79)) | (1 << (Java8Parser.DEC - 79)) | (1 << (Java8Parser.Identifier - 79)) | (1 << (Java8Parser.AT - 79)))) != 0):
                self.state = 1664
                self.forInit()


            self.state = 1667
            self.match(Java8Parser.SEMI)
            self.state = 1669
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                self.state = 1668
                self.expression()


            self.state = 1671
            self.match(Java8Parser.SEMI)
            self.state = 1673
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 79)) & ~0x3f) == 0 and ((1 << (_la - 79)) & ((1 << (Java8Parser.INC - 79)) | (1 << (Java8Parser.DEC - 79)) | (1 << (Java8Parser.Identifier - 79)) | (1 << (Java8Parser.AT - 79)))) != 0):
                self.state = 1672
                self.forUpdate()


            self.state = 1675
            self.match(Java8Parser.RPAREN)
            self.state = 1676
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicForStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Java8Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.SEMI)
            else:
                return self.getToken(Java8Parser.SEMI, i)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def statementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.StatementNoShortIfContext,0)


        def forInit(self):
            return self.getTypedRuleContext(Java8Parser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(Java8Parser.ForUpdateContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_basicForStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicForStatementNoShortIf" ):
                listener.enterBasicForStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicForStatementNoShortIf" ):
                listener.exitBasicForStatementNoShortIf(self)




    def basicForStatementNoShortIf(self):

        localctx = Java8Parser.BasicForStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_basicForStatementNoShortIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1678
            self.match(Java8Parser.FOR)
            self.state = 1679
            self.match(Java8Parser.LPAREN)
            self.state = 1681
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 79)) & ~0x3f) == 0 and ((1 << (_la - 79)) & ((1 << (Java8Parser.INC - 79)) | (1 << (Java8Parser.DEC - 79)) | (1 << (Java8Parser.Identifier - 79)) | (1 << (Java8Parser.AT - 79)))) != 0):
                self.state = 1680
                self.forInit()


            self.state = 1683
            self.match(Java8Parser.SEMI)
            self.state = 1685
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                self.state = 1684
                self.expression()


            self.state = 1687
            self.match(Java8Parser.SEMI)
            self.state = 1689
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 79)) & ~0x3f) == 0 and ((1 << (_la - 79)) & ((1 << (Java8Parser.INC - 79)) | (1 << (Java8Parser.DEC - 79)) | (1 << (Java8Parser.Identifier - 79)) | (1 << (Java8Parser.AT - 79)))) != 0):
                self.state = 1688
                self.forUpdate()


            self.state = 1691
            self.match(Java8Parser.RPAREN)
            self.state = 1692
            self.statementNoShortIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementExpressionList(self):
            return self.getTypedRuleContext(Java8Parser.StatementExpressionListContext,0)


        def localVariableDeclaration(self):
            return self.getTypedRuleContext(Java8Parser.LocalVariableDeclarationContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)




    def forInit(self):

        localctx = Java8Parser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_forInit)
        try:
            self.state = 1696
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,172,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1694
                self.statementExpressionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1695
                self.localVariableDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementExpressionList(self):
            return self.getTypedRuleContext(Java8Parser.StatementExpressionListContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)




    def forUpdate(self):

        localctx = Java8Parser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1698
            self.statementExpressionList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.StatementExpressionContext)
            else:
                return self.getTypedRuleContext(Java8Parser.StatementExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_statementExpressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementExpressionList" ):
                listener.enterStatementExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementExpressionList" ):
                listener.exitStatementExpressionList(self)




    def statementExpressionList(self):

        localctx = Java8Parser.StatementExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_statementExpressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1700
            self.statementExpression()
            self.state = 1705
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.COMMA:
                self.state = 1701
                self.match(Java8Parser.COMMA)
                self.state = 1702
                self.statementExpression()
                self.state = 1707
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnhancedForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Java8Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java8Parser.VariableDeclaratorIdContext,0)


        def COLON(self):
            return self.getToken(Java8Parser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(Java8Parser.StatementContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.VariableModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_enhancedForStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnhancedForStatement" ):
                listener.enterEnhancedForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnhancedForStatement" ):
                listener.exitEnhancedForStatement(self)




    def enhancedForStatement(self):

        localctx = Java8Parser.EnhancedForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_enhancedForStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1708
            self.match(Java8Parser.FOR)
            self.state = 1709
            self.match(Java8Parser.LPAREN)
            self.state = 1713
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.FINAL or _la==Java8Parser.AT:
                self.state = 1710
                self.variableModifier()
                self.state = 1715
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1716
            self.unannType()
            self.state = 1717
            self.variableDeclaratorId()
            self.state = 1718
            self.match(Java8Parser.COLON)
            self.state = 1719
            self.expression()
            self.state = 1720
            self.match(Java8Parser.RPAREN)
            self.state = 1721
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnhancedForStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Java8Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java8Parser.VariableDeclaratorIdContext,0)


        def COLON(self):
            return self.getToken(Java8Parser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def statementNoShortIf(self):
            return self.getTypedRuleContext(Java8Parser.StatementNoShortIfContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.VariableModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_enhancedForStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnhancedForStatementNoShortIf" ):
                listener.enterEnhancedForStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnhancedForStatementNoShortIf" ):
                listener.exitEnhancedForStatementNoShortIf(self)




    def enhancedForStatementNoShortIf(self):

        localctx = Java8Parser.EnhancedForStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_enhancedForStatementNoShortIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1723
            self.match(Java8Parser.FOR)
            self.state = 1724
            self.match(Java8Parser.LPAREN)
            self.state = 1728
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.FINAL or _la==Java8Parser.AT:
                self.state = 1725
                self.variableModifier()
                self.state = 1730
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1731
            self.unannType()
            self.state = 1732
            self.variableDeclaratorId()
            self.state = 1733
            self.match(Java8Parser.COLON)
            self.state = 1734
            self.expression()
            self.state = 1735
            self.match(Java8Parser.RPAREN)
            self.state = 1736
            self.statementNoShortIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(Java8Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = Java8Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_breakStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1738
            self.match(Java8Parser.BREAK)
            self.state = 1740
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.Identifier:
                self.state = 1739
                self.match(Java8Parser.Identifier)


            self.state = 1742
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(Java8Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = Java8Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_continueStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1744
            self.match(Java8Parser.CONTINUE)
            self.state = 1746
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.Identifier:
                self.state = 1745
                self.match(Java8Parser.Identifier)


            self.state = 1748
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(Java8Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = Java8Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1750
            self.match(Java8Parser.RETURN)
            self.state = 1752
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                self.state = 1751
                self.expression()


            self.state = 1754
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROW(self):
            return self.getToken(Java8Parser.THROW, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_throwStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowStatement" ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowStatement" ):
                listener.exitThrowStatement(self)




    def throwStatement(self):

        localctx = Java8Parser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1756
            self.match(Java8Parser.THROW)
            self.state = 1757
            self.expression()
            self.state = 1758
            self.match(Java8Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SynchronizedStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYNCHRONIZED(self):
            return self.getToken(Java8Parser.SYNCHRONIZED, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(Java8Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_synchronizedStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSynchronizedStatement" ):
                listener.enterSynchronizedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSynchronizedStatement" ):
                listener.exitSynchronizedStatement(self)




    def synchronizedStatement(self):

        localctx = Java8Parser.SynchronizedStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_synchronizedStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1760
            self.match(Java8Parser.SYNCHRONIZED)
            self.state = 1761
            self.match(Java8Parser.LPAREN)
            self.state = 1762
            self.expression()
            self.state = 1763
            self.match(Java8Parser.RPAREN)
            self.state = 1764
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(Java8Parser.TRY, 0)

        def block(self):
            return self.getTypedRuleContext(Java8Parser.BlockContext,0)


        def catches(self):
            return self.getTypedRuleContext(Java8Parser.CatchesContext,0)


        def finally_(self):
            return self.getTypedRuleContext(Java8Parser.Finally_Context,0)


        def tryWithResourcesStatement(self):
            return self.getTypedRuleContext(Java8Parser.TryWithResourcesStatementContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_tryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)




    def tryStatement(self):

        localctx = Java8Parser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_tryStatement)
        self._la = 0 # Token type
        try:
            self.state = 1778
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,180,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1766
                self.match(Java8Parser.TRY)
                self.state = 1767
                self.block()
                self.state = 1768
                self.catches()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1770
                self.match(Java8Parser.TRY)
                self.state = 1771
                self.block()
                self.state = 1773
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.CATCH:
                    self.state = 1772
                    self.catches()


                self.state = 1775
                self.finally_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1777
                self.tryWithResourcesStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def catchClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.CatchClauseContext)
            else:
                return self.getTypedRuleContext(Java8Parser.CatchClauseContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_catches

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatches" ):
                listener.enterCatches(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatches" ):
                listener.exitCatches(self)




    def catches(self):

        localctx = Java8Parser.CatchesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_catches)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1780
            self.catchClause()
            self.state = 1784
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.CATCH:
                self.state = 1781
                self.catchClause()
                self.state = 1786
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(Java8Parser.CATCH, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def catchFormalParameter(self):
            return self.getTypedRuleContext(Java8Parser.CatchFormalParameterContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(Java8Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_catchClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchClause" ):
                listener.enterCatchClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchClause" ):
                listener.exitCatchClause(self)




    def catchClause(self):

        localctx = Java8Parser.CatchClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_catchClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1787
            self.match(Java8Parser.CATCH)
            self.state = 1788
            self.match(Java8Parser.LPAREN)
            self.state = 1789
            self.catchFormalParameter()
            self.state = 1790
            self.match(Java8Parser.RPAREN)
            self.state = 1791
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchFormalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def catchType(self):
            return self.getTypedRuleContext(Java8Parser.CatchTypeContext,0)


        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java8Parser.VariableDeclaratorIdContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.VariableModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_catchFormalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchFormalParameter" ):
                listener.enterCatchFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchFormalParameter" ):
                listener.exitCatchFormalParameter(self)




    def catchFormalParameter(self):

        localctx = Java8Parser.CatchFormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_catchFormalParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1796
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.FINAL or _la==Java8Parser.AT:
                self.state = 1793
                self.variableModifier()
                self.state = 1798
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1799
            self.catchType()
            self.state = 1800
            self.variableDeclaratorId()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannClassType(self):
            return self.getTypedRuleContext(Java8Parser.UnannClassTypeContext,0)


        def BITOR(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.BITOR)
            else:
                return self.getToken(Java8Parser.BITOR, i)

        def classType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ClassTypeContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ClassTypeContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_catchType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchType" ):
                listener.enterCatchType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchType" ):
                listener.exitCatchType(self)




    def catchType(self):

        localctx = Java8Parser.CatchTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_catchType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1802
            self.unannClassType()
            self.state = 1807
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.BITOR:
                self.state = 1803
                self.match(Java8Parser.BITOR)
                self.state = 1804
                self.classType()
                self.state = 1809
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Finally_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINALLY(self):
            return self.getToken(Java8Parser.FINALLY, 0)

        def block(self):
            return self.getTypedRuleContext(Java8Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_finally_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinally_" ):
                listener.enterFinally_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinally_" ):
                listener.exitFinally_(self)




    def finally_(self):

        localctx = Java8Parser.Finally_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_finally_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1810
            self.match(Java8Parser.FINALLY)
            self.state = 1811
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryWithResourcesStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(Java8Parser.TRY, 0)

        def resourceSpecification(self):
            return self.getTypedRuleContext(Java8Parser.ResourceSpecificationContext,0)


        def block(self):
            return self.getTypedRuleContext(Java8Parser.BlockContext,0)


        def catches(self):
            return self.getTypedRuleContext(Java8Parser.CatchesContext,0)


        def finally_(self):
            return self.getTypedRuleContext(Java8Parser.Finally_Context,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_tryWithResourcesStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryWithResourcesStatement" ):
                listener.enterTryWithResourcesStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryWithResourcesStatement" ):
                listener.exitTryWithResourcesStatement(self)




    def tryWithResourcesStatement(self):

        localctx = Java8Parser.TryWithResourcesStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_tryWithResourcesStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1813
            self.match(Java8Parser.TRY)
            self.state = 1814
            self.resourceSpecification()
            self.state = 1815
            self.block()
            self.state = 1817
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.CATCH:
                self.state = 1816
                self.catches()


            self.state = 1820
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.FINALLY:
                self.state = 1819
                self.finally_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceSpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def resourceList(self):
            return self.getTypedRuleContext(Java8Parser.ResourceListContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(Java8Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_resourceSpecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResourceSpecification" ):
                listener.enterResourceSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResourceSpecification" ):
                listener.exitResourceSpecification(self)




    def resourceSpecification(self):

        localctx = Java8Parser.ResourceSpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_resourceSpecification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1822
            self.match(Java8Parser.LPAREN)
            self.state = 1823
            self.resourceList()
            self.state = 1825
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.SEMI:
                self.state = 1824
                self.match(Java8Parser.SEMI)


            self.state = 1827
            self.match(Java8Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def resource(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ResourceContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ResourceContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.SEMI)
            else:
                return self.getToken(Java8Parser.SEMI, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_resourceList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResourceList" ):
                listener.enterResourceList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResourceList" ):
                listener.exitResourceList(self)




    def resourceList(self):

        localctx = Java8Parser.ResourceListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_resourceList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1829
            self.resource()
            self.state = 1834
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,187,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1830
                    self.match(Java8Parser.SEMI)
                    self.state = 1831
                    self.resource() 
                self.state = 1836
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,187,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java8Parser.UnannTypeContext,0)


        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java8Parser.VariableDeclaratorIdContext,0)


        def ASSIGN(self):
            return self.getToken(Java8Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java8Parser.VariableModifierContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_resource

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResource" ):
                listener.enterResource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResource" ):
                listener.exitResource(self)




    def resource(self):

        localctx = Java8Parser.ResourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_resource)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1840
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.FINAL or _la==Java8Parser.AT:
                self.state = 1837
                self.variableModifier()
                self.state = 1842
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1843
            self.unannType()
            self.state = 1844
            self.variableDeclaratorId()
            self.state = 1845
            self.match(Java8Parser.ASSIGN)
            self.state = 1846
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryNoNewArray_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.PrimaryNoNewArray_lfno_primaryContext,0)


        def arrayCreationExpression(self):
            return self.getTypedRuleContext(Java8Parser.ArrayCreationExpressionContext,0)


        def primaryNoNewArray_lf_primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.PrimaryNoNewArray_lf_primaryContext)
            else:
                return self.getTypedRuleContext(Java8Parser.PrimaryNoNewArray_lf_primaryContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = Java8Parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_primary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1850
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,189,self._ctx)
            if la_ == 1:
                self.state = 1848
                self.primaryNoNewArray_lfno_primary()
                pass

            elif la_ == 2:
                self.state = 1849
                self.arrayCreationExpression()
                pass


            self.state = 1855
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,190,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1852
                    self.primaryNoNewArray_lf_primary() 
                self.state = 1857
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,190,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryNoNewArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(Java8Parser.LiteralContext,0)


        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def CLASS(self):
            return self.getToken(Java8Parser.CLASS, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.LBRACK)
            else:
                return self.getToken(Java8Parser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.RBRACK)
            else:
                return self.getToken(Java8Parser.RBRACK, i)

        def VOID(self):
            return self.getToken(Java8Parser.VOID, 0)

        def THIS(self):
            return self.getToken(Java8Parser.THIS, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def classInstanceCreationExpression(self):
            return self.getTypedRuleContext(Java8Parser.ClassInstanceCreationExpressionContext,0)


        def fieldAccess(self):
            return self.getTypedRuleContext(Java8Parser.FieldAccessContext,0)


        def arrayAccess(self):
            return self.getTypedRuleContext(Java8Parser.ArrayAccessContext,0)


        def methodInvocation(self):
            return self.getTypedRuleContext(Java8Parser.MethodInvocationContext,0)


        def methodReference(self):
            return self.getTypedRuleContext(Java8Parser.MethodReferenceContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_primaryNoNewArray

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryNoNewArray" ):
                listener.enterPrimaryNoNewArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryNoNewArray" ):
                listener.exitPrimaryNoNewArray(self)




    def primaryNoNewArray(self):

        localctx = Java8Parser.PrimaryNoNewArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_primaryNoNewArray)
        self._la = 0 # Token type
        try:
            self.state = 1887
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,192,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1858
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1859
                self.typeName()
                self.state = 1864
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.LBRACK:
                    self.state = 1860
                    self.match(Java8Parser.LBRACK)
                    self.state = 1861
                    self.match(Java8Parser.RBRACK)
                    self.state = 1866
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1867
                self.match(Java8Parser.DOT)
                self.state = 1868
                self.match(Java8Parser.CLASS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1870
                self.match(Java8Parser.VOID)
                self.state = 1871
                self.match(Java8Parser.DOT)
                self.state = 1872
                self.match(Java8Parser.CLASS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1873
                self.match(Java8Parser.THIS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1874
                self.typeName()
                self.state = 1875
                self.match(Java8Parser.DOT)
                self.state = 1876
                self.match(Java8Parser.THIS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1878
                self.match(Java8Parser.LPAREN)
                self.state = 1879
                self.expression()
                self.state = 1880
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1882
                self.classInstanceCreationExpression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1883
                self.fieldAccess()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1884
                self.arrayAccess()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1885
                self.methodInvocation()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1886
                self.methodReference()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryNoNewArray_lf_arrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Java8Parser.RULE_primaryNoNewArray_lf_arrayAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryNoNewArray_lf_arrayAccess" ):
                listener.enterPrimaryNoNewArray_lf_arrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryNoNewArray_lf_arrayAccess" ):
                listener.exitPrimaryNoNewArray_lf_arrayAccess(self)




    def primaryNoNewArray_lf_arrayAccess(self):

        localctx = Java8Parser.PrimaryNoNewArray_lf_arrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_primaryNoNewArray_lf_arrayAccess)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryNoNewArray_lfno_arrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(Java8Parser.LiteralContext,0)


        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def CLASS(self):
            return self.getToken(Java8Parser.CLASS, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.LBRACK)
            else:
                return self.getToken(Java8Parser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.RBRACK)
            else:
                return self.getToken(Java8Parser.RBRACK, i)

        def VOID(self):
            return self.getToken(Java8Parser.VOID, 0)

        def THIS(self):
            return self.getToken(Java8Parser.THIS, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def classInstanceCreationExpression(self):
            return self.getTypedRuleContext(Java8Parser.ClassInstanceCreationExpressionContext,0)


        def fieldAccess(self):
            return self.getTypedRuleContext(Java8Parser.FieldAccessContext,0)


        def methodInvocation(self):
            return self.getTypedRuleContext(Java8Parser.MethodInvocationContext,0)


        def methodReference(self):
            return self.getTypedRuleContext(Java8Parser.MethodReferenceContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_primaryNoNewArray_lfno_arrayAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryNoNewArray_lfno_arrayAccess" ):
                listener.enterPrimaryNoNewArray_lfno_arrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryNoNewArray_lfno_arrayAccess" ):
                listener.exitPrimaryNoNewArray_lfno_arrayAccess(self)




    def primaryNoNewArray_lfno_arrayAccess(self):

        localctx = Java8Parser.PrimaryNoNewArray_lfno_arrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_primaryNoNewArray_lfno_arrayAccess)
        self._la = 0 # Token type
        try:
            self.state = 1919
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,194,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1891
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1892
                self.typeName()
                self.state = 1897
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.LBRACK:
                    self.state = 1893
                    self.match(Java8Parser.LBRACK)
                    self.state = 1894
                    self.match(Java8Parser.RBRACK)
                    self.state = 1899
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1900
                self.match(Java8Parser.DOT)
                self.state = 1901
                self.match(Java8Parser.CLASS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1903
                self.match(Java8Parser.VOID)
                self.state = 1904
                self.match(Java8Parser.DOT)
                self.state = 1905
                self.match(Java8Parser.CLASS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1906
                self.match(Java8Parser.THIS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1907
                self.typeName()
                self.state = 1908
                self.match(Java8Parser.DOT)
                self.state = 1909
                self.match(Java8Parser.THIS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1911
                self.match(Java8Parser.LPAREN)
                self.state = 1912
                self.expression()
                self.state = 1913
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1915
                self.classInstanceCreationExpression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1916
                self.fieldAccess()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1917
                self.methodInvocation()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1918
                self.methodReference()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryNoNewArray_lf_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classInstanceCreationExpression_lf_primary(self):
            return self.getTypedRuleContext(Java8Parser.ClassInstanceCreationExpression_lf_primaryContext,0)


        def fieldAccess_lf_primary(self):
            return self.getTypedRuleContext(Java8Parser.FieldAccess_lf_primaryContext,0)


        def arrayAccess_lf_primary(self):
            return self.getTypedRuleContext(Java8Parser.ArrayAccess_lf_primaryContext,0)


        def methodInvocation_lf_primary(self):
            return self.getTypedRuleContext(Java8Parser.MethodInvocation_lf_primaryContext,0)


        def methodReference_lf_primary(self):
            return self.getTypedRuleContext(Java8Parser.MethodReference_lf_primaryContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_primaryNoNewArray_lf_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryNoNewArray_lf_primary" ):
                listener.enterPrimaryNoNewArray_lf_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryNoNewArray_lf_primary" ):
                listener.exitPrimaryNoNewArray_lf_primary(self)




    def primaryNoNewArray_lf_primary(self):

        localctx = Java8Parser.PrimaryNoNewArray_lf_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_primaryNoNewArray_lf_primary)
        try:
            self.state = 1926
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,195,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1921
                self.classInstanceCreationExpression_lf_primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1922
                self.fieldAccess_lf_primary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1923
                self.arrayAccess_lf_primary()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1924
                self.methodInvocation_lf_primary()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1925
                self.methodReference_lf_primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Java8Parser.RULE_primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary" ):
                listener.enterPrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary" ):
                listener.exitPrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary(self)




    def primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary(self):

        localctx = Java8Parser.PrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classInstanceCreationExpression_lf_primary(self):
            return self.getTypedRuleContext(Java8Parser.ClassInstanceCreationExpression_lf_primaryContext,0)


        def fieldAccess_lf_primary(self):
            return self.getTypedRuleContext(Java8Parser.FieldAccess_lf_primaryContext,0)


        def methodInvocation_lf_primary(self):
            return self.getTypedRuleContext(Java8Parser.MethodInvocation_lf_primaryContext,0)


        def methodReference_lf_primary(self):
            return self.getTypedRuleContext(Java8Parser.MethodReference_lf_primaryContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary" ):
                listener.enterPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary" ):
                listener.exitPrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary(self)




    def primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary(self):

        localctx = Java8Parser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary)
        try:
            self.state = 1934
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,196,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1930
                self.classInstanceCreationExpression_lf_primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1931
                self.fieldAccess_lf_primary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1932
                self.methodInvocation_lf_primary()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1933
                self.methodReference_lf_primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryNoNewArray_lfno_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(Java8Parser.LiteralContext,0)


        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def CLASS(self):
            return self.getToken(Java8Parser.CLASS, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.LBRACK)
            else:
                return self.getToken(Java8Parser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.RBRACK)
            else:
                return self.getToken(Java8Parser.RBRACK, i)

        def unannPrimitiveType(self):
            return self.getTypedRuleContext(Java8Parser.UnannPrimitiveTypeContext,0)


        def VOID(self):
            return self.getToken(Java8Parser.VOID, 0)

        def THIS(self):
            return self.getToken(Java8Parser.THIS, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def classInstanceCreationExpression_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.ClassInstanceCreationExpression_lfno_primaryContext,0)


        def fieldAccess_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.FieldAccess_lfno_primaryContext,0)


        def arrayAccess_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.ArrayAccess_lfno_primaryContext,0)


        def methodInvocation_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.MethodInvocation_lfno_primaryContext,0)


        def methodReference_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.MethodReference_lfno_primaryContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_primaryNoNewArray_lfno_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryNoNewArray_lfno_primary" ):
                listener.enterPrimaryNoNewArray_lfno_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryNoNewArray_lfno_primary" ):
                listener.exitPrimaryNoNewArray_lfno_primary(self)




    def primaryNoNewArray_lfno_primary(self):

        localctx = Java8Parser.PrimaryNoNewArray_lfno_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_primaryNoNewArray_lfno_primary)
        self._la = 0 # Token type
        try:
            self.state = 1976
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,199,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1936
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1937
                self.typeName()
                self.state = 1942
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.LBRACK:
                    self.state = 1938
                    self.match(Java8Parser.LBRACK)
                    self.state = 1939
                    self.match(Java8Parser.RBRACK)
                    self.state = 1944
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1945
                self.match(Java8Parser.DOT)
                self.state = 1946
                self.match(Java8Parser.CLASS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1948
                self.unannPrimitiveType()
                self.state = 1953
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.LBRACK:
                    self.state = 1949
                    self.match(Java8Parser.LBRACK)
                    self.state = 1950
                    self.match(Java8Parser.RBRACK)
                    self.state = 1955
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1956
                self.match(Java8Parser.DOT)
                self.state = 1957
                self.match(Java8Parser.CLASS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1959
                self.match(Java8Parser.VOID)
                self.state = 1960
                self.match(Java8Parser.DOT)
                self.state = 1961
                self.match(Java8Parser.CLASS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1962
                self.match(Java8Parser.THIS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1963
                self.typeName()
                self.state = 1964
                self.match(Java8Parser.DOT)
                self.state = 1965
                self.match(Java8Parser.THIS)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1967
                self.match(Java8Parser.LPAREN)
                self.state = 1968
                self.expression()
                self.state = 1969
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1971
                self.classInstanceCreationExpression_lfno_primary()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1972
                self.fieldAccess_lfno_primary()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1973
                self.arrayAccess_lfno_primary()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1974
                self.methodInvocation_lfno_primary()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 1975
                self.methodReference_lfno_primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Java8Parser.RULE_primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary" ):
                listener.enterPrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary" ):
                listener.exitPrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary(self)




    def primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary(self):

        localctx = Java8Parser.PrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(Java8Parser.LiteralContext,0)


        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def CLASS(self):
            return self.getToken(Java8Parser.CLASS, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.LBRACK)
            else:
                return self.getToken(Java8Parser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.RBRACK)
            else:
                return self.getToken(Java8Parser.RBRACK, i)

        def unannPrimitiveType(self):
            return self.getTypedRuleContext(Java8Parser.UnannPrimitiveTypeContext,0)


        def VOID(self):
            return self.getToken(Java8Parser.VOID, 0)

        def THIS(self):
            return self.getToken(Java8Parser.THIS, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def classInstanceCreationExpression_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.ClassInstanceCreationExpression_lfno_primaryContext,0)


        def fieldAccess_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.FieldAccess_lfno_primaryContext,0)


        def methodInvocation_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.MethodInvocation_lfno_primaryContext,0)


        def methodReference_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.MethodReference_lfno_primaryContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary" ):
                listener.enterPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary" ):
                listener.exitPrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary(self)




    def primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary(self):

        localctx = Java8Parser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary)
        self._la = 0 # Token type
        try:
            self.state = 2019
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,202,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1980
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1981
                self.typeName()
                self.state = 1986
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.LBRACK:
                    self.state = 1982
                    self.match(Java8Parser.LBRACK)
                    self.state = 1983
                    self.match(Java8Parser.RBRACK)
                    self.state = 1988
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1989
                self.match(Java8Parser.DOT)
                self.state = 1990
                self.match(Java8Parser.CLASS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1992
                self.unannPrimitiveType()
                self.state = 1997
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.LBRACK:
                    self.state = 1993
                    self.match(Java8Parser.LBRACK)
                    self.state = 1994
                    self.match(Java8Parser.RBRACK)
                    self.state = 1999
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2000
                self.match(Java8Parser.DOT)
                self.state = 2001
                self.match(Java8Parser.CLASS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2003
                self.match(Java8Parser.VOID)
                self.state = 2004
                self.match(Java8Parser.DOT)
                self.state = 2005
                self.match(Java8Parser.CLASS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2006
                self.match(Java8Parser.THIS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2007
                self.typeName()
                self.state = 2008
                self.match(Java8Parser.DOT)
                self.state = 2009
                self.match(Java8Parser.THIS)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2011
                self.match(Java8Parser.LPAREN)
                self.state = 2012
                self.expression()
                self.state = 2013
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 2015
                self.classInstanceCreationExpression_lfno_primary()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 2016
                self.fieldAccess_lfno_primary()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 2017
                self.methodInvocation_lfno_primary()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 2018
                self.methodReference_lfno_primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassInstanceCreationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(Java8Parser.NEW, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.Identifier)
            else:
                return self.getToken(Java8Parser.Identifier, i)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.DOT)
            else:
                return self.getToken(Java8Parser.DOT, i)

        def typeArgumentsOrDiamond(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsOrDiamondContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java8Parser.ArgumentListContext,0)


        def classBody(self):
            return self.getTypedRuleContext(Java8Parser.ClassBodyContext,0)


        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def primary(self):
            return self.getTypedRuleContext(Java8Parser.PrimaryContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_classInstanceCreationExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassInstanceCreationExpression" ):
                listener.enterClassInstanceCreationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassInstanceCreationExpression" ):
                listener.exitClassInstanceCreationExpression(self)




    def classInstanceCreationExpression(self):

        localctx = Java8Parser.ClassInstanceCreationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_classInstanceCreationExpression)
        self._la = 0 # Token type
        try:
            self.state = 2104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,220,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2021
                self.match(Java8Parser.NEW)
                self.state = 2023
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2022
                    self.typeArguments()


                self.state = 2028
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 2025
                    self.annotation()
                    self.state = 2030
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2031
                self.match(Java8Parser.Identifier)
                self.state = 2042
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.DOT:
                    self.state = 2032
                    self.match(Java8Parser.DOT)
                    self.state = 2036
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==Java8Parser.AT:
                        self.state = 2033
                        self.annotation()
                        self.state = 2038
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 2039
                    self.match(Java8Parser.Identifier)
                    self.state = 2044
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2046
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2045
                    self.typeArgumentsOrDiamond()


                self.state = 2048
                self.match(Java8Parser.LPAREN)
                self.state = 2050
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2049
                    self.argumentList()


                self.state = 2052
                self.match(Java8Parser.RPAREN)
                self.state = 2054
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LBRACE:
                    self.state = 2053
                    self.classBody()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2056
                self.expressionName()
                self.state = 2057
                self.match(Java8Parser.DOT)
                self.state = 2058
                self.match(Java8Parser.NEW)
                self.state = 2060
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2059
                    self.typeArguments()


                self.state = 2065
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 2062
                    self.annotation()
                    self.state = 2067
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2068
                self.match(Java8Parser.Identifier)
                self.state = 2070
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2069
                    self.typeArgumentsOrDiamond()


                self.state = 2072
                self.match(Java8Parser.LPAREN)
                self.state = 2074
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2073
                    self.argumentList()


                self.state = 2076
                self.match(Java8Parser.RPAREN)
                self.state = 2078
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LBRACE:
                    self.state = 2077
                    self.classBody()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2080
                self.primary()
                self.state = 2081
                self.match(Java8Parser.DOT)
                self.state = 2082
                self.match(Java8Parser.NEW)
                self.state = 2084
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2083
                    self.typeArguments()


                self.state = 2089
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 2086
                    self.annotation()
                    self.state = 2091
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2092
                self.match(Java8Parser.Identifier)
                self.state = 2094
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2093
                    self.typeArgumentsOrDiamond()


                self.state = 2096
                self.match(Java8Parser.LPAREN)
                self.state = 2098
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2097
                    self.argumentList()


                self.state = 2100
                self.match(Java8Parser.RPAREN)
                self.state = 2102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LBRACE:
                    self.state = 2101
                    self.classBody()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassInstanceCreationExpression_lf_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def NEW(self):
            return self.getToken(Java8Parser.NEW, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def typeArgumentsOrDiamond(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsOrDiamondContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java8Parser.ArgumentListContext,0)


        def classBody(self):
            return self.getTypedRuleContext(Java8Parser.ClassBodyContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_classInstanceCreationExpression_lf_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassInstanceCreationExpression_lf_primary" ):
                listener.enterClassInstanceCreationExpression_lf_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassInstanceCreationExpression_lf_primary" ):
                listener.exitClassInstanceCreationExpression_lf_primary(self)




    def classInstanceCreationExpression_lf_primary(self):

        localctx = Java8Parser.ClassInstanceCreationExpression_lf_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_classInstanceCreationExpression_lf_primary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2106
            self.match(Java8Parser.DOT)
            self.state = 2107
            self.match(Java8Parser.NEW)
            self.state = 2109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LT:
                self.state = 2108
                self.typeArguments()


            self.state = 2114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 2111
                self.annotation()
                self.state = 2116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2117
            self.match(Java8Parser.Identifier)
            self.state = 2119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LT:
                self.state = 2118
                self.typeArgumentsOrDiamond()


            self.state = 2121
            self.match(Java8Parser.LPAREN)
            self.state = 2123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                self.state = 2122
                self.argumentList()


            self.state = 2125
            self.match(Java8Parser.RPAREN)
            self.state = 2127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,225,self._ctx)
            if la_ == 1:
                self.state = 2126
                self.classBody()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassInstanceCreationExpression_lfno_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(Java8Parser.NEW, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.Identifier)
            else:
                return self.getToken(Java8Parser.Identifier, i)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.DOT)
            else:
                return self.getToken(Java8Parser.DOT, i)

        def typeArgumentsOrDiamond(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsOrDiamondContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java8Parser.ArgumentListContext,0)


        def classBody(self):
            return self.getTypedRuleContext(Java8Parser.ClassBodyContext,0)


        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_classInstanceCreationExpression_lfno_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassInstanceCreationExpression_lfno_primary" ):
                listener.enterClassInstanceCreationExpression_lfno_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassInstanceCreationExpression_lfno_primary" ):
                listener.exitClassInstanceCreationExpression_lfno_primary(self)




    def classInstanceCreationExpression_lfno_primary(self):

        localctx = Java8Parser.ClassInstanceCreationExpression_lfno_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_classInstanceCreationExpression_lfno_primary)
        self._la = 0 # Token type
        try:
            self.state = 2188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2129
                self.match(Java8Parser.NEW)
                self.state = 2131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2130
                    self.typeArguments()


                self.state = 2136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 2133
                    self.annotation()
                    self.state = 2138
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2139
                self.match(Java8Parser.Identifier)
                self.state = 2150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.DOT:
                    self.state = 2140
                    self.match(Java8Parser.DOT)
                    self.state = 2144
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==Java8Parser.AT:
                        self.state = 2141
                        self.annotation()
                        self.state = 2146
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 2147
                    self.match(Java8Parser.Identifier)
                    self.state = 2152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2153
                    self.typeArgumentsOrDiamond()


                self.state = 2156
                self.match(Java8Parser.LPAREN)
                self.state = 2158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2157
                    self.argumentList()


                self.state = 2160
                self.match(Java8Parser.RPAREN)
                self.state = 2162
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,232,self._ctx)
                if la_ == 1:
                    self.state = 2161
                    self.classBody()


                pass
            elif token in [Java8Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2164
                self.expressionName()
                self.state = 2165
                self.match(Java8Parser.DOT)
                self.state = 2166
                self.match(Java8Parser.NEW)
                self.state = 2168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2167
                    self.typeArguments()


                self.state = 2173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.AT:
                    self.state = 2170
                    self.annotation()
                    self.state = 2175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2176
                self.match(Java8Parser.Identifier)
                self.state = 2178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2177
                    self.typeArgumentsOrDiamond()


                self.state = 2180
                self.match(Java8Parser.LPAREN)
                self.state = 2182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2181
                    self.argumentList()


                self.state = 2184
                self.match(Java8Parser.RPAREN)
                self.state = 2186
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,237,self._ctx)
                if la_ == 1:
                    self.state = 2185
                    self.classBody()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeArgumentsOrDiamondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def LT(self):
            return self.getToken(Java8Parser.LT, 0)

        def GT(self):
            return self.getToken(Java8Parser.GT, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_typeArgumentsOrDiamond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeArgumentsOrDiamond" ):
                listener.enterTypeArgumentsOrDiamond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeArgumentsOrDiamond" ):
                listener.exitTypeArgumentsOrDiamond(self)




    def typeArgumentsOrDiamond(self):

        localctx = Java8Parser.TypeArgumentsOrDiamondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_typeArgumentsOrDiamond)
        try:
            self.state = 2193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,239,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2190
                self.typeArguments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2191
                self.match(Java8Parser.LT)
                self.state = 2192
                self.match(Java8Parser.GT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(Java8Parser.PrimaryContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.DOT)
            else:
                return self.getToken(Java8Parser.DOT, i)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def SUPER(self):
            return self.getToken(Java8Parser.SUPER, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_fieldAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldAccess" ):
                listener.enterFieldAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldAccess" ):
                listener.exitFieldAccess(self)




    def fieldAccess(self):

        localctx = Java8Parser.FieldAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_fieldAccess)
        try:
            self.state = 2208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,240,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2195
                self.primary()
                self.state = 2196
                self.match(Java8Parser.DOT)
                self.state = 2197
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2199
                self.match(Java8Parser.SUPER)
                self.state = 2200
                self.match(Java8Parser.DOT)
                self.state = 2201
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2202
                self.typeName()
                self.state = 2203
                self.match(Java8Parser.DOT)
                self.state = 2204
                self.match(Java8Parser.SUPER)
                self.state = 2205
                self.match(Java8Parser.DOT)
                self.state = 2206
                self.match(Java8Parser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldAccess_lf_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_fieldAccess_lf_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldAccess_lf_primary" ):
                listener.enterFieldAccess_lf_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldAccess_lf_primary" ):
                listener.exitFieldAccess_lf_primary(self)




    def fieldAccess_lf_primary(self):

        localctx = Java8Parser.FieldAccess_lf_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_fieldAccess_lf_primary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2210
            self.match(Java8Parser.DOT)
            self.state = 2211
            self.match(Java8Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldAccess_lfno_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUPER(self):
            return self.getToken(Java8Parser.SUPER, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.DOT)
            else:
                return self.getToken(Java8Parser.DOT, i)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_fieldAccess_lfno_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldAccess_lfno_primary" ):
                listener.enterFieldAccess_lfno_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldAccess_lfno_primary" ):
                listener.exitFieldAccess_lfno_primary(self)




    def fieldAccess_lfno_primary(self):

        localctx = Java8Parser.FieldAccess_lfno_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_fieldAccess_lfno_primary)
        try:
            self.state = 2222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.SUPER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2213
                self.match(Java8Parser.SUPER)
                self.state = 2214
                self.match(Java8Parser.DOT)
                self.state = 2215
                self.match(Java8Parser.Identifier)
                pass
            elif token in [Java8Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2216
                self.typeName()
                self.state = 2217
                self.match(Java8Parser.DOT)
                self.state = 2218
                self.match(Java8Parser.SUPER)
                self.state = 2219
                self.match(Java8Parser.DOT)
                self.state = 2220
                self.match(Java8Parser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.LBRACK)
            else:
                return self.getToken(Java8Parser.LBRACK, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ExpressionContext,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.RBRACK)
            else:
                return self.getToken(Java8Parser.RBRACK, i)

        def primaryNoNewArray_lfno_arrayAccess(self):
            return self.getTypedRuleContext(Java8Parser.PrimaryNoNewArray_lfno_arrayAccessContext,0)


        def primaryNoNewArray_lf_arrayAccess(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.PrimaryNoNewArray_lf_arrayAccessContext)
            else:
                return self.getTypedRuleContext(Java8Parser.PrimaryNoNewArray_lf_arrayAccessContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_arrayAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess" ):
                listener.enterArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess" ):
                listener.exitArrayAccess(self)




    def arrayAccess(self):

        localctx = Java8Parser.ArrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_arrayAccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,242,self._ctx)
            if la_ == 1:
                self.state = 2224
                self.expressionName()
                self.state = 2225
                self.match(Java8Parser.LBRACK)
                self.state = 2226
                self.expression()
                self.state = 2227
                self.match(Java8Parser.RBRACK)
                pass

            elif la_ == 2:
                self.state = 2229
                self.primaryNoNewArray_lfno_arrayAccess()
                self.state = 2230
                self.match(Java8Parser.LBRACK)
                self.state = 2231
                self.expression()
                self.state = 2232
                self.match(Java8Parser.RBRACK)
                pass


            self.state = 2243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.LBRACK:
                self.state = 2236
                self.primaryNoNewArray_lf_arrayAccess()
                self.state = 2237
                self.match(Java8Parser.LBRACK)
                self.state = 2238
                self.expression()
                self.state = 2239
                self.match(Java8Parser.RBRACK)
                self.state = 2245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccess_lf_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary(self):
            return self.getTypedRuleContext(Java8Parser.PrimaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primaryContext,0)


        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.LBRACK)
            else:
                return self.getToken(Java8Parser.LBRACK, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ExpressionContext,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.RBRACK)
            else:
                return self.getToken(Java8Parser.RBRACK, i)

        def primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.PrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primaryContext)
            else:
                return self.getTypedRuleContext(Java8Parser.PrimaryNoNewArray_lf_primary_lf_arrayAccess_lf_primaryContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_arrayAccess_lf_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess_lf_primary" ):
                listener.enterArrayAccess_lf_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess_lf_primary" ):
                listener.exitArrayAccess_lf_primary(self)




    def arrayAccess_lf_primary(self):

        localctx = Java8Parser.ArrayAccess_lf_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_arrayAccess_lf_primary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2246
            self.primaryNoNewArray_lf_primary_lfno_arrayAccess_lf_primary()
            self.state = 2247
            self.match(Java8Parser.LBRACK)
            self.state = 2248
            self.expression()
            self.state = 2249
            self.match(Java8Parser.RBRACK)
            self.state = 2258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,244,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2251
                    self.primaryNoNewArray_lf_primary_lf_arrayAccess_lf_primary()
                    self.state = 2252
                    self.match(Java8Parser.LBRACK)
                    self.state = 2253
                    self.expression()
                    self.state = 2254
                    self.match(Java8Parser.RBRACK) 
                self.state = 2260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,244,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccess_lfno_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.LBRACK)
            else:
                return self.getToken(Java8Parser.LBRACK, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ExpressionContext,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.RBRACK)
            else:
                return self.getToken(Java8Parser.RBRACK, i)

        def primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary(self):
            return self.getTypedRuleContext(Java8Parser.PrimaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primaryContext,0)


        def primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.PrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primaryContext)
            else:
                return self.getTypedRuleContext(Java8Parser.PrimaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primaryContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_arrayAccess_lfno_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess_lfno_primary" ):
                listener.enterArrayAccess_lfno_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess_lfno_primary" ):
                listener.exitArrayAccess_lfno_primary(self)




    def arrayAccess_lfno_primary(self):

        localctx = Java8Parser.ArrayAccess_lfno_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_arrayAccess_lfno_primary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,245,self._ctx)
            if la_ == 1:
                self.state = 2261
                self.expressionName()
                self.state = 2262
                self.match(Java8Parser.LBRACK)
                self.state = 2263
                self.expression()
                self.state = 2264
                self.match(Java8Parser.RBRACK)
                pass

            elif la_ == 2:
                self.state = 2266
                self.primaryNoNewArray_lfno_primary_lfno_arrayAccess_lfno_primary()
                self.state = 2267
                self.match(Java8Parser.LBRACK)
                self.state = 2268
                self.expression()
                self.state = 2269
                self.match(Java8Parser.RBRACK)
                pass


            self.state = 2280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,246,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2273
                    self.primaryNoNewArray_lfno_primary_lf_arrayAccess_lfno_primary()
                    self.state = 2274
                    self.match(Java8Parser.LBRACK)
                    self.state = 2275
                    self.expression()
                    self.state = 2276
                    self.match(Java8Parser.RBRACK) 
                self.state = 2282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,246,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodName(self):
            return self.getTypedRuleContext(Java8Parser.MethodNameContext,0)


        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(Java8Parser.ArgumentListContext,0)


        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.DOT)
            else:
                return self.getToken(Java8Parser.DOT, i)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def primary(self):
            return self.getTypedRuleContext(Java8Parser.PrimaryContext,0)


        def SUPER(self):
            return self.getToken(Java8Parser.SUPER, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_methodInvocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodInvocation" ):
                listener.enterMethodInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodInvocation" ):
                listener.exitMethodInvocation(self)




    def methodInvocation(self):

        localctx = Java8Parser.MethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_methodInvocation)
        self._la = 0 # Token type
        try:
            self.state = 2351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,258,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2283
                self.methodName()
                self.state = 2284
                self.match(Java8Parser.LPAREN)
                self.state = 2286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2285
                    self.argumentList()


                self.state = 2288
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2290
                self.typeName()
                self.state = 2291
                self.match(Java8Parser.DOT)
                self.state = 2293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2292
                    self.typeArguments()


                self.state = 2295
                self.match(Java8Parser.Identifier)
                self.state = 2296
                self.match(Java8Parser.LPAREN)
                self.state = 2298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2297
                    self.argumentList()


                self.state = 2300
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2302
                self.expressionName()
                self.state = 2303
                self.match(Java8Parser.DOT)
                self.state = 2305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2304
                    self.typeArguments()


                self.state = 2307
                self.match(Java8Parser.Identifier)
                self.state = 2308
                self.match(Java8Parser.LPAREN)
                self.state = 2310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2309
                    self.argumentList()


                self.state = 2312
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2314
                self.primary()
                self.state = 2315
                self.match(Java8Parser.DOT)
                self.state = 2317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2316
                    self.typeArguments()


                self.state = 2319
                self.match(Java8Parser.Identifier)
                self.state = 2320
                self.match(Java8Parser.LPAREN)
                self.state = 2322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2321
                    self.argumentList()


                self.state = 2324
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2326
                self.match(Java8Parser.SUPER)
                self.state = 2327
                self.match(Java8Parser.DOT)
                self.state = 2329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2328
                    self.typeArguments()


                self.state = 2331
                self.match(Java8Parser.Identifier)
                self.state = 2332
                self.match(Java8Parser.LPAREN)
                self.state = 2334
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2333
                    self.argumentList()


                self.state = 2336
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2337
                self.typeName()
                self.state = 2338
                self.match(Java8Parser.DOT)
                self.state = 2339
                self.match(Java8Parser.SUPER)
                self.state = 2340
                self.match(Java8Parser.DOT)
                self.state = 2342
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2341
                    self.typeArguments()


                self.state = 2344
                self.match(Java8Parser.Identifier)
                self.state = 2345
                self.match(Java8Parser.LPAREN)
                self.state = 2347
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2346
                    self.argumentList()


                self.state = 2349
                self.match(Java8Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvocation_lf_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java8Parser.ArgumentListContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_methodInvocation_lf_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodInvocation_lf_primary" ):
                listener.enterMethodInvocation_lf_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodInvocation_lf_primary" ):
                listener.exitMethodInvocation_lf_primary(self)




    def methodInvocation_lf_primary(self):

        localctx = Java8Parser.MethodInvocation_lf_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_methodInvocation_lf_primary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2353
            self.match(Java8Parser.DOT)
            self.state = 2355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LT:
                self.state = 2354
                self.typeArguments()


            self.state = 2357
            self.match(Java8Parser.Identifier)
            self.state = 2358
            self.match(Java8Parser.LPAREN)
            self.state = 2360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                self.state = 2359
                self.argumentList()


            self.state = 2362
            self.match(Java8Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvocation_lfno_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodName(self):
            return self.getTypedRuleContext(Java8Parser.MethodNameContext,0)


        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(Java8Parser.ArgumentListContext,0)


        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.DOT)
            else:
                return self.getToken(Java8Parser.DOT, i)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def SUPER(self):
            return self.getToken(Java8Parser.SUPER, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_methodInvocation_lfno_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodInvocation_lfno_primary" ):
                listener.enterMethodInvocation_lfno_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodInvocation_lfno_primary" ):
                listener.exitMethodInvocation_lfno_primary(self)




    def methodInvocation_lfno_primary(self):

        localctx = Java8Parser.MethodInvocation_lfno_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_methodInvocation_lfno_primary)
        self._la = 0 # Token type
        try:
            self.state = 2420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,270,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2364
                self.methodName()
                self.state = 2365
                self.match(Java8Parser.LPAREN)
                self.state = 2367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2366
                    self.argumentList()


                self.state = 2369
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2371
                self.typeName()
                self.state = 2372
                self.match(Java8Parser.DOT)
                self.state = 2374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2373
                    self.typeArguments()


                self.state = 2376
                self.match(Java8Parser.Identifier)
                self.state = 2377
                self.match(Java8Parser.LPAREN)
                self.state = 2379
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2378
                    self.argumentList()


                self.state = 2381
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2383
                self.expressionName()
                self.state = 2384
                self.match(Java8Parser.DOT)
                self.state = 2386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2385
                    self.typeArguments()


                self.state = 2388
                self.match(Java8Parser.Identifier)
                self.state = 2389
                self.match(Java8Parser.LPAREN)
                self.state = 2391
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2390
                    self.argumentList()


                self.state = 2393
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2395
                self.match(Java8Parser.SUPER)
                self.state = 2396
                self.match(Java8Parser.DOT)
                self.state = 2398
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2397
                    self.typeArguments()


                self.state = 2400
                self.match(Java8Parser.Identifier)
                self.state = 2401
                self.match(Java8Parser.LPAREN)
                self.state = 2403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2402
                    self.argumentList()


                self.state = 2405
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2406
                self.typeName()
                self.state = 2407
                self.match(Java8Parser.DOT)
                self.state = 2408
                self.match(Java8Parser.SUPER)
                self.state = 2409
                self.match(Java8Parser.DOT)
                self.state = 2411
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2410
                    self.typeArguments()


                self.state = 2413
                self.match(Java8Parser.Identifier)
                self.state = 2414
                self.match(Java8Parser.LPAREN)
                self.state = 2416
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.NEW) | (1 << Java8Parser.SHORT) | (1 << Java8Parser.SUPER) | (1 << Java8Parser.THIS) | (1 << Java8Parser.VOID) | (1 << Java8Parser.IntegerLiteral) | (1 << Java8Parser.FloatingPointLiteral) | (1 << Java8Parser.BooleanLiteral) | (1 << Java8Parser.CharacterLiteral) | (1 << Java8Parser.StringLiteral) | (1 << Java8Parser.NullLiteral) | (1 << Java8Parser.LPAREN))) != 0) or ((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java8Parser.BANG - 69)) | (1 << (Java8Parser.TILDE - 69)) | (1 << (Java8Parser.INC - 69)) | (1 << (Java8Parser.DEC - 69)) | (1 << (Java8Parser.ADD - 69)) | (1 << (Java8Parser.SUB - 69)) | (1 << (Java8Parser.Identifier - 69)) | (1 << (Java8Parser.AT - 69)))) != 0):
                    self.state = 2415
                    self.argumentList()


                self.state = 2418
                self.match(Java8Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Java8Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = Java8Parser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2422
            self.expression()
            self.state = 2427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.COMMA:
                self.state = 2423
                self.match(Java8Parser.COMMA)
                self.state = 2424
                self.expression()
                self.state = 2429
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def COLONCOLON(self):
            return self.getToken(Java8Parser.COLONCOLON, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def referenceType(self):
            return self.getTypedRuleContext(Java8Parser.ReferenceTypeContext,0)


        def primary(self):
            return self.getTypedRuleContext(Java8Parser.PrimaryContext,0)


        def SUPER(self):
            return self.getToken(Java8Parser.SUPER, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def classType(self):
            return self.getTypedRuleContext(Java8Parser.ClassTypeContext,0)


        def NEW(self):
            return self.getToken(Java8Parser.NEW, 0)

        def arrayType(self):
            return self.getTypedRuleContext(Java8Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_methodReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodReference" ):
                listener.enterMethodReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodReference" ):
                listener.exitMethodReference(self)




    def methodReference(self):

        localctx = Java8Parser.MethodReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_methodReference)
        self._la = 0 # Token type
        try:
            self.state = 2477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,278,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2430
                self.expressionName()
                self.state = 2431
                self.match(Java8Parser.COLONCOLON)
                self.state = 2433
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2432
                    self.typeArguments()


                self.state = 2435
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2437
                self.referenceType()
                self.state = 2438
                self.match(Java8Parser.COLONCOLON)
                self.state = 2440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2439
                    self.typeArguments()


                self.state = 2442
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2444
                self.primary()
                self.state = 2445
                self.match(Java8Parser.COLONCOLON)
                self.state = 2447
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2446
                    self.typeArguments()


                self.state = 2449
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2451
                self.match(Java8Parser.SUPER)
                self.state = 2452
                self.match(Java8Parser.COLONCOLON)
                self.state = 2454
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2453
                    self.typeArguments()


                self.state = 2456
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2457
                self.typeName()
                self.state = 2458
                self.match(Java8Parser.DOT)
                self.state = 2459
                self.match(Java8Parser.SUPER)
                self.state = 2460
                self.match(Java8Parser.COLONCOLON)
                self.state = 2462
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2461
                    self.typeArguments()


                self.state = 2464
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2466
                self.classType()
                self.state = 2467
                self.match(Java8Parser.COLONCOLON)
                self.state = 2469
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2468
                    self.typeArguments()


                self.state = 2471
                self.match(Java8Parser.NEW)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2473
                self.arrayType()
                self.state = 2474
                self.match(Java8Parser.COLONCOLON)
                self.state = 2475
                self.match(Java8Parser.NEW)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodReference_lf_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLONCOLON(self):
            return self.getToken(Java8Parser.COLONCOLON, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_methodReference_lf_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodReference_lf_primary" ):
                listener.enterMethodReference_lf_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodReference_lf_primary" ):
                listener.exitMethodReference_lf_primary(self)




    def methodReference_lf_primary(self):

        localctx = Java8Parser.MethodReference_lf_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_methodReference_lf_primary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2479
            self.match(Java8Parser.COLONCOLON)
            self.state = 2481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java8Parser.LT:
                self.state = 2480
                self.typeArguments()


            self.state = 2483
            self.match(Java8Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodReference_lfno_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def COLONCOLON(self):
            return self.getToken(Java8Parser.COLONCOLON, 0)

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java8Parser.TypeArgumentsContext,0)


        def referenceType(self):
            return self.getTypedRuleContext(Java8Parser.ReferenceTypeContext,0)


        def SUPER(self):
            return self.getToken(Java8Parser.SUPER, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java8Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java8Parser.DOT, 0)

        def classType(self):
            return self.getTypedRuleContext(Java8Parser.ClassTypeContext,0)


        def NEW(self):
            return self.getToken(Java8Parser.NEW, 0)

        def arrayType(self):
            return self.getTypedRuleContext(Java8Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_methodReference_lfno_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodReference_lfno_primary" ):
                listener.enterMethodReference_lfno_primary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodReference_lfno_primary" ):
                listener.exitMethodReference_lfno_primary(self)




    def methodReference_lfno_primary(self):

        localctx = Java8Parser.MethodReference_lfno_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_methodReference_lfno_primary)
        self._la = 0 # Token type
        try:
            self.state = 2525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,285,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2485
                self.expressionName()
                self.state = 2486
                self.match(Java8Parser.COLONCOLON)
                self.state = 2488
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2487
                    self.typeArguments()


                self.state = 2490
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2492
                self.referenceType()
                self.state = 2493
                self.match(Java8Parser.COLONCOLON)
                self.state = 2495
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2494
                    self.typeArguments()


                self.state = 2497
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2499
                self.match(Java8Parser.SUPER)
                self.state = 2500
                self.match(Java8Parser.COLONCOLON)
                self.state = 2502
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2501
                    self.typeArguments()


                self.state = 2504
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2505
                self.typeName()
                self.state = 2506
                self.match(Java8Parser.DOT)
                self.state = 2507
                self.match(Java8Parser.SUPER)
                self.state = 2508
                self.match(Java8Parser.COLONCOLON)
                self.state = 2510
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2509
                    self.typeArguments()


                self.state = 2512
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2514
                self.classType()
                self.state = 2515
                self.match(Java8Parser.COLONCOLON)
                self.state = 2517
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java8Parser.LT:
                    self.state = 2516
                    self.typeArguments()


                self.state = 2519
                self.match(Java8Parser.NEW)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2521
                self.arrayType()
                self.state = 2522
                self.match(Java8Parser.COLONCOLON)
                self.state = 2523
                self.match(Java8Parser.NEW)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayCreationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(Java8Parser.NEW, 0)

        def primitiveType(self):
            return self.getTypedRuleContext(Java8Parser.PrimitiveTypeContext,0)


        def dimExprs(self):
            return self.getTypedRuleContext(Java8Parser.DimExprsContext,0)


        def dims(self):
            return self.getTypedRuleContext(Java8Parser.DimsContext,0)


        def classOrInterfaceType(self):
            return self.getTypedRuleContext(Java8Parser.ClassOrInterfaceTypeContext,0)


        def arrayInitializer(self):
            return self.getTypedRuleContext(Java8Parser.ArrayInitializerContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_arrayCreationExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayCreationExpression" ):
                listener.enterArrayCreationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayCreationExpression" ):
                listener.exitArrayCreationExpression(self)




    def arrayCreationExpression(self):

        localctx = Java8Parser.ArrayCreationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_arrayCreationExpression)
        try:
            self.state = 2549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,288,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2527
                self.match(Java8Parser.NEW)
                self.state = 2528
                self.primitiveType()
                self.state = 2529
                self.dimExprs()
                self.state = 2531
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,286,self._ctx)
                if la_ == 1:
                    self.state = 2530
                    self.dims()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2533
                self.match(Java8Parser.NEW)
                self.state = 2534
                self.classOrInterfaceType()
                self.state = 2535
                self.dimExprs()
                self.state = 2537
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,287,self._ctx)
                if la_ == 1:
                    self.state = 2536
                    self.dims()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2539
                self.match(Java8Parser.NEW)
                self.state = 2540
                self.primitiveType()
                self.state = 2541
                self.dims()
                self.state = 2542
                self.arrayInitializer()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2544
                self.match(Java8Parser.NEW)
                self.state = 2545
                self.classOrInterfaceType()
                self.state = 2546
                self.dims()
                self.state = 2547
                self.arrayInitializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.DimExprContext)
            else:
                return self.getTypedRuleContext(Java8Parser.DimExprContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_dimExprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimExprs" ):
                listener.enterDimExprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimExprs" ):
                listener.exitDimExprs(self)




    def dimExprs(self):

        localctx = Java8Parser.DimExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_dimExprs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2551
            self.dimExpr()
            self.state = 2555
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,289,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2552
                    self.dimExpr() 
                self.state = 2557
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,289,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(Java8Parser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(Java8Parser.RBRACK, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_dimExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimExpr" ):
                listener.enterDimExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimExpr" ):
                listener.exitDimExpr(self)




    def dimExpr(self):

        localctx = Java8Parser.DimExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_dimExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2561
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.AT:
                self.state = 2558
                self.annotation()
                self.state = 2563
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2564
            self.match(Java8Parser.LBRACK)
            self.state = 2565
            self.expression()
            self.state = 2566
            self.match(Java8Parser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_constantExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExpression" ):
                listener.enterConstantExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExpression" ):
                listener.exitConstantExpression(self)




    def constantExpression(self):

        localctx = Java8Parser.ConstantExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_constantExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2568
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaExpression(self):
            return self.getTypedRuleContext(Java8Parser.LambdaExpressionContext,0)


        def assignmentExpression(self):
            return self.getTypedRuleContext(Java8Parser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = Java8Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_expression)
        try:
            self.state = 2572
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,291,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2570
                self.lambdaExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2571
                self.assignmentExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaParameters(self):
            return self.getTypedRuleContext(Java8Parser.LambdaParametersContext,0)


        def ARROW(self):
            return self.getToken(Java8Parser.ARROW, 0)

        def lambdaBody(self):
            return self.getTypedRuleContext(Java8Parser.LambdaBodyContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_lambdaExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExpression" ):
                listener.enterLambdaExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExpression" ):
                listener.exitLambdaExpression(self)




    def lambdaExpression(self):

        localctx = Java8Parser.LambdaExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_lambdaExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2574
            self.lambdaParameters()
            self.state = 2575
            self.match(Java8Parser.ARROW)
            self.state = 2576
            self.lambdaBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java8Parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(Java8Parser.FormalParameterListContext,0)


        def inferredFormalParameterList(self):
            return self.getTypedRuleContext(Java8Parser.InferredFormalParameterListContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_lambdaParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaParameters" ):
                listener.enterLambdaParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaParameters" ):
                listener.exitLambdaParameters(self)




    def lambdaParameters(self):

        localctx = Java8Parser.LambdaParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_lambdaParameters)
        self._la = 0 # Token type
        try:
            self.state = 2588
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,293,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2578
                self.match(Java8Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2579
                self.match(Java8Parser.LPAREN)
                self.state = 2581
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java8Parser.BOOLEAN) | (1 << Java8Parser.BYTE) | (1 << Java8Parser.CHAR) | (1 << Java8Parser.DOUBLE) | (1 << Java8Parser.FINAL) | (1 << Java8Parser.FLOAT) | (1 << Java8Parser.INT) | (1 << Java8Parser.LONG) | (1 << Java8Parser.SHORT))) != 0) or _la==Java8Parser.Identifier or _la==Java8Parser.AT:
                    self.state = 2580
                    self.formalParameterList()


                self.state = 2583
                self.match(Java8Parser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2584
                self.match(Java8Parser.LPAREN)
                self.state = 2585
                self.inferredFormalParameterList()
                self.state = 2586
                self.match(Java8Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InferredFormalParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.Identifier)
            else:
                return self.getToken(Java8Parser.Identifier, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.COMMA)
            else:
                return self.getToken(Java8Parser.COMMA, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_inferredFormalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInferredFormalParameterList" ):
                listener.enterInferredFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInferredFormalParameterList" ):
                listener.exitInferredFormalParameterList(self)




    def inferredFormalParameterList(self):

        localctx = Java8Parser.InferredFormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 418, self.RULE_inferredFormalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2590
            self.match(Java8Parser.Identifier)
            self.state = 2595
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java8Parser.COMMA:
                self.state = 2591
                self.match(Java8Parser.COMMA)
                self.state = 2592
                self.match(Java8Parser.Identifier)
                self.state = 2597
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(Java8Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_lambdaBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaBody" ):
                listener.enterLambdaBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaBody" ):
                listener.exitLambdaBody(self)




    def lambdaBody(self):

        localctx = Java8Parser.LambdaBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_lambdaBody)
        try:
            self.state = 2600
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.BOOLEAN, Java8Parser.BYTE, Java8Parser.CHAR, Java8Parser.DOUBLE, Java8Parser.FLOAT, Java8Parser.INT, Java8Parser.LONG, Java8Parser.NEW, Java8Parser.SHORT, Java8Parser.SUPER, Java8Parser.THIS, Java8Parser.VOID, Java8Parser.IntegerLiteral, Java8Parser.FloatingPointLiteral, Java8Parser.BooleanLiteral, Java8Parser.CharacterLiteral, Java8Parser.StringLiteral, Java8Parser.NullLiteral, Java8Parser.LPAREN, Java8Parser.BANG, Java8Parser.TILDE, Java8Parser.INC, Java8Parser.DEC, Java8Parser.ADD, Java8Parser.SUB, Java8Parser.Identifier, Java8Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2598
                self.expression()
                pass
            elif token in [Java8Parser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2599
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(Java8Parser.ConditionalExpressionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(Java8Parser.AssignmentContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_assignmentExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)




    def assignmentExpression(self):

        localctx = Java8Parser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_assignmentExpression)
        try:
            self.state = 2604
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,296,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2602
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2603
                self.assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def leftHandSide(self):
            return self.getTypedRuleContext(Java8Parser.LeftHandSideContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(Java8Parser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = Java8Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 424, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2606
            self.leftHandSide()
            self.state = 2607
            self.assignmentOperator()
            self.state = 2608
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftHandSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def fieldAccess(self):
            return self.getTypedRuleContext(Java8Parser.FieldAccessContext,0)


        def arrayAccess(self):
            return self.getTypedRuleContext(Java8Parser.ArrayAccessContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_leftHandSide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeftHandSide" ):
                listener.enterLeftHandSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeftHandSide" ):
                listener.exitLeftHandSide(self)




    def leftHandSide(self):

        localctx = Java8Parser.LeftHandSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_leftHandSide)
        try:
            self.state = 2613
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,297,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2610
                self.expressionName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2611
                self.fieldAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2612
                self.arrayAccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(Java8Parser.ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(Java8Parser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(Java8Parser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(Java8Parser.MOD_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(Java8Parser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(Java8Parser.SUB_ASSIGN, 0)

        def LSHIFT_ASSIGN(self):
            return self.getToken(Java8Parser.LSHIFT_ASSIGN, 0)

        def RSHIFT_ASSIGN(self):
            return self.getToken(Java8Parser.RSHIFT_ASSIGN, 0)

        def URSHIFT_ASSIGN(self):
            return self.getToken(Java8Parser.URSHIFT_ASSIGN, 0)

        def AND_ASSIGN(self):
            return self.getToken(Java8Parser.AND_ASSIGN, 0)

        def XOR_ASSIGN(self):
            return self.getToken(Java8Parser.XOR_ASSIGN, 0)

        def OR_ASSIGN(self):
            return self.getToken(Java8Parser.OR_ASSIGN, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)




    def assignmentOperator(self):

        localctx = Java8Parser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2615
            _la = self._input.LA(1)
            if not(((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (Java8Parser.ASSIGN - 66)) | (1 << (Java8Parser.ADD_ASSIGN - 66)) | (1 << (Java8Parser.SUB_ASSIGN - 66)) | (1 << (Java8Parser.MUL_ASSIGN - 66)) | (1 << (Java8Parser.DIV_ASSIGN - 66)) | (1 << (Java8Parser.AND_ASSIGN - 66)) | (1 << (Java8Parser.OR_ASSIGN - 66)) | (1 << (Java8Parser.XOR_ASSIGN - 66)) | (1 << (Java8Parser.MOD_ASSIGN - 66)) | (1 << (Java8Parser.LSHIFT_ASSIGN - 66)) | (1 << (Java8Parser.RSHIFT_ASSIGN - 66)) | (1 << (Java8Parser.URSHIFT_ASSIGN - 66)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalOrExpression(self):
            return self.getTypedRuleContext(Java8Parser.ConditionalOrExpressionContext,0)


        def QUESTION(self):
            return self.getToken(Java8Parser.QUESTION, 0)

        def expression(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(Java8Parser.COLON, 0)

        def conditionalExpression(self):
            return self.getTypedRuleContext(Java8Parser.ConditionalExpressionContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_conditionalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalExpression" ):
                listener.enterConditionalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalExpression" ):
                listener.exitConditionalExpression(self)




    def conditionalExpression(self):

        localctx = Java8Parser.ConditionalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_conditionalExpression)
        try:
            self.state = 2624
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,298,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2617
                self.conditionalOrExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2618
                self.conditionalOrExpression(0)
                self.state = 2619
                self.match(Java8Parser.QUESTION)
                self.state = 2620
                self.expression()
                self.state = 2621
                self.match(Java8Parser.COLON)
                self.state = 2622
                self.conditionalExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalAndExpression(self):
            return self.getTypedRuleContext(Java8Parser.ConditionalAndExpressionContext,0)


        def conditionalOrExpression(self):
            return self.getTypedRuleContext(Java8Parser.ConditionalOrExpressionContext,0)


        def OR(self):
            return self.getToken(Java8Parser.OR, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_conditionalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalOrExpression" ):
                listener.enterConditionalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalOrExpression" ):
                listener.exitConditionalOrExpression(self)



    def conditionalOrExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.ConditionalOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 432
        self.enterRecursionRule(localctx, 432, self.RULE_conditionalOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2627
            self.conditionalAndExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2634
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,299,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java8Parser.ConditionalOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionalOrExpression)
                    self.state = 2629
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2630
                    self.match(Java8Parser.OR)
                    self.state = 2631
                    self.conditionalAndExpression(0) 
                self.state = 2636
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,299,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inclusiveOrExpression(self):
            return self.getTypedRuleContext(Java8Parser.InclusiveOrExpressionContext,0)


        def conditionalAndExpression(self):
            return self.getTypedRuleContext(Java8Parser.ConditionalAndExpressionContext,0)


        def AND(self):
            return self.getToken(Java8Parser.AND, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_conditionalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalAndExpression" ):
                listener.enterConditionalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalAndExpression" ):
                listener.exitConditionalAndExpression(self)



    def conditionalAndExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.ConditionalAndExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 434
        self.enterRecursionRule(localctx, 434, self.RULE_conditionalAndExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2638
            self.inclusiveOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2645
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,300,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java8Parser.ConditionalAndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionalAndExpression)
                    self.state = 2640
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2641
                    self.match(Java8Parser.AND)
                    self.state = 2642
                    self.inclusiveOrExpression(0) 
                self.state = 2647
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,300,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class InclusiveOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exclusiveOrExpression(self):
            return self.getTypedRuleContext(Java8Parser.ExclusiveOrExpressionContext,0)


        def inclusiveOrExpression(self):
            return self.getTypedRuleContext(Java8Parser.InclusiveOrExpressionContext,0)


        def BITOR(self):
            return self.getToken(Java8Parser.BITOR, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_inclusiveOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclusiveOrExpression" ):
                listener.enterInclusiveOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclusiveOrExpression" ):
                listener.exitInclusiveOrExpression(self)



    def inclusiveOrExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.InclusiveOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 436
        self.enterRecursionRule(localctx, 436, self.RULE_inclusiveOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2649
            self.exclusiveOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2656
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,301,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java8Parser.InclusiveOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_inclusiveOrExpression)
                    self.state = 2651
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2652
                    self.match(Java8Parser.BITOR)
                    self.state = 2653
                    self.exclusiveOrExpression(0) 
                self.state = 2658
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,301,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExclusiveOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpression(self):
            return self.getTypedRuleContext(Java8Parser.AndExpressionContext,0)


        def exclusiveOrExpression(self):
            return self.getTypedRuleContext(Java8Parser.ExclusiveOrExpressionContext,0)


        def CARET(self):
            return self.getToken(Java8Parser.CARET, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_exclusiveOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExclusiveOrExpression" ):
                listener.enterExclusiveOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExclusiveOrExpression" ):
                listener.exitExclusiveOrExpression(self)



    def exclusiveOrExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.ExclusiveOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 438
        self.enterRecursionRule(localctx, 438, self.RULE_exclusiveOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2660
            self.andExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2667
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,302,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java8Parser.ExclusiveOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exclusiveOrExpression)
                    self.state = 2662
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2663
                    self.match(Java8Parser.CARET)
                    self.state = 2664
                    self.andExpression(0) 
                self.state = 2669
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,302,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self):
            return self.getTypedRuleContext(Java8Parser.EqualityExpressionContext,0)


        def andExpression(self):
            return self.getTypedRuleContext(Java8Parser.AndExpressionContext,0)


        def BITAND(self):
            return self.getToken(Java8Parser.BITAND, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_andExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)



    def andExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.AndExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 440
        self.enterRecursionRule(localctx, 440, self.RULE_andExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2671
            self.equalityExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2678
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,303,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java8Parser.AndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpression)
                    self.state = 2673
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2674
                    self.match(Java8Parser.BITAND)
                    self.state = 2675
                    self.equalityExpression(0) 
                self.state = 2680
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,303,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self):
            return self.getTypedRuleContext(Java8Parser.RelationalExpressionContext,0)


        def equalityExpression(self):
            return self.getTypedRuleContext(Java8Parser.EqualityExpressionContext,0)


        def EQUAL(self):
            return self.getToken(Java8Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(Java8Parser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)



    def equalityExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.EqualityExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 442
        self.enterRecursionRule(localctx, 442, self.RULE_equalityExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2682
            self.relationalExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2692
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,305,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2690
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,304,self._ctx)
                    if la_ == 1:
                        localctx = Java8Parser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 2684
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 2685
                        self.match(Java8Parser.EQUAL)
                        self.state = 2686
                        self.relationalExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = Java8Parser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 2687
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2688
                        self.match(Java8Parser.NOTEQUAL)
                        self.state = 2689
                        self.relationalExpression(0)
                        pass

             
                self.state = 2694
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,305,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shiftExpression(self):
            return self.getTypedRuleContext(Java8Parser.ShiftExpressionContext,0)


        def relationalExpression(self):
            return self.getTypedRuleContext(Java8Parser.RelationalExpressionContext,0)


        def LT(self):
            return self.getToken(Java8Parser.LT, 0)

        def GT(self):
            return self.getToken(Java8Parser.GT, 0)

        def LE(self):
            return self.getToken(Java8Parser.LE, 0)

        def GE(self):
            return self.getToken(Java8Parser.GE, 0)

        def INSTANCEOF(self):
            return self.getToken(Java8Parser.INSTANCEOF, 0)

        def referenceType(self):
            return self.getTypedRuleContext(Java8Parser.ReferenceTypeContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)



    def relationalExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.RelationalExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 444
        self.enterRecursionRule(localctx, 444, self.RULE_relationalExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2696
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2715
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,307,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2713
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,306,self._ctx)
                    if la_ == 1:
                        localctx = Java8Parser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 2698
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 2699
                        self.match(Java8Parser.LT)
                        self.state = 2700
                        self.shiftExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = Java8Parser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 2701
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 2702
                        self.match(Java8Parser.GT)
                        self.state = 2703
                        self.shiftExpression(0)
                        pass

                    elif la_ == 3:
                        localctx = Java8Parser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 2704
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 2705
                        self.match(Java8Parser.LE)
                        self.state = 2706
                        self.shiftExpression(0)
                        pass

                    elif la_ == 4:
                        localctx = Java8Parser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 2707
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 2708
                        self.match(Java8Parser.GE)
                        self.state = 2709
                        self.shiftExpression(0)
                        pass

                    elif la_ == 5:
                        localctx = Java8Parser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 2710
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2711
                        self.match(Java8Parser.INSTANCEOF)
                        self.state = 2712
                        self.referenceType()
                        pass

             
                self.state = 2717
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,307,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ShiftExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(Java8Parser.AdditiveExpressionContext,0)


        def shiftExpression(self):
            return self.getTypedRuleContext(Java8Parser.ShiftExpressionContext,0)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.LT)
            else:
                return self.getToken(Java8Parser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(Java8Parser.GT)
            else:
                return self.getToken(Java8Parser.GT, i)

        def getRuleIndex(self):
            return Java8Parser.RULE_shiftExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShiftExpression" ):
                listener.enterShiftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShiftExpression" ):
                listener.exitShiftExpression(self)



    def shiftExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.ShiftExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 446
        self.enterRecursionRule(localctx, 446, self.RULE_shiftExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2719
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2736
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,309,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2734
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,308,self._ctx)
                    if la_ == 1:
                        localctx = Java8Parser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 2721
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 2722
                        self.match(Java8Parser.LT)
                        self.state = 2723
                        self.match(Java8Parser.LT)
                        self.state = 2724
                        self.additiveExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = Java8Parser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 2725
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 2726
                        self.match(Java8Parser.GT)
                        self.state = 2727
                        self.match(Java8Parser.GT)
                        self.state = 2728
                        self.additiveExpression(0)
                        pass

                    elif la_ == 3:
                        localctx = Java8Parser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 2729
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2730
                        self.match(Java8Parser.GT)
                        self.state = 2731
                        self.match(Java8Parser.GT)
                        self.state = 2732
                        self.match(Java8Parser.GT)
                        self.state = 2733
                        self.additiveExpression(0)
                        pass

             
                self.state = 2738
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,309,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self):
            return self.getTypedRuleContext(Java8Parser.MultiplicativeExpressionContext,0)


        def additiveExpression(self):
            return self.getTypedRuleContext(Java8Parser.AdditiveExpressionContext,0)


        def ADD(self):
            return self.getToken(Java8Parser.ADD, 0)

        def SUB(self):
            return self.getToken(Java8Parser.SUB, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)



    def additiveExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 448
        self.enterRecursionRule(localctx, 448, self.RULE_additiveExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2740
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2750
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,311,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2748
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,310,self._ctx)
                    if la_ == 1:
                        localctx = Java8Parser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 2742
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 2743
                        self.match(Java8Parser.ADD)
                        self.state = 2744
                        self.multiplicativeExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = Java8Parser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 2745
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2746
                        self.match(Java8Parser.SUB)
                        self.state = 2747
                        self.multiplicativeExpression(0)
                        pass

             
                self.state = 2752
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,311,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(Java8Parser.UnaryExpressionContext,0)


        def multiplicativeExpression(self):
            return self.getTypedRuleContext(Java8Parser.MultiplicativeExpressionContext,0)


        def MUL(self):
            return self.getToken(Java8Parser.MUL, 0)

        def DIV(self):
            return self.getToken(Java8Parser.DIV, 0)

        def MOD(self):
            return self.getToken(Java8Parser.MOD, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)



    def multiplicativeExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java8Parser.MultiplicativeExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 450
        self.enterRecursionRule(localctx, 450, self.RULE_multiplicativeExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2754
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2767
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,313,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2765
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,312,self._ctx)
                    if la_ == 1:
                        localctx = Java8Parser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 2756
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 2757
                        self.match(Java8Parser.MUL)
                        self.state = 2758
                        self.unaryExpression()
                        pass

                    elif la_ == 2:
                        localctx = Java8Parser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 2759
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 2760
                        self.match(Java8Parser.DIV)
                        self.state = 2761
                        self.unaryExpression()
                        pass

                    elif la_ == 3:
                        localctx = Java8Parser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 2762
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2763
                        self.match(Java8Parser.MOD)
                        self.state = 2764
                        self.unaryExpression()
                        pass

             
                self.state = 2769
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,313,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preIncrementExpression(self):
            return self.getTypedRuleContext(Java8Parser.PreIncrementExpressionContext,0)


        def preDecrementExpression(self):
            return self.getTypedRuleContext(Java8Parser.PreDecrementExpressionContext,0)


        def ADD(self):
            return self.getToken(Java8Parser.ADD, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Java8Parser.UnaryExpressionContext,0)


        def SUB(self):
            return self.getToken(Java8Parser.SUB, 0)

        def unaryExpressionNotPlusMinus(self):
            return self.getTypedRuleContext(Java8Parser.UnaryExpressionNotPlusMinusContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)




    def unaryExpression(self):

        localctx = Java8Parser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 452, self.RULE_unaryExpression)
        try:
            self.state = 2777
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java8Parser.INC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2770
                self.preIncrementExpression()
                pass
            elif token in [Java8Parser.DEC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2771
                self.preDecrementExpression()
                pass
            elif token in [Java8Parser.ADD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2772
                self.match(Java8Parser.ADD)
                self.state = 2773
                self.unaryExpression()
                pass
            elif token in [Java8Parser.SUB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2774
                self.match(Java8Parser.SUB)
                self.state = 2775
                self.unaryExpression()
                pass
            elif token in [Java8Parser.BOOLEAN, Java8Parser.BYTE, Java8Parser.CHAR, Java8Parser.DOUBLE, Java8Parser.FLOAT, Java8Parser.INT, Java8Parser.LONG, Java8Parser.NEW, Java8Parser.SHORT, Java8Parser.SUPER, Java8Parser.THIS, Java8Parser.VOID, Java8Parser.IntegerLiteral, Java8Parser.FloatingPointLiteral, Java8Parser.BooleanLiteral, Java8Parser.CharacterLiteral, Java8Parser.StringLiteral, Java8Parser.NullLiteral, Java8Parser.LPAREN, Java8Parser.BANG, Java8Parser.TILDE, Java8Parser.Identifier, Java8Parser.AT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2776
                self.unaryExpressionNotPlusMinus()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreIncrementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INC(self):
            return self.getToken(Java8Parser.INC, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Java8Parser.UnaryExpressionContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_preIncrementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreIncrementExpression" ):
                listener.enterPreIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreIncrementExpression" ):
                listener.exitPreIncrementExpression(self)




    def preIncrementExpression(self):

        localctx = Java8Parser.PreIncrementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 454, self.RULE_preIncrementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2779
            self.match(Java8Parser.INC)
            self.state = 2780
            self.unaryExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreDecrementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC(self):
            return self.getToken(Java8Parser.DEC, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Java8Parser.UnaryExpressionContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_preDecrementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreDecrementExpression" ):
                listener.enterPreDecrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreDecrementExpression" ):
                listener.exitPreDecrementExpression(self)




    def preDecrementExpression(self):

        localctx = Java8Parser.PreDecrementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 456, self.RULE_preDecrementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2782
            self.match(Java8Parser.DEC)
            self.state = 2783
            self.unaryExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionNotPlusMinusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(Java8Parser.PostfixExpressionContext,0)


        def TILDE(self):
            return self.getToken(Java8Parser.TILDE, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Java8Parser.UnaryExpressionContext,0)


        def BANG(self):
            return self.getToken(Java8Parser.BANG, 0)

        def castExpression(self):
            return self.getTypedRuleContext(Java8Parser.CastExpressionContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_unaryExpressionNotPlusMinus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpressionNotPlusMinus" ):
                listener.enterUnaryExpressionNotPlusMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpressionNotPlusMinus" ):
                listener.exitUnaryExpressionNotPlusMinus(self)




    def unaryExpressionNotPlusMinus(self):

        localctx = Java8Parser.UnaryExpressionNotPlusMinusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 458, self.RULE_unaryExpressionNotPlusMinus)
        try:
            self.state = 2791
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,315,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2785
                self.postfixExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2786
                self.match(Java8Parser.TILDE)
                self.state = 2787
                self.unaryExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2788
                self.match(Java8Parser.BANG)
                self.state = 2789
                self.unaryExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2790
                self.castExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(Java8Parser.PrimaryContext,0)


        def expressionName(self):
            return self.getTypedRuleContext(Java8Parser.ExpressionNameContext,0)


        def postIncrementExpression_lf_postfixExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.PostIncrementExpression_lf_postfixExpressionContext)
            else:
                return self.getTypedRuleContext(Java8Parser.PostIncrementExpression_lf_postfixExpressionContext,i)


        def postDecrementExpression_lf_postfixExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.PostDecrementExpression_lf_postfixExpressionContext)
            else:
                return self.getTypedRuleContext(Java8Parser.PostDecrementExpression_lf_postfixExpressionContext,i)


        def getRuleIndex(self):
            return Java8Parser.RULE_postfixExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixExpression" ):
                listener.enterPostfixExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixExpression" ):
                listener.exitPostfixExpression(self)




    def postfixExpression(self):

        localctx = Java8Parser.PostfixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 460, self.RULE_postfixExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2795
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,316,self._ctx)
            if la_ == 1:
                self.state = 2793
                self.primary()
                pass

            elif la_ == 2:
                self.state = 2794
                self.expressionName()
                pass


            self.state = 2801
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,318,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2799
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [Java8Parser.INC]:
                        self.state = 2797
                        self.postIncrementExpression_lf_postfixExpression()
                        pass
                    elif token in [Java8Parser.DEC]:
                        self.state = 2798
                        self.postDecrementExpression_lf_postfixExpression()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 2803
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,318,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostIncrementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(Java8Parser.PostfixExpressionContext,0)


        def INC(self):
            return self.getToken(Java8Parser.INC, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_postIncrementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostIncrementExpression" ):
                listener.enterPostIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostIncrementExpression" ):
                listener.exitPostIncrementExpression(self)




    def postIncrementExpression(self):

        localctx = Java8Parser.PostIncrementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 462, self.RULE_postIncrementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2804
            self.postfixExpression()
            self.state = 2805
            self.match(Java8Parser.INC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostIncrementExpression_lf_postfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INC(self):
            return self.getToken(Java8Parser.INC, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_postIncrementExpression_lf_postfixExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostIncrementExpression_lf_postfixExpression" ):
                listener.enterPostIncrementExpression_lf_postfixExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostIncrementExpression_lf_postfixExpression" ):
                listener.exitPostIncrementExpression_lf_postfixExpression(self)




    def postIncrementExpression_lf_postfixExpression(self):

        localctx = Java8Parser.PostIncrementExpression_lf_postfixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 464, self.RULE_postIncrementExpression_lf_postfixExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2807
            self.match(Java8Parser.INC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostDecrementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(Java8Parser.PostfixExpressionContext,0)


        def DEC(self):
            return self.getToken(Java8Parser.DEC, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_postDecrementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostDecrementExpression" ):
                listener.enterPostDecrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostDecrementExpression" ):
                listener.exitPostDecrementExpression(self)




    def postDecrementExpression(self):

        localctx = Java8Parser.PostDecrementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 466, self.RULE_postDecrementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2809
            self.postfixExpression()
            self.state = 2810
            self.match(Java8Parser.DEC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostDecrementExpression_lf_postfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC(self):
            return self.getToken(Java8Parser.DEC, 0)

        def getRuleIndex(self):
            return Java8Parser.RULE_postDecrementExpression_lf_postfixExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostDecrementExpression_lf_postfixExpression" ):
                listener.enterPostDecrementExpression_lf_postfixExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostDecrementExpression_lf_postfixExpression" ):
                listener.exitPostDecrementExpression_lf_postfixExpression(self)




    def postDecrementExpression_lf_postfixExpression(self):

        localctx = Java8Parser.PostDecrementExpression_lf_postfixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 468, self.RULE_postDecrementExpression_lf_postfixExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2812
            self.match(Java8Parser.DEC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Java8Parser.LPAREN, 0)

        def primitiveType(self):
            return self.getTypedRuleContext(Java8Parser.PrimitiveTypeContext,0)


        def RPAREN(self):
            return self.getToken(Java8Parser.RPAREN, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Java8Parser.UnaryExpressionContext,0)


        def referenceType(self):
            return self.getTypedRuleContext(Java8Parser.ReferenceTypeContext,0)


        def unaryExpressionNotPlusMinus(self):
            return self.getTypedRuleContext(Java8Parser.UnaryExpressionNotPlusMinusContext,0)


        def additionalBound(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java8Parser.AdditionalBoundContext)
            else:
                return self.getTypedRuleContext(Java8Parser.AdditionalBoundContext,i)


        def lambdaExpression(self):
            return self.getTypedRuleContext(Java8Parser.LambdaExpressionContext,0)


        def getRuleIndex(self):
            return Java8Parser.RULE_castExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastExpression" ):
                listener.enterCastExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastExpression" ):
                listener.exitCastExpression(self)




    def castExpression(self):

        localctx = Java8Parser.CastExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 470, self.RULE_castExpression)
        self._la = 0 # Token type
        try:
            self.state = 2841
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,321,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2814
                self.match(Java8Parser.LPAREN)
                self.state = 2815
                self.primitiveType()
                self.state = 2816
                self.match(Java8Parser.RPAREN)
                self.state = 2817
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2819
                self.match(Java8Parser.LPAREN)
                self.state = 2820
                self.referenceType()
                self.state = 2824
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.BITAND:
                    self.state = 2821
                    self.additionalBound()
                    self.state = 2826
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2827
                self.match(Java8Parser.RPAREN)
                self.state = 2828
                self.unaryExpressionNotPlusMinus()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2830
                self.match(Java8Parser.LPAREN)
                self.state = 2831
                self.referenceType()
                self.state = 2835
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java8Parser.BITAND:
                    self.state = 2832
                    self.additionalBound()
                    self.state = 2837
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2838
                self.match(Java8Parser.RPAREN)
                self.state = 2839
                self.lambdaExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.packageName_sempred
        self._predicates[27] = self.packageOrTypeName_sempred
        self._predicates[30] = self.ambiguousName_sempred
        self._predicates[216] = self.conditionalOrExpression_sempred
        self._predicates[217] = self.conditionalAndExpression_sempred
        self._predicates[218] = self.inclusiveOrExpression_sempred
        self._predicates[219] = self.exclusiveOrExpression_sempred
        self._predicates[220] = self.andExpression_sempred
        self._predicates[221] = self.equalityExpression_sempred
        self._predicates[222] = self.relationalExpression_sempred
        self._predicates[223] = self.shiftExpression_sempred
        self._predicates[224] = self.additiveExpression_sempred
        self._predicates[225] = self.multiplicativeExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def packageName_sempred(self, localctx:PackageNameContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def packageOrTypeName_sempred(self, localctx:PackageOrTypeNameContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def ambiguousName_sempred(self, localctx:AmbiguousNameContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def conditionalOrExpression_sempred(self, localctx:ConditionalOrExpressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def conditionalAndExpression_sempred(self, localctx:ConditionalAndExpressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def inclusiveOrExpression_sempred(self, localctx:InclusiveOrExpressionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def exclusiveOrExpression_sempred(self, localctx:ExclusiveOrExpressionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def andExpression_sempred(self, localctx:AndExpressionContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def equalityExpression_sempred(self, localctx:EqualityExpressionContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         

    def relationalExpression_sempred(self, localctx:RelationalExpressionContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 1)
         

    def shiftExpression_sempred(self, localctx:ShiftExpressionContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 1)
         

    def additiveExpression_sempred(self, localctx:AdditiveExpressionContext, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         

    def multiplicativeExpression_sempred(self, localctx:MultiplicativeExpressionContext, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 1)
         




