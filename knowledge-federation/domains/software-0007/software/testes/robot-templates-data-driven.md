---
id: software.testes.tranche17.001078
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

# Robot Framework: usar modelos para testes orientados a dados

## Em uma frase
A configuração de modelo faz o caso executar a mesma palavra-chave para cada linha de dados, transformando a tabela em conjunto de cenários.

## Por que importa
Variações de entrada verificadas pela mesma lógica ficam concisas e cobrem mais combinações do que casos duplicados manualmente.

## Como funciona
Declare o modelo no caso, coloque os dados em linhas e mantenha cada coluna com um papel claro no teste.

## Exemplo
Um caso de validação de acesso pode listar pares de usuário e senha com a mensagem de erro esperada para cada combinação.

## Limites e trade-offs
Modelos que testam coisas diferentes na mesma tabela confundem a leitura, e a ausência de cabeçalho claro dificulta saber o que cada coluna representa.

## Como verificar
Acrescente uma linha de dados inválida e confirme que ela aparece como caso independente no relatório, com resultado próprio.

## Conexões
- [[robot-keywords-and-arguments]] — Veja também: Robot Framework: extrair palavras-chave próprias.
- [[robot-setup-teardown]] — Veja também: Robot Framework: preparar e limpar em níveis distintos.

## Fontes
- [Robot Framework — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — sintaxe de casos, palavras-chave, variáveis, modelos, etiquetas e relatórios; consultado em 2026-10-03.
- [Robot Framework — repositório oficial](https://github.com/robotframework/robotframework) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
