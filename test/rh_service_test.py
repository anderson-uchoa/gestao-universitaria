import unittest

from src.aluno.base.professor import Professor
from src.aluno.base.sta import STA
from src.aluno.base.terceirizado import Terceirizado
from src.aluno.manager.rh_service import RHService
from src.cliente.tipo import Tipo


class RHServiceCase(unittest.TestCase):


    @classmethod
    def setUp(cls):
        cls.rh = RHService()

        cls.profJonas = Professor("16", "Jonas", 'C')  # salario 7000
        cls.profAlessio = Professor("15", "Alessio", 'B')  # salario 5000

        cls.staMiriam = STA("43", "Miriam", 10)  # salario 2000
        cls.staLacerda = STA("23", "Lacerda", 5)  # salario 1500

        cls.tercCarla = Terceirizado("12", "Carla", False)  # salario 1000
        cls.tercAdriana = Terceirizado("78", "Adriana", True)  # salario 1500

        cls.cpfJonas = "16"
        cls.cpfAlessio = "15"
        cls.cpfLacerda = "23"
        cls.cpfMiriam = "43"
        cls.cpfCarla = "12"
        cls.cpfAdriana = "78"
        cls.cpfNulo = "99"

    def test_cadastrarTerceirizado(self):
        self.assertEqual(0, self.rh.getTotalFuncionarios(), "O RH deve iniciar vazio")
        self.assertTrue(self.rh.cadastrar(self.tercAdriana), "O terceirizado deveria ter sido adicionado")
        self.assertTrue(self.rh.cadastrar(self.tercCarla), "O terceirizado deveria ter sido adicionado")
        self.assertEqual(2, self.rh.getTotalFuncionarios(), "O RH deveria ter dois funcionarios registrados")

    def test_cadastrarSTA(self):
        self.assertEqual(0, self.rh.getTotalFuncionarios(), "O RH deve iniciar vazio")
        self.assertTrue(self.rh.cadastrar(self.staMiriam), "O STA deveria ter sido adicionado")
        self.assertEqual(1, self.rh.getTotalFuncionarios(), "O RH deveria ter um funcionario registrado")

    def test_cadastrarProfessor(self):
        self.assertEqual(0, self.rh.getTotalFuncionarios(), "O RH deve iniciar vazio")
        self.assertTrue(self.rh.cadastrar(self.profJonas), "O Professor deveria ter sido adicionado")
        self.assertEqual(1, self.rh.getTotalFuncionarios(), "O RH deveria ter um funcionario registrado")

    def test_cadastrarFuncionarioDuplicado(self):
        self.assertTrue(self.rh.cadastrar(self.tercCarla), "O terceirizado deveria ter sido adicionado")
        self.assertFalse(self.rh.cadastrar(Professor(self.cpfCarla, "claudio", 'C')),
                         "Nao deve ser possivel adiciona o mesmo funcionario(cpf) duas vezes")
        self.assertEqual(1, self.rh.getTotalFuncionarios(), "O RH deveria ter um funcionario registrado")

    def test_cadastrarProfessorComClasseInvalida(self):
        self.assertFalse(self.rh.cadastrar(Professor(self.cpfNulo, "claudio", 'X')),
                         "Nao podemos cadastrar professor com classe invalida")
        self.assertEqual(0, self.rh.getTotalFuncionarios(), "Funcionario cadastrado indevidamente")

    def test_cadastrarSTAComNivelInvalido(self):
        self.assertFalse(self.rh.cadastrar(STA(self.cpfNulo, "claudio", 35)), "Nao podemos cadastrar sta com nivel invalido")
        self.assertEquals(0, self.rh.getTotalFuncionarios(), "Funcionario cadastrado indevidamente")

    def test_inserirFuncionarios(self):
        self.assertTrue(self.rh.cadastrar(self.profAlessio), "O terceirizado deveria ter sido adicionado")
        self.assertTrue(self.rh.cadastrar(self.profJonas), "O terceirizado deveria ter sido adicionado")

        self.assertTrue(self.rh.cadastrar(self.staMiriam), "O STA deveria ter sido adicionado")
        self.assertTrue(self.rh.cadastrar(self.staLacerda), "O STA deveria ter sido adicionado")

        self.assertTrue(self.rh.cadastrar(self.tercCarla), "O terceirizado deveria ter sido adicionado")
        self.assertTrue(self.rh.cadastrar(self.tercAdriana), "O terceirizado deveria ter sido adicionado")

    def test_removerFuncionario(self):
        self.test_inserirFuncionarios()

        self.assertTrue(self.rh.remover(self.cpfLacerda), "Deve ser possivel remover funcionario cadastrado")
        self.assertTrue(self.rh.remover(self.cpfAdriana), "Deve ser possivel remover funcionario cadastrado")
        self.assertTrue(self.rh.remover(self.cpfAlessio), "Deve ser possivel remover funcionario cadastrado")
        self.assertFalse(self.rh.remover(self.cpfNulo), "Nao e possivel remover um usuario nao cadastrado")

    def test_removerFuncionarioDuasVezes(self):
        self.test_inserirFuncionarios()

        self.assertTrue(self.rh.remover(self.cpfAlessio), "Deve ser possivel remover funcionario cadastrado")
        self.assertFalse(self.rh.remover(self.cpfAlessio), "Nao e possivel remover um usuario duas vezes")
        self.assertEqual(5, self.rh.getTotalFuncionarios(), "O total de funcionarios deve ser 5")

    def test_removerFuncionarioInexistente(self):
        self.test_inserirFuncionarios()

        self.assertFalse(self.rh.remover(self.cpfNulo), "Nao e possivel remover um usuario nao cadastrado")
        self.assertEqual(6, self.rh.getTotalFuncionarios(), "O total de funcionarios deve ser 6")

    def test_buscarProfessor(self):
        self.test_inserirFuncionarios()
        self.assertEqual(self.profJonas, self.rh.obterFuncionario(self.cpfJonas), "Deve ser possivel achar esse professor")

    def test_buscarSTA(self):
        self.test_inserirFuncionarios()
        self.assertEqual(self.staMiriam, self.rh.obterFuncionario(self.cpfMiriam), "Deve ser possivel achar esse STA")

    def buscarTerceirizado(self):
        self.test_inserirFuncionarios()
        self.assertEqual(self.tercCarla, self.rh.obterFuncionario(self.cpfCarla),
                         "Deve ser possivel achar esse terceirizado")

    def buscarFuncionariosNaoExistente(self):
        self.test_inserirFuncionarios()

        self.assertTrue(self.rh.remover(self.cpfLacerda))
        self.assertTrue(self.rh.remover(self.cpfAlessio))

        self.assertEqual(None, self.rh.obterFuncionario(self.cpfAlessio), "Este funcionario foi removido antes")
        self.assertEqual(None, self.rh.obterFuncionario(self.cpfLacerda), "Este funcionario foi removido antes")

    def test_buscarTodosOsProfessores(self):
        self.test_inserirFuncionarios()

        profChico = Professor("91", "Chico", 'E')
        profX = Professor("92", "Xarles", 'D')
        self.rh.cadastrar(profChico)
        self.rh.cadastrar(profX)

        self.assertEqual([self.profAlessio, profChico, self.profJonas, profX],
                         self.rh.getFuncionariosPorCategorias(Tipo.PROF),
                         "A lista deve conter os mesmo funcionario e deve estar ordenada pelo nome funcionario")

    def test_buscarTodosOsSTAs(self):
        self.test_inserirFuncionarios()
        profChico = Professor("91", "Chico", 'E')
        profX = Professor("92", "Xarles", 'D')
        self.rh.cadastrar(profChico)
        self.rh.cadastrar(profX)

        self.assertEqual([self.staLacerda, self.staMiriam],
                         self.rh.getFuncionariosPorCategorias(STA),
                         "A lista deve conter os mesmo funcionario e deve estar ordenada pelo nome funcionario")

    def test_buscarTodosOsTerceirizados(self):
        self.test_inserirFuncionarios()

        self.assertEqual([self.tercAdriana, self.tercCarla],
                         self.rh.getFuncionariosPorCategorias(Tipo.TERC),
                         "A lista deve conter os mesmo funcionario e deve estar ordenada pelo nome funcionario")

    def test_buscarTodosOsFuncionarios(self):
        self.test_inserirFuncionarios()

        self.assertEqual(
            [self.tercAdriana, self.profAlessio, self.tercCarla, self.profJonas, self.staLacerda,
                          self.staMiriam],
            self.rh.getFuncionarios(),
            "A lista deve conter os mesmo funcionario e deve estar ordenada pelo nome funcionario")

    def test_calcularSalarioProfessor(self):
        self.assertTrue(self.rh.cadastrar(self.profJonas))
        self.assertTrue(self.rh.cadastrar(self.profAlessio))

        self.assertEqual(7000.0, self.rh.calcularSalarioDoFuncionario(self.cpfJonas), "Calculo incorreto")
        self.assertEqual(5000.0, self.rh.calcularSalarioDoFuncionario(self.cpfAlessio), "Calculo incorreto")

    def test_calcularSalarioSTA(self):
        self.assertTrue(self.rh.cadastrar(self.staMiriam))
        self.assertEqual(2000.0, self.rh.calcularSalarioDoFuncionario(self.cpfMiriam), "Calculo incorreto")

    def test_calcularSalarioTerceirizados(self):
        self.assertTrue(self.rh.cadastrar(self.tercCarla))
        self.assertEqual(1000.0, self.rh.calcularSalarioDoFuncionario(self.cpfCarla),"Calculo incorreto")

    def test_salarioProfessorComDiaria(self):
        self.assertTrue(self.rh.cadastrar(self.profJonas))
        self.assertTrue(self.rh.solicitarDiaria(self.cpfJonas), "Um professor tem direito a tres diarias")
        self.assertEqual(7100.0, self.rh.calcularSalarioDoFuncionario(self.cpfJonas), "Calculo de diaria incorreto")

    def test_salarioSTAComDiaria(self):
        self.assertTrue(self.rh.cadastrar(self.staLacerda))
        self.assertTrue(self.rh.solicitarDiaria(self.cpfLacerda), "Um sta tem direito a uma diaria")
        self.assertEqual(1600.0, self.rh.calcularSalarioDoFuncionario(self.cpfLacerda), "Calculo de diaria incorreto")

    def test_salarioTerceirizadoComDiaria(self):
        self.assertTrue(self.rh.cadastrar(self.tercCarla))
        self.assertFalse(self.rh.solicitarDiaria(self.cpfCarla), "Um terceirizado nao tem direito a diaria")
        self.assertEqual(1000.0, self.rh.calcularSalarioDoFuncionario(self.cpfCarla), "Calculo de diarias incorreto")

    def test_diariaAlemDoLimiteProfessor(self):
        self.assertTrue(self.rh.cadastrar(self.profJonas))
        self.assertTrue(self.rh.solicitarDiaria(self.cpfJonas), "Um professor tem direito a tres diarias")
        self.assertEqual(7100.0, self.rh.calcularSalarioDoFuncionario(self.cpfJonas), "O calculo do salario esta incorreto")
        self.assertTrue(self.rh.solicitarDiaria(self.cpfJonas), "Um professor tem direito a tres diarias")
        self.assertTrue(self.rh.solicitarDiaria(self.cpfJonas), "Um professor tem direito a tres diarias")
        self.assertFalse(self.rh.solicitarDiaria(self.cpfJonas), "Diarias alem do limite foram concedidas")
        self.assertEqual(7300.0, self.rh.calcularSalarioDoFuncionario(self.cpfJonas),
                         "O calculo do salario esta incorreto")

    def test_diariaAlemDoLimiteSTA(self):
        self.assertTrue(self.rh.cadastrar(self.staLacerda))
        self.assertTrue(self.rh.solicitarDiaria(self.cpfLacerda))
        self.assertEqual(1600.0, self.rh.calcularSalarioDoFuncionario(self.cpfLacerda),
                         "O calculo do salario esta incorreto")
        self.assertFalse(self.rh.solicitarDiaria(self.cpfLacerda), "O funcionario nao tem mais direito a diarias")
        self.assertEqual(1600.0, self.rh.calcularSalarioDoFuncionario(self.cpfLacerda), "O calculo do salario esta incorreto")

    def test_calcularFolhaVazia(self):
        self.assertEqual(0.0, self.rh.calcularFolhaDePagamento(), "Folha de pagamento esta vazia")

    def test_calcularFolha(self):
        self.assertTrue(self.rh.cadastrar(self.profJonas))
        self.assertTrue(self.rh.cadastrar(self.staMiriam))
        self.assertTrue(self.rh.cadastrar(self.tercCarla))

        self.assertEqual(10000.0, self.rh.calcularFolhaDePagamento(), "Soma de salarios incorreta")

        self.assertTrue(self.rh.cadastrar(self.staLacerda))
        self.assertTrue(self.rh.cadastrar(self.profAlessio))
        self.assertTrue(self.rh.cadastrar(self.tercAdriana))

        self.assertEqual(18000.0, self.rh.calcularFolhaDePagamento(),"Soma de salarios incorreta")

    def test_calcularFolhaComDiarias(self):
        self.assertEqual(0.0, self.rh.calcularFolhaDePagamento())

        self.assertTrue(self.rh.cadastrar(self.profJonas))
        self.assertTrue(self.rh.cadastrar(self.staMiriam))
        self.assertTrue(self.rh.cadastrar(self.tercCarla))

        self.assertEqual(10000.0, self.rh.calcularFolhaDePagamento(), "Soma de salarios incorreta")

        self.assertTrue(self.rh.cadastrar(self.staLacerda))
        self.assertTrue(self.rh.cadastrar(self.profAlessio))
        self.assertTrue(self.rh.cadastrar(self.tercAdriana))

        self.assertEqual(18000.0, self.rh.calcularFolhaDePagamento(), "Soma de salarios incorreta")

        self.assertTrue(self.rh.solicitarDiaria(self.cpfJonas))
        self.assertEqual(7100.0, self.rh.calcularSalarioDoFuncionario(self.cpfJonas),"Soma de salarios com diaria incorreta")
        self.assertTrue(self.rh.solicitarDiaria(self.cpfJonas))
        self.assertTrue(self.rh.solicitarDiaria(self.cpfJonas))
        self.assertFalse(self.rh.solicitarDiaria(self.cpfJonas))

        self.assertEqual(7300.0, self.rh.calcularSalarioDoFuncionario(self.cpfJonas),"Soma de salarios com diaria incorreta")

        self.assertFalse(self.rh.solicitarDiaria(self.cpfCarla))

        self.assertTrue(self.rh.solicitarDiaria(self.cpfLacerda))
        self.assertFalse(self.rh.solicitarDiaria(self.cpfLacerda))

        self.assertEqual(18400.0, self.rh.calcularFolhaDePagamento(), "Soma de salarios com diaria incorreta")

    def test_participacaoNosLucros(self):
        self.assertEquals(0.0, self.rh.calcularFolhaDePagamento())

        self.assertTrue(self.rh.cadastrar(self.profJonas))
        self.assertTrue(self.rh.cadastrar(self.staMiriam))
        self.assertTrue(self.rh.cadastrar(self.tercCarla))

        self.assertEquals(10000.0, self.rh.calcularFolhaDePagamento())

        self.assertTrue(self.rh.partilharLucros(6.00))

        self.assertEquals(2002.0, self.rh.calcularSalarioDoFuncionario(self.cpfMiriam),
                          "Salarios com participacao nos lucros incorreto")

    def test_calcularFolhaComPL(self):
        self.test_participacaoNosLucros()
        self.assertEqual(10006.0, self.rh.calcularFolhaDePagamento(),
                         "Soma de salarios com participacao nos lucros incorreta")

    def test_iniciandoNovoMes(self):
        self.test_calcularFolhaComPL()
        self.rh.iniciarMes()
        self.assertEqual(10000.0, self.rh.calcularFolhaDePagamento())


if __name__ == '__main__':
    unittest.main()
