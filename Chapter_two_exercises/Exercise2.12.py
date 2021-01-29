""" (7% Investment Return) Some investment advisors say that it’s reasonable to expect a 7%
return over the long term in the stock market. Assuming that you begin with
$1000 and leave your money invested, calculate and display how much money you’ll have
after 10, 20 and 30 years. Use the following formula for determining these amounts:

a = p(1 + r)n

where

p is the original amount invested (i.e., the principal of $1000),
r is the annual rate of return (7%),
n is the number of years (10, 20 or 30) and
a is the amount on deposit at the end of the nth year."""

principal_investment = int(input("How much do you want to invest? "))

rate_of_return_on_investment_annually = int((input("How much return are you expecting on the investment per year? "))) / 100

lenght_of_investment = int(input("How many years do you plan to leave your investment? "))

income = principal_investment * (1 + rate_of_return_on_investment_annually) * lenght_of_investment

print("Return on", principal_investment, "investment after", lenght_of_investment, "years is", income)

