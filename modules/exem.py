
class Exem():
  def __hash__(self):
    return self.date.__hash__()
  def __eq__(self, other):
    return self.date == other.date