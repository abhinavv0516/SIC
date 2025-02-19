def arrange_oranges_ascending(num_oranges, diameters):
    last_entered_diameter = diameters[-1]
    
    # Separate oranges into smaller and larger based on the last entered orange
    smaller_oranges = [d for d in diameters if d < last_entered_diameter]
    larger_oranges = [d for d in diameters if d >= last_entered_diameter]
    
    # Sort both lists
    smaller_oranges.sort()
    larger_oranges.sort()
    
    # Combine the lists such that smaller oranges are on the left and larger ones are on the right
    arranged_oranges = smaller_oranges + larger_oranges
    
    return arranged_oranges

# Example usage
num_oranges = int(input("Enter the number of oranges: "))
diameters = list(map(float, input(f"Enter the diameters of {num_oranges} oranges, separated by spaces: ").split()))

if len(diameters) == num_oranges:
    result = arrange_oranges_ascending(num_oranges, diameters)
    print("Arranged oranges by diameters in ascending order:", result)
else:
    print("The number of diameters entered does not match the number of oranges.")
