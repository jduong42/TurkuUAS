const amount = 36.5;
const sentence_1 = "I have ";
const sentence_2 = " euros.";

const full_sentence = `${sentence_1}${amount}${sentence_2}`;    // Concating strings and number with template literals
console.log(full_sentence);

const full_sentence_2 = sentence_1 + String(amount) + sentence_2;    // Concating strings and number with + operator and converting amount to str -value.
console.log(full_sentence_2);

/* Part 3 */

const sentence_3 = "The quick brown fox jumps over the lazy dog";

// Extract a substring from index 4 to index 15
const substring = sentence_3.substring(4, 15);
console.log(substring);

const sentence_4 = "HELLO WORLD";

// Convert the entire string to lowercase
const lowercase_sentence = sentence_4.toLowerCase();
console.log(lowercase_sentence);

const sentence_5 = "The quick brown fox";

// Split the string into an array of words
const words_to_array = sentence_5.split(" ");
console.log(words_to_array);


