---
id: software.seguranca.tranche17.001685
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

# kube-bench: Execução seletiva por IDs

## Em uma frase
**kube-bench — Execução seletiva por IDs:** Checks podem ser selecionados por identificadores para investigação focada e validação de remediação.

## Por que importa
O recorte de **execução seletiva por ids** ajuda a verificar hardening de cluster e transformar recomendações documentadas em tarefas rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **execução seletiva por ids**, checks descritos em arquivos YAML executam auditorias locais ou comandos de configuração e comparam saída a critérios previstos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rode apenas ID do controle corrigido em staging, preservando relatório completo como baseline. Teste em staging autorizado.

## Limites e trade-offs
Scan seletivo não equivale à auditoria do benchmark inteiro. Exceções exigem responsável e prazo.

## Como verificar
Registre IDs selecionados e indique cobertura parcial no ticket de change. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-bench-diferenca-entre-fail-e-warning]] — Complementa o tópico com kube-bench: diferença entre fail e warning.

## Fontes
- [Aqua kube-bench — Repository](https://github.com/aquasecurity/kube-bench) — repositório oficial e descrição da ferramenta CIS Kubernetes Benchmark; consultado em 2026-10-04.
- [Aqua kube-bench — Controls and YAML](https://aquasecurity.github.io/kube-bench/v0.6.6/controls/) — documentação versionada dos arquivos de controles, comandos de auditoria e critérios de checks; consultado em 2026-10-04.
