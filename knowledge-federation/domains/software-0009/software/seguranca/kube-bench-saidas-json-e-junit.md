---
id: software.seguranca.tranche17.001687
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
fontes: ["https://github.com/aquasecurity/kube-bench", "https://aquasecurity.github.io/kube-bench/v0.6.6/controls/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# kube-bench: Saídas JSON e JUnit

## Em uma frase
**kube-bench — Saídas JSON e JUnit:** Formatos de máquina podem alimentar pipeline de conformidade e comparação de regressões.

## Por que importa
O recorte de **saídas json e junit** ajuda a verificar hardening de cluster e transformar recomendações documentadas em tarefas rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **saídas json e junit**, checks descritos em arquivos YAML executam auditorias locais ou comandos de configuração e comparam saída a critérios previstos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em staging, exporte JSON ou JUnit e confira que check id e status chegam ao dashboard. Teste em staging autorizado.

## Limites e trade-offs
A conversão pode perder texto de remediation ou distinção de not-applicable. Exceções exigem responsável e prazo.

## Como verificar
Reconcilie contagem dos checks com saída textual e valide formato importado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-bench-remediacoes-como-plano-de-mudanca]] — Complementa o tópico com kube-bench: remediações como plano de mudança.

## Fontes
- [Aqua kube-bench — Repository](https://github.com/aquasecurity/kube-bench) — repositório oficial e descrição da ferramenta CIS Kubernetes Benchmark; consultado em 2026-10-04.
- [Aqua kube-bench — Controls and YAML](https://aquasecurity.github.io/kube-bench/v0.6.6/controls/) — documentação versionada dos arquivos de controles, comandos de auditoria e critérios de checks; consultado em 2026-10-04.
