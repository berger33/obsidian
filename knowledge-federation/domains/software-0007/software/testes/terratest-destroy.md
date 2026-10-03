---
id: software.testes.tranche19.001299
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/terraform", "https://github.com/gruntwork-io/terratest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Terratest: garantir a destruição dos recursos

## Em uma frase
A destruição dos recursos é agendada no início do teste para executar ao final, inclusive quando verificações falham no meio.

## Por que importa
Recursos esquecidos geram custo contínuo e limites de cota, e a destruição automática evita a limpeza manual esquecida.

## Como funciona
Agende a destruição imediatamente após montar as opções, antes da aplicação, e verifique ao final que nada permanece.

## Exemplo
Um teste interrompido por falha de asserção ainda pode destruir o ambiente, desde que a destruição esteja agendada.

## Limites e trade-offs
Interromper o processo à força pode impedir a execução do agendamento, deixando recursos órfãos que precisam ser removidos por fora.

## Como verificar
Introduza uma falha no meio do teste e confirme que os recursos ainda são destruídos ao final da execução.

## Conexões
- [[terratest-basic-test]] — Veja também: Terratest: estruturar um teste de infraestrutura.
- [[terratest-stages]] — Veja também: Terratest: dividir o teste em estágios.

## Fontes
- [Terratest — Módulo terraform](https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/terraform) — opções, aplicação, saídas e destruição; consultado em 2026-10-03.
- [Terratest — repositório oficial](https://github.com/gruntwork-io/terratest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
