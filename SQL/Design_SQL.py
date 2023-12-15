class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.dict = {}
        for i in range(len(names)):
            self.dict[names[i]] = [[0] * columns[i]]

    def insertRow(self, name: str, row: List[str]) -> None:
        self.dict[name].append(row)

    def deleteRow(self, name: str, rowId: int) -> None:
        self.dict[name][rowId] = None

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.dict[name][rowId][columnId - 1]
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)