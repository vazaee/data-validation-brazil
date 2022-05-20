from cpf_cnpj import Document


cnpj_example = "35379838000112"
cpf_example = "32007832062"

doc = Document.create_document(cnpj_example)
print(doc)