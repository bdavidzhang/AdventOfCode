String convertToDigitsOnly(String input) {
  final Map<String, String> digitWords = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    // Specific concatenated digit words
    'zerone': '01', 'twoone': '21', 'oneight': '18', 'threeight': '38',
    'fiveight': '58', 'nineight': '98', 'eighthree': '83', 'eightwo': '82',
    'sevenine': '79'
  };

  String result = '';
  String currentWord = '';
  input = input.toLowerCase(); // Convert input to lowercase for case-insensitive matching

  for (int i = 0; i < input.length; i++) {
    currentWord += input[i];
    if (digitWords.containsKey(currentWord)) {
      // If the current word segment matches a digit word or specific combination
      result += digitWords[currentWord]!;
      currentWord = ''; // Reset current word
    } else if (!digitWords.keys.any((word) => word.startsWith(currentWord))) {
      // If no digit word or specific combination starts with the current word segment
      currentWord = ''; // Reset current word
    }
  }

  // Catch any trailing digit if the input ends with a digit word or specific combination
  if (digitWords.containsKey(currentWord)) {
    result += digitWords[currentWord]!;
  }

  return result;
}

void main() {
  // Test with one of the specific combinations
  String input = "threeight";
  String result = convertToDigitsOnly(input);
  print(result); // Should print: 83
}
