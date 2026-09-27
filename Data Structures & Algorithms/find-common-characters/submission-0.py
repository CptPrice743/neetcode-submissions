class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_counts = {}

        for letter in words[0]:
            min_counts[letter] = min_counts.get(letter, 0) + 1

        for word in words[1:]:
            
            current_count = {}
            
            for letter in word:
                current_count[letter] = current_count.get(letter, 0) + 1
            
            for letter in min_counts:
                min_counts[letter] = min(min_counts[letter], current_count.get(letter, 0))
        
        result_list = []

        # NOTE FOR REVIEW:
        # Don't just append keys! If count is 0, we want 0 copies (skip).
        # If count is 2, range(2) repeats append twice:
        for letter, count in min_counts.items():
            for _ in range(count):
                result_list.append(letter)
        
        return result_list