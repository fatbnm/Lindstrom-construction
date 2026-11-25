import galois

def lindstrom_code(s, m):
    # Define GF(s)
    GF_s = galois.GF(s)
    
    # Elements β1, β2, ..., βs of GF(s)
    beta = [GF_s(i) for i in range(s)]
    print("Elements of GF(s):", beta)
    
    # Define GF(s^m)
    GF_sm = galois.GF(s**m)
    
    # Find all primitive elements α of GF(s^m)
    alpha_elements = GF_sm.primitive_elements
    print("Primitive elements α of GF(s^m):", alpha_elements[:1])  # Print first 10 primitive elements
    
    # Dictionary to hold x values for each primitive element
    x_values_dict = {}
    
    # Iterate over the first 10 primitive elements α
    for alpha in alpha_elements[:1]:
        x_values = []
        
        # Solve for x_i such that α^xi = α + βi
        for i in range(s):
            for j in range(GF_sm.order):
                if alpha**j == alpha + GF_sm(beta[i]):
                    x_values.append(j)
                    break
        
        # Store x values for the current primitive element
        x_values_dict[int(alpha)] = x_values  # Use int(alpha) to make it hashable
    
    return x_values_dict

# Example usage:
s = 31
m = 5
x_values_dict = lindstrom_code(s, m)

# Print the x values for each primitive element
for alpha, x_values in x_values_dict.items():
    print(f"For primitive element α = {alpha}, the values x1, x2, ..., xs are: {x_values}")
import time

start_time = time.time()
x_values = lindstrom_code(s, m)
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")