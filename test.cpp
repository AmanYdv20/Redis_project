#include<bits/stdc++.h>
using namespace std;

struct Cmp
{
    bool operator ()(const pair<string, int> &a, const pair<string,int> &b)
    {
        return a.second < b.second;
    }
};

set<pair<string, int>, Cmp> mp;
int main(){
    mp.insert({"aman",21});
    mp.insert({"yadav",1});
    mp.insert({"great",6});
    // for(auto i:mp){
    //     cout<<i.first<<" "<<i.second<<endl;
    // }

    int count=0;
    auto it=mp.rbegin();
    advance(it,-1);
    for(;it!=mp.rend();it++){
        cout<<it->first<<" "<<it->second<<" "<<endl;
        count++;
    }
    // int i=distance(mp.begin(), find({6,"great"}));
    // cout<<i<<endl;
    // multiset<pair<string,int>> st;
    // st.insert({"aman",21});
    // st.insert({"yadav",1});
    // st.insert({"great",6});
    // auto i=st.find({"yadav", 1});
    // int pos=distance(st.begin(), i);
    // cout<<pos;
    //cout<<i->first<<" "<<i->second;
    return 0;
}