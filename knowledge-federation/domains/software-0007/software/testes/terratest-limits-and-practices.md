---
id: software.testes.tranche19.001307
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

# Terratest: reconhecer limites e boas práticas

## Em uma frase
Testes de infraestrutura são lentos, custam recursos reais e dependem do provedor, complementando a análise estática e os testes de unidade da configuração.

## Por que importa
Usar a ferramenta para tudo encarece a esteira e diminui a frequência de execução, enfraquecendo a proteção que ela deveria dar.

## Como funciona
Reserve testes de infraestrutura para os caminhos críticos, valide a configuração estaticamente antes e mantenha os módulos pequenos e reutilizáveis.

## Exemplo
A maior parte das mudanças pode ser verificada por análise estática, com aplicação real apenas para os módulos centrais.

## Limites e trade-offs
Suítes extensas de infraestrutura se tornam caras e lentas, e acabam desativadas ou executadas raramente por falta de orçamento.

## Como verificar
Compare a cobertura de uma execução completa com a de uma seleção crítica e verifique se a diferença é intencional e documentada.

## Conexões
- [[terratest-ci-integration]] — Veja também: Terratest: rodar na esteira com credenciais controladas.

## Fontes
- [Terratest — Módulo terraform](https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/terraform) — opções, aplicação, saídas e destruição; consultado em 2026-10-03.
- [Terratest — repositório oficial](https://github.com/gruntwork-io/terratest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
