---
id: software.seguranca.tranche17.001683
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

# kube-bench: Estrutura dos controles YAML

## Em uma frase
**kube-bench — Estrutura dos controles YAML:** Cada check descreve identificador, texto, comando de auditoria, critérios, remediação e se é scored.

## Por que importa
O recorte de **estrutura dos controles yaml** ajuda a verificar hardening de cluster e transformar recomendações documentadas em tarefas rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **estrutura dos controles yaml**, checks descritos em arquivos YAML executam auditorias locais ou comandos de configuração e comparam saída a critérios previstos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Inspecione controle YAML específico e compare comando com configuração real do nó de teste. Teste em staging autorizado.

## Limites e trade-offs
Check customizado ou alterado pode divergir do benchmark publicado. Exceções exigem responsável e prazo.

## Como verificar
Versione arquivo de controles e compare hash com pacote aprovado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-bench-interpretacao-de-audit-e-test-items]] — Complementa o tópico com kube-bench: interpretação de audit e test_items.

## Fontes
- [Aqua kube-bench — Repository](https://github.com/aquasecurity/kube-bench) — repositório oficial e descrição da ferramenta CIS Kubernetes Benchmark; consultado em 2026-10-04.
- [Aqua kube-bench — Controls and YAML](https://aquasecurity.github.io/kube-bench/v0.6.6/controls/) — documentação versionada dos arquivos de controles, comandos de auditoria e critérios de checks; consultado em 2026-10-04.
