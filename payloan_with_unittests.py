from math import floor


def get_days_of_power(r1, d1, r2, d2, r3, d3, k):

    total_days, total_rate = 0, 0

	#check if all the repayment days are different
    if d3 != d1 != d2 != d3:

		#create dictionary to map days to their daily rates
        rate_days = {d1: r1, d2: r2, d3: r3}

        days = [d1, d2, d3]

		#order days from smallest to largest
        ordered_days = bubbleSort(days)

        smallest = ordered_days[0]

        middle = ordered_days[1]

        largest = ordered_days[2]

		#check if the payment amount actually merits atleast one day of power
        if k < rate_days[smallest]:
            return total_days
        else:
            day_diff = middle - smallest

			#ensure there are no decimal places
            divisible_by = floor(k / rate_days[smallest])

            if divisible_by > day_diff:
                total_rate += day_diff * rate_days[smallest]
                total_days += day_diff

            else:
			#exit if there isn't enough money to buy another full day of power
                total_rate += day_diff * rate_days[smallest]
                total_days += divisible_by
                return total_days
			
            balance = k - total_rate

            second_day_diff = largest - middle

            divisible_by_second = floor(balance / (rate_days[smallest] + rate_days[middle]))

            if divisible_by_second > second_day_diff:
                total_rate += second_day_diff * (rate_days[smallest] + rate_days[middle])
                total_days += second_day_diff
            else:
                total_days += divisible_by_second
                return total_days
                return

            balance = k - total_rate
			
			#calculate the total number of times the balance from the paid amount is fully divisible by the sum of the three daily rates 
            divisible_by_third = floor(balance / (rate_days[smallest] + rate_days[middle] + rate_days[largest]))

            if divisible_by_third > 0:
                total_rate += divisible_by_third * (rate_days[smallest] + rate_days[middle] + rate_days[largest])
                total_days += divisible_by_third
                return total_days
            else:
                return total_days

    else:
		#check similarities in the repayment days
        if d1 == d2 != d3:

            d = d1

            rate_days = {d: r1 + r2, d3: r3}

            days = [d, d3]

            ordered_days = bubbleSort(days)

            smallest = ordered_days[0]

            largest = ordered_days[1]

            if k < rate_days[smallest]:
                return total_days
            else:
                day_diff = largest - smallest

                divisible_by = floor(k / rate_days[smallest])

                if divisible_by > day_diff:
                    total_rate += day_diff * rate_days[smallest]
                    total_days += day_diff

                else:
                    total_rate += divisible_by * rate_days[smallest]
                    total_days += divisible_by
                    return total_days

                balance = k - total_rate

                divisible_by_second = floor(balance / (rate_days[smallest] + rate_days[largest]))

                if divisible_by_second > 0:
                    total_rate += divisible_by_second * (rate_days[smallest] + rate_days[largest])
                    total_days += divisible_by_second
                    return total_days
                else:
                    return total_days


        elif d1 == d3 != d2:

            d = d1

            rate_days = {d: d1 + d3, d2: r2}

            days = [d, d2]

            ordered_days = bubbleSort(days)

            smallest = ordered_days[0]

            largest = ordered_days[1]

            if k < rate_days[smallest]:
                return total_days
            else:
                day_diff = largest - smallest

                divisible_by = floor(k / rate_days[smallest])

                if divisible_by > day_diff:
                    total_rate += day_diff * rate_days[smallest]
                    total_days += day_diff

                else:
                    total_rate += divisible_by * rate_days[smallest]
                    total_days += divisible_by
                    return total_days

                balance = k - total_rate

                divisible_by_second = floor(balance / (rate_days[smallest] + rate_days[largest]))

                if divisible_by_second > 0:
                    total_rate += divisible_by_second * (rate_days[smallest] + rate_days[largest])
                    total_days += divisible_by_second
                    return total_days
                else:
                    return total_days

        elif d2 == d3 != d1:

            d = d2

            rate_days = {d: r2 + r3, d1: r1}

            days = [d, d1]

            ordered_days = bubbleSort(days)

            smallest = ordered_days[0]

            largest = ordered_days[1]

            if k < rate_days[smallest]:
                return total_days
            else:
                day_diff = largest - smallest

                divisible_by = floor(k / rate_days[smallest])

                if divisible_by > day_diff:
                    total_rate += day_diff * rate_days[smallest]
                    total_days += day_diff

                else:
                    total_rate += divisible_by * rate_days[smallest]
                    total_days += divisible_by
                    return total_days

                balance = k - total_rate

                divisible_by_second = floor(balance / (rate_days[smallest] + rate_days[largest]))

                if divisible_by_second > 0:
                    total_rate += divisible_by_second * (rate_days[smallest] + rate_days[largest])
                    total_days += divisible_by_second
                    return total_days
                else:
                    return total_days

        elif d1 == d2 == d3:

            divisible_by = floor(k / (r1 + r2 + r3))

            if divisible_by > 0:
                total_rate += divisible_by * (r1 + r2 + r3)
                total_days += divisible_by
                return total_days
            else:
                return total_days


#to reorder the list in ascending order
def bubbleSort(nlist):
    for passnum in range(len(nlist) - 1, 0, -1):
        for i in range(passnum):
            if nlist[i] > nlist[i + 1]:
                temp = nlist[i]
                nlist[i] = nlist[i + 1]
                nlist[i + 1] = temp
    return nlist


assert get_days_of_power(3000, 3, 500, 10, 1500, 7, 700000) == 141, "Should be 141"
assert get_days_of_power(500, 3, 500, 10, 500, 7,21000) == 17, "Should be 17"
assert get_days_of_power(1300, 0, 500, 0, 1500, 7, 10000) == 5, "Should be 5"
assert get_days_of_power(10000, 3, 500, 10, 1500, 7, 11000) == 1, "Should be 1"