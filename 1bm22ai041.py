# -*- coding: utf-8 -*-
"""1BM22AI041

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11d1ITNYjEDs7i9WmYhB_aKh9SY9je85w
"""

#1

def unboundedKnapsack(k, arr):

    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        for num in arr:
            if num <= i:
                dp[i] = max(dp[i], dp[i - num] + num)

    return dp[k]

k = int(input("Enter the capacity: "))
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
result = unboundedKnapsack(k, arr)
print("Maximum sum possible with given capacity:", result)

class Town:
    def __init__(self, location, population):
        self.location = location
        self.population = population
        self.total_clouds_over_town = 0
        self.cloud_location = -1  # Initial value for cloud location

    def __lt__(self, other):
        return self.location < other.location

def maximum_people_in_sunny_towns(towns, towns_with_more_than_one_cloud):
    if len(towns_with_more_than_one_cloud) == len(towns):
        return 0

    people_in_towns_without_clouds = 0
    max_people_in_town_under_one_cloud = 0
    cloud_max_cover = {}

    for town in towns.values():
        total_clouds_over_town = town.total_clouds_over_town

        if total_clouds_over_town == 0:
            people_in_towns_without_clouds += town.population
        elif total_clouds_over_town == 1:
            cloud_location = town.cloud_location
            if cloud_location not in cloud_max_cover:
                cloud_max_cover[cloud_location] = town.population
            else:
                cloud_max_cover[cloud_location] += town.population

            if max_people_in_town_under_one_cloud < cloud_max_cover[cloud_location]:
                max_people_in_town_under_one_cloud = cloud_max_cover[cloud_location]

    return people_in_towns_without_clouds + max_people_in_town_under_one_cloud

def binary_search(lower_index, upper_index, start_cloud, end_cloud, towns):
    if lower_index <= upper_index:
        mid = (lower_index + upper_index) // 2
        if towns[mid].location >= start_cloud and towns[mid].location <= end_cloud:
            return mid
        elif towns[mid].location > end_cloud:
            return binary_search(lower_index, mid - 1, start_cloud, end_cloud, towns)
        elif towns[mid].location < start_cloud:
            return binary_search(mid + 1, upper_index, start_cloud, end_cloud, towns)
    return -1

def main():
    data = """
    4
    100 200 300 400
    1 2 3 4
    3
    2 3 3
    """.split()

    index = 0
    number_of_towns = int(data[index])
    index += 1

    population_towns = []
    for i in range(number_of_towns):
        population_towns.append(int(data[index]))
        index += 1

    location_towns = {}
    for i in range(number_of_towns):
        location = int(data[index])
        if location not in location_towns:
            location_towns[location] = Town(location, population_towns[i])
        else:
            location_towns[location].population += population_towns[i]
        index += 1

    towns = sorted(location_towns.values())

    number_of_clouds = int(data[index])
    index += 1

    location_cloud = []
    for i in range(number_of_clouds):
        location_cloud.append(int(data[index]))
        index += 1

    location_towns_with_more_than_one_cloud = set()

    for i in range(number_of_clouds):
        town_last_location = towns[-1].location
        range_cloud = int(data[index])
        index += 1

        start_cloud = location_cloud[i] - range_cloud if location_cloud[i] - range_cloud >= 0 else 0
        end_cloud = location_cloud[i] + range_cloud if location_cloud[i] + range_cloud <= town_last_location else town_last_location

        index_town = binary_search(0, len(towns) - 1, start_cloud, end_cloud, towns)
        if index_town == -1:
            continue

        decrease = index_town
        while decrease >= 0 and towns[decrease].location >= start_cloud:
            if towns[decrease].total_clouds_over_town < 2:
                towns[decrease].total_clouds_over_town += 1
                towns[decrease].cloud_location = location_cloud[i]

                if towns[decrease].total_clouds_over_town == 2:
                    location_towns_with_more_than_one_cloud.add(towns[decrease].location)
                    if len(location_towns_with_more_than_one_cloud) == len(towns):
                        break

            decrease -= 1

        increase = index_town + 1
        while increase < len(towns) and towns[increase].location <= end_cloud:
            if towns[increase].total_clouds_over_town < 2:
                towns[increase].total_clouds_over_town += 1
                towns[increase].cloud_location = location_cloud[i]

                if towns[increase].total_clouds_over_town == 2:
                    location_towns_with_more_than_one_cloud.add(towns[increase].location)
                    if len(location_towns_with_more_than_one_cloud) == len(towns):
                        break

            increase += 1

    result = maximum_people_in_sunny_towns(location_towns, location_towns_with_more_than_one_cloud)
    print(result)

if __name__ == "__main__":
    main()

#3
def quick(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick(less) + [pivot] + quick(greater)

n = input("Enter array elements separated by spaces: ")
arr = [int(x) for x in n.split()]
sorted_arr = quick(arr)
print("Sorted array:", sorted_arr)

#4
n = int(input())
for _ in range(n):
    input_str = input()
    visited = set()
    cost = 0
    for char in input_str:
        if char not in visited:
            cost += 1
            visited.add(char)
    print(cost)
