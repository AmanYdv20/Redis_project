#include <bits/stdc++.h>
#include <chrono>

using namespace std;
using namespace std::chrono;
#define func_time std::chrono::high_resolution_clock::time_point

struct Cmp
{
    bool operator ()(const pair<string, int> &a, const pair<string,int> &b)
    {
        return a.second < b.second;
    }
};

struct node{
    string value;
    func_time start;
    int expire;
    node(string val, func_time tm_value, int exp=-1){
        value=val;
        start=tm_value;
        expire=exp;
    }
};

unordered_map<string, node*> mp;
unordered_map<string, set <pair<string, int>, Cmp>> zmp;
//This hash table is for checking if the value with the particular key is already present.
map<pair<string,string>, int> c_mp;

//here the partiular key with value will be first checked in c_mp and then it will insert the value in the map.
// //c_mp is of no use because i am not able to track the rank.
int z_add(string key, int rank, string value){
    auto p=make_pair(key,value);
    if(c_mp.count(p)==0){
        zmp[key].insert(make_pair(value,rank));
        c_mp[p]=rank;
    } else{
        int prev_rank=c_mp[p];
        auto it=zmp[key].find({value,prev_rank});
        zmp[key].erase(it);
        c_mp[p]=rank;
        zmp[key].insert(make_pair(value,rank));
    }
}

//we can also use unordered_map like unordered_map<string,unordered_map<string,int>> c_mp for storing the rank of corresponding key and value
int zrank(string key, string value){
    auto p=make_pair(key,value);
    if(c_mp.count(p)==0){
        return -1;
    }
    auto i=zmp[key].find({value, c_mp[p]});
    int pos=distance(zmp[key].begin(), i);
    return pos;
}

void zrange(string key, int start, int end){
    if(start < 0 && end < 0){
        auto it=zmp[key].rbegin();
        advance(it,end);
        int count=abs(start-end+1);
        for(;(it!=zmp[key].rend()) && count > 0;it++){
            cout<<it->first<<" "<<it->second<<endl;
            count--;
        }
    } else{
        if(end < 0 || end >= zmp[key].size()){
            end=zmp[key].size()-1;
        }
        auto it=zmp[key].begin();
        advance(it,start);
        int count=end-start+1;
        for(;(it!=zmp[key].end()) && count > 0;it++){
            cout<<it->first<<" "<<it->second<<endl;
        }
    }
}

void set_mp(string key, string val, int ex=-1){
    func_time tmp=high_resolution_clock::now();
    if(ex == -1){
        mp[key]=new node(val, tmp);
    } else{
        mp[key]=new node(val, tmp, ex);
    }
}

string get_mp(string key){
    if(mp.count(key)==0){
        return "Sorry!! Key does not Found";
    } else{
        if(mp[key] -> expire != -1){
            func_time stop=high_resolution_clock::now();
            auto duration=duration_cast<seconds>(stop - (mp[key]->start));
            int cnt=duration.count();
            cout<<cnt<<endl;
            if(cnt > mp[key]->expire){
                return "Nil";
            } else {
                return mp[key]->value;
            }
        } else {
            return mp[key]->value;
        }
    }
}

//incomplete
string expire_key(string key, int exp){
    if(mp.count(key) == 0){
        return "Key not found";
    } else{
        //This part has to complete after checking if expire time already exist then what will happen.
        string val=mp[key] -> value;
        mp.erase(key);
        func_time tmp=high_resolution_clock::now();
        mp[key]=new node(val, tmp, exp);
        return "ok";
    }
}

int main(){
    // set_mp("aman", "yadav");
    // cout<<mp["aman"]->value<<endl;
    // cout<<mp["aman"]->expire;
    // int sum=0;

    // for(int i=0;i<100000;i++){
    //     for(int j=0;j<10000;j++){
    //         sum += 1;
    //     }
    // }
    // cout<<get_mp("aman")<<endl;
    string key="aman";
    string key2="priya";
    z_add(key,2,"yadav");
    z_add(key,5,"pratap");
    z_add(key,12,"Jadon");
    z_add(key,19,"Jadon");
    z_add(key2,2,"yadav");
    z_add(key2,5,"pratap");
    z_add(key2,12,"Jadon");

    zrange("aman",-1,-2);
    //cout<<zrank("priya","yadav");


    // for(auto it:c_mp){
    //     cout<<it.first.first<<" "<<it.first.second<<" "<<it.second<<endl;
    // }
    return 0;
}

