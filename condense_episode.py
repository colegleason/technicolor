import sys, glob, json, pprint

def main(): #file file_glob
    if (len(sys.argv) < 3):
        print("Correct usage is condense_episode.py <title> <outputfile> <file glob>")
        exit(1)
    compressed = {'nodes':[], 'arcs':[], 'title':sys.argv[1]}
    generate_nodes_list(compressed)
    generate_arcs_list(compressed)
    out_file = open(sys.argv[2], 'w')
    json.dump(compressed, out_file, indent=4, sort_keys=True)
    out_file.close()
    

def append_arc(n1, n2, arcs):
    arc_list = [n1, n2]
    arcs.append(arc_list)

def generate_arcs_list(compressed):
    nodes = compressed['nodes']
    arcs = compressed['arcs']
    for node_ind in range(len(nodes)):
        node_color = nodes[node_ind]['color']
        for other_node_ind in range(node_ind+1, len(nodes)):
            other_node_color = nodes[other_node_ind]['color']
            if node_color == other_node_color:
                append_arc(node_ind, other_node_ind, arcs)

def append_blank_node(node_list):
    node_dict = {'name':'', 'color':''}
    node_list.append(node_dict)


def get_frequent_colors(ep_data, node_list):
    color_hist = generate_color_hist(ep_data)
    s_colors = sorted(color_hist.iteritems(), key = lambda (k,v):(v,k))
    append_most_frequent(s_colors, node_list, ep_data['title'])

def generate_color_hist(ep_data):
    color_dict = {}
    for node in ep_data['nodes']:
        if node['color'] in color_dict:
            color_dict[node['color']] = color_dict[node['color']] + 1
        else:
            color_dict[node['color']] = 1
    return color_dict

def append_most_frequent(s_colors, node_list, title):
    num_nodes = 5
    if len(s_colors) < 5:
        num_nodes = len(s_colors)
    for node in range(1,num_nodes+1):
        node_dict = {}
        node_dict['color'] = s_colors[len(s_colors) - node][0]
        node_dict['name'] = title
        node_list.append(node_dict)

def generate_nodes_list(compressed):
    files = sys.argv[3:]
    for file_index in range(len(files)):
        file = files[file_index]
        ep_json = open(file)
        ep_data = json.load(ep_json)
        ep_json.close()
        #get 5 most frequent
        get_frequent_colors(ep_data, compressed['nodes'])
        if file_index+1 != len(files):
            append_blank_node(compressed['nodes'])


if __name__ == "__main__":
    main()
