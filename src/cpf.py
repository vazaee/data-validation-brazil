from validate_docbr import CPF


class Cpf:

    def __init__(self, doc):
        doc = str(doc)
        if self.is_cpf_valid(doc):
            self.cpf = doc
        else:
            raise ValueError('Invalid cpf')

    def __str__(self):
        return self.format_cpf()

    def is_cpf_valid(self, cpf):
        if len(cpf) == 11:
            validate = CPF()
            return validate.validate(cpf)
        raise ValueError("Invalid number of digits")

    def format_cpf(self):
        mask = CPF()
        return mask.mask(self.cpf)
