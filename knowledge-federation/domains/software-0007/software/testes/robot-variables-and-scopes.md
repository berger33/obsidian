---
id: software.testes.tranche17.001082
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "https://github.com/robotframework/robotframework"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: entender escopos de variáveis

## Em uma frase
Variáveis podem ser locais ao caso, comuns à suíte, globais à execução ou passadas por linha de comando, com precedência definida entre elas.

## Por que importa
Valores diferentes por ambiente precisam entrar sem alterar os arquivos de teste, e escopos mal escolhidos criam dependência invisível entre casos.

## Como funciona
Declare variáveis de ambiente na linha de comando, mantenha constantes na seção de variáveis e limite variáveis de execução a valores realmente compartilhados.

## Exemplo
O endereço do serviço pode ser passado na execução, enquanto caminhos de apoio ficam declarados no arquivo da suíte.

## Limites e trade-offs
Variáveis globais facilmente viram estado compartilhado entre casos, e sobrescrever valores da suíte sem perceber produz falhas difíceis de rastrear.

## Como verificar
Execute a mesma suíte com dois valores de variável de ambiente e confirme que o log mostra o valor efetivamente usado em cada caso.

## Conexões
- [[robot-teardown-and-continuation]] — Veja também: Robot Framework: continuar após falhas quando faz sentido.
- [[robot-timeouts-and-stability]] — Veja também: Robot Framework: controlar tempo e instabilidade.

## Fontes
- [Robot Framework — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — sintaxe de casos, palavras-chave, variáveis, modelos, etiquetas e relatórios; consultado em 2026-10-03.
- [Robot Framework — repositório oficial](https://github.com/robotframework/robotframework) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
