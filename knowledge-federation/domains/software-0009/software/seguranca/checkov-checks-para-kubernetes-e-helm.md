---
id: software.seguranca.tranche17.001673
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

# Checkov: Checks para Kubernetes e Helm

## Em uma frase
**Checkov — Checks para Kubernetes e Helm:** Manifestos e charts podem ser avaliados por checks de configuração antes da implantação.

## Por que importa
O recorte de **checks para kubernetes e helm** ajuda a identificar controles de segurança ausentes ainda no repositório ou plano de infraestrutura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **checks para kubernetes e helm**, descobre os arquivos e frameworks suportados, executa checks sobre definições ou plano e apresenta finding com identificador e localização. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Analise chart renderizado com values de staging e procure privilégios, exposição e ausência de recursos de segurança. Teste em staging autorizado.

## Limites e trade-offs
Chart fonte sem values de ambiente pode não refletir o YAML final aplicado. Exceções exigem responsável e prazo.

## Como verificar
Guarde o manifest renderizado e valide os mesmos controles no admission do cluster. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[checkov-analise-de-dockerfile-e-imagens]] — Complementa o tópico com checkov: análise de dockerfile e imagens.

## Fontes
- [Checkov — What is Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) — introdução oficial aos frameworks IaC e modelos de análise; consultado em 2026-10-04.
- [Checkov — CLI Command Reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html) — referência oficial da CLI, escopo, formatos e opções; consultado em 2026-10-04.
