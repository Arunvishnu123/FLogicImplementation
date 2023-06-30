ERGOROOT = "C:/Users/ArunRAVEENDRANNAIRSH/Coherent/ERGOAI-3.0/ErgoEngine/ErgoAI"
XSBARCHDIR = "C:/Users/ArunRAVEENDRANNAIRSH/Coherent/ERGOAI-3.0/XSB/config/x64-pc-windows"

import sys


sys.path.append(ERGOROOT.replace('\\','/') + '/python')

from pyergo import \
pyergo_start_session, pyergo_end_session, \
pyergo_command, pyergo_query, \
HILOGFunctor, PROLOGFunctor, \
ERGOVariable, ERGOString, ERGOIRI, ERGOSymbol, \
ERGOIRI, ERGOCharlist, ERGODatetime, ERGODuration, ERGOUserDatatype, \
pyxsb_query, pyxsb_command, \
XSBFunctor, XSBVariable, XSBAtom, XSBString, \
PYERGOException, PYXSBException

pyergo_start_session(XSBARCHDIR,ERGOROOT)

try:
    pyergo_command("['C:\Users\ArunRAVEENDRANNAIRSH\Desktop\New folder (28)\knowledgebase.flr'].")
    result = pyergo_query('final.')
except:
    pass