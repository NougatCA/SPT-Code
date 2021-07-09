# Generated from GoParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

if __name__ is not None and "." in __name__:
    from .GoParserBase import GoParserBase
else:
    from GoParserBase import GoParserBase


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3U")
        buf.write("\u03b2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\3\2\3\2\3\2\3\2\3\2")
        buf.write("\7\2\u00ce\n\2\f\2\16\2\u00d1\13\2\3\2\3\2\3\2\5\2\u00d6")
        buf.write("\n\2\3\2\3\2\7\2\u00da\n\2\f\2\16\2\u00dd\13\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u00ea\n\4\f\4")
        buf.write("\16\4\u00ed\13\4\3\4\5\4\u00f0\n\4\3\5\5\5\u00f3\n\5\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\7\5\7\u00fc\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\7\b\u0104\n\b\f\b\16\b\u0107\13\b\3\b\5\b\u010a")
        buf.write("\n\b\3\t\3\t\5\t\u010e\n\t\3\t\3\t\5\t\u0112\n\t\3\n\3")
        buf.write("\n\3\n\7\n\u0117\n\n\f\n\16\n\u011a\13\n\3\13\3\13\3\13")
        buf.write("\7\13\u011f\n\13\f\13\16\13\u0122\13\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\7\f\u012a\n\f\f\f\16\f\u012d\13\f\3\f\5\f\u0130")
        buf.write("\n\f\3\r\3\r\5\r\u0134\n\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u013c\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u0143\n")
        buf.write("\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u014d")
        buf.write("\n\21\f\21\16\21\u0150\13\21\3\21\5\21\u0153\n\21\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u0159\n\22\3\22\3\22\5\22\u015d\n")
        buf.write("\22\3\23\3\23\5\23\u0161\n\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\6\24\u0168\n\24\r\24\16\24\u0169\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u017b\n\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0183")
        buf.write("\n\26\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\5\33\u0193\n\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\5\36\u01a0\n\36")
        buf.write("\3\37\3\37\5\37\u01a4\n\37\3 \3 \5 \u01a8\n \3!\3!\5!")
        buf.write("\u01ac\n!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3%\5%\u01ba")
        buf.write("\n%\3%\3%\3%\3%\3%\5%\u01c1\n%\5%\u01c3\n%\3&\3&\5&\u01c7")
        buf.write("\n&\3\'\3\'\3\'\3\'\5\'\u01cd\n\'\3\'\5\'\u01d0\n\'\3")
        buf.write("\'\3\'\7\'\u01d4\n\'\f\'\16\'\u01d7\13\'\3\'\3\'\3(\3")
        buf.write("(\3(\5(\u01de\n(\3)\3)\3)\5)\u01e3\n)\3*\3*\3*\3*\5*\u01e9")
        buf.write("\n*\3*\3*\3*\7*\u01ee\n*\f*\16*\u01f1\13*\3*\3*\3+\3+")
        buf.write("\5+\u01f7\n+\3+\3+\3+\3+\3+\3+\3,\3,\3,\5,\u0202\n,\3")
        buf.write("-\3-\3-\5-\u0207\n-\3.\3.\5.\u020b\n.\3.\3.\3.\5.\u0210")
        buf.write("\n.\7.\u0212\n.\f.\16.\u0215\13.\3/\3/\3/\7/\u021a\n/")
        buf.write("\f/\16/\u021d\13/\3/\3/\3\60\3\60\3\60\5\60\u0224\n\60")
        buf.write("\3\61\3\61\3\61\5\61\u0229\n\61\3\61\5\61\u022c\n\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\5\62\u0234\n\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\5\63\u023c\n\63\3\63\3\63\3\64\5")
        buf.write("\64\u0241\n\64\3\64\3\64\5\64\u0245\n\64\3\64\3\64\5\64")
        buf.write("\u0249\n\64\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0251\n")
        buf.write("\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\5\67\u025f\n\67\38\38\58\u0263\n8\39\39\39")
        buf.write("\39\39\39\39\39\59\u026d\n9\3:\3:\3:\3:\3:\3;\3;\3<\3")
        buf.write("<\3=\3=\3=\3>\3>\3>\3>\5>\u027f\n>\3>\3>\7>\u0283\n>\f")
        buf.write(">\16>\u0286\13>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3")
        buf.write("A\3A\3A\3A\3A\5A\u0299\nA\3A\3A\3B\3B\3B\3B\3B\3B\3B\5")
        buf.write("B\u02a4\nB\3C\3C\3C\3D\3D\3D\3D\3D\5D\u02ae\nD\3E\3E\5")
        buf.write("E\u02b2\nE\3F\3F\3F\3F\7F\u02b8\nF\fF\16F\u02bb\13F\3")
        buf.write("F\5F\u02be\nF\5F\u02c0\nF\3F\3F\3G\5G\u02c5\nG\3G\5G\u02c8")
        buf.write("\nG\3G\3G\3H\3H\3H\5H\u02cf\nH\3H\3H\3H\3H\3H\3H\3H\3")
        buf.write("H\3H\3H\3H\3H\3H\3H\3H\7H\u02e0\nH\fH\16H\u02e3\13H\3")
        buf.write("I\3I\3I\3I\5I\u02e9\nI\3I\3I\3I\3I\3I\3I\3I\5I\u02f2\n")
        buf.write("I\7I\u02f4\nI\fI\16I\u02f7\13I\3J\3J\3J\5J\u02fc\nJ\3")
        buf.write("K\3K\3K\3K\5K\u0302\nK\3K\3K\3L\3L\3L\3L\3L\3L\5L\u030c")
        buf.write("\nL\3M\3M\3M\5M\u0311\nM\3N\3N\3N\3N\3N\3N\5N\u0319\n")
        buf.write("N\3O\3O\3P\3P\3P\5P\u0320\nP\3Q\3Q\3Q\3Q\3R\3R\3R\3S\3")
        buf.write("S\3S\3S\3S\3S\3S\3S\3S\5S\u0332\nS\3T\3T\3T\5T\u0337\n")
        buf.write("T\5T\u0339\nT\3T\3T\3U\3U\3U\7U\u0340\nU\fU\16U\u0343")
        buf.write("\13U\3V\3V\3V\5V\u0348\nV\3V\3V\3W\3W\3W\5W\u034f\nW\3")
        buf.write("X\3X\5X\u0353\nX\3Y\3Y\3Y\3Y\3Y\7Y\u035a\nY\fY\16Y\u035d")
        buf.write("\13Y\3Y\3Y\3Z\3Z\3Z\3Z\3Z\5Z\u0366\nZ\3Z\5Z\u0369\nZ\3")
        buf.write("[\3[\3\\\5\\\u036e\n\\\3\\\3\\\3]\3]\3]\3]\3^\3^\3^\3")
        buf.write("^\3_\3_\5_\u037c\n_\3_\3_\5_\u0380\n_\3_\5_\u0383\n_\3")
        buf.write("_\3_\3_\3_\3_\5_\u038a\n_\3_\3_\3`\3`\3`\3`\3`\3a\3a\3")
        buf.write("a\3a\3a\5a\u0398\na\5a\u039a\na\3a\5a\u039d\na\3a\5a\u03a0")
        buf.write("\na\5a\u03a2\na\3a\3a\3b\3b\3b\3b\3c\3c\3d\3d\3d\3d\5")
        buf.write("d\u03b0\nd\3d\2\4\u008e\u0090e\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c")
        buf.write("\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae")
        buf.write("\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0")
        buf.write("\u00c2\u00c4\u00c6\2\13\4\2\35\35((\3\2)*\4\2\65:<@\4")
        buf.write("\2\66:?@\4\2\65\65<>\3\2/\64\3\2;A\4\2BEIJ\3\2PQ\2\u03ea")
        buf.write("\2\u00c8\3\2\2\2\4\u00e0\3\2\2\2\6\u00e3\3\2\2\2\b\u00f2")
        buf.write("\3\2\2\2\n\u00f6\3\2\2\2\f\u00fb\3\2\2\2\16\u00fd\3\2")
        buf.write("\2\2\20\u010b\3\2\2\2\22\u0113\3\2\2\2\24\u011b\3\2\2")
        buf.write("\2\26\u0123\3\2\2\2\30\u0131\3\2\2\2\32\u0137\3\2\2\2")
        buf.write("\34\u013d\3\2\2\2\36\u0144\3\2\2\2 \u0146\3\2\2\2\"\u0154")
        buf.write("\3\2\2\2$\u015e\3\2\2\2&\u0167\3\2\2\2(\u017a\3\2\2\2")
        buf.write("*\u0182\3\2\2\2,\u0184\3\2\2\2.\u0186\3\2\2\2\60\u018a")
        buf.write("\3\2\2\2\62\u018d\3\2\2\2\64\u0192\3\2\2\2\66\u0196\3")
        buf.write("\2\2\28\u019a\3\2\2\2:\u019c\3\2\2\2<\u01a1\3\2\2\2>\u01a5")
        buf.write("\3\2\2\2@\u01a9\3\2\2\2B\u01ad\3\2\2\2D\u01b0\3\2\2\2")
        buf.write("F\u01b2\3\2\2\2H\u01b5\3\2\2\2J\u01c6\3\2\2\2L\u01c8\3")
        buf.write("\2\2\2N\u01da\3\2\2\2P\u01e2\3\2\2\2R\u01e4\3\2\2\2T\u01f6")
        buf.write("\3\2\2\2V\u01fe\3\2\2\2X\u0206\3\2\2\2Z\u020a\3\2\2\2")
        buf.write("\\\u0216\3\2\2\2^\u0220\3\2\2\2`\u022b\3\2\2\2b\u0233")
        buf.write("\3\2\2\2d\u0237\3\2\2\2f\u0240\3\2\2\2h\u0250\3\2\2\2")
        buf.write("j\u0255\3\2\2\2l\u025e\3\2\2\2n\u0262\3\2\2\2p\u026c\3")
        buf.write("\2\2\2r\u026e\3\2\2\2t\u0273\3\2\2\2v\u0275\3\2\2\2x\u0277")
        buf.write("\3\2\2\2z\u027a\3\2\2\2|\u0289\3\2\2\2~\u028d\3\2\2\2")
        buf.write("\u0080\u0298\3\2\2\2\u0082\u02a3\3\2\2\2\u0084\u02a5\3")
        buf.write("\2\2\2\u0086\u02ad\3\2\2\2\u0088\u02b1\3\2\2\2\u008a\u02b3")
        buf.write("\3\2\2\2\u008c\u02c4\3\2\2\2\u008e\u02ce\3\2\2\2\u0090")
        buf.write("\u02e8\3\2\2\2\u0092\u02fb\3\2\2\2\u0094\u02fd\3\2\2\2")
        buf.write("\u0096\u030b\3\2\2\2\u0098\u0310\3\2\2\2\u009a\u0318\3")
        buf.write("\2\2\2\u009c\u031a\3\2\2\2\u009e\u031c\3\2\2\2\u00a0\u0321")
        buf.write("\3\2\2\2\u00a2\u0325\3\2\2\2\u00a4\u0331\3\2\2\2\u00a6")
        buf.write("\u0333\3\2\2\2\u00a8\u033c\3\2\2\2\u00aa\u0347\3\2\2\2")
        buf.write("\u00ac\u034e\3\2\2\2\u00ae\u0352\3\2\2\2\u00b0\u0354\3")
        buf.write("\2\2\2\u00b2\u0365\3\2\2\2\u00b4\u036a\3\2\2\2\u00b6\u036d")
        buf.write("\3\2\2\2\u00b8\u0371\3\2\2\2\u00ba\u0375\3\2\2\2\u00bc")
        buf.write("\u0379\3\2\2\2\u00be\u038d\3\2\2\2\u00c0\u0392\3\2\2\2")
        buf.write("\u00c2\u03a5\3\2\2\2\u00c4\u03a9\3\2\2\2\u00c6\u03af\3")
        buf.write("\2\2\2\u00c8\u00c9\5\4\3\2\u00c9\u00cf\5\u00c6d\2\u00ca")
        buf.write("\u00cb\5\6\4\2\u00cb\u00cc\5\u00c6d\2\u00cc\u00ce\3\2")
        buf.write("\2\2\u00cd\u00ca\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00db\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d2\u00d6\5\32\16\2\u00d3\u00d6\5\34")
        buf.write("\17\2\u00d4\u00d6\5\f\7\2\u00d5\u00d2\3\2\2\2\u00d5\u00d3")
        buf.write("\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7")
        buf.write("\u00d8\5\u00c6d\2\u00d8\u00da\3\2\2\2\u00d9\u00d5\3\2")
        buf.write("\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc")
        buf.write("\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write("\u00df\7\2\2\3\u00df\3\3\2\2\2\u00e0\u00e1\7\20\2\2\u00e1")
        buf.write("\u00e2\7\35\2\2\u00e2\5\3\2\2\2\u00e3\u00ef\7\31\2\2\u00e4")
        buf.write("\u00f0\5\b\5\2\u00e5\u00eb\7\36\2\2\u00e6\u00e7\5\b\5")
        buf.write("\2\u00e7\u00e8\5\u00c6d\2\u00e8\u00ea\3\2\2\2\u00e9\u00e6")
        buf.write("\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ee\u00f0\7\37\2\2\u00ef\u00e4\3\2\2\2\u00ef\u00e5")
        buf.write("\3\2\2\2\u00f0\7\3\2\2\2\u00f1\u00f3\t\2\2\2\u00f2\u00f1")
        buf.write("\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4")
        buf.write("\u00f5\5\n\6\2\u00f5\t\3\2\2\2\u00f6\u00f7\5\u00b4[\2")
        buf.write("\u00f7\13\3\2\2\2\u00f8\u00fc\5\16\b\2\u00f9\u00fc\5\26")
        buf.write("\f\2\u00fa\u00fc\5 \21\2\u00fb\u00f8\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\r\3\2\2\2\u00fd\u0109")
        buf.write("\7\22\2\2\u00fe\u010a\5\20\t\2\u00ff\u0105\7\36\2\2\u0100")
        buf.write("\u0101\5\20\t\2\u0101\u0102\5\u00c6d\2\u0102\u0104\3\2")
        buf.write("\2\2\u0103\u0100\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103")
        buf.write("\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108\3\2\2\2\u0107")
        buf.write("\u0105\3\2\2\2\u0108\u010a\7\37\2\2\u0109\u00fe\3\2\2")
        buf.write("\2\u0109\u00ff\3\2\2\2\u010a\17\3\2\2\2\u010b\u0111\5")
        buf.write("\22\n\2\u010c\u010e\5l\67\2\u010d\u010c\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\7$\2\2")
        buf.write("\u0110\u0112\5\24\13\2\u0111\u010d\3\2\2\2\u0111\u0112")
        buf.write("\3\2\2\2\u0112\21\3\2\2\2\u0113\u0118\7\35\2\2\u0114\u0115")
        buf.write("\7%\2\2\u0115\u0117\7\35\2\2\u0116\u0114\3\2\2\2\u0117")
        buf.write("\u011a\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2")
        buf.write("\u0119\23\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u0120\5\u008e")
        buf.write("H\2\u011c\u011d\7%\2\2\u011d\u011f\5\u008eH\2\u011e\u011c")
        buf.write("\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\25\3\2\2\2\u0122\u0120\3\2\2\2\u0123")
        buf.write("\u012f\7\26\2\2\u0124\u0130\5\30\r\2\u0125\u012b\7\36")
        buf.write("\2\2\u0126\u0127\5\30\r\2\u0127\u0128\5\u00c6d\2\u0128")
        buf.write("\u012a\3\2\2\2\u0129\u0126\3\2\2\2\u012a\u012d\3\2\2\2")
        buf.write("\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\3")
        buf.write("\2\2\2\u012d\u012b\3\2\2\2\u012e\u0130\7\37\2\2\u012f")
        buf.write("\u0124\3\2\2\2\u012f\u0125\3\2\2\2\u0130\27\3\2\2\2\u0131")
        buf.write("\u0133\7\35\2\2\u0132\u0134\7$\2\2\u0133\u0132\3\2\2\2")
        buf.write("\u0133\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\5")
        buf.write("l\67\2\u0136\31\3\2\2\2\u0137\u0138\7\5\2\2\u0138\u0139")
        buf.write("\7\35\2\2\u0139\u013b\5\u0086D\2\u013a\u013c\5$\23\2\u013b")
        buf.write("\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c\33\3\2\2\2\u013d")
        buf.write("\u013e\7\5\2\2\u013e\u013f\5\36\20\2\u013f\u0140\7\35")
        buf.write("\2\2\u0140\u0142\5\u0086D\2\u0141\u0143\5$\23\2\u0142")
        buf.write("\u0141\3\2\2\2\u0142\u0143\3\2\2\2\u0143\35\3\2\2\2\u0144")
        buf.write("\u0145\5\u008aF\2\u0145\37\3\2\2\2\u0146\u0152\7\33\2")
        buf.write("\2\u0147\u0153\5\"\22\2\u0148\u014e\7\36\2\2\u0149\u014a")
        buf.write("\5\"\22\2\u014a\u014b\5\u00c6d\2\u014b\u014d\3\2\2\2\u014c")
        buf.write("\u0149\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u014e\3")
        buf.write("\2\2\2\u0151\u0153\7\37\2\2\u0152\u0147\3\2\2\2\u0152")
        buf.write("\u0148\3\2\2\2\u0153!\3\2\2\2\u0154\u015c\5\22\n\2\u0155")
        buf.write("\u0158\5l\67\2\u0156\u0157\7$\2\2\u0157\u0159\5\24\13")
        buf.write("\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015d")
        buf.write("\3\2\2\2\u015a\u015b\7$\2\2\u015b\u015d\5\24\13\2\u015c")
        buf.write("\u0155\3\2\2\2\u015c\u015a\3\2\2\2\u015d#\3\2\2\2\u015e")
        buf.write("\u0160\7 \2\2\u015f\u0161\5&\24\2\u0160\u015f\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\7")
        buf.write("!\2\2\u0163%\3\2\2\2\u0164\u0165\5(\25\2\u0165\u0166\5")
        buf.write("\u00c6d\2\u0166\u0168\3\2\2\2\u0167\u0164\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016a\'\3\2\2\2\u016b\u017b\5\f\7\2\u016c\u017b\5:\36")
        buf.write("\2\u016d\u017b\5*\26\2\u016e\u017b\5j\66\2\u016f\u017b")
        buf.write("\5<\37\2\u0170\u017b\5> \2\u0171\u017b\5@!\2\u0172\u017b")
        buf.write("\5B\"\2\u0173\u017b\5D#\2\u0174\u017b\5$\23\2\u0175\u017b")
        buf.write("\5H%\2\u0176\u017b\5J&\2\u0177\u017b\5\\/\2\u0178\u017b")
        buf.write("\5d\63\2\u0179\u017b\5F$\2\u017a\u016b\3\2\2\2\u017a\u016c")
        buf.write("\3\2\2\2\u017a\u016d\3\2\2\2\u017a\u016e\3\2\2\2\u017a")
        buf.write("\u016f\3\2\2\2\u017a\u0170\3\2\2\2\u017a\u0171\3\2\2\2")
        buf.write("\u017a\u0172\3\2\2\2\u017a\u0173\3\2\2\2\u017a\u0174\3")
        buf.write("\2\2\2\u017a\u0175\3\2\2\2\u017a\u0176\3\2\2\2\u017a\u0177")
        buf.write("\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017b")
        buf.write(")\3\2\2\2\u017c\u0183\5.\30\2\u017d\u0183\5\60\31\2\u017e")
        buf.write("\u0183\5\62\32\2\u017f\u0183\5,\27\2\u0180\u0183\5\66")
        buf.write("\34\2\u0181\u0183\58\35\2\u0182\u017c\3\2\2\2\u0182\u017d")
        buf.write("\3\2\2\2\u0182\u017e\3\2\2\2\u0182\u017f\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183+\3\2\2\2\u0184")
        buf.write("\u0185\5\u008eH\2\u0185-\3\2\2\2\u0186\u0187\5\u008eH")
        buf.write("\2\u0187\u0188\7A\2\2\u0188\u0189\5\u008eH\2\u0189/\3")
        buf.write("\2\2\2\u018a\u018b\5\u008eH\2\u018b\u018c\t\3\2\2\u018c")
        buf.write("\61\3\2\2\2\u018d\u018e\5\24\13\2\u018e\u018f\5\64\33")
        buf.write("\2\u018f\u0190\5\24\13\2\u0190\63\3\2\2\2\u0191\u0193")
        buf.write("\t\4\2\2\u0192\u0191\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0195\7$\2\2\u0195\65\3\2\2\2\u0196")
        buf.write("\u0197\5\22\n\2\u0197\u0198\7+\2\2\u0198\u0199\5\24\13")
        buf.write("\2\u0199\67\3\2\2\2\u019a\u019b\7&\2\2\u019b9\3\2\2\2")
        buf.write("\u019c\u019d\7\35\2\2\u019d\u019f\7\'\2\2\u019e\u01a0")
        buf.write("\5(\25\2\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write(";\3\2\2\2\u01a1\u01a3\7\32\2\2\u01a2\u01a4\5\24\13\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4=\3\2\2\2\u01a5")
        buf.write("\u01a7\7\3\2\2\u01a6\u01a8\7\35\2\2\u01a7\u01a6\3\2\2")
        buf.write("\2\u01a7\u01a8\3\2\2\2\u01a8?\3\2\2\2\u01a9\u01ab\7\27")
        buf.write("\2\2\u01aa\u01ac\7\35\2\2\u01ab\u01aa\3\2\2\2\u01ab\u01ac")
        buf.write("\3\2\2\2\u01acA\3\2\2\2\u01ad\u01ae\7\17\2\2\u01ae\u01af")
        buf.write("\7\35\2\2\u01afC\3\2\2\2\u01b0\u01b1\7\23\2\2\u01b1E\3")
        buf.write("\2\2\2\u01b2\u01b3\7\t\2\2\u01b3\u01b4\5\u008eH\2\u01b4")
        buf.write("G\3\2\2\2\u01b5\u01b9\7\24\2\2\u01b6\u01b7\5*\26\2\u01b7")
        buf.write("\u01b8\7&\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01b6\3\2\2\2")
        buf.write("\u01b9\u01ba\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc\5")
        buf.write("\u008eH\2\u01bc\u01c2\5$\23\2\u01bd\u01c0\7\16\2\2\u01be")
        buf.write("\u01c1\5H%\2\u01bf\u01c1\5$\23\2\u01c0\u01be\3\2\2\2\u01c0")
        buf.write("\u01bf\3\2\2\2\u01c1\u01c3\3\2\2\2\u01c2\u01bd\3\2\2\2")
        buf.write("\u01c2\u01c3\3\2\2\2\u01c3I\3\2\2\2\u01c4\u01c7\5L\'\2")
        buf.write("\u01c5\u01c7\5R*\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2")
        buf.write("\2\2\u01c7K\3\2\2\2\u01c8\u01cc\7\21\2\2\u01c9\u01ca\5")
        buf.write("*\26\2\u01ca\u01cb\7&\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01c9")
        buf.write("\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce")
        buf.write("\u01d0\5\u008eH\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3\2")
        buf.write("\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d5\7 \2\2\u01d2\u01d4")
        buf.write("\5N(\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d8\u01d9\7!\2\2\u01d9M\3\2\2\2\u01da")
        buf.write("\u01db\5P)\2\u01db\u01dd\7\'\2\2\u01dc\u01de\5&\24\2\u01dd")
        buf.write("\u01dc\3\2\2\2\u01dd\u01de\3\2\2\2\u01deO\3\2\2\2\u01df")
        buf.write("\u01e0\7\b\2\2\u01e0\u01e3\5\24\13\2\u01e1\u01e3\7\4\2")
        buf.write("\2\u01e2\u01df\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3Q\3\2")
        buf.write("\2\2\u01e4\u01e8\7\21\2\2\u01e5\u01e6\5*\26\2\u01e6\u01e7")
        buf.write("\7&\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01e5\3\2\2\2\u01e8")
        buf.write("\u01e9\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb\5T+\2\u01eb")
        buf.write("\u01ef\7 \2\2\u01ec\u01ee\5V,\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write("\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01f2\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f3\7")
        buf.write("!\2\2\u01f3S\3\2\2\2\u01f4\u01f5\7\35\2\2\u01f5\u01f7")
        buf.write("\7+\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u01f9\5\u0090I\2\u01f9\u01fa\7(\2")
        buf.write("\2\u01fa\u01fb\7\36\2\2\u01fb\u01fc\7\26\2\2\u01fc\u01fd")
        buf.write("\7\37\2\2\u01fdU\3\2\2\2\u01fe\u01ff\5X-\2\u01ff\u0201")
        buf.write("\7\'\2\2\u0200\u0202\5&\24\2\u0201\u0200\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202W\3\2\2\2\u0203\u0204\7\b\2\2\u0204")
        buf.write("\u0207\5Z.\2\u0205\u0207\7\4\2\2\u0206\u0203\3\2\2\2\u0206")
        buf.write("\u0205\3\2\2\2\u0207Y\3\2\2\2\u0208\u020b\5l\67\2\u0209")
        buf.write("\u020b\7\34\2\2\u020a\u0208\3\2\2\2\u020a\u0209\3\2\2")
        buf.write("\2\u020b\u0213\3\2\2\2\u020c\u020f\7%\2\2\u020d\u0210")
        buf.write("\5l\67\2\u020e\u0210\7\34\2\2\u020f\u020d\3\2\2\2\u020f")
        buf.write("\u020e\3\2\2\2\u0210\u0212\3\2\2\2\u0211\u020c\3\2\2\2")
        buf.write("\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3")
        buf.write("\2\2\2\u0214[\3\2\2\2\u0215\u0213\3\2\2\2\u0216\u0217")
        buf.write("\7\7\2\2\u0217\u021b\7 \2\2\u0218\u021a\5^\60\2\u0219")
        buf.write("\u0218\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2")
        buf.write("\u021b\u021c\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u021b\3")
        buf.write("\2\2\2\u021e\u021f\7!\2\2\u021f]\3\2\2\2\u0220\u0221\5")
        buf.write("`\61\2\u0221\u0223\7\'\2\2\u0222\u0224\5&\24\2\u0223\u0222")
        buf.write("\3\2\2\2\u0223\u0224\3\2\2\2\u0224_\3\2\2\2\u0225\u0228")
        buf.write("\7\b\2\2\u0226\u0229\5.\30\2\u0227\u0229\5b\62\2\u0228")
        buf.write("\u0226\3\2\2\2\u0228\u0227\3\2\2\2\u0229\u022c\3\2\2\2")
        buf.write("\u022a\u022c\7\4\2\2\u022b\u0225\3\2\2\2\u022b\u022a\3")
        buf.write("\2\2\2\u022ca\3\2\2\2\u022d\u022e\5\24\13\2\u022e\u022f")
        buf.write("\7$\2\2\u022f\u0234\3\2\2\2\u0230\u0231\5\22\n\2\u0231")
        buf.write("\u0232\7+\2\2\u0232\u0234\3\2\2\2\u0233\u022d\3\2\2\2")
        buf.write("\u0233\u0230\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235\3")
        buf.write("\2\2\2\u0235\u0236\5\u008eH\2\u0236c\3\2\2\2\u0237\u023b")
        buf.write("\7\30\2\2\u0238\u023c\5\u008eH\2\u0239\u023c\5f\64\2\u023a")
        buf.write("\u023c\5h\65\2\u023b\u0238\3\2\2\2\u023b\u0239\3\2\2\2")
        buf.write("\u023b\u023a\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023d\3")
        buf.write("\2\2\2\u023d\u023e\5$\23\2\u023ee\3\2\2\2\u023f\u0241")
        buf.write("\5*\26\2\u0240\u023f\3\2\2\2\u0240\u0241\3\2\2\2\u0241")
        buf.write("\u0242\3\2\2\2\u0242\u0244\7&\2\2\u0243\u0245\5\u008e")
        buf.write("H\2\u0244\u0243\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0246")
        buf.write("\3\2\2\2\u0246\u0248\7&\2\2\u0247\u0249\5*\26\2\u0248")
        buf.write("\u0247\3\2\2\2\u0248\u0249\3\2\2\2\u0249g\3\2\2\2\u024a")
        buf.write("\u024b\5\24\13\2\u024b\u024c\7$\2\2\u024c\u0251\3\2\2")
        buf.write("\2\u024d\u024e\5\22\n\2\u024e\u024f\7+\2\2\u024f\u0251")
        buf.write("\3\2\2\2\u0250\u024a\3\2\2\2\u0250\u024d\3\2\2\2\u0250")
        buf.write("\u0251\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0253\7\25\2")
        buf.write("\2\u0253\u0254\5\u008eH\2\u0254i\3\2\2\2\u0255\u0256\7")
        buf.write("\n\2\2\u0256\u0257\5\u008eH\2\u0257k\3\2\2\2\u0258\u025f")
        buf.write("\5n8\2\u0259\u025f\5p9\2\u025a\u025b\7\36\2\2\u025b\u025c")
        buf.write("\5l\67\2\u025c\u025d\7\37\2\2\u025d\u025f\3\2\2\2\u025e")
        buf.write("\u0258\3\2\2\2\u025e\u0259\3\2\2\2\u025e\u025a\3\2\2\2")
        buf.write("\u025fm\3\2\2\2\u0260\u0263\5\u00a0Q\2\u0261\u0263\7\35")
        buf.write("\2\2\u0262\u0260\3\2\2\2\u0262\u0261\3\2\2\2\u0263o\3")
        buf.write("\2\2\2\u0264\u026d\5r:\2\u0265\u026d\5\u00b0Y\2\u0266")
        buf.write("\u026d\5x=\2\u0267\u026d\5\u0084C\2\u0268\u026d\5z>\2")
        buf.write("\u0269\u026d\5|?\2\u026a\u026d\5~@\2\u026b\u026d\5\u0080")
        buf.write("A\2\u026c\u0264\3\2\2\2\u026c\u0265\3\2\2\2\u026c\u0266")
        buf.write("\3\2\2\2\u026c\u0267\3\2\2\2\u026c\u0268\3\2\2\2\u026c")
        buf.write("\u0269\3\2\2\2\u026c\u026a\3\2\2\2\u026c\u026b\3\2\2\2")
        buf.write("\u026dq\3\2\2\2\u026e\u026f\7\"\2\2\u026f\u0270\5t;\2")
        buf.write("\u0270\u0271\7#\2\2\u0271\u0272\5v<\2\u0272s\3\2\2\2\u0273")
        buf.write("\u0274\5\u008eH\2\u0274u\3\2\2\2\u0275\u0276\5l\67\2\u0276")
        buf.write("w\3\2\2\2\u0277\u0278\7?\2\2\u0278\u0279\5l\67\2\u0279")
        buf.write("y\3\2\2\2\u027a\u027b\7\6\2\2\u027b\u0284\7 \2\2\u027c")
        buf.write("\u027f\5\u0082B\2\u027d\u027f\5n8\2\u027e\u027c\3\2\2")
        buf.write("\2\u027e\u027d\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0281")
        buf.write("\5\u00c6d\2\u0281\u0283\3\2\2\2\u0282\u027e\3\2\2\2\u0283")
        buf.write("\u0286\3\2\2\2\u0284\u0282\3\2\2\2\u0284\u0285\3\2\2\2")
        buf.write("\u0285\u0287\3\2\2\2\u0286\u0284\3\2\2\2\u0287\u0288\7")
        buf.write("!\2\2\u0288{\3\2\2\2\u0289\u028a\7\"\2\2\u028a\u028b\7")
        buf.write("#\2\2\u028b\u028c\5v<\2\u028c}\3\2\2\2\u028d\u028e\7\13")
        buf.write("\2\2\u028e\u028f\7\"\2\2\u028f\u0290\5l\67\2\u0290\u0291")
        buf.write("\7#\2\2\u0291\u0292\5v<\2\u0292\177\3\2\2\2\u0293\u0299")
        buf.write("\7\r\2\2\u0294\u0295\7\r\2\2\u0295\u0299\7A\2\2\u0296")
        buf.write("\u0297\7A\2\2\u0297\u0299\7\r\2\2\u0298\u0293\3\2\2\2")
        buf.write("\u0298\u0294\3\2\2\2\u0298\u0296\3\2\2\2\u0299\u029a\3")
        buf.write("\2\2\2\u029a\u029b\5v<\2\u029b\u0081\3\2\2\2\u029c\u029d")
        buf.write("\6B\2\2\u029d\u029e\7\35\2\2\u029e\u029f\5\u008aF\2\u029f")
        buf.write("\u02a0\5\u0088E\2\u02a0\u02a4\3\2\2\2\u02a1\u02a2\7\35")
        buf.write("\2\2\u02a2\u02a4\5\u008aF\2\u02a3\u029c\3\2\2\2\u02a3")
        buf.write("\u02a1\3\2\2\2\u02a4\u0083\3\2\2\2\u02a5\u02a6\7\5\2\2")
        buf.write("\u02a6\u02a7\5\u0086D\2\u02a7\u0085\3\2\2\2\u02a8\u02a9")
        buf.write("\6D\3\2\u02a9\u02aa\5\u008aF\2\u02aa\u02ab\5\u0088E\2")
        buf.write("\u02ab\u02ae\3\2\2\2\u02ac\u02ae\5\u008aF\2\u02ad\u02a8")
        buf.write("\3\2\2\2\u02ad\u02ac\3\2\2\2\u02ae\u0087\3\2\2\2\u02af")
        buf.write("\u02b2\5\u008aF\2\u02b0\u02b2\5l\67\2\u02b1\u02af\3\2")
        buf.write("\2\2\u02b1\u02b0\3\2\2\2\u02b2\u0089\3\2\2\2\u02b3\u02bf")
        buf.write("\7\36\2\2\u02b4\u02b9\5\u008cG\2\u02b5\u02b6\7%\2\2\u02b6")
        buf.write("\u02b8\5\u008cG\2\u02b7\u02b5\3\2\2\2\u02b8\u02bb\3\2")
        buf.write("\2\2\u02b9\u02b7\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba\u02bd")
        buf.write("\3\2\2\2\u02bb\u02b9\3\2\2\2\u02bc\u02be\7%\2\2\u02bd")
        buf.write("\u02bc\3\2\2\2\u02bd\u02be\3\2\2\2\u02be\u02c0\3\2\2\2")
        buf.write("\u02bf\u02b4\3\2\2\2\u02bf\u02c0\3\2\2\2\u02c0\u02c1\3")
        buf.write("\2\2\2\u02c1\u02c2\7\37\2\2\u02c2\u008b\3\2\2\2\u02c3")
        buf.write("\u02c5\5\22\n\2\u02c4\u02c3\3\2\2\2\u02c4\u02c5\3\2\2")
        buf.write("\2\u02c5\u02c7\3\2\2\2\u02c6\u02c8\7,\2\2\u02c7\u02c6")
        buf.write("\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9")
        buf.write("\u02ca\5l\67\2\u02ca\u008d\3\2\2\2\u02cb\u02cc\bH\1\2")
        buf.write("\u02cc\u02cf\5\u0090I\2\u02cd\u02cf\5\u0092J\2\u02ce\u02cb")
        buf.write("\3\2\2\2\u02ce\u02cd\3\2\2\2\u02cf\u02e1\3\2\2\2\u02d0")
        buf.write("\u02d1\f\7\2\2\u02d1\u02d2\t\5\2\2\u02d2\u02e0\5\u008e")
        buf.write("H\b\u02d3\u02d4\f\6\2\2\u02d4\u02d5\t\6\2\2\u02d5\u02e0")
        buf.write("\5\u008eH\7\u02d6\u02d7\f\5\2\2\u02d7\u02d8\t\7\2\2\u02d8")
        buf.write("\u02e0\5\u008eH\6\u02d9\u02da\f\4\2\2\u02da\u02db\7.\2")
        buf.write("\2\u02db\u02e0\5\u008eH\5\u02dc\u02dd\f\3\2\2\u02dd\u02de")
        buf.write("\7-\2\2\u02de\u02e0\5\u008eH\4\u02df\u02d0\3\2\2\2\u02df")
        buf.write("\u02d3\3\2\2\2\u02df\u02d6\3\2\2\2\u02df\u02d9\3\2\2\2")
        buf.write("\u02df\u02dc\3\2\2\2\u02e0\u02e3\3\2\2\2\u02e1\u02df\3")
        buf.write("\2\2\2\u02e1\u02e2\3\2\2\2\u02e2\u008f\3\2\2\2\u02e3\u02e1")
        buf.write("\3\2\2\2\u02e4\u02e5\bI\1\2\u02e5\u02e9\5\u0096L\2\u02e6")
        buf.write("\u02e9\5\u0094K\2\u02e7\u02e9\5\u00c2b\2\u02e8\u02e4\3")
        buf.write("\2\2\2\u02e8\u02e6\3\2\2\2\u02e8\u02e7\3\2\2\2\u02e9\u02f5")
        buf.write("\3\2\2\2\u02ea\u02f1\f\3\2\2\u02eb\u02ec\7(\2\2\u02ec")
        buf.write("\u02f2\7\35\2\2\u02ed\u02f2\5\u00ba^\2\u02ee\u02f2\5\u00bc")
        buf.write("_\2\u02ef\u02f2\5\u00be`\2\u02f0\u02f2\5\u00c0a\2\u02f1")
        buf.write("\u02eb\3\2\2\2\u02f1\u02ed\3\2\2\2\u02f1\u02ee\3\2\2\2")
        buf.write("\u02f1\u02ef\3\2\2\2\u02f1\u02f0\3\2\2\2\u02f2\u02f4\3")
        buf.write("\2\2\2\u02f3\u02ea\3\2\2\2\u02f4\u02f7\3\2\2\2\u02f5\u02f3")
        buf.write("\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u0091\3\2\2\2\u02f7")
        buf.write("\u02f5\3\2\2\2\u02f8\u02fc\5\u0090I\2\u02f9\u02fa\t\b")
        buf.write("\2\2\u02fa\u02fc\5\u008eH\2\u02fb\u02f8\3\2\2\2\u02fb")
        buf.write("\u02f9\3\2\2\2\u02fc\u0093\3\2\2\2\u02fd\u02fe\5l\67\2")
        buf.write("\u02fe\u02ff\7\36\2\2\u02ff\u0301\5\u008eH\2\u0300\u0302")
        buf.write("\7%\2\2\u0301\u0300\3\2\2\2\u0301\u0302\3\2\2\2\u0302")
        buf.write("\u0303\3\2\2\2\u0303\u0304\7\37\2\2\u0304\u0095\3\2\2")
        buf.write("\2\u0305\u030c\5\u0098M\2\u0306\u030c\5\u009eP\2\u0307")
        buf.write("\u0308\7\36\2\2\u0308\u0309\5\u008eH\2\u0309\u030a\7\37")
        buf.write("\2\2\u030a\u030c\3\2\2\2\u030b\u0305\3\2\2\2\u030b\u0306")
        buf.write("\3\2\2\2\u030b\u0307\3\2\2\2\u030c\u0097\3\2\2\2\u030d")
        buf.write("\u0311\5\u009aN\2\u030e\u0311\5\u00a2R\2\u030f\u0311\5")
        buf.write("\u00b8]\2\u0310\u030d\3\2\2\2\u0310\u030e\3\2\2\2\u0310")
        buf.write("\u030f\3\2\2\2\u0311\u0099\3\2\2\2\u0312\u0319\7\34\2")
        buf.write("\2\u0313\u0319\5\u009cO\2\u0314\u0319\5\u00b4[\2\u0315")
        buf.write("\u0319\7F\2\2\u0316\u0319\7I\2\2\u0317\u0319\7J\2\2\u0318")
        buf.write("\u0312\3\2\2\2\u0318\u0313\3\2\2\2\u0318\u0314\3\2\2\2")
        buf.write("\u0318\u0315\3\2\2\2\u0318\u0316\3\2\2\2\u0318\u0317\3")
        buf.write("\2\2\2\u0319\u009b\3\2\2\2\u031a\u031b\t\t\2\2\u031b\u009d")
        buf.write("\3\2\2\2\u031c\u031f\7\35\2\2\u031d\u031e\7(\2\2\u031e")
        buf.write("\u0320\7\35\2\2\u031f\u031d\3\2\2\2\u031f\u0320\3\2\2")
        buf.write("\2\u0320\u009f\3\2\2\2\u0321\u0322\7\35\2\2\u0322\u0323")
        buf.write("\7(\2\2\u0323\u0324\7\35\2\2\u0324\u00a1\3\2\2\2\u0325")
        buf.write("\u0326\5\u00a4S\2\u0326\u0327\5\u00a6T\2\u0327\u00a3\3")
        buf.write("\2\2\2\u0328\u0332\5\u00b0Y\2\u0329\u0332\5r:\2\u032a")
        buf.write("\u032b\7\"\2\2\u032b\u032c\7,\2\2\u032c\u032d\7#\2\2\u032d")
        buf.write("\u0332\5v<\2\u032e\u0332\5|?\2\u032f\u0332\5~@\2\u0330")
        buf.write("\u0332\5n8\2\u0331\u0328\3\2\2\2\u0331\u0329\3\2\2\2\u0331")
        buf.write("\u032a\3\2\2\2\u0331\u032e\3\2\2\2\u0331\u032f\3\2\2\2")
        buf.write("\u0331\u0330\3\2\2\2\u0332\u00a5\3\2\2\2\u0333\u0338\7")
        buf.write(" \2\2\u0334\u0336\5\u00a8U\2\u0335\u0337\7%\2\2\u0336")
        buf.write("\u0335\3\2\2\2\u0336\u0337\3\2\2\2\u0337\u0339\3\2\2\2")
        buf.write("\u0338\u0334\3\2\2\2\u0338\u0339\3\2\2\2\u0339\u033a\3")
        buf.write("\2\2\2\u033a\u033b\7!\2\2\u033b\u00a7\3\2\2\2\u033c\u0341")
        buf.write("\5\u00aaV\2\u033d\u033e\7%\2\2\u033e\u0340\5\u00aaV\2")
        buf.write("\u033f\u033d\3\2\2\2\u0340\u0343\3\2\2\2\u0341\u033f\3")
        buf.write("\2\2\2\u0341\u0342\3\2\2\2\u0342\u00a9\3\2\2\2\u0343\u0341")
        buf.write("\3\2\2\2\u0344\u0345\5\u00acW\2\u0345\u0346\7\'\2\2\u0346")
        buf.write("\u0348\3\2\2\2\u0347\u0344\3\2\2\2\u0347\u0348\3\2\2\2")
        buf.write("\u0348\u0349\3\2\2\2\u0349\u034a\5\u00aeX\2\u034a\u00ab")
        buf.write("\3\2\2\2\u034b\u034f\7\35\2\2\u034c\u034f\5\u008eH\2\u034d")
        buf.write("\u034f\5\u00a6T\2\u034e\u034b\3\2\2\2\u034e\u034c\3\2")
        buf.write("\2\2\u034e\u034d\3\2\2\2\u034f\u00ad\3\2\2\2\u0350\u0353")
        buf.write("\5\u008eH\2\u0351\u0353\5\u00a6T\2\u0352\u0350\3\2\2\2")
        buf.write("\u0352\u0351\3\2\2\2\u0353\u00af\3\2\2\2\u0354\u0355\7")
        buf.write("\f\2\2\u0355\u035b\7 \2\2\u0356\u0357\5\u00b2Z\2\u0357")
        buf.write("\u0358\5\u00c6d\2\u0358\u035a\3\2\2\2\u0359\u0356\3\2")
        buf.write("\2\2\u035a\u035d\3\2\2\2\u035b\u0359\3\2\2\2\u035b\u035c")
        buf.write("\3\2\2\2\u035c\u035e\3\2\2\2\u035d\u035b\3\2\2\2\u035e")
        buf.write("\u035f\7!\2\2\u035f\u00b1\3\2\2\2\u0360\u0361\6Z\n\2\u0361")
        buf.write("\u0362\5\22\n\2\u0362\u0363\5l\67\2\u0363\u0366\3\2\2")
        buf.write("\2\u0364\u0366\5\u00b6\\\2\u0365\u0360\3\2\2\2\u0365\u0364")
        buf.write("\3\2\2\2\u0366\u0368\3\2\2\2\u0367\u0369\5\u00b4[\2\u0368")
        buf.write("\u0367\3\2\2\2\u0368\u0369\3\2\2\2\u0369\u00b3\3\2\2\2")
        buf.write("\u036a\u036b\t\n\2\2\u036b\u00b5\3\2\2\2\u036c\u036e\7")
        buf.write("?\2\2\u036d\u036c\3\2\2\2\u036d\u036e\3\2\2\2\u036e\u036f")
        buf.write("\3\2\2\2\u036f\u0370\5n8\2\u0370\u00b7\3\2\2\2\u0371\u0372")
        buf.write("\7\5\2\2\u0372\u0373\5\u0086D\2\u0373\u0374\5$\23\2\u0374")
        buf.write("\u00b9\3\2\2\2\u0375\u0376\7\"\2\2\u0376\u0377\5\u008e")
        buf.write("H\2\u0377\u0378\7#\2\2\u0378\u00bb\3\2\2\2\u0379\u0389")
        buf.write("\7\"\2\2\u037a\u037c\5\u008eH\2\u037b\u037a\3\2\2\2\u037b")
        buf.write("\u037c\3\2\2\2\u037c\u037d\3\2\2\2\u037d\u037f\7\'\2\2")
        buf.write("\u037e\u0380\5\u008eH\2\u037f\u037e\3\2\2\2\u037f\u0380")
        buf.write("\3\2\2\2\u0380\u038a\3\2\2\2\u0381\u0383\5\u008eH\2\u0382")
        buf.write("\u0381\3\2\2\2\u0382\u0383\3\2\2\2\u0383\u0384\3\2\2\2")
        buf.write("\u0384\u0385\7\'\2\2\u0385\u0386\5\u008eH\2\u0386\u0387")
        buf.write("\7\'\2\2\u0387\u0388\5\u008eH\2\u0388\u038a\3\2\2\2\u0389")
        buf.write("\u037b\3\2\2\2\u0389\u0382\3\2\2\2\u038a\u038b\3\2\2\2")
        buf.write("\u038b\u038c\7#\2\2\u038c\u00bd\3\2\2\2\u038d\u038e\7")
        buf.write("(\2\2\u038e\u038f\7\36\2\2\u038f\u0390\5l\67\2\u0390\u0391")
        buf.write("\7\37\2\2\u0391\u00bf\3\2\2\2\u0392\u03a1\7\36\2\2\u0393")
        buf.write("\u039a\5\24\13\2\u0394\u0397\5l\67\2\u0395\u0396\7%\2")
        buf.write("\2\u0396\u0398\5\24\13\2\u0397\u0395\3\2\2\2\u0397\u0398")
        buf.write("\3\2\2\2\u0398\u039a\3\2\2\2\u0399\u0393\3\2\2\2\u0399")
        buf.write("\u0394\3\2\2\2\u039a\u039c\3\2\2\2\u039b\u039d\7,\2\2")
        buf.write("\u039c\u039b\3\2\2\2\u039c\u039d\3\2\2\2\u039d\u039f\3")
        buf.write("\2\2\2\u039e\u03a0\7%\2\2\u039f\u039e\3\2\2\2\u039f\u03a0")
        buf.write("\3\2\2\2\u03a0\u03a2\3\2\2\2\u03a1\u0399\3\2\2\2\u03a1")
        buf.write("\u03a2\3\2\2\2\u03a2\u03a3\3\2\2\2\u03a3\u03a4\7\37\2")
        buf.write("\2\u03a4\u00c1\3\2\2\2\u03a5\u03a6\5\u00c4c\2\u03a6\u03a7")
        buf.write("\7(\2\2\u03a7\u03a8\7\35\2\2\u03a8\u00c3\3\2\2\2\u03a9")
        buf.write("\u03aa\5l\67\2\u03aa\u00c5\3\2\2\2\u03ab\u03b0\7&\2\2")
        buf.write("\u03ac\u03b0\7\2\2\3\u03ad\u03b0\6d\13\2\u03ae\u03b0\6")
        buf.write("d\f\2\u03af\u03ab\3\2\2\2\u03af\u03ac\3\2\2\2\u03af\u03ad")
        buf.write("\3\2\2\2\u03af\u03ae\3\2\2\2\u03b0\u00c7\3\2\2\2k\u00cf")
        buf.write("\u00d5\u00db\u00eb\u00ef\u00f2\u00fb\u0105\u0109\u010d")
        buf.write("\u0111\u0118\u0120\u012b\u012f\u0133\u013b\u0142\u014e")
        buf.write("\u0152\u0158\u015c\u0160\u0169\u017a\u0182\u0192\u019f")
        buf.write("\u01a3\u01a7\u01ab\u01b9\u01c0\u01c2\u01c6\u01cc\u01cf")
        buf.write("\u01d5\u01dd\u01e2\u01e8\u01ef\u01f6\u0201\u0206\u020a")
        buf.write("\u020f\u0213\u021b\u0223\u0228\u022b\u0233\u023b\u0240")
        buf.write("\u0244\u0248\u0250\u025e\u0262\u026c\u027e\u0284\u0298")
        buf.write("\u02a3\u02ad\u02b1\u02b9\u02bd\u02bf\u02c4\u02c7\u02ce")
        buf.write("\u02df\u02e1\u02e8\u02f1\u02f5\u02fb\u0301\u030b\u0310")
        buf.write("\u0318\u031f\u0331\u0336\u0338\u0341\u0347\u034e\u0352")
        buf.write("\u035b\u0365\u0368\u036d\u037b\u037f\u0382\u0389\u0397")
        buf.write("\u0399\u039c\u039f\u03a1\u03af")
        return buf.getvalue()


class GoParser ( GoParserBase ):

    grammarFileName = "GoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'break'", "'default'", "'func'", "'interface'", 
                     "'select'", "'case'", "'defer'", "'go'", "'map'", "'struct'", 
                     "'chan'", "'else'", "'goto'", "'package'", "'switch'", 
                     "'const'", "'fallthrough'", "'if'", "'range'", "'type'", 
                     "'continue'", "'for'", "'import'", "'return'", "'var'", 
                     "'nil'", "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "'='", "','", "';'", "':'", "'.'", "'++'", "'--'", 
                     "':='", "'...'", "'||'", "'&&'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'|'", "'/'", "'%'", "'<<'", 
                     "'>>'", "'&^'", "'!'", "'+'", "'-'", "'^'", "'*'", 
                     "'&'", "'<-'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "DEFAULT", "FUNC", "INTERFACE", 
                      "SELECT", "CASE", "DEFER", "GO", "MAP", "STRUCT", 
                      "CHAN", "ELSE", "GOTO", "PACKAGE", "SWITCH", "CONST", 
                      "FALLTHROUGH", "IF", "RANGE", "TYPE", "CONTINUE", 
                      "FOR", "IMPORT", "RETURN", "VAR", "NIL_LIT", "IDENTIFIER", 
                      "L_PAREN", "R_PAREN", "L_CURLY", "R_CURLY", "L_BRACKET", 
                      "R_BRACKET", "ASSIGN", "COMMA", "SEMI", "COLON", "DOT", 
                      "PLUS_PLUS", "MINUS_MINUS", "DECLARE_ASSIGN", "ELLIPSIS", 
                      "LOGICAL_OR", "LOGICAL_AND", "EQUALS", "NOT_EQUALS", 
                      "LESS", "LESS_OR_EQUALS", "GREATER", "GREATER_OR_EQUALS", 
                      "OR", "DIV", "MOD", "LSHIFT", "RSHIFT", "BIT_CLEAR", 
                      "EXCLAMATION", "PLUS", "MINUS", "CARET", "STAR", "AMPERSAND", 
                      "RECEIVE", "DECIMAL_LIT", "BINARY_LIT", "OCTAL_LIT", 
                      "HEX_LIT", "FLOAT_LIT", "DECIMAL_FLOAT_LIT", "HEX_FLOAT_LIT", 
                      "IMAGINARY_LIT", "RUNE_LIT", "BYTE_VALUE", "OCTAL_BYTE_VALUE", 
                      "HEX_BYTE_VALUE", "LITTLE_U_VALUE", "BIG_U_VALUE", 
                      "RAW_STRING_LIT", "INTERPRETED_STRING_LIT", "WS", 
                      "COMMENT", "TERMINATOR", "LINE_COMMENT" ]

    RULE_sourceFile = 0
    RULE_packageClause = 1
    RULE_importDecl = 2
    RULE_importSpec = 3
    RULE_importPath = 4
    RULE_declaration = 5
    RULE_constDecl = 6
    RULE_constSpec = 7
    RULE_identifierList = 8
    RULE_expressionList = 9
    RULE_typeDecl = 10
    RULE_typeSpec = 11
    RULE_functionDecl = 12
    RULE_methodDecl = 13
    RULE_receiver = 14
    RULE_varDecl = 15
    RULE_varSpec = 16
    RULE_block = 17
    RULE_statementList = 18
    RULE_statement = 19
    RULE_simpleStmt = 20
    RULE_expressionStmt = 21
    RULE_sendStmt = 22
    RULE_incDecStmt = 23
    RULE_assignment = 24
    RULE_assign_op = 25
    RULE_shortVarDecl = 26
    RULE_emptyStmt = 27
    RULE_labeledStmt = 28
    RULE_returnStmt = 29
    RULE_breakStmt = 30
    RULE_continueStmt = 31
    RULE_gotoStmt = 32
    RULE_fallthroughStmt = 33
    RULE_deferStmt = 34
    RULE_ifStmt = 35
    RULE_switchStmt = 36
    RULE_exprSwitchStmt = 37
    RULE_exprCaseClause = 38
    RULE_exprSwitchCase = 39
    RULE_typeSwitchStmt = 40
    RULE_typeSwitchGuard = 41
    RULE_typeCaseClause = 42
    RULE_typeSwitchCase = 43
    RULE_typeList = 44
    RULE_selectStmt = 45
    RULE_commClause = 46
    RULE_commCase = 47
    RULE_recvStmt = 48
    RULE_forStmt = 49
    RULE_forClause = 50
    RULE_rangeClause = 51
    RULE_goStmt = 52
    RULE_type_ = 53
    RULE_typeName = 54
    RULE_typeLit = 55
    RULE_arrayType = 56
    RULE_arrayLength = 57
    RULE_elementType = 58
    RULE_pointerType = 59
    RULE_interfaceType = 60
    RULE_sliceType = 61
    RULE_mapType = 62
    RULE_channelType = 63
    RULE_methodSpec = 64
    RULE_functionType = 65
    RULE_signature = 66
    RULE_result = 67
    RULE_parameters = 68
    RULE_parameterDecl = 69
    RULE_expression = 70
    RULE_primaryExpr = 71
    RULE_unaryExpr = 72
    RULE_conversion = 73
    RULE_operand = 74
    RULE_literal = 75
    RULE_basicLit = 76
    RULE_integer = 77
    RULE_operandName = 78
    RULE_qualifiedIdent = 79
    RULE_compositeLit = 80
    RULE_literalType = 81
    RULE_literalValue = 82
    RULE_elementList = 83
    RULE_keyedElement = 84
    RULE_key = 85
    RULE_element = 86
    RULE_structType = 87
    RULE_fieldDecl = 88
    RULE_string_ = 89
    RULE_embeddedField = 90
    RULE_functionLit = 91
    RULE_index = 92
    RULE_slice_ = 93
    RULE_typeAssertion = 94
    RULE_arguments = 95
    RULE_methodExpr = 96
    RULE_receiverType = 97
    RULE_eos = 98

    ruleNames =  [ "sourceFile", "packageClause", "importDecl", "importSpec", 
                   "importPath", "declaration", "constDecl", "constSpec", 
                   "identifierList", "expressionList", "typeDecl", "typeSpec", 
                   "functionDecl", "methodDecl", "receiver", "varDecl", 
                   "varSpec", "block", "statementList", "statement", "simpleStmt", 
                   "expressionStmt", "sendStmt", "incDecStmt", "assignment", 
                   "assign_op", "shortVarDecl", "emptyStmt", "labeledStmt", 
                   "returnStmt", "breakStmt", "continueStmt", "gotoStmt", 
                   "fallthroughStmt", "deferStmt", "ifStmt", "switchStmt", 
                   "exprSwitchStmt", "exprCaseClause", "exprSwitchCase", 
                   "typeSwitchStmt", "typeSwitchGuard", "typeCaseClause", 
                   "typeSwitchCase", "typeList", "selectStmt", "commClause", 
                   "commCase", "recvStmt", "forStmt", "forClause", "rangeClause", 
                   "goStmt", "type_", "typeName", "typeLit", "arrayType", 
                   "arrayLength", "elementType", "pointerType", "interfaceType", 
                   "sliceType", "mapType", "channelType", "methodSpec", 
                   "functionType", "signature", "result", "parameters", 
                   "parameterDecl", "expression", "primaryExpr", "unaryExpr", 
                   "conversion", "operand", "literal", "basicLit", "integer", 
                   "operandName", "qualifiedIdent", "compositeLit", "literalType", 
                   "literalValue", "elementList", "keyedElement", "key", 
                   "element", "structType", "fieldDecl", "string_", "embeddedField", 
                   "functionLit", "index", "slice_", "typeAssertion", "arguments", 
                   "methodExpr", "receiverType", "eos" ]

    EOF = Token.EOF
    BREAK=1
    DEFAULT=2
    FUNC=3
    INTERFACE=4
    SELECT=5
    CASE=6
    DEFER=7
    GO=8
    MAP=9
    STRUCT=10
    CHAN=11
    ELSE=12
    GOTO=13
    PACKAGE=14
    SWITCH=15
    CONST=16
    FALLTHROUGH=17
    IF=18
    RANGE=19
    TYPE=20
    CONTINUE=21
    FOR=22
    IMPORT=23
    RETURN=24
    VAR=25
    NIL_LIT=26
    IDENTIFIER=27
    L_PAREN=28
    R_PAREN=29
    L_CURLY=30
    R_CURLY=31
    L_BRACKET=32
    R_BRACKET=33
    ASSIGN=34
    COMMA=35
    SEMI=36
    COLON=37
    DOT=38
    PLUS_PLUS=39
    MINUS_MINUS=40
    DECLARE_ASSIGN=41
    ELLIPSIS=42
    LOGICAL_OR=43
    LOGICAL_AND=44
    EQUALS=45
    NOT_EQUALS=46
    LESS=47
    LESS_OR_EQUALS=48
    GREATER=49
    GREATER_OR_EQUALS=50
    OR=51
    DIV=52
    MOD=53
    LSHIFT=54
    RSHIFT=55
    BIT_CLEAR=56
    EXCLAMATION=57
    PLUS=58
    MINUS=59
    CARET=60
    STAR=61
    AMPERSAND=62
    RECEIVE=63
    DECIMAL_LIT=64
    BINARY_LIT=65
    OCTAL_LIT=66
    HEX_LIT=67
    FLOAT_LIT=68
    DECIMAL_FLOAT_LIT=69
    HEX_FLOAT_LIT=70
    IMAGINARY_LIT=71
    RUNE_LIT=72
    BYTE_VALUE=73
    OCTAL_BYTE_VALUE=74
    HEX_BYTE_VALUE=75
    LITTLE_U_VALUE=76
    BIG_U_VALUE=77
    RAW_STRING_LIT=78
    INTERPRETED_STRING_LIT=79
    WS=80
    COMMENT=81
    TERMINATOR=82
    LINE_COMMENT=83

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SourceFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def packageClause(self):
            return self.getTypedRuleContext(GoParser.PackageClauseContext,0)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def EOF(self):
            return self.getToken(GoParser.EOF, 0)

        def importDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ImportDeclContext)
            else:
                return self.getTypedRuleContext(GoParser.ImportDeclContext,i)


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(GoParser.FunctionDeclContext,i)


        def methodDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.MethodDeclContext)
            else:
                return self.getTypedRuleContext(GoParser.MethodDeclContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(GoParser.DeclarationContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_sourceFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceFile" ):
                listener.enterSourceFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceFile" ):
                listener.exitSourceFile(self)




    def sourceFile(self):

        localctx = GoParser.SourceFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sourceFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.packageClause()
            self.state = 199
            self.eos()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GoParser.IMPORT:
                self.state = 200
                self.importDecl()
                self.state = 201
                self.eos()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.CONST) | (1 << GoParser.TYPE) | (1 << GoParser.VAR))) != 0):
                self.state = 211
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 208
                    self.functionDecl()
                    pass

                elif la_ == 2:
                    self.state = 209
                    self.methodDecl()
                    pass

                elif la_ == 3:
                    self.state = 210
                    self.declaration()
                    pass


                self.state = 213
                self.eos()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 220
            self.match(GoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.packageName = None # Token

        def PACKAGE(self):
            return self.getToken(GoParser.PACKAGE, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_packageClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageClause" ):
                listener.enterPackageClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageClause" ):
                listener.exitPackageClause(self)




    def packageClause(self):

        localctx = GoParser.PackageClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_packageClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(GoParser.PACKAGE)
            self.state = 223
            localctx.packageName = self.match(GoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(GoParser.IMPORT, 0)

        def importSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ImportSpecContext)
            else:
                return self.getTypedRuleContext(GoParser.ImportSpecContext,i)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_importDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDecl" ):
                listener.enterImportDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDecl" ):
                listener.exitImportDecl(self)




    def importDecl(self):

        localctx = GoParser.ImportDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(GoParser.IMPORT)
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER, GoParser.DOT, GoParser.RAW_STRING_LIT, GoParser.INTERPRETED_STRING_LIT]:
                self.state = 226
                self.importSpec()
                pass
            elif token in [GoParser.L_PAREN]:
                self.state = 227
                self.match(GoParser.L_PAREN)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & ((1 << (GoParser.IDENTIFIER - 27)) | (1 << (GoParser.DOT - 27)) | (1 << (GoParser.RAW_STRING_LIT - 27)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 27)))) != 0):
                    self.state = 228
                    self.importSpec()
                    self.state = 229
                    self.eos()
                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 236
                self.match(GoParser.R_PAREN)
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


    class ImportSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.alias = None # Token

        def importPath(self):
            return self.getTypedRuleContext(GoParser.ImportPathContext,0)


        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_importSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportSpec" ):
                listener.enterImportSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportSpec" ):
                listener.exitImportSpec(self)




    def importSpec(self):

        localctx = GoParser.ImportSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_importSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GoParser.IDENTIFIER or _la==GoParser.DOT:
                self.state = 239
                localctx.alias = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==GoParser.IDENTIFIER or _la==GoParser.DOT):
                    localctx.alias = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 242
            self.importPath()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportPathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_(self):
            return self.getTypedRuleContext(GoParser.String_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_importPath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportPath" ):
                listener.enterImportPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportPath" ):
                listener.exitImportPath(self)




    def importPath(self):

        localctx = GoParser.ImportPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_importPath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.string_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constDecl(self):
            return self.getTypedRuleContext(GoParser.ConstDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(GoParser.TypeDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(GoParser.VarDeclContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = GoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration)
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.constDecl()
                pass
            elif token in [GoParser.TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.typeDecl()
                pass
            elif token in [GoParser.VAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.varDecl()
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


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(GoParser.CONST, 0)

        def constSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ConstSpecContext)
            else:
                return self.getTypedRuleContext(GoParser.ConstSpecContext,i)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_constDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstDecl" ):
                listener.enterConstDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstDecl" ):
                listener.exitConstDecl(self)




    def constDecl(self):

        localctx = GoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(GoParser.CONST)
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER]:
                self.state = 252
                self.constSpec()
                pass
            elif token in [GoParser.L_PAREN]:
                self.state = 253
                self.match(GoParser.L_PAREN)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GoParser.IDENTIFIER:
                    self.state = 254
                    self.constSpec()
                    self.state = 255
                    self.eos()
                    self.state = 261
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 262
                self.match(GoParser.R_PAREN)
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


    class ConstSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_constSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstSpec" ):
                listener.enterConstSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstSpec" ):
                listener.exitConstSpec(self)




    def constSpec(self):

        localctx = GoParser.ConstSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.identifierList()
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.STAR) | (1 << GoParser.RECEIVE))) != 0):
                    self.state = 266
                    self.type_()


                self.state = 269
                self.match(GoParser.ASSIGN)
                self.state = 270
                self.expressionList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.IDENTIFIER)
            else:
                return self.getToken(GoParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_identifierList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierList" ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierList" ):
                listener.exitIdentifierList(self)




    def identifierList(self):

        localctx = GoParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifierList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(GoParser.IDENTIFIER)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 274
                    self.match(GoParser.COMMA)
                    self.state = 275
                    self.match(GoParser.IDENTIFIER) 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = GoParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.expression(0)
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 282
                    self.match(GoParser.COMMA)
                    self.state = 283
                    self.expression(0) 
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(GoParser.TYPE, 0)

        def typeSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.TypeSpecContext)
            else:
                return self.getTypedRuleContext(GoParser.TypeSpecContext,i)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_typeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDecl" ):
                listener.enterTypeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDecl" ):
                listener.exitTypeDecl(self)




    def typeDecl(self):

        localctx = GoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(GoParser.TYPE)
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER]:
                self.state = 290
                self.typeSpec()
                pass
            elif token in [GoParser.L_PAREN]:
                self.state = 291
                self.match(GoParser.L_PAREN)
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GoParser.IDENTIFIER:
                    self.state = 292
                    self.typeSpec()
                    self.state = 293
                    self.eos()
                    self.state = 299
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 300
                self.match(GoParser.R_PAREN)
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


    class TypeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_typeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpec" ):
                listener.enterTypeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpec" ):
                listener.exitTypeSpec(self)




    def typeSpec(self):

        localctx = GoParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(GoParser.IDENTIFIER)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GoParser.ASSIGN:
                self.state = 304
                self.match(GoParser.ASSIGN)


            self.state = 307
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(GoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(GoParser.BlockContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)




    def functionDecl(self):

        localctx = GoParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(GoParser.FUNC)
            self.state = 310
            self.match(GoParser.IDENTIFIER)

            self.state = 311
            self.signature()
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 312
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def receiver(self):
            return self.getTypedRuleContext(GoParser.ReceiverContext,0)


        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def signature(self):
            return self.getTypedRuleContext(GoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(GoParser.BlockContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_methodDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDecl" ):
                listener.enterMethodDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDecl" ):
                listener.exitMethodDecl(self)




    def methodDecl(self):

        localctx = GoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methodDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(GoParser.FUNC)
            self.state = 316
            self.receiver()
            self.state = 317
            self.match(GoParser.IDENTIFIER)

            self.state = 318
            self.signature()
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 319
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(GoParser.ParametersContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_receiver

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceiver" ):
                listener.enterReceiver(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceiver" ):
                listener.exitReceiver(self)




    def receiver(self):

        localctx = GoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.parameters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GoParser.VAR, 0)

        def varSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.VarSpecContext)
            else:
                return self.getTypedRuleContext(GoParser.VarSpecContext,i)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = GoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(GoParser.VAR)
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER]:
                self.state = 325
                self.varSpec()
                pass
            elif token in [GoParser.L_PAREN]:
                self.state = 326
                self.match(GoParser.L_PAREN)
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GoParser.IDENTIFIER:
                    self.state = 327
                    self.varSpec()
                    self.state = 328
                    self.eos()
                    self.state = 334
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 335
                self.match(GoParser.R_PAREN)
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


    class VarSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_varSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarSpec" ):
                listener.enterVarSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarSpec" ):
                listener.exitVarSpec(self)




    def varSpec(self):

        localctx = GoParser.VarSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_varSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.identifierList()
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.FUNC, GoParser.INTERFACE, GoParser.MAP, GoParser.STRUCT, GoParser.CHAN, GoParser.IDENTIFIER, GoParser.L_PAREN, GoParser.L_BRACKET, GoParser.STAR, GoParser.RECEIVE]:
                self.state = 339
                self.type_()
                self.state = 342
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 340
                    self.match(GoParser.ASSIGN)
                    self.state = 341
                    self.expressionList()


                pass
            elif token in [GoParser.ASSIGN]:
                self.state = 344
                self.match(GoParser.ASSIGN)
                self.state = 345
                self.expressionList()
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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def statementList(self):
            return self.getTypedRuleContext(GoParser.StatementListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = GoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(GoParser.L_CURLY)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.BREAK) | (1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.SELECT) | (1 << GoParser.DEFER) | (1 << GoParser.GO) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.GOTO) | (1 << GoParser.SWITCH) | (1 << GoParser.CONST) | (1 << GoParser.FALLTHROUGH) | (1 << GoParser.IF) | (1 << GoParser.TYPE) | (1 << GoParser.CONTINUE) | (1 << GoParser.FOR) | (1 << GoParser.RETURN) | (1 << GoParser.VAR) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 349
                self.statementList()


            self.state = 352
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.StatementContext)
            else:
                return self.getTypedRuleContext(GoParser.StatementContext,i)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = GoParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 354
                self.statement()
                self.state = 355
                self.eos()
                self.state = 359 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.BREAK) | (1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.SELECT) | (1 << GoParser.DEFER) | (1 << GoParser.GO) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.GOTO) | (1 << GoParser.SWITCH) | (1 << GoParser.CONST) | (1 << GoParser.FALLTHROUGH) | (1 << GoParser.IF) | (1 << GoParser.TYPE) | (1 << GoParser.CONTINUE) | (1 << GoParser.FOR) | (1 << GoParser.RETURN) | (1 << GoParser.VAR) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0)):
                    break

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

        def declaration(self):
            return self.getTypedRuleContext(GoParser.DeclarationContext,0)


        def labeledStmt(self):
            return self.getTypedRuleContext(GoParser.LabeledStmtContext,0)


        def simpleStmt(self):
            return self.getTypedRuleContext(GoParser.SimpleStmtContext,0)


        def goStmt(self):
            return self.getTypedRuleContext(GoParser.GoStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(GoParser.ReturnStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(GoParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(GoParser.ContinueStmtContext,0)


        def gotoStmt(self):
            return self.getTypedRuleContext(GoParser.GotoStmtContext,0)


        def fallthroughStmt(self):
            return self.getTypedRuleContext(GoParser.FallthroughStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(GoParser.BlockContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(GoParser.IfStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(GoParser.SwitchStmtContext,0)


        def selectStmt(self):
            return self.getTypedRuleContext(GoParser.SelectStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(GoParser.ForStmtContext,0)


        def deferStmt(self):
            return self.getTypedRuleContext(GoParser.DeferStmtContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = GoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.labeledStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363
                self.simpleStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 364
                self.goStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 365
                self.returnStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 366
                self.breakStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 367
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 368
                self.gotoStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 369
                self.fallthroughStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 370
                self.block()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 371
                self.ifStmt()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 372
                self.switchStmt()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 373
                self.selectStmt()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 374
                self.forStmt()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 375
                self.deferStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sendStmt(self):
            return self.getTypedRuleContext(GoParser.SendStmtContext,0)


        def incDecStmt(self):
            return self.getTypedRuleContext(GoParser.IncDecStmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(GoParser.AssignmentContext,0)


        def expressionStmt(self):
            return self.getTypedRuleContext(GoParser.ExpressionStmtContext,0)


        def shortVarDecl(self):
            return self.getTypedRuleContext(GoParser.ShortVarDeclContext,0)


        def emptyStmt(self):
            return self.getTypedRuleContext(GoParser.EmptyStmtContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_simpleStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleStmt" ):
                listener.enterSimpleStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleStmt" ):
                listener.exitSimpleStmt(self)




    def simpleStmt(self):

        localctx = GoParser.SimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_simpleStmt)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.sendStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.incDecStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 380
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 381
                self.expressionStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 382
                self.shortVarDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 383
                self.emptyStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_expressionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStmt" ):
                listener.enterExpressionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStmt" ):
                listener.exitExpressionStmt(self)




    def expressionStmt(self):

        localctx = GoParser.ExpressionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expressionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SendStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.channel = None # ExpressionContext

        def RECEIVE(self):
            return self.getToken(GoParser.RECEIVE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_sendStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSendStmt" ):
                listener.enterSendStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSendStmt" ):
                listener.exitSendStmt(self)




    def sendStmt(self):

        localctx = GoParser.SendStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sendStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            localctx.channel = self.expression(0)
            self.state = 389
            self.match(GoParser.RECEIVE)
            self.state = 390
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncDecStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def PLUS_PLUS(self):
            return self.getToken(GoParser.PLUS_PLUS, 0)

        def MINUS_MINUS(self):
            return self.getToken(GoParser.MINUS_MINUS, 0)

        def getRuleIndex(self):
            return GoParser.RULE_incDecStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncDecStmt" ):
                listener.enterIncDecStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncDecStmt" ):
                listener.exitIncDecStmt(self)




    def incDecStmt(self):

        localctx = GoParser.IncDecStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_incDecStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.expression(0)
            self.state = 393
            _la = self._input.LA(1)
            if not(_la==GoParser.PLUS_PLUS or _la==GoParser.MINUS_MINUS):
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExpressionListContext)
            else:
                return self.getTypedRuleContext(GoParser.ExpressionListContext,i)


        def assign_op(self):
            return self.getTypedRuleContext(GoParser.Assign_opContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = GoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.expressionList()
            self.state = 396
            self.assign_op()
            self.state = 397
            self.expressionList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def PLUS(self):
            return self.getToken(GoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GoParser.MINUS, 0)

        def OR(self):
            return self.getToken(GoParser.OR, 0)

        def CARET(self):
            return self.getToken(GoParser.CARET, 0)

        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def DIV(self):
            return self.getToken(GoParser.DIV, 0)

        def MOD(self):
            return self.getToken(GoParser.MOD, 0)

        def LSHIFT(self):
            return self.getToken(GoParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(GoParser.RSHIFT, 0)

        def AMPERSAND(self):
            return self.getToken(GoParser.AMPERSAND, 0)

        def BIT_CLEAR(self):
            return self.getToken(GoParser.BIT_CLEAR, 0)

        def getRuleIndex(self):
            return GoParser.RULE_assign_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_op" ):
                listener.enterAssign_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_op" ):
                listener.exitAssign_op(self)




    def assign_op(self):

        localctx = GoParser.Assign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.OR) | (1 << GoParser.DIV) | (1 << GoParser.MOD) | (1 << GoParser.LSHIFT) | (1 << GoParser.RSHIFT) | (1 << GoParser.BIT_CLEAR) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND))) != 0):
                self.state = 399
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.OR) | (1 << GoParser.DIV) | (1 << GoParser.MOD) | (1 << GoParser.LSHIFT) | (1 << GoParser.RSHIFT) | (1 << GoParser.BIT_CLEAR) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 402
            self.match(GoParser.ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortVarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def DECLARE_ASSIGN(self):
            return self.getToken(GoParser.DECLARE_ASSIGN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_shortVarDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShortVarDecl" ):
                listener.enterShortVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShortVarDecl" ):
                listener.exitShortVarDecl(self)




    def shortVarDecl(self):

        localctx = GoParser.ShortVarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_shortVarDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.identifierList()
            self.state = 405
            self.match(GoParser.DECLARE_ASSIGN)
            self.state = 406
            self.expressionList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(GoParser.SEMI, 0)

        def getRuleIndex(self):
            return GoParser.RULE_emptyStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStmt" ):
                listener.enterEmptyStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStmt" ):
                listener.exitEmptyStmt(self)




    def emptyStmt(self):

        localctx = GoParser.EmptyStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_emptyStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(GoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(GoParser.COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(GoParser.StatementContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_labeledStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledStmt" ):
                listener.enterLabeledStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledStmt" ):
                listener.exitLabeledStmt(self)




    def labeledStmt(self):

        localctx = GoParser.LabeledStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_labeledStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(GoParser.IDENTIFIER)
            self.state = 411
            self.match(GoParser.COLON)
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 412
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(GoParser.RETURN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = GoParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(GoParser.RETURN)
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 416
                self.expressionList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(GoParser.BREAK, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)




    def breakStmt(self):

        localctx = GoParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(GoParser.BREAK)
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 420
                self.match(GoParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(GoParser.CONTINUE, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)




    def continueStmt(self):

        localctx = GoParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(GoParser.CONTINUE)
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 424
                self.match(GoParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(GoParser.GOTO, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_gotoStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoStmt" ):
                listener.enterGotoStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoStmt" ):
                listener.exitGotoStmt(self)




    def gotoStmt(self):

        localctx = GoParser.GotoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_gotoStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(GoParser.GOTO)
            self.state = 428
            self.match(GoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FallthroughStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FALLTHROUGH(self):
            return self.getToken(GoParser.FALLTHROUGH, 0)

        def getRuleIndex(self):
            return GoParser.RULE_fallthroughStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFallthroughStmt" ):
                listener.enterFallthroughStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFallthroughStmt" ):
                listener.exitFallthroughStmt(self)




    def fallthroughStmt(self):

        localctx = GoParser.FallthroughStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_fallthroughStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(GoParser.FALLTHROUGH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeferStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFER(self):
            return self.getToken(GoParser.DEFER, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_deferStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeferStmt" ):
                listener.enterDeferStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeferStmt" ):
                listener.exitDeferStmt(self)




    def deferStmt(self):

        localctx = GoParser.DeferStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_deferStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(GoParser.DEFER)
            self.state = 433
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GoParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.BlockContext)
            else:
                return self.getTypedRuleContext(GoParser.BlockContext,i)


        def simpleStmt(self):
            return self.getTypedRuleContext(GoParser.SimpleStmtContext,0)


        def SEMI(self):
            return self.getToken(GoParser.SEMI, 0)

        def ELSE(self):
            return self.getToken(GoParser.ELSE, 0)

        def ifStmt(self):
            return self.getTypedRuleContext(GoParser.IfStmtContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)




    def ifStmt(self):

        localctx = GoParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(GoParser.IF)
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 436
                self.simpleStmt()
                self.state = 437
                self.match(GoParser.SEMI)


            self.state = 441
            self.expression(0)
            self.state = 442
            self.block()
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 443
                self.match(GoParser.ELSE)
                self.state = 446
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GoParser.IF]:
                    self.state = 444
                    self.ifStmt()
                    pass
                elif token in [GoParser.L_CURLY]:
                    self.state = 445
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


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprSwitchStmt(self):
            return self.getTypedRuleContext(GoParser.ExprSwitchStmtContext,0)


        def typeSwitchStmt(self):
            return self.getTypedRuleContext(GoParser.TypeSwitchStmtContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_switchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStmt" ):
                listener.enterSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStmt" ):
                listener.exitSwitchStmt(self)




    def switchStmt(self):

        localctx = GoParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_switchStmt)
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.exprSwitchStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.typeSwitchStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprSwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(GoParser.SWITCH, 0)

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def simpleStmt(self):
            return self.getTypedRuleContext(GoParser.SimpleStmtContext,0)


        def SEMI(self):
            return self.getToken(GoParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def exprCaseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExprCaseClauseContext)
            else:
                return self.getTypedRuleContext(GoParser.ExprCaseClauseContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_exprSwitchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSwitchStmt" ):
                listener.enterExprSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSwitchStmt" ):
                listener.exitExprSwitchStmt(self)




    def exprSwitchStmt(self):

        localctx = GoParser.ExprSwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exprSwitchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(GoParser.SWITCH)
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 455
                self.simpleStmt()
                self.state = 456
                self.match(GoParser.SEMI)


            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 460
                self.expression(0)


            self.state = 463
            self.match(GoParser.L_CURLY)
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GoParser.DEFAULT or _la==GoParser.CASE:
                self.state = 464
                self.exprCaseClause()
                self.state = 469
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 470
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprCaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprSwitchCase(self):
            return self.getTypedRuleContext(GoParser.ExprSwitchCaseContext,0)


        def COLON(self):
            return self.getToken(GoParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(GoParser.StatementListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_exprCaseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprCaseClause" ):
                listener.enterExprCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprCaseClause" ):
                listener.exitExprCaseClause(self)




    def exprCaseClause(self):

        localctx = GoParser.ExprCaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exprCaseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.exprSwitchCase()
            self.state = 473
            self.match(GoParser.COLON)
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.BREAK) | (1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.SELECT) | (1 << GoParser.DEFER) | (1 << GoParser.GO) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.GOTO) | (1 << GoParser.SWITCH) | (1 << GoParser.CONST) | (1 << GoParser.FALLTHROUGH) | (1 << GoParser.IF) | (1 << GoParser.TYPE) | (1 << GoParser.CONTINUE) | (1 << GoParser.FOR) | (1 << GoParser.RETURN) | (1 << GoParser.VAR) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 474
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprSwitchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(GoParser.CASE, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def DEFAULT(self):
            return self.getToken(GoParser.DEFAULT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_exprSwitchCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSwitchCase" ):
                listener.enterExprSwitchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSwitchCase" ):
                listener.exitExprSwitchCase(self)




    def exprSwitchCase(self):

        localctx = GoParser.ExprSwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exprSwitchCase)
        try:
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.match(GoParser.CASE)
                self.state = 478
                self.expressionList()
                pass
            elif token in [GoParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.match(GoParser.DEFAULT)
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


    class TypeSwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(GoParser.SWITCH, 0)

        def typeSwitchGuard(self):
            return self.getTypedRuleContext(GoParser.TypeSwitchGuardContext,0)


        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def simpleStmt(self):
            return self.getTypedRuleContext(GoParser.SimpleStmtContext,0)


        def SEMI(self):
            return self.getToken(GoParser.SEMI, 0)

        def typeCaseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.TypeCaseClauseContext)
            else:
                return self.getTypedRuleContext(GoParser.TypeCaseClauseContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_typeSwitchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSwitchStmt" ):
                listener.enterTypeSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSwitchStmt" ):
                listener.exitTypeSwitchStmt(self)




    def typeSwitchStmt(self):

        localctx = GoParser.TypeSwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_typeSwitchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(GoParser.SWITCH)
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 483
                self.simpleStmt()
                self.state = 484
                self.match(GoParser.SEMI)


            self.state = 488
            self.typeSwitchGuard()
            self.state = 489
            self.match(GoParser.L_CURLY)
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GoParser.DEFAULT or _la==GoParser.CASE:
                self.state = 490
                self.typeCaseClause()
                self.state = 495
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 496
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSwitchGuardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(GoParser.PrimaryExprContext,0)


        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def TYPE(self):
            return self.getToken(GoParser.TYPE, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def DECLARE_ASSIGN(self):
            return self.getToken(GoParser.DECLARE_ASSIGN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_typeSwitchGuard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSwitchGuard" ):
                listener.enterTypeSwitchGuard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSwitchGuard" ):
                listener.exitTypeSwitchGuard(self)




    def typeSwitchGuard(self):

        localctx = GoParser.TypeSwitchGuardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_typeSwitchGuard)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 498
                self.match(GoParser.IDENTIFIER)
                self.state = 499
                self.match(GoParser.DECLARE_ASSIGN)


            self.state = 502
            self.primaryExpr(0)
            self.state = 503
            self.match(GoParser.DOT)
            self.state = 504
            self.match(GoParser.L_PAREN)
            self.state = 505
            self.match(GoParser.TYPE)
            self.state = 506
            self.match(GoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeCaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSwitchCase(self):
            return self.getTypedRuleContext(GoParser.TypeSwitchCaseContext,0)


        def COLON(self):
            return self.getToken(GoParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(GoParser.StatementListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_typeCaseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCaseClause" ):
                listener.enterTypeCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCaseClause" ):
                listener.exitTypeCaseClause(self)




    def typeCaseClause(self):

        localctx = GoParser.TypeCaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_typeCaseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.typeSwitchCase()
            self.state = 509
            self.match(GoParser.COLON)
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.BREAK) | (1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.SELECT) | (1 << GoParser.DEFER) | (1 << GoParser.GO) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.GOTO) | (1 << GoParser.SWITCH) | (1 << GoParser.CONST) | (1 << GoParser.FALLTHROUGH) | (1 << GoParser.IF) | (1 << GoParser.TYPE) | (1 << GoParser.CONTINUE) | (1 << GoParser.FOR) | (1 << GoParser.RETURN) | (1 << GoParser.VAR) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 510
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSwitchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(GoParser.CASE, 0)

        def typeList(self):
            return self.getTypedRuleContext(GoParser.TypeListContext,0)


        def DEFAULT(self):
            return self.getToken(GoParser.DEFAULT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_typeSwitchCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSwitchCase" ):
                listener.enterTypeSwitchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSwitchCase" ):
                listener.exitTypeSwitchCase(self)




    def typeSwitchCase(self):

        localctx = GoParser.TypeSwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_typeSwitchCase)
        try:
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
                self.match(GoParser.CASE)
                self.state = 514
                self.typeList()
                pass
            elif token in [GoParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.match(GoParser.DEFAULT)
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


    class TypeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.Type_Context)
            else:
                return self.getTypedRuleContext(GoParser.Type_Context,i)


        def NIL_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.NIL_LIT)
            else:
                return self.getToken(GoParser.NIL_LIT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_typeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeList" ):
                listener.enterTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeList" ):
                listener.exitTypeList(self)




    def typeList(self):

        localctx = GoParser.TypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_typeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.FUNC, GoParser.INTERFACE, GoParser.MAP, GoParser.STRUCT, GoParser.CHAN, GoParser.IDENTIFIER, GoParser.L_PAREN, GoParser.L_BRACKET, GoParser.STAR, GoParser.RECEIVE]:
                self.state = 518
                self.type_()
                pass
            elif token in [GoParser.NIL_LIT]:
                self.state = 519
                self.match(GoParser.NIL_LIT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 529
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GoParser.COMMA:
                self.state = 522
                self.match(GoParser.COMMA)
                self.state = 525
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GoParser.FUNC, GoParser.INTERFACE, GoParser.MAP, GoParser.STRUCT, GoParser.CHAN, GoParser.IDENTIFIER, GoParser.L_PAREN, GoParser.L_BRACKET, GoParser.STAR, GoParser.RECEIVE]:
                    self.state = 523
                    self.type_()
                    pass
                elif token in [GoParser.NIL_LIT]:
                    self.state = 524
                    self.match(GoParser.NIL_LIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 531
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(GoParser.SELECT, 0)

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def commClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.CommClauseContext)
            else:
                return self.getTypedRuleContext(GoParser.CommClauseContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_selectStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStmt" ):
                listener.enterSelectStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStmt" ):
                listener.exitSelectStmt(self)




    def selectStmt(self):

        localctx = GoParser.SelectStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_selectStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(GoParser.SELECT)
            self.state = 533
            self.match(GoParser.L_CURLY)
            self.state = 537
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GoParser.DEFAULT or _la==GoParser.CASE:
                self.state = 534
                self.commClause()
                self.state = 539
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 540
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commCase(self):
            return self.getTypedRuleContext(GoParser.CommCaseContext,0)


        def COLON(self):
            return self.getToken(GoParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(GoParser.StatementListContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_commClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommClause" ):
                listener.enterCommClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommClause" ):
                listener.exitCommClause(self)




    def commClause(self):

        localctx = GoParser.CommClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_commClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.commCase()
            self.state = 543
            self.match(GoParser.COLON)
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.BREAK) | (1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.SELECT) | (1 << GoParser.DEFER) | (1 << GoParser.GO) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.GOTO) | (1 << GoParser.SWITCH) | (1 << GoParser.CONST) | (1 << GoParser.FALLTHROUGH) | (1 << GoParser.IF) | (1 << GoParser.TYPE) | (1 << GoParser.CONTINUE) | (1 << GoParser.FOR) | (1 << GoParser.RETURN) | (1 << GoParser.VAR) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 544
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(GoParser.CASE, 0)

        def sendStmt(self):
            return self.getTypedRuleContext(GoParser.SendStmtContext,0)


        def recvStmt(self):
            return self.getTypedRuleContext(GoParser.RecvStmtContext,0)


        def DEFAULT(self):
            return self.getToken(GoParser.DEFAULT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_commCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommCase" ):
                listener.enterCommCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommCase" ):
                listener.exitCommCase(self)




    def commCase(self):

        localctx = GoParser.CommCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_commCase)
        try:
            self.state = 553
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.match(GoParser.CASE)
                self.state = 550
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 548
                    self.sendStmt()
                    pass

                elif la_ == 2:
                    self.state = 549
                    self.recvStmt()
                    pass


                pass
            elif token in [GoParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.match(GoParser.DEFAULT)
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


    class RecvStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.recvExpr = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def DECLARE_ASSIGN(self):
            return self.getToken(GoParser.DECLARE_ASSIGN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_recvStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecvStmt" ):
                listener.enterRecvStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecvStmt" ):
                listener.exitRecvStmt(self)




    def recvStmt(self):

        localctx = GoParser.RecvStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_recvStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 555
                self.expressionList()
                self.state = 556
                self.match(GoParser.ASSIGN)

            elif la_ == 2:
                self.state = 558
                self.identifierList()
                self.state = 559
                self.match(GoParser.DECLARE_ASSIGN)


            self.state = 563
            localctx.recvExpr = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GoParser.FOR, 0)

        def block(self):
            return self.getTypedRuleContext(GoParser.BlockContext,0)


        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def forClause(self):
            return self.getTypedRuleContext(GoParser.ForClauseContext,0)


        def rangeClause(self):
            return self.getTypedRuleContext(GoParser.RangeClauseContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)




    def forStmt(self):

        localctx = GoParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.match(GoParser.FOR)
            self.state = 569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 566
                self.expression(0)

            elif la_ == 2:
                self.state = 567
                self.forClause()

            elif la_ == 3:
                self.state = 568
                self.rangeClause()


            self.state = 571
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.initStmt = None # SimpleStmtContext
            self.postStmt = None # SimpleStmtContext

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.SEMI)
            else:
                return self.getToken(GoParser.SEMI, i)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def simpleStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.SimpleStmtContext)
            else:
                return self.getTypedRuleContext(GoParser.SimpleStmtContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_forClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForClause" ):
                listener.enterForClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForClause" ):
                listener.exitForClause(self)




    def forClause(self):

        localctx = GoParser.ForClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_forClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 573
                localctx.initStmt = self.simpleStmt()


            self.state = 576
            self.match(GoParser.SEMI)
            self.state = 578
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 577
                self.expression(0)


            self.state = 580
            self.match(GoParser.SEMI)
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.SEMI) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 581
                localctx.postStmt = self.simpleStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(GoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def ASSIGN(self):
            return self.getToken(GoParser.ASSIGN, 0)

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def DECLARE_ASSIGN(self):
            return self.getToken(GoParser.DECLARE_ASSIGN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_rangeClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeClause" ):
                listener.enterRangeClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeClause" ):
                listener.exitRangeClause(self)




    def rangeClause(self):

        localctx = GoParser.RangeClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_rangeClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 584
                self.expressionList()
                self.state = 585
                self.match(GoParser.ASSIGN)

            elif la_ == 2:
                self.state = 587
                self.identifierList()
                self.state = 588
                self.match(GoParser.DECLARE_ASSIGN)


            self.state = 592
            self.match(GoParser.RANGE)
            self.state = 593
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GO(self):
            return self.getToken(GoParser.GO, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_goStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoStmt" ):
                listener.enterGoStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoStmt" ):
                listener.exitGoStmt(self)




    def goStmt(self):

        localctx = GoParser.GoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_goStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.match(GoParser.GO)
            self.state = 596
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(GoParser.TypeNameContext,0)


        def typeLit(self):
            return self.getTypedRuleContext(GoParser.TypeLitContext,0)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_type_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_" ):
                listener.enterType_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_" ):
                listener.exitType_(self)




    def type_(self):

        localctx = GoParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_type_)
        try:
            self.state = 604
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.typeName()
                pass
            elif token in [GoParser.FUNC, GoParser.INTERFACE, GoParser.MAP, GoParser.STRUCT, GoParser.CHAN, GoParser.L_BRACKET, GoParser.STAR, GoParser.RECEIVE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 599
                self.typeLit()
                pass
            elif token in [GoParser.L_PAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 600
                self.match(GoParser.L_PAREN)
                self.state = 601
                self.type_()
                self.state = 602
                self.match(GoParser.R_PAREN)
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


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedIdent(self):
            return self.getTypedRuleContext(GoParser.QualifiedIdentContext,0)


        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)




    def typeName(self):

        localctx = GoParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_typeName)
        try:
            self.state = 608
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                self.qualifiedIdent()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 607
                self.match(GoParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(GoParser.ArrayTypeContext,0)


        def structType(self):
            return self.getTypedRuleContext(GoParser.StructTypeContext,0)


        def pointerType(self):
            return self.getTypedRuleContext(GoParser.PointerTypeContext,0)


        def functionType(self):
            return self.getTypedRuleContext(GoParser.FunctionTypeContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(GoParser.InterfaceTypeContext,0)


        def sliceType(self):
            return self.getTypedRuleContext(GoParser.SliceTypeContext,0)


        def mapType(self):
            return self.getTypedRuleContext(GoParser.MapTypeContext,0)


        def channelType(self):
            return self.getTypedRuleContext(GoParser.ChannelTypeContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_typeLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeLit" ):
                listener.enterTypeLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeLit" ):
                listener.exitTypeLit(self)




    def typeLit(self):

        localctx = GoParser.TypeLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_typeLit)
        try:
            self.state = 618
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 610
                self.arrayType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
                self.structType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 612
                self.pointerType()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 613
                self.functionType()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 614
                self.interfaceType()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 615
                self.sliceType()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 616
                self.mapType()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 617
                self.channelType()
                pass


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

        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def arrayLength(self):
            return self.getTypedRuleContext(GoParser.ArrayLengthContext,0)


        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def elementType(self):
            return self.getTypedRuleContext(GoParser.ElementTypeContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_arrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)




    def arrayType(self):

        localctx = GoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self.match(GoParser.L_BRACKET)
            self.state = 621
            self.arrayLength()
            self.state = 622
            self.match(GoParser.R_BRACKET)
            self.state = 623
            self.elementType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLengthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_arrayLength

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLength" ):
                listener.enterArrayLength(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLength" ):
                listener.exitArrayLength(self)




    def arrayLength(self):

        localctx = GoParser.ArrayLengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_arrayLength)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_elementType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementType" ):
                listener.enterElementType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementType" ):
                listener.exitElementType(self)




    def elementType(self):

        localctx = GoParser.ElementTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_elementType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_pointerType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerType" ):
                listener.enterPointerType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerType" ):
                listener.exitPointerType(self)




    def pointerType(self):

        localctx = GoParser.PointerTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_pointerType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(GoParser.STAR)
            self.state = 630
            self.type_()
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

        def INTERFACE(self):
            return self.getToken(GoParser.INTERFACE, 0)

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def methodSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.MethodSpecContext)
            else:
                return self.getTypedRuleContext(GoParser.MethodSpecContext,i)


        def typeName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.TypeNameContext)
            else:
                return self.getTypedRuleContext(GoParser.TypeNameContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_interfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceType" ):
                listener.enterInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceType" ):
                listener.exitInterfaceType(self)




    def interfaceType(self):

        localctx = GoParser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_interfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.match(GoParser.INTERFACE)
            self.state = 633
            self.match(GoParser.L_CURLY)
            self.state = 642
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 636
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                    if la_ == 1:
                        self.state = 634
                        self.methodSpec()
                        pass

                    elif la_ == 2:
                        self.state = 635
                        self.typeName()
                        pass


                    self.state = 638
                    self.eos() 
                self.state = 644
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

            self.state = 645
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SliceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def elementType(self):
            return self.getTypedRuleContext(GoParser.ElementTypeContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_sliceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSliceType" ):
                listener.enterSliceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSliceType" ):
                listener.exitSliceType(self)




    def sliceType(self):

        localctx = GoParser.SliceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_sliceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.match(GoParser.L_BRACKET)
            self.state = 648
            self.match(GoParser.R_BRACKET)
            self.state = 649
            self.elementType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP(self):
            return self.getToken(GoParser.MAP, 0)

        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def elementType(self):
            return self.getTypedRuleContext(GoParser.ElementTypeContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_mapType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapType" ):
                listener.enterMapType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapType" ):
                listener.exitMapType(self)




    def mapType(self):

        localctx = GoParser.MapTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_mapType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            self.match(GoParser.MAP)
            self.state = 652
            self.match(GoParser.L_BRACKET)
            self.state = 653
            self.type_()
            self.state = 654
            self.match(GoParser.R_BRACKET)
            self.state = 655
            self.elementType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChannelTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementType(self):
            return self.getTypedRuleContext(GoParser.ElementTypeContext,0)


        def CHAN(self):
            return self.getToken(GoParser.CHAN, 0)

        def RECEIVE(self):
            return self.getToken(GoParser.RECEIVE, 0)

        def getRuleIndex(self):
            return GoParser.RULE_channelType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChannelType" ):
                listener.enterChannelType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChannelType" ):
                listener.exitChannelType(self)




    def channelType(self):

        localctx = GoParser.ChannelTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_channelType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 662
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 657
                self.match(GoParser.CHAN)
                pass

            elif la_ == 2:
                self.state = 658
                self.match(GoParser.CHAN)
                self.state = 659
                self.match(GoParser.RECEIVE)
                pass

            elif la_ == 3:
                self.state = 660
                self.match(GoParser.RECEIVE)
                self.state = 661
                self.match(GoParser.CHAN)
                pass


            self.state = 664
            self.elementType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def parameters(self):
            return self.getTypedRuleContext(GoParser.ParametersContext,0)


        def result(self):
            return self.getTypedRuleContext(GoParser.ResultContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_methodSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodSpec" ):
                listener.enterMethodSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodSpec" ):
                listener.exitMethodSpec(self)




    def methodSpec(self):

        localctx = GoParser.MethodSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_methodSpec)
        try:
            self.state = 673
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 666
                if not noTerminatorAfterParams(2):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "noTerminatorAfterParams(2)")
                self.state = 667
                self.match(GoParser.IDENTIFIER)
                self.state = 668
                self.parameters()
                self.state = 669
                self.result()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
                self.match(GoParser.IDENTIFIER)
                self.state = 672
                self.parameters()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def signature(self):
            return self.getTypedRuleContext(GoParser.SignatureContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_functionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionType" ):
                listener.enterFunctionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionType" ):
                listener.exitFunctionType(self)




    def functionType(self):

        localctx = GoParser.FunctionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_functionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
            self.match(GoParser.FUNC)
            self.state = 676
            self.signature()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(GoParser.ParametersContext,0)


        def result(self):
            return self.getTypedRuleContext(GoParser.ResultContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_signature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignature" ):
                listener.enterSignature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignature" ):
                listener.exitSignature(self)




    def signature(self):

        localctx = GoParser.SignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_signature)
        try:
            self.state = 683
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 678
                if not noTerminatorAfterParams(1):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "noTerminatorAfterParams(1)")
                self.state = 679
                self.parameters()
                self.state = 680
                self.result()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 682
                self.parameters()
                pass


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

        def parameters(self):
            return self.getTypedRuleContext(GoParser.ParametersContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResult" ):
                listener.enterResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResult" ):
                listener.exitResult(self)




    def result(self):

        localctx = GoParser.ResultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_result)
        try:
            self.state = 687
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 685
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 686
                self.type_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def parameterDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ParameterDeclContext)
            else:
                return self.getTypedRuleContext(GoParser.ParameterDeclContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = GoParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 689
            self.match(GoParser.L_PAREN)
            self.state = 701
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.ELLIPSIS) | (1 << GoParser.STAR) | (1 << GoParser.RECEIVE))) != 0):
                self.state = 690
                self.parameterDecl()
                self.state = 695
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 691
                        self.match(GoParser.COMMA)
                        self.state = 692
                        self.parameterDecl() 
                    self.state = 697
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

                self.state = 699
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GoParser.COMMA:
                    self.state = 698
                    self.match(GoParser.COMMA)




            self.state = 703
            self.match(GoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def ELLIPSIS(self):
            return self.getToken(GoParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return GoParser.RULE_parameterDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterDecl" ):
                listener.enterParameterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterDecl" ):
                listener.exitParameterDecl(self)




    def parameterDecl(self):

        localctx = GoParser.ParameterDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_parameterDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.state = 705
                self.identifierList()


            self.state = 709
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GoParser.ELLIPSIS:
                self.state = 708
                self.match(GoParser.ELLIPSIS)


            self.state = 711
            self.type_()
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
            self.mul_op = None # Token
            self.add_op = None # Token
            self.rel_op = None # Token

        def primaryExpr(self):
            return self.getTypedRuleContext(GoParser.PrimaryExprContext,0)


        def unaryExpr(self):
            return self.getTypedRuleContext(GoParser.UnaryExprContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoParser.ExpressionContext,i)


        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def DIV(self):
            return self.getToken(GoParser.DIV, 0)

        def MOD(self):
            return self.getToken(GoParser.MOD, 0)

        def LSHIFT(self):
            return self.getToken(GoParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(GoParser.RSHIFT, 0)

        def AMPERSAND(self):
            return self.getToken(GoParser.AMPERSAND, 0)

        def BIT_CLEAR(self):
            return self.getToken(GoParser.BIT_CLEAR, 0)

        def PLUS(self):
            return self.getToken(GoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GoParser.MINUS, 0)

        def OR(self):
            return self.getToken(GoParser.OR, 0)

        def CARET(self):
            return self.getToken(GoParser.CARET, 0)

        def EQUALS(self):
            return self.getToken(GoParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(GoParser.NOT_EQUALS, 0)

        def LESS(self):
            return self.getToken(GoParser.LESS, 0)

        def LESS_OR_EQUALS(self):
            return self.getToken(GoParser.LESS_OR_EQUALS, 0)

        def GREATER(self):
            return self.getToken(GoParser.GREATER, 0)

        def GREATER_OR_EQUALS(self):
            return self.getToken(GoParser.GREATER_OR_EQUALS, 0)

        def LOGICAL_AND(self):
            return self.getToken(GoParser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(GoParser.LOGICAL_OR, 0)

        def getRuleIndex(self):
            return GoParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.state = 714
                self.primaryExpr(0)
                pass

            elif la_ == 2:
                self.state = 715
                self.unaryExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 735
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,74,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 733
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
                    if la_ == 1:
                        localctx = GoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 718
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 719
                        localctx.mul_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.DIV) | (1 << GoParser.MOD) | (1 << GoParser.LSHIFT) | (1 << GoParser.RSHIFT) | (1 << GoParser.BIT_CLEAR) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND))) != 0)):
                            localctx.mul_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 720
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = GoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 721
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 722
                        localctx.add_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.OR) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET))) != 0)):
                            localctx.add_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 723
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = GoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 724
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 725
                        localctx.rel_op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.EQUALS) | (1 << GoParser.NOT_EQUALS) | (1 << GoParser.LESS) | (1 << GoParser.LESS_OR_EQUALS) | (1 << GoParser.GREATER) | (1 << GoParser.GREATER_OR_EQUALS))) != 0)):
                            localctx.rel_op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 726
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = GoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 727
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 728
                        self.match(GoParser.LOGICAL_AND)
                        self.state = 729
                        self.expression(3)
                        pass

                    elif la_ == 5:
                        localctx = GoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 730
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 731
                        self.match(GoParser.LOGICAL_OR)
                        self.state = 732
                        self.expression(2)
                        pass

             
                self.state = 737
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(GoParser.OperandContext,0)


        def conversion(self):
            return self.getTypedRuleContext(GoParser.ConversionContext,0)


        def methodExpr(self):
            return self.getTypedRuleContext(GoParser.MethodExprContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(GoParser.PrimaryExprContext,0)


        def index(self):
            return self.getTypedRuleContext(GoParser.IndexContext,0)


        def slice_(self):
            return self.getTypedRuleContext(GoParser.Slice_Context,0)


        def typeAssertion(self):
            return self.getTypedRuleContext(GoParser.TypeAssertionContext,0)


        def arguments(self):
            return self.getTypedRuleContext(GoParser.ArgumentsContext,0)


        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)



    def primaryExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GoParser.PrimaryExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 142
        self.enterRecursionRule(localctx, 142, self.RULE_primaryExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 742
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 739
                self.operand()
                pass

            elif la_ == 2:
                self.state = 740
                self.conversion()
                pass

            elif la_ == 3:
                self.state = 741
                self.methodExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 755
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,77,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GoParser.PrimaryExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                    self.state = 744
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 751
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                    if la_ == 1:
                        self.state = 745
                        self.match(GoParser.DOT)
                        self.state = 746
                        self.match(GoParser.IDENTIFIER)
                        pass

                    elif la_ == 2:
                        self.state = 747
                        self.index()
                        pass

                    elif la_ == 3:
                        self.state = 748
                        self.slice_()
                        pass

                    elif la_ == 4:
                        self.state = 749
                        self.typeAssertion()
                        pass

                    elif la_ == 5:
                        self.state = 750
                        self.arguments()
                        pass

             
                self.state = 757
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,77,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.unary_op = None # Token

        def primaryExpr(self):
            return self.getTypedRuleContext(GoParser.PrimaryExprContext,0)


        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def PLUS(self):
            return self.getToken(GoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GoParser.MINUS, 0)

        def EXCLAMATION(self):
            return self.getToken(GoParser.EXCLAMATION, 0)

        def CARET(self):
            return self.getToken(GoParser.CARET, 0)

        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def AMPERSAND(self):
            return self.getToken(GoParser.AMPERSAND, 0)

        def RECEIVE(self):
            return self.getToken(GoParser.RECEIVE, 0)

        def getRuleIndex(self):
            return GoParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)




    def unaryExpr(self):

        localctx = GoParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 761
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 758
                self.primaryExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 759
                localctx.unary_op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0)):
                    localctx.unary_op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 760
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConversionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def COMMA(self):
            return self.getToken(GoParser.COMMA, 0)

        def getRuleIndex(self):
            return GoParser.RULE_conversion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConversion" ):
                listener.enterConversion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConversion" ):
                listener.exitConversion(self)




    def conversion(self):

        localctx = GoParser.ConversionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_conversion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 763
            self.type_()
            self.state = 764
            self.match(GoParser.L_PAREN)
            self.state = 765
            self.expression(0)
            self.state = 767
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GoParser.COMMA:
                self.state = 766
                self.match(GoParser.COMMA)


            self.state = 769
            self.match(GoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(GoParser.LiteralContext,0)


        def operandName(self):
            return self.getTypedRuleContext(GoParser.OperandNameContext,0)


        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = GoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_operand)
        try:
            self.state = 777
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 771
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 772
                self.operandName()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 773
                self.match(GoParser.L_PAREN)
                self.state = 774
                self.expression(0)
                self.state = 775
                self.match(GoParser.R_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicLit(self):
            return self.getTypedRuleContext(GoParser.BasicLitContext,0)


        def compositeLit(self):
            return self.getTypedRuleContext(GoParser.CompositeLitContext,0)


        def functionLit(self):
            return self.getTypedRuleContext(GoParser.FunctionLitContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = GoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_literal)
        try:
            self.state = 782
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.NIL_LIT, GoParser.DECIMAL_LIT, GoParser.BINARY_LIT, GoParser.OCTAL_LIT, GoParser.HEX_LIT, GoParser.FLOAT_LIT, GoParser.IMAGINARY_LIT, GoParser.RUNE_LIT, GoParser.RAW_STRING_LIT, GoParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 779
                self.basicLit()
                pass
            elif token in [GoParser.MAP, GoParser.STRUCT, GoParser.IDENTIFIER, GoParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 780
                self.compositeLit()
                pass
            elif token in [GoParser.FUNC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 781
                self.functionLit()
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


    class BasicLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL_LIT(self):
            return self.getToken(GoParser.NIL_LIT, 0)

        def integer(self):
            return self.getTypedRuleContext(GoParser.IntegerContext,0)


        def string_(self):
            return self.getTypedRuleContext(GoParser.String_Context,0)


        def FLOAT_LIT(self):
            return self.getToken(GoParser.FLOAT_LIT, 0)

        def IMAGINARY_LIT(self):
            return self.getToken(GoParser.IMAGINARY_LIT, 0)

        def RUNE_LIT(self):
            return self.getToken(GoParser.RUNE_LIT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_basicLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicLit" ):
                listener.enterBasicLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicLit" ):
                listener.exitBasicLit(self)




    def basicLit(self):

        localctx = GoParser.BasicLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_basicLit)
        try:
            self.state = 790
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 784
                self.match(GoParser.NIL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 785
                self.integer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 786
                self.string_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 787
                self.match(GoParser.FLOAT_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 788
                self.match(GoParser.IMAGINARY_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 789
                self.match(GoParser.RUNE_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_LIT(self):
            return self.getToken(GoParser.DECIMAL_LIT, 0)

        def BINARY_LIT(self):
            return self.getToken(GoParser.BINARY_LIT, 0)

        def OCTAL_LIT(self):
            return self.getToken(GoParser.OCTAL_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(GoParser.HEX_LIT, 0)

        def IMAGINARY_LIT(self):
            return self.getToken(GoParser.IMAGINARY_LIT, 0)

        def RUNE_LIT(self):
            return self.getToken(GoParser.RUNE_LIT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = GoParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 792
            _la = self._input.LA(1)
            if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)))) != 0)):
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


    class OperandNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.IDENTIFIER)
            else:
                return self.getToken(GoParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_operandName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperandName" ):
                listener.enterOperandName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperandName" ):
                listener.exitOperandName(self)




    def operandName(self):

        localctx = GoParser.OperandNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_operandName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 794
            self.match(GoParser.IDENTIFIER)
            self.state = 797
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.state = 795
                self.match(GoParser.DOT)
                self.state = 796
                self.match(GoParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedIdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.IDENTIFIER)
            else:
                return self.getToken(GoParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_qualifiedIdent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedIdent" ):
                listener.enterQualifiedIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedIdent" ):
                listener.exitQualifiedIdent(self)




    def qualifiedIdent(self):

        localctx = GoParser.QualifiedIdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_qualifiedIdent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 799
            self.match(GoParser.IDENTIFIER)
            self.state = 800
            self.match(GoParser.DOT)
            self.state = 801
            self.match(GoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositeLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalType(self):
            return self.getTypedRuleContext(GoParser.LiteralTypeContext,0)


        def literalValue(self):
            return self.getTypedRuleContext(GoParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_compositeLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompositeLit" ):
                listener.enterCompositeLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompositeLit" ):
                listener.exitCompositeLit(self)




    def compositeLit(self):

        localctx = GoParser.CompositeLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_compositeLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 803
            self.literalType()
            self.state = 804
            self.literalValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structType(self):
            return self.getTypedRuleContext(GoParser.StructTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(GoParser.ArrayTypeContext,0)


        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def ELLIPSIS(self):
            return self.getToken(GoParser.ELLIPSIS, 0)

        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def elementType(self):
            return self.getTypedRuleContext(GoParser.ElementTypeContext,0)


        def sliceType(self):
            return self.getTypedRuleContext(GoParser.SliceTypeContext,0)


        def mapType(self):
            return self.getTypedRuleContext(GoParser.MapTypeContext,0)


        def typeName(self):
            return self.getTypedRuleContext(GoParser.TypeNameContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_literalType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralType" ):
                listener.enterLiteralType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralType" ):
                listener.exitLiteralType(self)




    def literalType(self):

        localctx = GoParser.LiteralTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_literalType)
        try:
            self.state = 815
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 806
                self.structType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 807
                self.arrayType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 808
                self.match(GoParser.L_BRACKET)
                self.state = 809
                self.match(GoParser.ELLIPSIS)
                self.state = 810
                self.match(GoParser.R_BRACKET)
                self.state = 811
                self.elementType()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 812
                self.sliceType()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 813
                self.mapType()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 814
                self.typeName()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def elementList(self):
            return self.getTypedRuleContext(GoParser.ElementListContext,0)


        def COMMA(self):
            return self.getToken(GoParser.COMMA, 0)

        def getRuleIndex(self):
            return GoParser.RULE_literalValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralValue" ):
                listener.enterLiteralValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralValue" ):
                listener.exitLiteralValue(self)




    def literalValue(self):

        localctx = GoParser.LiteralValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 817
            self.match(GoParser.L_CURLY)
            self.state = 822
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_CURLY) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 818
                self.elementList()
                self.state = 820
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GoParser.COMMA:
                    self.state = 819
                    self.match(GoParser.COMMA)




            self.state = 824
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyedElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.KeyedElementContext)
            else:
                return self.getTypedRuleContext(GoParser.KeyedElementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_elementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementList" ):
                listener.enterElementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementList" ):
                listener.exitElementList(self)




    def elementList(self):

        localctx = GoParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_elementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 826
            self.keyedElement()
            self.state = 831
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,87,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 827
                    self.match(GoParser.COMMA)
                    self.state = 828
                    self.keyedElement() 
                self.state = 833
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,87,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyedElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(GoParser.ElementContext,0)


        def key(self):
            return self.getTypedRuleContext(GoParser.KeyContext,0)


        def COLON(self):
            return self.getToken(GoParser.COLON, 0)

        def getRuleIndex(self):
            return GoParser.RULE_keyedElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyedElement" ):
                listener.enterKeyedElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyedElement" ):
                listener.exitKeyedElement(self)




    def keyedElement(self):

        localctx = GoParser.KeyedElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_keyedElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 837
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.state = 834
                self.key()
                self.state = 835
                self.match(GoParser.COLON)


            self.state = 839
            self.element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def literalValue(self):
            return self.getTypedRuleContext(GoParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = GoParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_key)
        try:
            self.state = 844
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 841
                self.match(GoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 842
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 843
                self.literalValue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def literalValue(self):
            return self.getTypedRuleContext(GoParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = GoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_element)
        try:
            self.state = 848
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GoParser.FUNC, GoParser.INTERFACE, GoParser.MAP, GoParser.STRUCT, GoParser.CHAN, GoParser.NIL_LIT, GoParser.IDENTIFIER, GoParser.L_PAREN, GoParser.L_BRACKET, GoParser.EXCLAMATION, GoParser.PLUS, GoParser.MINUS, GoParser.CARET, GoParser.STAR, GoParser.AMPERSAND, GoParser.RECEIVE, GoParser.DECIMAL_LIT, GoParser.BINARY_LIT, GoParser.OCTAL_LIT, GoParser.HEX_LIT, GoParser.FLOAT_LIT, GoParser.IMAGINARY_LIT, GoParser.RUNE_LIT, GoParser.RAW_STRING_LIT, GoParser.INTERPRETED_STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 846
                self.expression(0)
                pass
            elif token in [GoParser.L_CURLY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 847
                self.literalValue()
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


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(GoParser.STRUCT, 0)

        def L_CURLY(self):
            return self.getToken(GoParser.L_CURLY, 0)

        def R_CURLY(self):
            return self.getToken(GoParser.R_CURLY, 0)

        def fieldDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.FieldDeclContext)
            else:
                return self.getTypedRuleContext(GoParser.FieldDeclContext,i)


        def eos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.EosContext)
            else:
                return self.getTypedRuleContext(GoParser.EosContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_structType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructType" ):
                listener.enterStructType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructType" ):
                listener.exitStructType(self)




    def structType(self):

        localctx = GoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_structType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 850
            self.match(GoParser.STRUCT)
            self.state = 851
            self.match(GoParser.L_CURLY)
            self.state = 857
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,91,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 852
                    self.fieldDecl()
                    self.state = 853
                    self.eos() 
                self.state = 859
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,91,self._ctx)

            self.state = 860
            self.match(GoParser.R_CURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tag = None # String_Context

        def identifierList(self):
            return self.getTypedRuleContext(GoParser.IdentifierListContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def embeddedField(self):
            return self.getTypedRuleContext(GoParser.EmbeddedFieldContext,0)


        def string_(self):
            return self.getTypedRuleContext(GoParser.String_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_fieldDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDecl" ):
                listener.enterFieldDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDecl" ):
                listener.exitFieldDecl(self)




    def fieldDecl(self):

        localctx = GoParser.FieldDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_fieldDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 867
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.state = 862
                if not noTerminatorBetween(2):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "noTerminatorBetween(2)")
                self.state = 863
                self.identifierList()
                self.state = 864
                self.type_()
                pass

            elif la_ == 2:
                self.state = 866
                self.embeddedField()
                pass


            self.state = 870
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.state = 869
                localctx.tag = self.string_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RAW_STRING_LIT(self):
            return self.getToken(GoParser.RAW_STRING_LIT, 0)

        def INTERPRETED_STRING_LIT(self):
            return self.getToken(GoParser.INTERPRETED_STRING_LIT, 0)

        def getRuleIndex(self):
            return GoParser.RULE_string_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_" ):
                listener.enterString_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_" ):
                listener.exitString_(self)




    def string_(self):

        localctx = GoParser.String_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_string_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 872
            _la = self._input.LA(1)
            if not(_la==GoParser.RAW_STRING_LIT or _la==GoParser.INTERPRETED_STRING_LIT):
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


    class EmbeddedFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(GoParser.TypeNameContext,0)


        def STAR(self):
            return self.getToken(GoParser.STAR, 0)

        def getRuleIndex(self):
            return GoParser.RULE_embeddedField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmbeddedField" ):
                listener.enterEmbeddedField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmbeddedField" ):
                listener.exitEmbeddedField(self)




    def embeddedField(self):

        localctx = GoParser.EmbeddedFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_embeddedField)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 875
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GoParser.STAR:
                self.state = 874
                self.match(GoParser.STAR)


            self.state = 877
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(GoParser.FUNC, 0)

        def signature(self):
            return self.getTypedRuleContext(GoParser.SignatureContext,0)


        def block(self):
            return self.getTypedRuleContext(GoParser.BlockContext,0)


        def getRuleIndex(self):
            return GoParser.RULE_functionLit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionLit" ):
                listener.enterFunctionLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionLit" ):
                listener.exitFunctionLit(self)




    def functionLit(self):

        localctx = GoParser.FunctionLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_functionLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 879
            self.match(GoParser.FUNC)
            self.state = 880
            self.signature()
            self.state = 881
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(GoParser.ExpressionContext,0)


        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def getRuleIndex(self):
            return GoParser.RULE_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex" ):
                listener.enterIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex" ):
                listener.exitIndex(self)




    def index(self):

        localctx = GoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 883
            self.match(GoParser.L_BRACKET)
            self.state = 884
            self.expression(0)
            self.state = 885
            self.match(GoParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Slice_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACKET(self):
            return self.getToken(GoParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(GoParser.R_BRACKET, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COLON)
            else:
                return self.getToken(GoParser.COLON, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return GoParser.RULE_slice_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlice_" ):
                listener.enterSlice_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlice_" ):
                listener.exitSlice_(self)




    def slice_(self):

        localctx = GoParser.Slice_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_slice_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 887
            self.match(GoParser.L_BRACKET)
            self.state = 903
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.state = 889
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                    self.state = 888
                    self.expression(0)


                self.state = 891
                self.match(GoParser.COLON)
                self.state = 893
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                    self.state = 892
                    self.expression(0)


                pass

            elif la_ == 2:
                self.state = 896
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                    self.state = 895
                    self.expression(0)


                self.state = 898
                self.match(GoParser.COLON)
                self.state = 899
                self.expression(0)
                self.state = 900
                self.match(GoParser.COLON)
                self.state = 901
                self.expression(0)
                pass


            self.state = 905
            self.match(GoParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeAssertionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def getRuleIndex(self):
            return GoParser.RULE_typeAssertion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAssertion" ):
                listener.enterTypeAssertion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAssertion" ):
                listener.exitTypeAssertion(self)




    def typeAssertion(self):

        localctx = GoParser.TypeAssertionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_typeAssertion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 907
            self.match(GoParser.DOT)
            self.state = 908
            self.match(GoParser.L_PAREN)
            self.state = 909
            self.type_()
            self.state = 910
            self.match(GoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(GoParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(GoParser.R_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(GoParser.ExpressionListContext,0)


        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def ELLIPSIS(self):
            return self.getToken(GoParser.ELLIPSIS, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GoParser.COMMA)
            else:
                return self.getToken(GoParser.COMMA, i)

        def getRuleIndex(self):
            return GoParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = GoParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 912
            self.match(GoParser.L_PAREN)
            self.state = 927
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GoParser.FUNC) | (1 << GoParser.INTERFACE) | (1 << GoParser.MAP) | (1 << GoParser.STRUCT) | (1 << GoParser.CHAN) | (1 << GoParser.NIL_LIT) | (1 << GoParser.IDENTIFIER) | (1 << GoParser.L_PAREN) | (1 << GoParser.L_BRACKET) | (1 << GoParser.EXCLAMATION) | (1 << GoParser.PLUS) | (1 << GoParser.MINUS) | (1 << GoParser.CARET) | (1 << GoParser.STAR) | (1 << GoParser.AMPERSAND) | (1 << GoParser.RECEIVE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (GoParser.DECIMAL_LIT - 64)) | (1 << (GoParser.BINARY_LIT - 64)) | (1 << (GoParser.OCTAL_LIT - 64)) | (1 << (GoParser.HEX_LIT - 64)) | (1 << (GoParser.FLOAT_LIT - 64)) | (1 << (GoParser.IMAGINARY_LIT - 64)) | (1 << (GoParser.RUNE_LIT - 64)) | (1 << (GoParser.RAW_STRING_LIT - 64)) | (1 << (GoParser.INTERPRETED_STRING_LIT - 64)))) != 0):
                self.state = 919
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
                if la_ == 1:
                    self.state = 913
                    self.expressionList()
                    pass

                elif la_ == 2:
                    self.state = 914
                    self.type_()
                    self.state = 917
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
                    if la_ == 1:
                        self.state = 915
                        self.match(GoParser.COMMA)
                        self.state = 916
                        self.expressionList()


                    pass


                self.state = 922
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GoParser.ELLIPSIS:
                    self.state = 921
                    self.match(GoParser.ELLIPSIS)


                self.state = 925
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GoParser.COMMA:
                    self.state = 924
                    self.match(GoParser.COMMA)




            self.state = 929
            self.match(GoParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def receiverType(self):
            return self.getTypedRuleContext(GoParser.ReceiverTypeContext,0)


        def DOT(self):
            return self.getToken(GoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(GoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GoParser.RULE_methodExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodExpr" ):
                listener.enterMethodExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodExpr" ):
                listener.exitMethodExpr(self)




    def methodExpr(self):

        localctx = GoParser.MethodExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_methodExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 931
            self.receiverType()
            self.state = 932
            self.match(GoParser.DOT)
            self.state = 933
            self.match(GoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GoParser.Type_Context,0)


        def getRuleIndex(self):
            return GoParser.RULE_receiverType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceiverType" ):
                listener.enterReceiverType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceiverType" ):
                listener.exitReceiverType(self)




    def receiverType(self):

        localctx = GoParser.ReceiverTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_receiverType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 935
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(GoParser.SEMI, 0)

        def EOF(self):
            return self.getToken(GoParser.EOF, 0)

        def getRuleIndex(self):
            return GoParser.RULE_eos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEos" ):
                listener.enterEos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEos" ):
                listener.exitEos(self)




    def eos(self):

        localctx = GoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_eos)
        try:
            self.state = 941
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 937
                self.match(GoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 938
                self.match(GoParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 939
                if not lineTerminatorAhead():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "lineTerminatorAhead()")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 940
                if not checkPreviousTokenText("}"):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "checkPreviousTokenText(\"}\")")
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
        self._predicates[64] = self.methodSpec_sempred
        self._predicates[66] = self.signature_sempred
        self._predicates[70] = self.expression_sempred
        self._predicates[71] = self.primaryExpr_sempred
        self._predicates[88] = self.fieldDecl_sempred
        self._predicates[98] = self.eos_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def methodSpec_sempred(self, localctx:MethodSpecContext, predIndex:int):
            if predIndex == 0:
                return noTerminatorAfterParams(2)
         

    def signature_sempred(self, localctx:SignatureContext, predIndex:int):
            if predIndex == 1:
                return noTerminatorAfterParams(1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def primaryExpr_sempred(self, localctx:PrimaryExprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def fieldDecl_sempred(self, localctx:FieldDeclContext, predIndex:int):
            if predIndex == 8:
                return noTerminatorBetween(2)
         

    def eos_sempred(self, localctx:EosContext, predIndex:int):
            if predIndex == 9:
                return lineTerminatorAhead()
         

            if predIndex == 10:
                return checkPreviousTokenText("}")
         




