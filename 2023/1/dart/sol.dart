import 'dart:io';

bool isDigit(String character) {
  if (character.length != 1) {
    return false; // Ensure that the input is a single character
  }

  return character.codeUnitAt(0) >= '0'.codeUnitAt(0) && character.codeUnitAt(0) <= '9'.codeUnitAt(0);
}


void solve1(){
    String contents = new File('input.txt').readAsStringSync();
    List<String> lines = contents.split('\n');

    int sum = 0;

    for (String line in lines){
      List<String> nums = [];
        for (int i =0; i< line.length; ++i){
            if (isDigit(line[i])){
                nums.add(line[i]);
            } 
        }
      if (nums.isNotEmpty){
      sum += int.parse(nums[0]+nums[nums.length-1]);
      }

    }

  
    print(sum);


}


void solve2(){

 String contents = new File('input.txt').readAsStringSync();
    List<String> lines = contents.split('\n');

    int sum = 0;

    for (String line in lines){
      List<String> nums = [];
      List<String> digits = ['one','two','three','four','five','six','seven','eight','nine'];
        for (int i =0; i< line.length; ++i){
            if (isDigit(line[i])){
                nums.add(line[i]);
            } 
            for (var d in digits.asMap().entries){
               if (line.substring(i).startsWith(d.value)){
                  nums.add((d.key+1).toString());
              }
            }
        }
        if(nums.isNotEmpty){
          sum += int.parse(nums[0]+nums[nums.length-1]);
        }
    }
  print(sum);

}


void main(){
  solve1();

  solve2();
    
}