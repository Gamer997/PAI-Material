#include<iostream>
using namespace std;
struct Student {
int age;
string name;
};
int main(){
int size;
size = sizeof(Student);
cout<<"Enter the size of the array"<<endl;
cin>>size;
Student *s1 = new Student [size];
for(int i = 0;i<size;i++){
    cin>>s1[i].age;
    cin>>s1[i].name;
}
for(int i = 0;i<size;i++){
    cout<<"The age of student "<<i+1<<" is: "<<s1[i].age<<endl;
    cout<<"The name of student is: "<<s1[i].name<<endl;
}
cout<<size<<endl;
return 0;
}