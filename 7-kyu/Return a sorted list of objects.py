def sort_list(sort_by, lst: list[dict]) -> list[dict]:
    return sorted(lst, key=lambda x: x[sort_by], reverse=True)



print(sort_list("a", [{"a": 1, "b": 3}, {"a": 3, "b": 2}, {"a": 2, "b": 40}, {"a": 4, "b": 12}]))
