from src.aluno.base.professor import Professor
from src.aluno.base.sta import STA
from src.aluno.base.terceirizado import Terceirizado
from src.aluno.manager.rh_service import RHService
from src.cliente.tipo import Tipo

if __name__ == '__main__':
    rh = RHService()
    rh.cadastrar(Professor('16', 'Jonas', 'C'))
    rh.cadastrar(Professor('15', 'Alessio', 'B'))
    print("Total de funcionarios = {}".format(rh.getTotalFuncionarios())) #Total de funcionarios = 2

    rh.cadastrar(STA("43", "Miriam", 10))
    rh.cadastrar(STA("23", "Lacerda", 5))
    print("Total de funcionarios = {}".format(rh.getTotalFuncionarios()))  # Total de funcionarios = 4

    rh.cadastrar(Terceirizado("12", "Carla", False))
    rh.cadastrar(Terceirizado("78", "Adriana", True))
    print("Total de funcionarios = {}".format(rh.getTotalFuncionarios()))  # Total de funcionarios = 6

    rh.remover("12")
    print("Total de funcionarios = {}".format(rh.getTotalFuncionarios()))  # Total de funcionarios = 5
    print("Total de funcionarios = {}".format(len(rh.getFuncionariosPorCategorias(Tipo.TERC))))

    rh.solicitarDiaria("16")
    rh.solicitarDiaria("16")
    rh.solicitarDiaria("16")
    rh.solicitarDiaria("23")
    rh.solicitarDiaria("23")


    print(rh.calcularSalarioDoFuncionario("16")) #7300.0
    print(rh.calcularSalarioDoFuncionario("23")) #1600.0
    print(rh.calcularSalarioDoFuncionario("12")) #None
    print(rh.calcularSalarioDoFuncionario("78")) #1500.0

    rh.iniciarMes()
    rh.partilharLucros(20000)

    for funcionario in rh.getFuncionarios():
        print('{}(cpf: {}) -> salario= {} '.format(funcionario.getNome(), funcionario.getCpf(), funcionario.getSalario()))

        #Adriana(cpf=78) -> salario=5500.0
        #Alessio(cpf=15) -> salario=9000.0
        #Jonas(cpf=16) -> salario=11000.0
        #Lacerda(cpf=23) -> salario=5500.0
        #Miriam(cpf=43) -> salario=6000.0
    print('Folha do mes = {}'.format(rh.calcularFolhaDePagamento())) # Folha do mes = 37000.0

