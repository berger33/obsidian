---
id: software.seguranca.tranche17.001672
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://www.checkov.io/1.Welcome/What%20is%20Checkov.html", "https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Checkov: Análise de plano Terraform

## Em uma frase
**Checkov — Análise de plano Terraform:** Um plano renderizado pode oferecer valores calculados que não estão aparentes no HCL original.

## Por que importa
O recorte de **análise de plano terraform** ajuda a identificar controles de segurança ausentes ainda no repositório ou plano de infraestrutura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **análise de plano terraform**, descobre os arquivos e frameworks suportados, executa checks sobre definições ou plano e apresenta finding com identificador e localização. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Gere plan JSON em pipeline isolada e escaneie-o sem aplicar mudanças na conta cloud. Teste em staging autorizado.

## Limites e trade-offs
Plan files podem conter segredos e dados sensíveis; retenção e acesso precisam ser restringidos. Exceções exigem responsável e prazo.

## Como verificar
Confirme versão do provider e se recursos planejados estão presentes no relatório. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[checkov-checks-para-kubernetes-e-helm]] — Complementa o tópico com checkov: checks para kubernetes e helm.

## Fontes
- [Checkov — What is Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) — introdução oficial aos frameworks IaC e modelos de análise; consultado em 2026-10-04.
- [Checkov — CLI Command Reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html) — referência oficial da CLI, escopo, formatos e opções; consultado em 2026-10-04.
