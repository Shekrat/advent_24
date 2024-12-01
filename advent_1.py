def calculate_distance_from_single_file(file):
    """
    Calculate the sum of distances between corresponding pairs of numbers read from a single text file.
    
    Args:
    file (str): Path to the text file.
    
    Returns:
    float: The total distance between the pairs of numbers read from the file.
    """
    
    def read_file(filepath):
        with open(filepath, 'r') as file:
            pairs = [line.strip().split() for line in file]
            if len(pairs) != 1000:
                raise ValueError("The file should contain 1000 pairs of numbers.")
            numbers1 = [(int(pair[0])) for pair in pairs]
            numbers2 = [(int(pair[1])) for pair in pairs]
            numbers1.sort()
            numbers2.sort()
        return numbers1, numbers2
    
    number_pairs = read_file(file)
    #print(number_pairs)

    total_distance = 0 
    for num1, num2 in zip(number_pairs[0], number_pairs[1]):
        total_distance += abs(num1 - num2) 
    return total_distance

def calculate_smimilarity_from_single_file(file):
    def read_file(filepath):
        with open(filepath, 'r') as file:
            pairs = [line.strip().split() for line in file]
            if len(pairs) != 1000:
                raise ValueError("The file should contain 1000 pairs of numbers.")
            numbers1 = [(int(pair[0])) for pair in pairs]
            numbers2 = [(int(pair[1])) for pair in pairs]
        return numbers1, numbers2
    
    number_pairs = read_file(file)

    similarity_score = []
    total_count = 0
    for num1 in number_pairs[0]:
        count = number_pairs[1].count(num1)
        similarity_score.append((num1, count))
        total_count += (num1 * count)
    return similarity_score, total_count

# Example usage
file = 'input.txt'
print("Total Distance:", calculate_distance_from_single_file(file))
print("Similarity Score:", calculate_smimilarity_from_single_file(file))
