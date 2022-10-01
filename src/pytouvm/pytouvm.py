def get_indent_size(indent):
    return len(indent)/3

def plus_indent(indent):
    return indent + '   '

def minus_indent(indent):
    if len(indent) >= 3:
        return indent[:-3]
    else:
        return ''
    return indent + '   '

def write_srt(sstr, indent):
    log_node(sstr, indent)
    svfh.write(sstr.s)

def write_list(node, indent):
    svfh.write('{')
    tcnt = 0
    lenitem = len(node.elts)
    for item in node.elts:
            tcnt += 1

            if tcnt == lenitem:
                pass
            else:
                svfh.write(',')

    svfh.write('}')

def write_comment(str, indent):
    pass

def write_expr(node, indent):
    check_node(node.value, indent)

def write_target(targets, indent):
    pass

def write_boolop(node):
    pass
    #valuelen = len(boolnode.values)
    #for x in range(0, valuelen):
    #    if x != valuelen-1:
    #            check_node

def write_binop(node):
    if isinstance(node.op, ast.Add):
        op = ' + '
    elif isinstance(node.op, ast.Sub):
        op = ' - '
    elif isinstance(node.op, ast.Mult):
        op = ' * '
    elif isinstance(node.op, ast.Div):
        op = ' / '
    elif isinstance(node.op, ast.Mod):
        op = ' % '
    elif isinstance(node.op, ast.BitAnd):
        op = ' & '
    elif isinstance(node.op, ast.BitOr):
        op = ' | '
    elif isinstance(node.op, ast.RShift):
        op = ' >> '
    elif isinstance(node.op, ast.LShift):
        op = ' << '
    else:
        sys.exit()

    svfh.write(op)

    if hasattr(node, 'left'):
            check_node(node.left)

    if hasattr(node, 'right'):
            check_node(node.right)


def write_num(num):
    svfh.write(str(num.n))

def write_declaration(node):
    if len(node.targets) > 1:
        sys.exit("")

    if node.value.func.id == 'int':
        svfh.write(indent+'int '+node.targest[0])
    elif node.value.func.id == 'bool':
        svfh.write(indent+'bit '+node.targest[0])
    elif node.value.func.id == 'str':
        svfh.write(indent+'string '+node.targest[0])
    else:
        sys.exit('fixme line(%s)'%(sys._getframe().f_lineno))


def write_assign(node, indent):

    if isinstance(node.value, ast.Call):
        if hasattr(node.func, 'attr') and node.func.attr = 'pop':
            svfh.write()

def write_if(node, indent):
    svfh.write('\n'+indent+if('(')

    check_node(node.test, '')

    if skipL:
        svfh.write(') begin\n')
    else:
        svfh.write(') begin //'+str(node.lineno)+'\n')

    indent = plusindent(indent)

def write_elif(node, indent):
    pass

def write_else(node, indent = ''):
    pass



def write_args(args):
    lenargs = len(args):
    argcnt = 0

    svfh.write('(')

    for arg in args:
        argcnt += 1
        if hasattr(arg, 'id'):
            if arg.id in skipargs:
                pass
            else:
                if argcnt != lenargs:
                    svfh.write(', ')
                    check_node(arg, '')


def write_for(node, indent):
    svfh.write(indent+'for(int ')
    svfh.write(node.target.id)

    for bodynode in node.body:
        check_node(bodynode, indent)

    indent = minus_indent(indent)
    svfh.write(indent+'end\n')


def write_call(node, indent):
    if hasattr(node.func, 'value'):
        if node.func.value.id == 'pow':
            svfh.write('$pow(')
            for arg in node.args:
                tcnt += 1
                check_node(arg, indent)
                if tcnt  != len(node.args):
                    svfh.write(',')
                svfh.write(')')


def write_functionname_v3(node, indent = ''):
    pass

def write_functionname_v2(node, indent = ''):
    pass


def write_return(returnn, indent):
    pass

def write_break(indent):
    svfh.write(indent+'break;\n')

def write_while(node, indent):
    pass

def write_attribute(node, indent):
    pass

def check_node(node, indent, caleelno = 0):

    if isinstance(node, ast.Assign):
        write_assign(node, indent)
    elif isinstance(node, ast.Attribute):
        write_attribute(node, indent)
    elif isinstance(node, ast.FunctionDef):
        write_function(node, indent)
    elif isinstance(node, ast.While):
        write_while(node, indent)
    elif isinstance(node, ast.Break):
        write_break(node, indent)
    elif isinstance(node, ast.If):
        write_if(node, indent)
    elif isinstance(node, ast.Subscript):
        write_subscript(node, indent)
    elif isinstance(node, ast.BinOp):
        write_binop(node, indent)
    elif isinstance(node, ast.Name):
        write_name(node, indent)
    elif isinstance(node, ast.Compare):
        write_comparison(node)
    elif isinstance(node, ast.BoolOp):
        write_boolop(node, indent)
    elif isinstance(node, ast.Call):
        write_call(node, indent)
    elif isinstance(node, ast.For):
        write_for(node, indent)
    elif isinstance(node, ast.Str):
        write_str(node, indent)
    elif isinstance(node, ast.List):
        write_list(node, indent)
    elif isinstance(node, ast.Mult):
        svfh.write(' * ')
    elif isinstance(node, ast.Eq:
        svfh.write(' == ')
    elif isinstance(node, ast.IsNot):
        svfh.write(' != ')
    elif isinstance(node, ast.NotEq):
        svfh.write(' != ')
    elif isinstance(node, ast.And):
        svfh.write(' || ')
    elif isinstance(node, ast.Or):
        svfh.write(' || ')
    elif isinstance(node, ast.Gt):
        svfh.write(' > ')
    elif isinstance(node, ast.Lt):
        svfh.write(' < ')
    elif isinstance(node, ast.GtE):
        svfh.write(' >= ')
    elif isinstance(node, ast.LtE):
        svfh.write(' <= ')
    elif isinstance(node, ast.In):
        svfh.write(' inside ')


