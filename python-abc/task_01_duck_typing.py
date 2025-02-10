class VerboseList(list):
    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, items):
        print(f"Extended the list with [{len(items)}] items.")
        super().extend(items)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index] if len(self) else "nothing"
        print(f"Popped [{item}] from the list.")
        return super().pop(index) if len(self) else None
    