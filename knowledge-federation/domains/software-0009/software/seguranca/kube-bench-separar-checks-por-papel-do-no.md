---
id: software.seguranca.tranche17.001682
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

# kube-bench: Separar checks por papel do nó

## Em uma frase
**kube-bench — Separar checks por papel do nó:** Control plane, worker e outros papéis têm conjuntos de controles e comandos diferentes.

## Por que importa
O recorte de **separar checks por papel do nó** ajuda a verificar hardening de cluster e transformar recomendações documentadas em tarefas rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **separar checks por papel do nó**, checks descritos em arquivos YAML executam auditorias locais ou comandos de configuração e comparam saída a critérios previstos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute controles de nó de laboratório usando profile apropriado ao papel, não uma configuração genérica para todo host. Teste em staging autorizado.

## Limites e trade-offs
Perfil inadequado produz falhas ou omissões; clusters gerenciados podem ocultar acesso ao control plane. Exceções exigem responsável e prazo.

## Como verificar
Confirme papel do host e lista de grupos de check usados antes de interpretar resultado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-bench-estrutura-dos-controles-yaml]] — Complementa o tópico com kube-bench: estrutura dos controles yaml.

## Fontes
- [Aqua kube-bench — Repository](https://github.com/aquasecurity/kube-bench) — repositório oficial e descrição da ferramenta CIS Kubernetes Benchmark; consultado em 2026-10-04.
- [Aqua kube-bench — Controls and YAML](https://aquasecurity.github.io/kube-bench/v0.6.6/controls/) — documentação versionada dos arquivos de controles, comandos de auditoria e critérios de checks; consultado em 2026-10-04.
