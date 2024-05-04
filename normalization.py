def scale_data(input_file, output_file, lower=0, upper=1):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    scaled_lines = []
    for line in lines:
        elements = line.strip().split()
        scaled_elements = [elements[0]]  # 保留标签部分
        for el in elements[1:]:
            index, value = el.split(':')
            scaled_value = (float(value) - lower) / (upper - lower)
            scaled_elements.append(f"{index}:{scaled_value}")
        scaled_lines.append(' '.join(scaled_elements))

    with open(output_file, 'w') as f:
        f.write('\n'.join(scaled_lines))

# 使用示例
scale_data('train.svm', 'trainscale.svm', lower=0, upper=1)
