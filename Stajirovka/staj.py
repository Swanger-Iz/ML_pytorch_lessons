def strange_function(data):

    result = []

    for i in range(len(data)):

        val = 0

        for j in range(i, len(data)):

            val += data[j]

            result.append(val)

    return max(result)


x = [1., 2., 3.]


strange_function(x)