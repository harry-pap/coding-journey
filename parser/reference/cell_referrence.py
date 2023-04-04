import parser.cell
import parser.cell.cell_processor
import parser.expression.node


class CellReferencingNode:
    pass


class LastCellInColumnReferencingNode(CellReferencingNode):
    def __init__(self, column_name):
        self.column_name = column_name

    def instantiate(self, current_cell: parser.cell.cell.Cell, cell_storage: parser.cell.cell_processor.CellStorage):
        target_cell = parser.cell.cell.Cell.from_string("{}{}".format(self.column_name, current_cell.row - 1))
        cell = cell_storage.cells[target_cell]

        return cell.visit(target_cell, cell_storage) if isinstance(cell, parser.expression.node.Node) else cell


class LastComputedCellInColumnReferencingNode(CellReferencingNode):
    def __init__(self, column_id):
        self.column_id = column_id

    def instantiate(self, current_cell: parser.cell.cell.Cell, cell_storage: parser.cell.cell_processor.CellStorage):

        target_cell = cell_storage.last_added_before(parser.cell.cell.Cell(self.column_id, current_cell.row))

        node = cell_storage.cells[target_cell]

        return node.visit(target_cell, cell_storage) if isinstance(node, parser.expression.node.Node) else node
