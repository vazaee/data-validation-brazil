from validate_docbr import CPF, CNPJ


class Document:

    @staticmethod
    def create_document(doc):
        if len(doc) == 11:
            return CpfDoc(doc)
        elif len(doc) == 14:
            return CnpjDoc(doc)
        else:
            raise ValueError("Invalid number of digits")


class CpfDoc:
    def __init__(self, cpf):
        if self.is_valid(cpf):
            self.cpf = cpf
        else:
            raise ValueError("Invalid CPF")

    def is_valid(self, cpf):
        validate = CPF()
        return validate.validate(cpf)

    def format(self):
        mask = CPF()
        return mask.mask(self.cpf)

    def __str__(self):
        return self.format()


class CnpjDoc:
    def __init__(self, cnpj):
        if self.is_valid(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("Invalid CNPJ")

    def is_valid(self, cnpj):
        validate = CNPJ()
        return validate.validate(cnpj)

    def format(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)

    def __str__(self):
        return self.format()

class CpfCnpj:

    def __init__(self, doc, doc_type):
        self.doc_type = doc_type
        doc = str(doc)

        if doc_type == 'cpf':
            if self.is_cpf_valid(doc):
                self.cpf = doc
            else:
                raise ValueError('Invalid cpf')

        elif doc_type == 'cnpj':
            if self.is_cnpj_valid(doc):
                self.cnpj = doc
            else:
                raise ValueError('Invalid cnpj')

        else:
            raise ValueError('Invalid document')

    def is_cpf_valid(self, cpf):
        if len(cpf) == 11:
            validate = CPF()
            return validate.validate(cpf)
        raise ValueError("Invalid number of digits")

    def format_cpf(self):
        mask = CPF()
        return mask.mask(self.cpf)

    def format_cnpj(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)

    def __str__(self):
        if self.doc_type == 'cpf':
            return self.format_cpf()
        elif self.doc_type == 'cnpj':
            return self.format_cnpj()

    def is_cnpj_valid(self, cnpj):
        if len(cnpj) == 14:
            validate = CNPJ()
            return validate.validate(cnpj)
        raise ValueError("Invalid number of digits")