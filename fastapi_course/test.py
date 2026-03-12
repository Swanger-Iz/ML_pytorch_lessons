from functools import wraps
from typing import Annotated, get_args, get_origin, get_type_hints


def check_value_range(func):
    @wraps(func)  # копирует имя, документацию и аннотации из оригинальной функции в обертку
    def wrapper(x):  # take args from main func
        type_hints = get_type_hints(double, include_extras=True)
        hint = type_hints["x"]
        if get_origin(hint) is Annotated:
            hint_type, *hint_args = get_args(hint)  # get_args(hint)=(<class 'int'>, (0, 100))
            low, high = hint_args[0]

            if not low <= x <= high:
                raise ValueError(f"{x} falls outside boundary {low}--{high}")
            # execute function once all checks passes
        return func(x)

    return wrapper


# double = check_value_range(deco_param)(double)(wrap_func_param)


@check_value_range
def double(x: Annotated[int, (0, 100)]) -> int:
    return x * 2
    # type_hints = get_type_hints(double, include_extras=True)
    # hint = type_hints["x"]  # type_hints = {'x': <class 'int'>, 'return': <class 'int'>}
    # if get_origin(hint) is Annotated:
    #     hint_type, *hint_args = get_args(hint)  # get_args(hint)=(<class 'int'>, (0, 100))
    #     low, high = hint_args[0]

    #     # print(f"{hint_type=}")  # hint_type=<class 'int'>
    #     # print(f"{hint_args=}")  # hint_args=[(0, 100)]
    #     print(low, high)
    #     # assert <if condition == True then pass>, < if not print given error message>
    #     # assert low <= x <= high, f"{x} falls outside boundary {low}--{high}"
    #     if not low <= x <= high:
    #         raise ValueError(f"{x} falls outside boundary {low}--{high}")


result = double(22)
print(result)
# (*test_var,) = (88, 99, (228, 288, 1488))
# print(*test_var)
