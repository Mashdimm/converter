from PyQt6 import QtWidgets, QtCore, QtGui


class FramelessWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Window)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, False)
        self.setMouseTracking(True)

        self._margin = 6
        self._resizing = False
        self._moving = False
        self._pressed = False
        self._startPos = QtCore.QPoint()
        self._resizeDir = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self._pressed = True
            self._startPos = event.globalPosition().toPoint()
            self._resizeDir = self._detectResizeArea(event.pos())
            if self._resizeDir is None:
                self._moving = True

    def mouseMoveEvent(self, event):
        pos = event.pos()
        global_pos = event.globalPosition().toPoint()

        if not self._pressed:
            cursor = self._cursorForPosition(pos)
            self.setCursor(cursor)
            return

        if self._moving:
            delta = global_pos - self._startPos
            self.move(self.pos() + delta)
            self._startPos = global_pos
        elif self._resizeDir:
            self._resizeWindow(global_pos)

    def mouseReleaseEvent(self, event):
        self._pressed = False
        self._moving = False
        self._resizeDir = None

    def _detectResizeArea(self, pos):
        x, y = pos.x(), pos.y()
        w, h = self.width(), self.height()
        m = self._margin

        if x <= m and y <= m:
            return 'topleft'
        elif x >= w - m and y <= m:
            return 'topright'
        elif x <= m and y >= h - m:
            return 'bottomleft'
        elif x >= w - m and y >= h - m:
            return 'bottomright'
        elif x <= m:
            return 'left'
        elif x >= w - m:
            return 'right'
        elif y <= m:
            return 'top'
        elif y >= h - m:
            return 'bottom'
        return None

    def _cursorForPosition(self, pos):
        direction = self._detectResizeArea(pos)
        cursors = {
            'topleft': QtCore.Qt.CursorShape.SizeFDiagCursor,
            'bottomright': QtCore.Qt.CursorShape.SizeFDiagCursor,
            'topright': QtCore.Qt.CursorShape.SizeBDiagCursor,
            'bottomleft': QtCore.Qt.CursorShape.SizeBDiagCursor,
            'left': QtCore.Qt.CursorShape.SizeHorCursor,
            'right': QtCore.Qt.CursorShape.SizeHorCursor,
            'top': QtCore.Qt.CursorShape.SizeVerCursor,
            'bottom': QtCore.Qt.CursorShape.SizeVerCursor
        }
        return QtGui.QCursor(cursors.get(direction, QtCore.Qt.CursorShape.ArrowCursor))

    def _resizeWindow(self, global_pos):
        geo = self.geometry()
        diff = global_pos - self._startPos
        x, y, w, h = geo.x(), geo.y(), geo.width(), geo.height()

        if self._resizeDir == 'left':
            x += diff.x()
            w -= diff.x()
        elif self._resizeDir == 'right':
            w += diff.x()
        elif self._resizeDir == 'top':
            y += diff.y()
            h -= diff.y()
        elif self._resizeDir == 'bottom':
            h += diff.y()
        elif self._resizeDir == 'topleft':
            x += diff.x()
            w -= diff.x()
            y += diff.y()
            h -= diff.y()
        elif self._resizeDir == 'topright':
            w += diff.x()
            y += diff.y()
            h -= diff.y()
        elif self._resizeDir == 'bottomleft':
            x += diff.x()
            w -= diff.x()
            h += diff.y()
        elif self._resizeDir == 'bottomright':
            w += diff.x()
            h += diff.y()

        self.setGeometry(x, y, w, h)
        self._startPos = global_pos
