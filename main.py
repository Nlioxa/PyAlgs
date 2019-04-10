import quantizer as q
import matplotlib.pyplot as pp
import math

# domain
arguments = [x for x in range(1, 1000)]
# scope
values = [math.log10(x) for x in arguments]
# quantization levels
levels = q.generate_levels(0.1, max(values))
# an accuracy of quantization
accuracy = 0.1

# plot initial values
pp.plot(arguments, q.quantize(values, levels, accuracy))
# plot rusulting values
pp.plot(arguments, values)
pp.title("Figure 1. Initial and quantized signals")

pp.savefig("result.png")
pp.show()