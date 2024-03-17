// Problem : Find Closest Node to Given Two Nodes
// Problem Statement : You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

// The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

// You are also given two integers node1 and node2.

// Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

// Note that edges may contain cycles.


/**
 * @param {number[]} edges
 * @param {number} node1
 * @param {number} node2
 * @return {number}
 */
function closestMeetingNode (edges, node1, node2) {
    let map1 = {}
    let map2 = {}
    let count = 0;

    while(map1[node1] == undefined && node1 != -1){
        map1[node1] = count;
        count++
        node1 = edges[node1];
    }
    count = 0;
    while(map2[node2] == undefined && node2 != -1){
        map2[node2] = count;
        count++
        node2 = edges[node2]
    }
    let max = Infinity;
    let res = -1;

    for(let i =0; i<edges.length;i++){
        if(map1[i] == undefined || map2[i] == undefined) continue;
        let localMax = Math.max(map1[i],map2[i])
        if(localMax<max){
            max = localMax;
            res = i;
        }
    }

    return res;
}
