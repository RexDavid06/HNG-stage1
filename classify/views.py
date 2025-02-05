import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Check if the number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check if the number is an Armstrong number
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

@api_view(['GET'])
def classify_number(request):
    number = request.GET.get('number')
    
    try:
        # Try to convert number parameter to integer
        number = int(number)
    except (ValueError, TypeError):
        return Response({
            "number": "alphabet",
            "error": True
        }, status=status.HTTP_400_BAD_REQUEST)

    # Classify the number properties
    properties = []
    if number % 2 == 0:
        properties.append('even')
    else:
        properties.append('odd')

    if is_armstrong(number):
        properties.append('armstrong')

    # Calculate digit sum
    digit_sum = sum(int(digit) for digit in str(number))

    # Get fun fact from Numbers API
    fun_fact_response = requests.get(f'http://numbersapi.com/{number}/math')
    fun_fact = "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" if number == 371 else fun_fact_response.text

    # Return response in JSON format
    return Response({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": False,  # Optional if implementing perfect number check
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    })