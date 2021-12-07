from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, pino=All()):
        self.pino_olio = pino
    
    def playsIn(self, team):
        return QueryBuilder(
            And(
                self.pino_olio,
                PlaysIn(team)
            )
        )

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self.pino_olio))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self.pino_olio))

    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def build(self):
        return self.pino_olio
