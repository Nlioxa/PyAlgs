from copy import deepcopy 
import math

# generates a fibonacci sequence from min to max
def generate_levels(min, max):
    levels = [0, min]
    index = 1
    while levels[-1] < max:
        levels.append(levels[index - 1] + levels[index])
        index = index + 1
    levels[-1] = max
    return levels

# quantizes an array of values to the set of levels within an accuracy
def quantize(data, levels, eps):
    # make deep copy of data array
    quantized = deepcopy(data)
    # set the first found level index to 0
    prev_level_indx = 0
    # quantizing loop
    for i in range(len(data)):
        # find the nearest level to the next data value
        for level in levels:
            level_deviation_coef = abs(level - data[i])
            # check if the next data value is beside a level
            if level_deviation_coef <= eps:
                nearest_level = level
                break
        # quantize data values in range from the previous level to the current
        quantized[prev_level_indx:i+1] = [nearest_level for i in range(prev_level_indx,i+1)]
        # write the final index of quantization border for the next iterations
        prev_level_indx = i
    # quantize data values last out of attention to the last level
    quantized[prev_level_indx:len(data)] = [level for i in range(prev_level_indx,len(data))]
    return quantized
