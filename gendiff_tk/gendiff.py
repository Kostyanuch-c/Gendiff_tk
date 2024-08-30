from itertools import zip_longest


def gendiff(file1: str, file2: str) -> str:  # noqa
    with (
        open(file1, 'r') as f1,
        open(file2, 'r') as f2,
    ):
        result = ''
        diff1, diff2 = [], []
        for line1, line2 in zip_longest(f1, f2, fillvalue=''):
            if not line1.endswith('\n'):
                line1 += '\n'
            if not line2.endswith('\n'):
                line2 += '\n'
            if line1 == line2:
                if diff1 or diff2:
                    result += make_diff_view(diff1, diff2)
                    diff1 = []
                    diff2 = []
                if line1 == line2 == '\n':
                    continue
                result += (line1.rstrip() + '  (Строка в файлах совпадает)\n')
            else:
                diff1.append(line1)
                diff2.append(line2)
        if diff1 or diff2:
            result += make_diff_view(diff1, diff2)
        return result.strip()


def make_diff_view(diff1: list, diff2: list) -> str:
    template = f">>>file1>>>\n{''.join(diff1)}============\n{''.join(diff2)}<<<file2<<<\n"  # noqa: E501
    return template
