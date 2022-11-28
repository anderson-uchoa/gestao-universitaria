from src.aluno.base.funcionario import Funcionario
from src.cliente.irh_service import IRHService


class RHService(IRHService):

    def cadastrar(self, funcionario: Funcionario):
        return False

    def remover(self, cpf: str):
        return False

    def obterFuncionario(self, cpf: str):
        return None

    def getFuncionarios(self):
        return None

    def getFuncionariosPorCategorias(self, tipo):
        return None

    def getTotalFuncionarios(self):
        return 0

    def solicitarDiaria(self, cpf: str):
        return False

    def partilharLucros(self, valor: float):
        return False

    def iniciarMes(self):
        pass

    def calcularSalarioDoFuncionario(self, cpf: str):
        return None

    def calcularFolhaDePagamento(self):
        return 0
