---
id: software.testes.tranche19.001302
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
fontes: ["https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/random", "https://github.com/gruntwork-io/terratest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Terratest: gerar nomes únicos para recursos

## Em uma frase
A biblioteca oferece geração de identificadores aleatórios usados para nomear recursos de forma que execuções concorrentes não colidam.

## Por que importa
Nomes únicos permitem rodar testes em paralelo e evitam falhas causadas por recurso preexistente de outra execução.

## Como funciona
Gere o identificador no início do teste, componha o nome do recurso e mantenha-o curto e dentro das regras do provedor.

## Exemplo
Um teste pode criar um depósito cujo nome inclui sufixo aleatório, evitando colisão com o depósito de outra execução.

## Limites e trade-offs
Nomes fixos falham em execuções simultâneas, e identificadores longos demais violam limites de tamanho do provedor.

## Como verificar
Rode o mesmo teste duas vezes em paralelo e confirme que as duas execuções criam recursos distintos sem colisão.

## Conexões
- [[terratest-retries]] — Veja também: Terratest: tratar erros transitórios com repetição.
- [[terratest-verify-state]] — Veja também: Terratest: verificar o estado real após aplicar.

## Fontes
- [Terratest — Módulo random](https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/random) — geração de identificadores únicos para recursos; consultado em 2026-10-03.
- [Terratest — repositório oficial](https://github.com/gruntwork-io/terratest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
