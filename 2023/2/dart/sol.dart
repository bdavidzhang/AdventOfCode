import 'dart:io';

bool isInt(String s){
  try{
    int.parse(s);
    return true;
  } catch(e){
    return false;
  }
}


void main(){
  List<String> lines = File('input.txt').readAsLinesSync();
  
  int p1 = 0;
  int p2 = 0;

  for (String line in lines){
    List<String> contents = line.split(' ');
    List<int> index = [2];
      contents[1] = contents[1].replaceAll(':', '');
      for (int i = 0; i < contents.length; ++i){
        if (contents[i].contains(';')){
          index.add(i);
          contents[i] = contents[i].replaceAll(';', '');
        }
        if (contents[i].contains(',')){
          contents[i] = contents[i].replaceAll(',', '');
        }
      }
      index.add(contents.length-1);
    int id = int.parse(contents[1]);
    bool flag = true;
    int minr = 0;
    int ming = 0;
    int minb = 0;
    for (int i = 0; i< index.length-1; ++i){
      for (int j = index[i]; j <= index[i+1];++j){
        int rc = 0;
        int bc = 0;
        int gc = 0;
        if (isInt(contents[j])){
          if(contents[j+1] == "red"){
            rc += int.parse(contents[j]);
          }
          else if (contents[j+1] == "blue"){
            bc += int.parse(contents[j]);
          }
          else if (contents[j+1] == "green"){
            gc += int.parse(contents[j]);
          }
        }

        if(rc > 12 || gc > 13 || bc > 14){
          flag = false;

        }
        if (minr < rc) minr = rc;
        if (minb < bc) minb = bc;
        if (ming < gc) ming = gc;
      }
    }
    if(flag){
      p1 += id;
    }
    p2 += minr*minb*ming;

  }

  print(p1);
  print(p2);





}