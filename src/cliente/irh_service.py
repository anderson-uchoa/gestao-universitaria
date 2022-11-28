from abc import ABC, abstractmethod

from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class IRHService(ABC):
    """ Vamos modelar o controle de pagamento de uma empresa privada de ensino.
    Nessa universidade, existem tres tipos de funcionarios: "prof", "sta", "terc" representando  respectivamente professores, servidores tecnico administrativos e terceirizados.
    Para que o pagamento seja realizado td funcionario deve ter seu cpf e nome cadastrado na folha de pagamento.
    Professores sao classificados em classes(A, B, C, D, E). A classe a qual o professor pertence influencia diretamente no seu salario.
    STAs sao classificados em niveis, que vai do 1 ate 30.O nivel influencia no salario do STA.
    Terceirizados podem receber por insalubridade ou nao.
    Nessa empresa o salario ao fim dos mes e calculado da seguinte forma: SalarioBase + DivisaoNosLucros + Diarias
    Nem td mundo tem direito a diarias. Veja as regras ao longo do arquivo.
    """

    @abstractmethod
    def cadastrar(self, funcionario: Funcionario) -> bool:
        """
        Adiciona um funcionario na folha de pagamento
        Arguments:
            funcionario: Funcionario que deve ser adicionado
        Returns:
            false caso o usuario ja tiver sido adicionado, true caso contrario
        """
        pass

    @abstractmethod
    def remover(self, cpf: str) -> bool:
        """
        Remove o funcionario do folha de pagamento
        Arguments:
            cpf: cpf do funcionario que deve ser removido
        Returns:
             false se o usuario nao tiver cadastrado true caso contrario
        """
        pass

    @abstractmethod
    def obterFuncionario(self, cpf: str) -> Funcionario:
        """
        Retorna o funcionario de acordo com o cpf
        Arguments:
            cpf: cpf do usuario
        Returns:
            usuario caso ele esteja cadastrado, caso contrario retorna null
        """
        pass

    @abstractmethod
    def getFuncionarios(self) -> list:
        """
        Retorna todos os usuarios cadastrados
        Returns:
            lista com todos os usuarios
        """
        pass

    @abstractmethod
    def getFuncionariosPorCategorias(self, tipo: Tipo) -> list:
        """
        Retorna a lista de funcionario por tipo
        Arguments:
            tipo: tipo de funcionario que devem ser retornados
        Returns:
            lista de funcionario do tipo indicado
        """
        pass

    @abstractmethod
    def getTotalFuncionarios(self) -> int:
        """
        Returns:
             quantidade de funcionarios cadastrados
        """
        pass

    @abstractmethod
    def solicitarDiaria(self, cpf: str) -> bool:
        """
        Adiciona uma diaria ao funcionario indicado pelo cpf

        Regras das diarias:
            Professores tem direito de ATE TRES diarias
            STAs tem direito apenas a UMA diaria
            Terceirados nao tem direito a diarias

        Cada diaria vale 100 reais

        Se a diaria nao for aplicavel false deve ser retornado

        Arguments:
            cpf: cpf do funcionario o qual a diaria seria adicionada
        Returns:
            true caso a diaria seja adicionada e false caso contrario
        """
        pass

    @abstractmethod
    def partilharLucros(self, valor: float) -> bool:
        """
        Divide o lucro entre os funcionarios da empresa

        O lucro deve ser dividido igualmente entre os funcionarios.
            Ex: Gratificacao de 500 reais. Se existirem 5 funcionarios, cada funcionario deve receber 100 reais.
        Arguments:
            valor: valor do lucro a ser partilhado
        Returns:
            false se nao houverem funcionarios cadastrados, true caso contrario
        """
        pass

    @abstractmethod
    def iniciarMes(self):
        """
        Remove as diarias e a participacao do lucro de todos os funcionarios
        """
        pass

    @abstractmethod
    def calcularSalarioDoFuncionario(self, cpf: str) -> float:
        """
        Calcula o salario do funcionario dono do cpf informado
        Regras:
            Professores:
                A "classe" e um char que pode ser A, B, C, D ou E.
                O salario dos classes A, B, C, D, E Ã© respectivamente 3000, 5000, 7000, 9000 e 11000 reais.

            STA:
                O "nivel" e um int entre 1 e 30. O salario e calculado como 1000 + 100 * nivel;

        Terceirizado:
            Insalubridade e um boolean que define as condicoes de trabalho.
            O salario e 1000 sem insalubridade e 1500 com insalubridade.

        As diarias devem ser incluidas no salario, bem como a participacao nos lucros

        Arguments:
            cpf: cpf do usuario
        Returns:
            salario do funcionario dono do cpf e null se o funcionario nao estiver cadastrado

        """
        pass

    @abstractmethod
    def calcularFolhaDePagamento(self) -> float:
        """
        Returns:
            a soma dos salarios de todos os funcionarios
        """
        pass
