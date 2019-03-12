class Player:
  def __init__(self, name, id_num, score):
    self.name_ = name
    self.id_ = id_num
    self.score_ = score

  # pure virtual, implemented by child class
  def execute_moves():
    raise TypeError('Abstract method `' + self._class.__name__ \
                            + '.' + self._function + '\' called')

  # pure virtual, implemented by child class
  def compute_moves():
    raise TypeError('Abstract method `' + self._class.__name__ \
                            + '.' + self._function + '\' called')
