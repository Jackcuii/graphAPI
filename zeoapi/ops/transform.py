from zeoapi.helper import *
from zeoapi.dag import *
from zeoapi.zeotensor import *

def transform(dest, args, var_dict, graph):
    #print(dest,args)
    assert len(args)==2, "Interpret [transform] fail, please check it."
    # TO-DO: support multiple width and type
    # TO-DO: enable real LOAD/STORE
    # seq+=make_instr_1op("LOAD32", "_", var_dict[args
    print("transform", dest, args)
    graph.add_node(DAGnode(dest, "transform", Dimension(var_dict[dest][1])))
    graph.add_edge(args[0], dest)
    #seq+=[make_instr_3op("32TRANSFORM", args[0], var_dict[args[0]][1], args[1], var_dict[args[1]][1], dest, var_dict[dest][1] )] 
    



# test
#seq=[]
#dictt={ "Y": ("f32",[4,5]), "b": ("f32",[4,5]), "W": ("f32",[4,3]), "X":("f32",[3,5]), "Xf":("f32",[15]) }

#transform("Y", ["b","W","X"], seq, dictt)
