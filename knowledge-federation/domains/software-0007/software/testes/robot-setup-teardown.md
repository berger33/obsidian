---
id: software.testes.tranche17.001079
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

# Robot Framework: preparar e limpar em níveis distintos

## Em uma frase
Configurações e limpezas podem ser declaradas para a suíte, cada caso ou cada palavra-chave, com ordem de execução definida entre os níveis.

## Por que importa
O isolamento entre casos depende de restaurar o estado no momento certo, e preparar no nível errado mistura dados entre testes.

## Como funciona
Coloque a preparação de ambiente na suíte, a preparação de dados no caso e a limpeza correspondente no mesmo nível da preparação.

## Exemplo
Uma suíte pode subir o serviço uma vez, enquanto cada caso limpa o registro criado antes de encerrar.

## Limites e trade-offs
Limpeza no nível errado deixa resíduos que afetam casos seguintes, e dependências entre preparações de casos diferentes tornam a ordem de execução obrigatória.

## Como verificar
Rode o mesmo caso duas vezes seguidas e confirme que o resultado não depende de dados deixados pela execução anterior.

## Conexões
- [[robot-templates-data-driven]] — Veja também: Robot Framework: usar modelos para testes orientados a dados.
- [[robot-tags-and-selection]] — Veja também: Robot Framework: etiquetar e selecionar testes.

## Fontes
- [Robot Framework — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — sintaxe de casos, palavras-chave, variáveis, modelos, etiquetas e relatórios; consultado em 2026-10-03.
- [Robot Framework — repositório oficial](https://github.com/robotframework/robotframework) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
