class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations <= 0:
            return init
        step = iterations
        old = init
        new = 0
        while step > 0:
            new = old - learning_rate * 2 * old
            step -= 1
            old = new
        return round(new, 5)
        
